"""Graph arrays for the ablation experiment, built straight from the ConceptNet 5.7 dump with the importer's
filters (ideanet.conceptnet: English, min weight 0.5, one strongest relation per directed pair).

Per link also records a bitmask of asserting datasets and the surface texts of its assertions (used only to
build ablation families: text references to a removed concept). Output: arrays.npz + texts.json.gz.
"""
import argparse, gzip, json, math, re, time
import numpy as np
from ideanet.conceptnet import REL_WEIGHTS, SYMMETRIC, _term

ap = argparse.ArgumentParser()
ap.add_argument("dump"); ap.add_argument("out")
ap.add_argument("--min-weight", type=float, default=0.5)
a = ap.parse_args()
W = re.compile(r'"weight": ([0-9.eE+-]+)'); DS = re.compile(r'"dataset": "(/d/[^/"]+)'); ST = re.compile(r'"surfaceText": "((?:[^"\\]|\\.)*)"')
edges, dsets, t0, n = {}, [], time.time(), 0
with gzip.open(a.dump, "rt", encoding="utf-8") as fh:
    for line in fh:
        n += 1
        p = line.split("\t")
        if not (p[2].startswith("/c/en/") and p[3].startswith("/c/en/")):
            continue
        rel = p[1][3:].removeprefix("dbpedia/")
        base = REL_WEIGHTS.get(rel)
        if base is None:
            continue
        m = W.search(p[4]); cw = float(m.group(1)) if m else 1.0
        if cw < a.min_weight:
            continue
        s, t = _term(p[2], "en"), _term(p[3], "en")
        if not s or not t or s == t:
            continue
        d = DS.search(p[4]).group(1)
        if d not in dsets:
            dsets.append(d)
        bit = 1 << dsets.index(d)
        st = ST.search(p[4]); st = st.group(1) if st else None
        w = base * min(1.5, math.log1p(cw) / math.log1p(1.0))
        for key in ((s, t), (t, s)) if rel in SYMMETRIC else ((s, t),):
            rec = edges.get(key)
            if rec is None:
                edges[key] = rec = {}
            r = rec.get(rel)
            if r is None:
                rec[rel] = r = [w, 0, []]
            elif abs(w) > abs(r[0]):
                r[0] = w
            r[1] |= bit
            if st and len(r[2]) < 3:
                r[2].append(st)
        if n % 10_000_000 == 0:
            print(f"{time.time()-t0:.0f}s {n:,} lines {len(edges):,} pairs", flush=True)
ids = sorted({x for k in edges for x in k}); idx = {x: i for i, x in enumerate(ids)}
rels = sorted(REL_WEIGHTS); ridx = {r: i for i, r in enumerate(rels)}
E = len(edges)
src = np.empty(E, np.int32); dst = np.empty(E, np.int32); rel = np.empty(E, np.int16)
w = np.empty(E, np.float32); ds = np.empty(E, np.uint32); texts = []
for i, ((s, t), rec) in enumerate(edges.items()):
    best = max(rec, key=lambda r: abs(rec[r][0]))
    src[i], dst[i], rel[i], w[i], ds[i] = idx[s], idx[t], ridx[best], round(rec[best][0], 4), rec[best][1]
    texts.append(rec[best][2])
np.savez_compressed(a.out + "/arrays.npz", src=src, dst=dst, rel=rel, w=w, ds=ds, ids=np.array(ids), rels=np.array(rels),
                    datasets=np.array(dsets))
with gzip.open(a.out + "/texts.json.gz", "wt") as f:
    json.dump(texts, f)
print(f"{len(ids):,} ideas {E:,} links datasets {dsets} {time.time()-t0:.0f}s")
