"""Shared graph loading for the conceptual ablation-and-recovery experiment.

Analysis graph = ConceptNet 5.7 English links (importer filters) minus lexical relations (FormOf, DerivedFrom,
Etymologically*, HasContext) minus links asserted only by Wiktionary (gazetteer noise). Lexical / Wiktionary links
are kept separately (`lex_*`) and used only to build name families of ablated concepts, never by a detector.
"""
from __future__ import annotations
import numpy as np, scipy.sparse as sp

LEX = {"FormOf", "DerivedFrom", "EtymologicallyRelatedTo", "EtymologicallyDerivedFrom", "HasContext"}


class Graph:
    pass


def load(path):
    z = np.load(path)
    g = Graph()
    g.ids = [str(x) for x in z["ids"]]; g.rels = [str(r) for r in z["rels"]]
    g.idx = {t: i for i, t in enumerate(g.ids)}
    g.n, g.R = len(g.ids), len(g.rels)
    src, dst, rel, ds = z["src"], z["dst"], z["rel"], z["ds"]
    dsets = [str(d) for d in z["datasets"]]
    wk = 1 << dsets.index("/d/wiktionary")
    lex = np.isin(rel, [g.rels.index(r) for r in LEX])
    keep = (ds != wk) & ~lex & (src != dst)
    g.src, g.dst, g.rel, g.w = src[keep], dst[keep], rel[keep], z["w"][keep]
    g.link_index = np.flatnonzero(keep)
    g.lex_src, g.lex_dst, g.lex_rel = src[~keep], dst[~keep], rel[~keep]
    g.deg0 = degree(g.n, g.src, g.dst)
    return g


def undirected(n, s, d, mask=None):
    if mask is not None:
        s, d = s[mask], d[mask]
    A = sp.coo_matrix((np.ones(len(s), np.float32), (s, d)), shape=(n, n)).tocsr()
    A = (A + A.T).tocsr()
    A.data[:] = 1
    return A


def degree(n, s, d, mask=None):
    return np.asarray(undirected(n, s, d, mask).sum(1)).ravel()
