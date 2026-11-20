import random

from ideanet import Engine, Idea, IdeaGraph, Link, characterize, inject_unfamiliar, random_ontology, rewire
from ideanet.analysis import find_period, null_comparison


def chain(*weights, **idea_kw):
    g = IdeaGraph()
    for i in range(len(weights) + 1):
        g.add_idea(Idea(f"n{i}", [f"w{i}"], **idea_kw))
    for i, w in enumerate(weights):
        g.add_link(Link(f"n{i}", f"n{i+1}", w))
    return g


def test_activation_propagates_and_emits():
    eng = Engine(chain(1.2, 1.2))
    eng.stimulate("n0", 2.0)
    eng.run(10)
    assert eng.emissions == ["w0", "w1", "w2"]
    assert [f.time for f in eng.fires] == [0.0, 1.0, 2.0]


def test_subthreshold_inputs_converge():
    g = IdeaGraph()
    for k in "abd":
        g.add_idea(Idea(k, [k]))
    g.connect("a", "d", 0.6)
    g.connect("b", "d", 0.6)
    eng = Engine(g)
    eng.stimulate("a"); eng.run(5)
    assert "d" not in eng.emissions
    eng = Engine(g)
    eng.stimulate("a"); eng.stimulate("b"); eng.run(5)
    assert eng.fires[-1].idea == "d" and set(eng.fires[-1].inputs) == {"a", "b"}


def test_decay_prevents_late_summation():
    g = chain(0.6)
    eng = Engine(g)
    eng.stimulate("n1", 0.6, at=0)
    eng.stimulate("n1", 0.6, at=20)  # first input long decayed
    eng.run(30)
    assert eng.fires == []


def test_inhibition_blocks():
    g = IdeaGraph()
    for k in "aib":
        g.add_idea(Idea(k, [k]))
    g.connect("a", "b", 1.2, delay=2.0)
    g.connect("i", "b", -1.0, delay=1.0)
    eng = Engine(g)
    eng.stimulate("a"); eng.stimulate("i"); eng.run(5)
    assert "b" not in eng.emissions


def test_refractory_and_unnamed():
    g = IdeaGraph()
    g.add_idea(Idea("x", [], refractory=5.0))
    eng = Engine(g)
    for t in (0, 1, 2, 6):
        eng.stimulate("x", 2.0, at=t)
    eng.run(10)
    assert [f.time for f in eng.fires] == [0, 6]
    assert eng.emissions == [] and len(eng.trace) == 4


def test_context_gating():
    g = chain(1.2)
    g.out_links["n0"][0].context = "bio"
    for ctx, expect in (((), 1), (("bio",), 2)):
        eng = Engine(g, contexts=ctx)
        eng.stimulate("n0"); eng.run(5)
        assert len(eng.fires) == expect


def test_deterministic_with_seed():
    g = random_ontology(200, 4, seed=1)
    runs = []
    for _ in range(2):
        eng = Engine(g, seed=7, noise_rate=0.5, fire_gain=2.0)
        eng.stimulate("i0", 3.0)
        eng.run(50)
        runs.append([(r.time, r.target, r.potential_after) for r in eng.trace])
    assert runs[0] == runs[1] and runs[0]


def test_find_period():
    a, b = frozenset({"a"}), frozenset({"b"})
    assert find_period([a, b, a, b, a, b, a, b]) == 2
    assert find_period([a, b, b, a]) is None


def test_harbor_loop_is_periodic_and_beats_null():
    g = IdeaGraph.load("ontologies/harbor.json")
    eng = Engine(g)
    eng.stimulate("harbor")
    eng.run(300)
    d = characterize(eng, 300)
    assert d.kind == "periodic" and "x_moving_gate" in d.attractor and d.unnamed_fires > 0
    res = null_comparison(g, [("harbor", 2.0)], 80, samples=30)
    assert res["recurrent_states"]["observed"] > res["recurrent_states"]["null_mean"]


def test_rewire_preserves_degrees():
    g = random_ontology(300, 4, seed=2)
    r = rewire(g, random.Random(0))
    assert g.out_degree() == r.out_degree() and g.in_degree() == r.in_degree()
    assert sorted(l.weight for l in g.links) == sorted(l.weight for l in r.links)


