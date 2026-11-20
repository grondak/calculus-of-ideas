"""Import the English part of ConceptNet 5.x as an IdeaGraph.

Ideas are ConceptNet terms (/c/en/honey_bee -> label "honey bee"); POS/sense
suffixes are collapsed. Each relation type has a base weight; negative types
(Antonym, DistinctFrom, Not*) are inhibitory. Symmetric relations get links in
both directions. Weights are stored raw; apply `normalize_fanout` at run time
so hubs spread their activation instead of igniting the whole graph.
"""
from __future__ import annotations

import gzip
import json
import math

from .graph import Idea, IdeaGraph, Link

REL_WEIGHTS: dict[str, float] = {
    "Synonym": 0.7, "FormOf": 0.7, "SimilarTo": 0.6, "IsA": 0.6, "PartOf": 0.55,
    "HasA": 0.5, "MadeOf": 0.5, "DefinedAs": 0.6, "InstanceOf": 0.5, "MannerOf": 0.5,
    "Causes": 0.55, "UsedFor": 0.5, "CapableOf": 0.5, "AtLocation": 0.5, "LocatedNear": 0.45,
    "HasProperty": 0.45, "CreatedBy": 0.45, "SymbolOf": 0.45, "Entails": 0.45,
    "HasSubevent": 0.35, "HasFirstSubevent": 0.35, "HasLastSubevent": 0.35,
    "HasPrerequisite": 0.35, "MotivatedByGoal": 0.35, "CausesDesire": 0.35, "Desires": 0.35,
    "ReceivesAction": 0.35, "RelatedTo": 0.35, "DerivedFrom": 0.3, "HasContext": 0.2,
    "EtymologicallyRelatedTo": 0.15, "EtymologicallyDerivedFrom": 0.15,
    "Antonym": -0.7, "DistinctFrom": -0.45, "ObstructedBy": -0.4,
    "NotDesires": -0.35, "NotCapableOf": -0.35, "NotHasProperty": -0.35, "NotUsedFor": -0.35,
}
SYMMETRIC = {"RelatedTo", "Synonym", "Antonym", "DistinctFrom", "SimilarTo", "LocatedNear", "EtymologicallyRelatedTo"}


def _term(uri: str, lang: str) -> str | None:
    parts = uri.split("/")  # ['', 'c', 'en', 'honey_bee', 'n', ...]
    return parts[3] if len(parts) > 3 and parts[2] == lang else None


def import_conceptnet(path: str, *, lang: str = "en", min_weight: float = 0.5,
                      relations: dict[str, float] | None = None, log_every: int = 5_000_000) -> IdeaGraph:
    rels = relations or REL_WEIGHTS
    prefix = f"/c/{lang}/"
    edges: dict[tuple[str, str], tuple[float, str]] = {}
    n = 0
    with gzip.open(path, "rt", encoding="utf-8") as fh:
        for line in fh:
            n += 1
            if log_every and n % log_every == 0:
                print(f"  scanned {n:,} lines, kept {len(edges):,} edges", flush=True)
            parts = line.split("\t")
            if not (parts[2].startswith(prefix) and parts[3].startswith(prefix)):
                continue
            rel = parts[1][3:].removeprefix("dbpedia/")
            base = rels.get(rel)
            if base is None:
                continue
            cn_w = json.loads(parts[4]).get("weight", 1.0)
            if cn_w < min_weight:
                continue
            s, t = _term(parts[2], lang), _term(parts[3], lang)
            if not s or not t or s == t:
                continue
            w = base * min(1.5, math.log1p(cn_w) / math.log1p(1.0))
            for key in ((s, t), (t, s)) if rel in SYMMETRIC else ((s, t),):
                old = edges.get(key)
                if old is None or abs(w) > abs(old[0]):
                    edges[key] = (w, rel)

    g = IdeaGraph()
    for s, t in edges:
        for term in (s, t):
            if term not in g.ideas:
                g.add_idea(Idea(term, [term.replace("_", " ")]))
    for (s, t), (w, rel) in edges.items():
        g.add_link(Link(s, t, round(w, 4), relation=rel))
    return g
