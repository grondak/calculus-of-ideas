"""Ontology builders: synthetic graphs for scale and 'unfamiliar' link injection."""
from __future__ import annotations

import random

from .graph import Idea, IdeaGraph, Link


def random_ontology(n: int = 1000, k: int = 4, *, seed: int = 0, inhibitory: float = 0.2,
                    unnamed: float = 0.1, communities: int = 20, p_within: float = 0.85,
                    weight: tuple[float, float] = (0.35, 0.75)) -> IdeaGraph:
    """Community-structured random idea graph.

    Ideas are grouped into communities; most links stay within a community
    (like a topical cluster), some cross between them. A fraction of ideas
    have no human word. Each idea gets ~k out-links.
    """
    rng = random.Random(seed)
    g = IdeaGraph()
    comm = [i % communities for i in range(n)]
    members: dict[int, list[int]] = {}
    for i, c in enumerate(comm):
        members.setdefault(c, []).append(i)
    for i in range(n):
        labels = [] if rng.random() < unnamed else [f"c{comm[i]}.w{i}"]
        g.add_idea(Idea(f"i{i}", labels))
    for i in range(n):
        seen = set()
        for _ in range(k):
            pool = members[comm[i]] if rng.random() < p_within else range(n)
            j = rng.choice(list(pool))
            if j == i or j in seen:
                continue
            seen.add(j)
            w = rng.uniform(*weight) * (-1 if rng.random() < inhibitory else 1)
            g.add_link(Link(f"i{i}", f"i{j}", round(w, 3), delay=round(rng.uniform(0.5, 2.0), 2)))
    return g


def inject_unfamiliar(graph: IdeaGraph, n: int, *, seed: int = 0, weight: float = 0.6) -> list[Link]:
    """Add n 'bee-axle' links: structurally plausible but between unrelated ideas
    (no existing path of length <= 2). Returns the links added."""
    rng = random.Random(seed)
    ids = sorted(graph.ideas)
    near = {i: {l.target for l in graph.out_links[i]} for i in ids}
    added: list[Link] = []
    attempts = 0
    while len(added) < n and attempts < n * 200:
        attempts += 1
        a, b = rng.sample(ids, 2)
        two_hop = near[a] | {t for m in near[a] for t in near[m]}
        if b in two_hop:
            continue
        added.append(graph.add_link(Link(a, b, weight, delay=1.0)))
        near[a].add(b)
    return added


def normalize_fanout(graph: IdeaGraph, budget: float = 3.0, alpha: float = 0.5) -> None:
    """Scale each idea's out-links by min(1, budget / total_excitatory_out) ** alpha, in place.

    alpha=0 leaves weights alone; alpha=1 caps every idea's total excitatory
    output at `budget`. In between, hubs are damped without silencing them.
    """
    for links in graph.out_links.values():
        total = sum(l.weight for l in links if l.weight > 0)
        if total > budget:
            scale = (budget / total) ** alpha
            for l in links:
                l.weight *= scale
