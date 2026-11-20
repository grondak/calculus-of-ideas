"""Attractor basin map + simultaneous-stimulus interaction experiment.

Stage 1: stimulate N random ideas (out-degree >= 1) one at a time, take each run's
attractor signature (firing distribution over the late window, by idea id) and cluster
signatures into attractors. Reports how many attractors there are and how basin sizes
are distributed.

Stage 2: stimulate pairs of ideas from different attractors together and classify the
joint outcome (dominate / coexist / alternate / novel / extinct). For 'novel' outcomes,
look up whether the joint region is a known attractor in the map and how large its basin is.

usage: PYTHONPATH=. python experiments/basins.py conceptnet-en.pkl out.json.gz [--n 10000]
"""
from __future__ import annotations

import argparse
import gzip
import itertools
import json
import random
import statistics
import time
from collections import Counter

from ideanet import AttractorMap, Engine, IdeaGraph, TextStimulus, classify_pair, signature, weighted_jaccard

PARAMS = dict(fire_gain=2.0, top_k=10, global_inhibition=0.1)
UNTIL, LATE, STRENGTH = 100.0, 50.0, 2.0
NAMED = ["bee", "honey", "ant", "wasp", "flower", "wolf", "computer worm", "harbor", "violin",
         "mathematics", "democracy", "rain", "kitchen", "justice", "ocean", "sugar"]
NAMED_PAIRS = [("bee", "honey"), ("bee", "flower"), ("honey", "wolf"), ("ant", "honey"), ("bee", "computer worm"),
               ("flower", "honey"), ("mathematics", "justice"), ("harbor", "ocean"), ("violin", "kitchen"),
               ("wolf", "democracy"), ("rain", "sugar"), ("bee", "mathematics")]


def run(g, stimuli):
    eng = Engine(g, seed=0, max_events=300_000, **PARAMS)
    for idea, s in stimuli:
        eng.stimulate(idea, s)
    eng.run(UNTIL)
    return eng


