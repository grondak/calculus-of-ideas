"""Build ablation worlds, blind task files and a sealed answer key for a list of concepts (PROTOCOL.md).

Writes OUT/blind/{worlds/W*.npz, tasks.json, pool.json} (all the recovery program may read) and
OUT/key/{key.json.gz, families.json.gz} (scorer only). World IDs are anonymous and shuffled.
"""
import argparse, gzip, json, os, sys
import numpy as np
from experiments.ablation.common import load, undirected
from experiments.ablation.families import Families
from experiments.morphology import shuffle_dst

ap = argparse.ArgumentParser()
ap.add_argument("concepts"); ap.add_argument("out")
ap.add_argument("--arrays", default=os.path.expanduser("~/data/abl/arrays.npz"))
ap.add_argument("--names", default=os.path.expanduser("~/data/abl/names-minilm.npz"))
ap.add_argument("--texts", default=os.path.expanduser("~/data/abl/texts.json.gz"))
ap.add_argument("--classes", default="experiments/results-merged/classes.json.gz")
ap.add_argument("--seed", type=int, default=1)
ap.add_argument("--max-batches", type=int, default=12)
ap.add_argument("--limit", type=int, default=0, help="keep the first N concepts that pass the checks")
ap.add_argument("--max-family", type=int, default=0, help="skip concepts whose ND family is larger")
a = ap.parse_args()
rng = np.random.default_rng(a.seed)
g = load(a.arrays)
F = Families(g, a.classes, a.names, a.texts)
A, deg = F.A, F.deg
core = deg >= 2
conc = [l.split() for l in open(a.concepts) if l.strip() and not l.startswith("#")]
fams, info = {}, {}
for cat, c in conc:
    if c not in g.idx or deg[g.idx[c]] == 0:
        print("skip (absent)", c); continue
    if a.limit and len(fams) >= a.limit:
        break
    f = F.family(g.idx[c]); f["cat"] = cat
    if a.max_family and len(f["nd"]) > a.max_family:
        print("skip (family > max)", c); continue
    ni1 = np.zeros(g.n, bool); ni1[f["ni1"]] = True
    nbr = np.flatnonzero((np.asarray(A[:, f["nd"]].sum(1)).ravel() > 0) & ~ni1 & core)
    f["nbr"] = nbr
    if len(nbr) < 5:
        print("skip (<5 surviving neighbours)", c); continue
    fams[c] = f
    print(f"{cat:9s} {c:14s} deg {deg[g.idx[c]]:5.0f} names {len(f['names']):3d} nd {len(f['nd']):5d} ni1 {len(f['ni1']):5d} "
          f"ni2 {len(f['ni2_links']):3d} ni3 {len(f['ni3_links']):5d} nbr {len(nbr):5d}", flush=True)
# batches: concepts whose removed sets and surviving neighbourhoods are disjoint share a world
# batches: a concept's removed ideas must not touch another batch member's footprint (removed ideas + surviving
# neighbours), and two members may share at most 10% of the smaller surviving neighbourhood
rem_ = {c: set(f["ni1"]) for c, f in fams.items()}; nb_ = {c: set(f["nbr"].tolist()) for c, f in fams.items()}
def clash(c, o):
    return bool(rem_[c] & (rem_[o] | nb_[o]) or rem_[o] & nb_[c]) or len(nb_[c] & nb_[o]) > 0.1 * min(len(nb_[c]), len(nb_[o]))
batches = []
for c in sorted(fams, key=lambda c: -len(nb_[c])):
    for b in batches:
        if not any(clash(c, o) for o in b):
            b.append(c); break
    else:
        batches.append([c])
print("batches", [len(b) for b in batches])
assert len(batches) <= a.max_batches

L = len(g.src)
def node_mask(nodes):
    m = np.zeros(g.n, bool); m[list(nodes)] = True; return m

def sham(removed_links, protect):
    """Remove, for each survivor, as many random other links as it lost (no coherent missing idea)."""
    lost = np.zeros(g.n, np.int64)
    rs, rd = g.src[removed_links], g.dst[removed_links]
    for x, y in ((rs, rd), (rd, rs)):
        ok = ~protect[x]; np.add.at(lost, x[ok], 1)
    keep = np.ones(L, bool)
    inc = {}
    cand = np.flatnonzero(~(protect[g.src] | protect[g.dst]))
    order = rng.permutation(cand)
    need = lost.copy()
    for j in order:
        s, d = g.src[j], g.dst[j]
        if need[s] > 0 or need[d] > 0:
            keep[j] = False; need[s] -= 1; need[d] -= 1
    return keep

