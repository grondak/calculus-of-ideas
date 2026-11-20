"""Dynamics measurements, null models and perturbation experiments."""
from __future__ import annotations

import random
import statistics
from collections import Counter, defaultdict
from dataclasses import dataclass
from typing import Callable

from .engine import Engine, Fire
from .graph import IdeaGraph, Link


def windows(fires: list[Fire], width: float, until: float) -> list[frozenset[str]]:
    n = max(1, int(until // width) + 1)
    bins: list[set[str]] = [set() for _ in range(n)]
    for f in fires:
        bins[min(int(f.time // width), n - 1)].add(f.idea)
    return [frozenset(b) for b in bins]


def find_period(seq: list[frozenset[str]], min_repeats: int = 3) -> int | None:
    """Smallest p such that the tail of seq repeats with period p at least min_repeats times."""
    while seq and not seq[-1]:
        seq = seq[:-1]
    n = len(seq)
    for p in range(1, n // min_repeats + 1):
        tail = seq[n - p * min_repeats:]
        if any(tail) and all(tail[i] == tail[i + p] for i in range(len(tail) - p)):
            return p
    return None


@dataclass
class Dynamics:
    kind: str  # extinct | runaway | periodic | persistent
    fires: int
    last_fire: float
    period: int | None
    attractor: list[str]  # ideas active within one period of the attractor
    recurrent_states: int  # distinct non-empty window states seen 2+ times
    path_diversity: dict[str, int]  # idea -> distinct input sets across its fires (ideas firing 2+ times)
    unnamed_fires: int  # fires of ideas with no human word

    def summary(self) -> str:
        top = sorted(self.path_diversity.items(), key=lambda kv: -kv[1])[:5]
        return (
            f"dynamics={self.kind} fires={self.fires} last_fire={self.last_fire:.1f} "
            f"period={self.period} recurrent_states={self.recurrent_states} unnamed_fires={self.unnamed_fires}\n"
            f"attractor={self.attractor}\n"
            f"path_diversity(top)={top}"
        )


def characterize(engine: Engine, until: float, width: float = 1.0) -> Dynamics:
    fires = engine.fires
    last = fires[-1].time if fires else 0.0
    seq = windows(fires, width, until)
    period = find_period(seq)
    trimmed = list(seq)
    while trimmed and not trimmed[-1]:
        trimmed.pop()
    attractor = sorted(set().union(*trimmed[-period:])) if period else []
    counts = Counter(s for s in seq if s)
    inputs_by_idea: dict[str, set[tuple[str, ...]]] = defaultdict(set)
    fire_counts = Counter(f.idea for f in fires)
    for f in fires:
        inputs_by_idea[f.idea].add(tuple(sorted(f.inputs)))
    diversity = {k: len(v) for k, v in inputs_by_idea.items() if fire_counts[k] > 1}
    unnamed = sum(1 for f in fires if not engine.graph.ideas[f.idea].labels)

    if engine.hit_event_limit:
        kind = "runaway"
    elif not fires or last < until - 2 * max(engine.graph.ideas[f.idea].refractory + engine.graph.ideas[f.idea].decay_tau for f in fires):
        kind = "extinct"
    elif period:
        kind = "periodic"
    else:
        kind = "persistent"
    return Dynamics(kind, len(fires), last, period, attractor,
                    sum(1 for c in counts.values() if c > 1), diversity, unnamed)


# --- null models -----------------------------------------------------------

def rewire(graph: IdeaGraph, rng: random.Random, tries: int = 20) -> IdeaGraph:
    """Degree-preserving null: shuffle link targets, keep sources, weights, delays.

    Every idea keeps its out-degree and in-degree; only who-connects-to-whom changes.
    Self-loops and duplicate edges are avoided by retrying.
    """
    links = graph.links
    for _ in range(tries):
        targets = [l.target for l in links]
        rng.shuffle(targets)
        pairs = [(l.source, t) for l, t in zip(links, targets)]
        if all(s != t for s, t in pairs) and len(set(pairs)) == len(pairs):
            break
    g = IdeaGraph()
    for idea in graph.ideas.values():
        g.add_idea(idea)
    for l, t in zip(links, targets):
        g.add_link(Link(l.source, t, l.weight, l.delay, l.context))
    return g


Metric = Callable[[Dynamics], float]

METRICS: dict[str, Metric] = {
    "fires": lambda d: d.fires,
    "recurrent_states": lambda d: d.recurrent_states,
    "max_path_diversity": lambda d: max(d.path_diversity.values(), default=0),
    "persistence": lambda d: d.last_fire,
}


def simulate(graph: IdeaGraph, stimuli: list[tuple[str, float]], until: float, seed: int = 0, **engine_kw) -> tuple[Engine, Dynamics]:
    eng = Engine(graph, seed=seed, **engine_kw)
    for idea, strength in stimuli:
        eng.stimulate(idea, strength)
    eng.run(until)
    return eng, characterize(eng, until)


def null_comparison(graph: IdeaGraph, stimuli: list[tuple[str, float]], until: float,
                    samples: int = 50, seed: int = 0, **engine_kw) -> dict[str, dict[str, float]]:
    """Compare observed metrics against degree-preserving rewired graphs.

    Returns per-metric observed value, null mean/stdev, z-score and an
    empirical one-sided p-value (fraction of nulls >= observed, add-one smoothed).
    """
    _, observed = simulate(graph, stimuli, until, seed=seed, **engine_kw)
    rng = random.Random(seed)
    nulls = [simulate(rewire(graph, rng), stimuli, until, seed=seed, **engine_kw)[1] for _ in range(samples)]
    out = {}
    for name, m in METRICS.items():
        obs = m(observed)
        vals = [m(d) for d in nulls]
        mu = statistics.fmean(vals)
        sd = statistics.pstdev(vals)
        out[name] = {
            "observed": obs, "null_mean": mu, "null_sd": sd,
            "z": (obs - mu) / sd if sd else 0.0,
            "p": (1 + sum(v >= obs for v in vals)) / (1 + samples),
        }
    return out


# --- perturbation ---------------------------------------------------------

def jaccard(a: set, b: set) -> float:
    return len(a & b) / len(a | b) if a | b else 1.0


def perturb_links(graph: IdeaGraph, stimuli: list[tuple[str, float]], until: float,
                  seed: int = 0, top: int = 10, **engine_kw) -> list[dict]:
    """Remove each link in turn and measure how much the dynamics change.

    Links whose removal most changes the attractor/active set are the ones the
    observed pattern actually depends on.
    """
    _, base = simulate(graph, stimuli, until, seed=seed, **engine_kw)
    base_eng, _ = simulate(graph, stimuli, until, seed=seed, **engine_kw)
    base_active = {f.idea for f in base_eng.fires}
    results = []
    for i, link in enumerate(graph.links):
        g = IdeaGraph()
        for idea in graph.ideas.values():
            g.add_idea(idea)
        for j, l in enumerate(graph.links):
            if j != i:
                g.add_link(l)
        eng, d = simulate(g, stimuli, until, seed=seed, **engine_kw)
        results.append({
            "link": f"{link.source}->{link.target} ({link.weight:+.2f})",
            "kind": d.kind,
            "fires_delta": d.fires - base.fires,
            "active_jaccard": round(jaccard(base_active, {f.idea for f in eng.fires}), 3),
            "attractor_jaccard": round(jaccard(set(base.attractor), set(d.attractor)), 3),
        })
    results.sort(key=lambda r: (r["attractor_jaccard"], r["active_jaccard"], -abs(r["fires_delta"])))
    return results[:top]


def shuffle_targets(graph: IdeaGraph, rng: random.Random, mode: str = "relation") -> tuple[Callable[[], None], dict]:
    """In-place degree-preserving rewiring for graphs too large to copy.

    Sources, weights, delays and relation types stay on their links; only targets move.
    Every idea keeps its in- and out-degree (per relation type for "relation"/"reciprocal").

    mode="global":     shuffle all targets.
    mode="relation":   shuffle targets within each relation type.
    mode="reciprocal": like "relation", but links whose reverse exists (same relation) are
                       re-paired as reciprocal pairs, so every idea keeps its reciprocal degree
                       and the graph keeps its reciprocity. One-way links shuffle within relation.

    Returns (restore, stats); call restore() to undo.
    """
    links = graph.links
    original = [l.target for l in links]
    stats = {"links": len(links), "reciprocal_links": 0}

    def restore() -> None:
        for l, t in zip(links, original):
            l.target = t

    if mode == "global":
        t = original[:]
        rng.shuffle(t)
        for l, x in zip(links, t):
            l.target = x
    elif mode in ("relation", "reciprocal"):
        reciprocal: dict[str | None, list[int]] = defaultdict(list)
        one_way: dict[str | None, list[int]] = defaultdict(list)
        if mode == "reciprocal":
            index = {k: i for i, k in enumerate(graph.ideas)}
            rels = {r: i for i, r in enumerate({l.relation for l in links})}
            n, nr = len(index), len(rels)
            key = lambda s, t, r: (index[s] * n + index[t]) * nr + rels[r]
            present = {key(l.source, l.target, l.relation) for l in links}
            for i, l in enumerate(links):
                is_rec = l.source != l.target and key(l.target, l.source, l.relation) in present
                (reciprocal if is_rec else one_way)[l.relation].append(i)
            del present
        else:
            for i, l in enumerate(links):
                one_way[l.relation].append(i)
        for idxs in one_way.values():
            t = [original[i] for i in idxs]
            rng.shuffle(t)
            for i, x in zip(idxs, t):
                links[i].target = x
        for idxs in reciprocal.values():
            stubs = idxs[:]
            rng.shuffle(stubs)
            stats["reciprocal_links"] += len(stubs)
            for a, b in zip(stubs[0::2], stubs[1::2]):
                links[a].target, links[b].target = links[b].source, links[a].source
    else:
        raise ValueError(mode)
    stats["self_loops"] = sum(l.source == l.target for l in links)
    return restore, stats