def test_inject_unfamiliar_links_are_distant():
    g = random_ontology(300, 3, seed=3)
    before = {k: {l.target for l in v} for k, v in g.out_links.items()}
    for link in inject_unfamiliar(g, 10, seed=0):
        two_hop = before[link.source] | {t for m in before[link.source] for t in before[m]}
        assert link.target not in two_hop


def test_save_load_roundtrip(tmp_path):
    g = IdeaGraph.load("ontologies/harbor.json")
    p = tmp_path / "g.json"
    g.save(p)
    h = IdeaGraph.load(p)
    assert h.to_dict() == g.to_dict()


def test_text_stimulus_matching():
    from ideanet import TextStimulus
    g = IdeaGraph()
    for k in ("bee", "honey_bee", "flower", "city"):
        g.add_idea(Idea(k, [k.replace("_", " ")]))
    ts = TextStimulus(g)
    matched, unmatched = ts.match("The honey bee visits flowers in cities, zzz!")
    assert matched == ["honey_bee", "flower", "city"] and unmatched == ["visits", "zzz"]
    assert ts.stimuli("bee", 1.5) == [("bee", 1.5)]


def test_normalize_fanout():
    from ideanet import normalize_fanout
    g = IdeaGraph()
    for k in "habcd":
        g.add_idea(Idea(k))
    for k in "abcd":
        g.connect("h", k, 1.0)
    g.connect("a", "b", 1.0)
    normalize_fanout(g, budget=1.0, alpha=1.0)
    assert abs(sum(l.weight for l in g.out_links["h"]) - 1.0) < 1e-9
    assert g.out_links["a"][0].weight == 1.0


def test_top_k_limits_propagation():
    g = IdeaGraph()
    for k in "habc":
        g.add_idea(Idea(k, [k]))
    g.connect("h", "a", 1.5); g.connect("h", "b", 1.2); g.connect("h", "c", 1.1)
    eng = Engine(g, top_k=2)
    eng.stimulate("h"); eng.run(5)
    assert eng.emissions == ["h", "a", "b"]


def test_global_inhibition_damps_cascade():
    g = random_ontology(500, 6, seed=4, inhibitory=0.0)
    counts = []
    for inh in (0.0, 0.5):
        eng = Engine(g, fire_gain=3.0, global_inhibition=inh, max_events=50_000)
        eng.stimulate("i0", 3.0); eng.run(40)
        counts.append(len(eng.fires))
    assert counts[1] < counts[0] / 3


def _sym_graph(n=60, seed=3):
    rng = random.Random(seed)
    g = IdeaGraph()
    for i in range(n):
        g.add_idea(Idea(f"n{i}"))
    for _ in range(150):
        a, b = rng.sample(range(n), 2)
        g.add_link(Link(f"n{a}", f"n{b}", 0.5, relation="Synonym"))
        g.add_link(Link(f"n{b}", f"n{a}", 0.5, relation="Synonym"))
    for _ in range(100):
        a, b = rng.sample(range(n), 2)
        g.add_link(Link(f"n{a}", f"n{b}", 0.4, relation="IsA"))
    return g


def test_reciprocal_shuffle_preserves_degrees_and_reciprocity():
    from collections import Counter
    from ideanet import shuffle_targets
    g = _sym_graph()
    def stats(g):
        ls = g.links
        trip = {(l.source, l.target, l.relation) for l in ls}
        rec = sum((l.target, l.source, l.relation) in trip for l in ls)
        return (Counter((l.source, l.relation) for l in ls), Counter((l.target, l.relation) for l in ls), rec)
    before = stats(g)
    edges = sorted((l.source, l.target) for l in g.links)
    restore, info = shuffle_targets(g, random.Random(1), "reciprocal")
    after = stats(g)
    assert after[0] == before[0] and after[1] == before[1]
    assert after[2] >= before[2] - 2 * info["self_loops"] - 10
    assert sorted((l.source, l.target) for l in g.links) != edges
    restore()
    assert sorted((l.source, l.target) for l in g.links) == edges


def test_attractor_signature_and_map():
    from ideanet import AttractorMap, signature, weighted_jaccard, jensen_shannon
    from ideanet.engine import Fire
    fires = [Fire(t, x, None, ()) for t, x in [(1, "a"), (60, "a"), (61, "b"), (62, "a")]]
    s = signature(fires, 50)
    assert s == {"a": 2 / 3, "b": 1 / 3}
    assert weighted_jaccard(s, s) == 1 and weighted_jaccard(s, {"c": 1}) == 0
    assert jensen_shannon(s, s) == 0 and abs(jensen_shannon({"a": 1}, {"c": 1}) - 1) < 1e-9
    m = AttractorMap(0.5)
    assert m.assign(s, "x") == m.assign({"a": 0.6, "b": 0.4}, "y") == 1
    assert m.assign({"c": 1}, "z") == 2 and m.assign({}, "w") == 0