def top(sig, n=8):
    return [k for k, _ in sorted(sig.items(), key=lambda kv: -kv[1])[:n]]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("graph")
    ap.add_argument("out")
    ap.add_argument("--n", type=int, default=10_000)
    ap.add_argument("--threshold", type=float, default=0.5)
    ap.add_argument("--top-attractors", type=int, default=30)
    ap.add_argument("--random-pairs", type=int, default=400)
    ap.add_argument("--seed", type=int, default=1)
    a = ap.parse_args()
    rng = random.Random(a.seed)
    t0 = time.time()
    log = lambda *m: print(f"[{time.time() - t0:7.1f}s]", *m, flush=True)

    g = IdeaGraph.load(a.graph)
    ts = TextStimulus(g)
    log(f"loaded {len(g.ideas):,} ideas")

    # ---------- stage 1: basin map
    amap = AttractorMap(a.threshold)
    sigs: dict[str, dict] = {}
    rows = []
    for name in NAMED:
        stim = ts.stimuli(name, STRENGTH)
        e = run(g, stim)
        sigs[name] = signature(e.fires, LATE, UNTIL)
    candidates = sorted(i for i, ls in g.out_links.items() if ls)
    starts = rng.sample(candidates, a.n)
    for k, s in enumerate(starts):
        e = run(g, [(s, STRENGTH)])
        sig = signature(e.fires, LATE, UNTIL)
        sigs[s] = sig
        aid = amap.assign(sig, s)
        rows.append({"start": s, "attractor": aid, "fires": len(e.fires), "runaway": e.hit_event_limit,
                     "late_distinct": len(sig)})
        if (k + 1) % 1000 == 0:
            log(f"{k + 1} starts, {len(amap.reps) - 1} attractors")
    named_assign = {}
    for name in NAMED:
        aid, sim = amap.lookup(sigs[name])
        named_assign[name] = {"attractor": aid, "sim": round(sim, 3), "top": top(sigs[name], 6)}

    sizes = amap.sizes()
    live = [(i, n) for i, n in sizes if i != AttractorMap.EXTINCT]
    n_live = sum(n for _, n in live)
    cover = {}
    for frac in (0.5, 0.8, 0.9):
        acc, cnt = 0, 0
        for _, n in live:
            acc += n; cnt += 1
            if acc >= frac * n_live:
                break
        cover[frac] = cnt
    size_hist = Counter(min(n, 1000) if n < 10 else (10 * (n // 10) if n < 100 else 100 * (n // 100)) for _, n in live)
    extinct = len(amap.members[0])
    summary = {
        "n": a.n, "threshold": a.threshold, "extinct": extinct, "runaway": sum(r["runaway"] for r in rows),
        "attractors": len(live), "singletons": sum(n == 1 for _, n in live),
        "attractors_covering": cover, "size_hist": dict(sorted(size_hist.items())),
    }
    # threshold sensitivity
    sens = {}
    for th in (0.3, 0.7):
        m = AttractorMap(th)
        for s in starts:
            m.assign(sigs[s], s)
        lv = [n for i, n in m.sizes() if i != 0]
        sens[th] = {"attractors": len(lv), "singletons": sum(n == 1 for n in lv), "largest": lv[:5]}
    summary["threshold_sensitivity"] = sens
    top_attr = []
    for aid, n in live[:60]:
        rep = amap.reps[aid]
        mem_sigs = [sigs[m] for m in amap.members[aid]]
        cohesion = statistics.fmean(weighted_jaccard(rep, s) for s in mem_sigs)
        top_attr.append({"id": aid, "basin": n, "basin_frac": round(n / a.n, 4), "ideas": len(rep),
                         "cohesion": round(cohesion, 3), "top": top(rep), "examples": amap.members[aid][:8]})
    log("basin summary", summary)
    for t in top_attr[:25]:
        log(f"  A{t['id']:<5} basin={t['basin']:<5} ideas={t['ideas']:<4} coh={t['cohesion']} {t['top'][:6]} e.g. {t['examples'][:4]}")
    log("named", {k: (v["attractor"], v["top"][:3]) for k, v in named_assign.items()})

    # ---------- stage 2: pairs
    basin_of = {aid: n for aid, n in sizes}

    def joint(label_a, stim_a, label_b, stim_b, group):
        sa, sb = sigs[label_a], sigs[label_b]
        e = run(g, stim_a + stim_b)
        res, sig_ab = classify_pair(sa, sb, e.fires, LATE, UNTIL, a.threshold)
        aid, sim = amap.lookup(sig_ab)
        res.update(group=group, a=label_a, b=label_b, joint_attractor=aid, joint_sim=round(sim, 3),
                   joint_basin=basin_of.get(aid, 0) if aid is not None else 0, joint_top=top(sig_ab, 6),
                   a_top=top(sa, 4), b_top=top(sb, 4))
        return res

    pairs = []
    for x, y in NAMED_PAIRS:
        pairs.append(joint(x, ts.stimuli(x, STRENGTH), y, ts.stimuli(y, STRENGTH), "named"))
    reps = [(aid, amap.members[aid][0]) for aid, _ in live[:a.top_attractors]]
    for (_, x), (_, y) in itertools.combinations(reps, 2):
        pairs.append(joint(x, [(x, STRENGTH)], y, [(y, STRENGTH)], "top_attractors"))
    live_starts = [r["start"] for r in rows if r["attractor"] != 0]
    for _ in range(a.random_pairs):
        x, y = rng.sample(live_starts, 2)
        pairs.append(joint(x, [(x, STRENGTH)], y, [(y, STRENGTH)], "random"))

    pair_summary = {}
    for grp in ("named", "top_attractors", "random"):
        ps = [p for p in pairs if p["group"] == grp]
        kinds = Counter(p["kind"] for p in ps)
        nov = [p for p in ps if p["kind"] == "novel"]
        pair_summary[grp] = {
            "n": len(ps), "kinds": dict(kinds.most_common()),
            "novel_unmapped": sum(p["joint_attractor"] is None for p in nov),
            "novel_known_median_basin": statistics.median([p["joint_basin"] for p in nov if p["joint_attractor"] is not None]) if any(p["joint_attractor"] is not None for p in nov) else None,
        }
    log("pair summary", pair_summary)
    for p in pairs:
        if p["group"] == "named":
            log(f"  {p['a']}+{p['b']}: {p['kind']} massA={p['mass_a']} massB={p['mass_b']} other={p['mass_other']} {p.get('sides', '')} joint={p['joint_top'][:5]} (attr {p['joint_attractor']}, basin {p['joint_basin']})")
    unmapped = [p for p in pairs if p["kind"] == "novel" and p["joint_attractor"] is None]
    for p in unmapped[:20]:
        log(f"  UNMAPPED {p['group']} {p['a']}({p['a_top'][:2]}) + {p['b']}({p['b_top'][:2]}) -> {p['joint_top']}")

    out = {"params": PARAMS, "until": UNTIL, "late": LATE, "summary": summary, "top_attractors": top_attr,
           "named": named_assign, "starts": rows, "pair_summary": pair_summary, "pairs": pairs,
           "attractor_reps": {aid: amap.reps[aid] for aid, _ in live[:200]}}
    with gzip.open(a.out, "wt") as fh:
        json.dump(out, fh, default=str)
    log(f"wrote {a.out}")


if __name__ == "__main__":
    main()
