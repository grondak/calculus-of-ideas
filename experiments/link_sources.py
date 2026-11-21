"""Attach ConceptNet source-dataset provenance to every link in graph-arrays.npz.

Rescans the ConceptNet dump with the importer's filters and records, for each (source, target, relation)
link, a bitmask of the datasets (e.g. /d/wiktionary, /d/conceptnet, /d/wordnet) that assert it.
"""
import argparse, gzip, re, time
import numpy as np
from ideanet.conceptnet import REL_WEIGHTS, SYMMETRIC, _term

ap = argparse.ArgumentParser()
ap.add_argument("dump"); ap.add_argument("arrays"); ap.add_argument("out")
ap.add_argument("--min-weight", type=float, default=0.5)
a = ap.parse_args()
G = np.load(a.arrays, allow_pickle=True)
ids, rels = list(G["ids"]), list(G["rels"])
idx = {t: i for i, t in enumerate(ids)}
ridx = {r: i for i, r in enumerate(rels)}
n = len(ids)
key = (G["src"].astype(np.int64) * n + G["dst"]) * len(rels) + G["rel"]
order = np.argsort(key); skey = key[order]
DS = re.compile(r'"dataset": "(/d/[^/"]+)'); W = re.compile(r'"weight": ([0-9.eE+-]+)')
names, mask = [], np.zeros(len(key), np.uint32)
t0, lines, hits = time.time(), 0, 0
batch_k, batch_b = [], []

def flush():
    global batch_k, batch_b, hits
    if not batch_k:
        return
    k = np.array(batch_k, np.int64); b = np.array(batch_b, np.uint32)
    pos = np.searchsorted(skey, k); pos[pos >= len(skey)] = 0
    ok = skey[pos] == k
    np.bitwise_or.at(mask, order[pos[ok]], b[ok]); hits += int(ok.sum())
    batch_k, batch_b = [], []

with gzip.open(a.dump, "rt", encoding="utf-8") as fh:
    for line in fh:
        lines += 1
        p = line.split("\t")
        if not (p[2].startswith("/c/en/") and p[3].startswith("/c/en/")):
            continue
        rel = p[1][3:].removeprefix("dbpedia/")
        if rel not in REL_WEIGHTS or rel not in ridx:
            continue
        m = W.search(p[4])
        if m and float(m.group(1)) < a.min_weight:
            continue
        s, t = _term(p[2], "en"), _term(p[3], "en")
        if not s or not t or s == t or s not in idx or t not in idx:
            continue
        d = DS.search(p[4]).group(1)
        if d not in names:
            names.append(d)
        bit = 1 << names.index(d)
        r = ridx[rel]
        for x, y in ((s, t), (t, s)) if rel in SYMMETRIC else ((s, t),):
            batch_k.append((idx[x] * n + idx[y]) * len(rels) + r); batch_b.append(bit)
        if len(batch_k) > 2_000_000:
            flush()
            print(f"{time.time()-t0:.0f}s {lines:,} lines", flush=True)
flush()
print("datasets", names, "link hits", hits, "links without provenance", int((mask == 0).sum()))
for i, d in enumerate(names):
    only = int((mask == (1 << i)).sum()); anyd = int(((mask >> i) & 1).sum())
    print(f"  {d}: asserts {anyd:,} links, sole source of {only:,}")
np.savez_compressed(a.out, mask=mask, names=np.array(names))