worlds, key = [], {"concepts": {}, "worlds": {}}
famout = {}
for bi, b in enumerate(batches):
    nd = node_mask(set().union(*(fams[c]["nd"] for c in b)))
    nd0 = node_mask([g.idx[c] for c in b])
    ni1 = node_mask(set().union(*(fams[c]["ni1"] for c in b)))
    ni2l = np.zeros(L, bool); ni3l = np.zeros(L, bool)
    for c in b:
        ni2l[fams[c]["ni2_links"]] = True; ni3l[fams[c]["ni3_links"]] = True
    k_nd = ~(nd[g.src] | nd[g.dst]); k_nd0 = ~(nd0[g.src] | nd0[g.dst]); k_ni1 = ~(ni1[g.src] | ni1[g.dst])
    k_ni2 = k_ni1 & ~ni2l; k_ni3 = k_ni2 & ~ni3l
    k_shnd = sham(np.flatnonzero(~k_nd), nd)
    k_shni = sham(np.flatnonzero(~k_ni2 & ~(ni1[g.src] & ni1[g.dst])), ni1)
    if bi == 0:
        dsh = shuffle_dst(g.src, g.dst, g.rel, "reciprocal", np.random.default_rng(a.seed * 1000), g.n)
    spec = {"ND0": (k_nd0, None), "ND": (k_nd, None), "NI1": (k_ni1, None), "NI2": (k_ni2, None), "NI3": (k_ni3, None),
            "SHAM-ND": (k_shnd, None), "SHAM-NI2": (k_shni, None), "NULL": (np.ones(L, bool), dsh),
            "NULL-ND": (~(nd[g.src] | nd[dsh]), dsh), "INTACT": (np.ones(L, bool), None)}
    for kind, (keep, dd) in spec.items():
        if kind in ("INTACT", "NULL") and bi > 0:
            continue
        worlds.append((bi, kind, keep, dd))
    for c in b:
        f = fams[c]
        famout[c] = {k: [int(x) for x in f[k]] for k in ("names", "nd", "ni1")}
        famout[c]["ni2_links"] = f["ni2_links"].tolist(); famout[c]["ni3_links"] = f["ni3_links"].tolist()
        key["concepts"][c] = {"cat": f["cat"], "batch": bi, "node": g.idx[c], "deg": float(deg[g.idx[c]]),
                              "n_names": len(f["names"]), "n_nd": len(f["nd"]), "n_ni1": len(f["ni1"]),
                              "n_ni2": len(f["ni2_links"]), "n_ni3": len(f["ni3_links"])}
ids = rng.permutation(len(worlds))
os.makedirs(a.out + "/blind/worlds", exist_ok=True); os.makedirs(a.out + "/key", exist_ok=True)
for wid, (bi, kind, keep, dd) in zip(ids, worlds):
    d = g.dst if dd is None else dd
    np.savez_compressed(f"{a.out}/blind/worlds/W{wid:03d}.npz", src=g.src[keep], dst=d[keep], rel=g.rel[keep], n=g.n)
    key["worlds"][f"W{wid:03d}"] = {"batch": int(bi), "kind": kind, "removed_links": int((~keep).sum())}
    # surviving neighbours of each concept, with intact relation/direction (reconstruction target)
    if kind in ("ND0", "ND", "NI1", "NI2", "NI3"):
        Aw = undirected(g.n, g.src, d, keep)
        degw = np.asarray(Aw.sum(1)).ravel()
        for c in batches[bi]:
            f = fams[c]; famset = node_mask(f["nd"] if kind != "ND0" else [g.idx[c]])
            m = famset[g.src] ^ famset[g.dst]
            other = np.where(famset[g.src[m]], g.dst[m], g.src[m])
            outward = famset[g.src[m]]
            alive = degw[other] >= 2
            tgt = {}
            for o, r, out in zip(other[alive], g.rel[m][alive], outward[alive]):
                tgt.setdefault(int(o), []).append([g.rels[r], bool(out)])
            key["concepts"][c].setdefault("targets", {})[f"W{wid:03d}"] = tgt
json.dump({"n": g.n, "worlds": sorted(key["worlds"])}, open(a.out + "/blind/worlds.json", "w"))
with gzip.open(a.out + "/key/key.json.gz", "wt") as fh:
    json.dump(key, fh)
with gzip.open(a.out + "/key/families.json.gz", "wt") as fh:
    json.dump(famout, fh)
print("worlds", len(worlds))