def test_classify_pair_kinds():
    from ideanet import classify_pair
    from ideanet.engine import Fire
    A, B = {"a": 1.0}, {"b": 1.0}
    mk = lambda pairs: [Fire(t, x, None, ()) for t, x in pairs]
    assert classify_pair(A, B, mk([(t, "a") for t in range(50, 100)]), 50, 100)[0]["kind"] == "dominate_a"
    assert classify_pair(A, B, mk([(t, "c") for t in range(50, 100)]), 50, 100)[0]["kind"] == "novel"
    alt = mk([(t, "a" if (t // 10) % 2 == 0 else "b") for t in range(50, 100)])
    assert classify_pair(A, B, alt, 50, 100)[0]["kind"] == "alternate"
    mix = mk([(t, "a" if t % 2 else "b") for t in range(50, 100)])
    assert classify_pair(A, B, mix, 50, 100)[0]["kind"] == "coexist"


def _corpus_graph():
    from ideanet.graph import Idea, IdeaGraph, Link
    g = IdeaGraph()
    for i in ["bee", "honey", "hive", "car", "road", "honey_bee"]:
        g.add_idea(Idea(i, [i.replace("_", " ")]))
    for s, t, w, r in [("bee", "honey", 0.35, "RelatedTo"), ("honey", "bee", 0.35, "RelatedTo"),
                       ("bee", "hive", 0.5, "AtLocation"), ("car", "road", 0.5, "AtLocation"),
                       ("bee", "car", -0.45, "DistinctFrom"), ("honey_bee", "bee", 0.6, "IsA")]:
        g.add_link(Link(s, t, w, relation=r))
    return g


def test_concept_matcher_and_cooccurrence():
    import numpy as np
    from ideanet.corpus import ConceptMatcher, count_cooccurrence, ppmi_weights, apply_weights
    g = _corpus_graph()
    m = ConceptMatcher(g)
    assert [m.ids[i] for i in m.match_tokens("the honey bee makes honey in hives".split())] == ["honey_bee", "honey", "hive"]
    text = ["Bees make honey. The bee lives in a hive.", "A car drives on the road. The car is red."] * 5
    c = count_cooccurrence(g, text, window=5, workers=1, matcher=m, log=lambda *a, **k: None)
    assert c["stats"]["sentences"] == 20
    for mode in ("replace", "evidence"):
        w, info = ppmi_weights(g, c, min_count=1, mode=mode)
        orig = np.array([l.weight for l in g.links])
        assert np.allclose(np.sort(np.abs(w)), np.sort(np.abs(orig)))  # marginal preserved
        assert (np.sign(w) == np.sign(orig)).all()                      # inhibition preserved
    w, info = ppmi_weights(g, c, min_count=1, mode="evidence")
    links = g.links
    unseen = [i for i, l in enumerate(links) if l.source == "honey_bee"]
    assert all(w[i] == np.float32(links[i].weight) for i in unseen)
    before = [l.weight for l in links]
    restore = apply_weights(g, w)
    assert [l.weight for l in g.links] == [float(x) for x in w]
    restore()
    assert [l.weight for l in g.links] == before


def test_weight_table_matches_apply_weights():
    import numpy as np
    from ideanet import Engine
    from ideanet.corpus import WeightTable, apply_weights
    g = _corpus_graph()
    wt = WeightTable(g)
    w = np.array([0.9, 0.2, 0.6, 0.4, -0.3, 0.8])
    e1 = Engine(g, fire_gain=2.0, weight_of=wt.weight_fn(w, 3, 0.1))
    e1.stimulate("honey_bee", 2.0)
    e1.run(20)
    restore = apply_weights(g, w * WeightTable.jitter(len(w), 3, 0.1))
    e2 = Engine(g, fire_gain=2.0)
    e2.stimulate("honey_bee", 2.0)
    e2.run(20)
    restore()
    assert [(f.time, f.idea) for f in e1.fires] == [(f.time, f.idea) for f in e2.fires]
    assert [r.potential_after for r in e1.trace] == [r.potential_after for r in e2.trace]
