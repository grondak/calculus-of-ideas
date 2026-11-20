"""Word-independent attractor identity.

A run's attractor signature is the distribution of firings over ideas (by id, not by
word) in a late window. Two runs reach the same dynamical region when their signatures
overlap, even if their activation sequences differ.
"""
from __future__ import annotations

import math
from collections import Counter, defaultdict

from .engine import Fire

Signature = dict[str, float]


def signature(fires: list[Fire], start: float, end: float = math.inf) -> Signature:
    c = Counter(f.idea for f in fires if start <= f.time < end)
    total = sum(c.values())
    return {k: v / total for k, v in c.items()} if total else {}


def weighted_jaccard(a: Signature, b: Signature) -> float:
    """sum(min)/sum(max): 1 = identical distribution, 0 = disjoint. Two empty signatures = 1."""
    if not a and not b:
        return 1.0
    keys = a.keys() | b.keys()
    return sum(min(a.get(k, 0), b.get(k, 0)) for k in keys) / sum(max(a.get(k, 0), b.get(k, 0)) for k in keys)


def jensen_shannon(a: Signature, b: Signature) -> float:
    """JS divergence in bits (0 = identical, 1 = disjoint)."""
    if not a or not b:
        return 0.0 if a == b else 1.0
    d = 0.0
    for k in a.keys() | b.keys():
        p, q = a.get(k, 0.0), b.get(k, 0.0)
        m = (p + q) / 2
        d += (p * math.log2(p / m) if p else 0) + (q * math.log2(q / m) if q else 0)
    return d / 2


def mass(sig: Signature, ideas) -> float:
    return sum(sig.get(i, 0.0) for i in ideas)


class AttractorMap:
    """Greedy online clustering of signatures into attractors.

    A signature joins the most similar existing attractor if weighted Jaccard with its
    representative (first member) is >= threshold; otherwise it founds a new attractor.
    Attractor 0 is reserved for extinction (empty signature).
    """

    EXTINCT = 0

    def __init__(self, threshold: float = 0.5) -> None:
        self.threshold = threshold
        self.reps: list[Signature] = [{}]
        self.members: list[list[str]] = [[]]
        self._index: dict[str, set[int]] = defaultdict(set)

    def lookup(self, sig: Signature) -> tuple[int | None, float]:
        if not sig:
            return self.EXTINCT, 1.0
        cands = set().union(*(self._index.get(k, ()) for k in sig))
        best, best_sim = None, 0.0
        for c in cands:
            s = weighted_jaccard(sig, self.reps[c])
            if s > best_sim:
                best, best_sim = c, s
        return (best, best_sim) if best_sim >= self.threshold else (None, best_sim)

    def assign(self, sig: Signature, label: str) -> int:
        aid, _ = self.lookup(sig)
        if aid is None:
            aid = len(self.reps)
            self.reps.append(sig)
            self.members.append([])
            for k in sig:
                self._index[k].add(aid)
        self.members[aid].append(label)
        return aid

    def sizes(self) -> list[tuple[int, int]]:
        return sorted(((i, len(m)) for i, m in enumerate(self.members) if m), key=lambda x: -x[1])


def classify_pair(sig_a: Signature, sig_b: Signature, fires_ab: list[Fire], start: float, end: float,
                  threshold: float = 0.5, bins: int = 5) -> dict:
    """What happens when the stimuli behind attractors A and B are applied together?

    dominate_a / dominate_b: joint run lives mostly in one side's region.
    coexist:   both regions hold >= 20% of joint late firing, steadily.
    alternate: sub-windows switch between A-dominated and B-dominated at least twice.
    novel:     >= 50% of joint late firing falls outside both regions.
    same:      A and B were already the same attractor.
    """
    sig_ab = signature(fires_ab, start, end)
    out = {"sim_a_b": round(weighted_jaccard(sig_a, sig_b), 3),
           "sim_ab_a": round(weighted_jaccard(sig_ab, sig_a), 3),
           "sim_ab_b": round(weighted_jaccard(sig_ab, sig_b), 3)}
    ma, mb = mass(sig_ab, sig_a), mass(sig_ab, sig_b)
    other = 1.0 - mass(sig_ab, sig_a.keys() | sig_b.keys()) if sig_ab else 0.0
    out.update(mass_a=round(ma, 3), mass_b=round(mb, 3), mass_other=round(other, 3))
    if sig_a and sig_b and out["sim_a_b"] >= threshold:
        kind = "same"
    elif not sig_ab:
        kind = "extinct"
    elif other >= 0.5:
        kind = "novel"
    elif ma >= 0.2 and mb >= 0.2:
        width = (end - start) / bins
        sides = []
        for i in range(bins):
            s = signature(fires_ab, start + i * width, start + (i + 1) * width)
            a, b = mass(s, sig_a), mass(s, sig_b)
            sides.append("A" if a > 2 * b else "B" if b > 2 * a else "-")
        seq = [x for x in sides if x != "-"]
        switches = sum(1 for x, y in zip(seq, seq[1:]) if x != y)
        out["sides"] = "".join(sides)
        kind = "alternate" if switches >= 2 else "coexist"
    else:
        kind = "dominate_a" if ma > mb else "dominate_b"
    out["kind"] = kind
    return out, sig_ab
