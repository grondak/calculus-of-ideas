"""Ablation families: which ideas and links each world removes for a concept (see PROTOCOL.md)."""
from __future__ import annotations
import gzip, json, re
from collections import defaultdict
import numpy as np, scipy.sparse as sp
from experiments.ablation.common import undirected

NAMEREL = {"FormOf", "DerivedFrom"}
ALIASREL = {"Synonym", "SimilarTo"}
SUBORD = {"IsA", "PartOf", "InstanceOf", "MannerOf", "MadeOf"}


def variants(name):
    """Singular/plural forms; other inflections come only from ConceptNet FormOf/DerivedFrom links."""
    out = {name, name + "s"}
    if name.endswith(("s", "x", "z", "ch", "sh", "o")):
        out.add(name + "es")
    if name.endswith("y"):
        out.add(name[:-1] + "ies")
    if name.endswith("ies"):
        out.add(name[:-3] + "y")
    elif name.endswith("es") and len(name) > 4:
        out |= {name[:-2], name[:-1]}
    elif name.endswith("s") and len(name) > 3:
        out.add(name[:-1])
    return out


class Families:
    def __init__(self, g, classes_path, names_path, texts_path):
        self.g = g
        self.A = undirected(g.n, g.src, g.dst)
        self.deg = np.asarray(self.A.sum(1)).ravel()
        cl = json.load(gzip.open(classes_path))["classes"]
        self.cls = defaultdict(set)
        for c in cl:
            for m in c["members"]:
                self.cls[m] |= set(c["members"])
        z = np.load(names_path)
        self.epos = np.full(g.n, -1, np.int64); self.epos[z["nodes"]] = np.arange(len(z["nodes"]))
        self.E = z["E"].astype(np.float32)
        lexm = np.isin(g.lex_rel, [g.rels.index(r) for r in NAMEREL])
        self.L = undirected(g.n, g.lex_src[lexm], g.lex_dst[lexm])
        am = np.isin(g.rel, [g.rels.index(r) for r in ALIASREL])
        self.S = undirected(g.n, g.src[am], g.dst[am])
        self.tok = defaultdict(list)
        for i in np.flatnonzero(self.deg > 0):
            for t in set(g.ids[i].split("_")):
                self.tok[t].append(i)
        self.texts_path = texts_path
        self._texts = None
        self.sub = np.isin(g.rel, [g.rels.index(r) for r in SUBORD])

    def cos(self, a, b):
        ia, ib = self.epos[a], self.epos[b]
        return float(self.E[ia] @ self.E[ib]) if ia >= 0 and ib >= 0 else 0.0

    def names(self, c):
        """Ideas that are names of c (not compounds)."""
        g, idx = self.g, self.g.idx
        c_id = g.ids[c]
        fam = {c}
        for v in variants(c_id):
            if v in idx:
                fam.add(idx[v])
        fam |= set(self.L[c].indices)
        fam |= {idx[m] for m in self.cls.get(c_id, ()) if m in idx}
        return fam

    def aliases(self, c):
        """Synonym/SimilarTo neighbours that read as another name of c (and are not bigger hubs than c)."""
        out = set()
        for s in self.S[c].indices:
            if self.cos(c, s) >= 0.5 and self.deg[s] <= 2 * self.deg[c]:
                out |= {self.g.idx[v] for v in variants(self.g.ids[s]) if v in self.g.idx}
        return out

    def compounds(self, fam):
        g = self.g
        out = set()
        for f in fam:
            toks = g.ids[f].split("_")
            forms = set()
            if len(toks) == 1:
                forms = variants(toks[0])
                for t in forms:
                    out |= set(self.tok.get(t, ()))
            else:
                key = "_".join(toks)
                for i in self.tok.get(toks[0], ()):
                    if key in g.ids[i] and re.search(r"(^|_)" + re.escape(key) + r"(_|$)", g.ids[i]):
                        out.add(i)
        return out

    def family(self, c):
        """Removed node sets for ND0/ND/NI1 and removed link masks (over analysis links) for NI2/NI3."""
        g = self.g
        own = self.names(c)
        names = own | self.aliases(c)
        nd = names | self.compounds(own)
        nd = {v for v in nd if self.deg[v] > 0} | {c}
        rem = np.zeros(g.n, bool); rem[list(nd)] = True
        ni1 = rem.copy()
        for _ in range(2):
            toR = np.asarray(self.A[:, ni1].sum(1)).ravel()
            frac = np.where(self.deg > 0, toR / np.maximum(self.deg, 1), 0)
            sub_to = np.zeros(g.n, bool)
            m = self.sub & ni1[g.dst]
            sub_to[g.src[m]] = True
            add = (~ni1) & (self.deg > 0) & ((frac >= 0.5) | (sub_to & (frac >= 0.25)))
            ni1 |= add
        lm = ~(ni1[g.src] | ni1[g.dst])
        forms = set()
        for f in names:
            forms |= variants(g.ids[f]) if "_" not in g.ids[f] else {g.ids[f]}
        pat = re.compile(r"\b(" + "|".join(re.escape(f.replace("_", " ")) for f in sorted(forms, key=len, reverse=True)) + r")\b", re.I)
        texts = self.texts()
        cand = np.flatnonzero(lm)
        ni2 = np.zeros(len(g.src), bool)
        for j in cand:
            ts = texts[g.link_index[j]]
            if ts and any(pat.search(t) for t in ts):
                ni2[j] = True
        nbr = np.zeros(g.n, bool)
        nbr[np.asarray(self.A[:, rem].sum(1)).ravel() > 0] = True
        nbr &= ~ni1
        ni3 = lm & ~ni2 & nbr[g.src] & nbr[g.dst]
        return dict(names=sorted(names), nd=sorted(nd), ni1=sorted(np.flatnonzero(ni1)), ni2_links=np.flatnonzero(ni2),
                    ni3_links=np.flatnonzero(ni3))

    def texts(self):
        if self._texts is None:
            self._texts = json.load(gzip.open(self.texts_path))
        return self._texts
