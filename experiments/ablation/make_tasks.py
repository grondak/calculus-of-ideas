"""Blind task files from the sealed key (PROTOCOL.md): seeded reconstruction/identification tasks and detection pools.

Writes OUT/blind/tasks.json (seeds, anonymous candidate profiles, pools) and OUT/key/tasks_key.json (answers)."""
import argparse, gzip, json, os
import numpy as np
from experiments.ablation.common import load, undirected

ap = argparse.ArgumentParser()
ap.add_argument("out")
ap.add_argument("--arrays", default=os.path.expanduser("~/data/abl/arrays.npz"))
ap.add_argument("--names", default=os.path.expanduser("~/data/abl/names-minilm.npz"))
ap.add_argument("--seed", type=int, default=2)
ap.add_argument("--pool-per-concept", type=int, default=30)
a = ap.parse_args()
rng = np.random.default_rng(a.seed)
g = load(a.arrays)
A = undirected(g.n, g.src, g.dst); deg = np.asarray(A.sum(1)).ravel()
key = json.load(gzip.open(a.out + "/key/key.json.gz")); fams = json.load(gzip.open(a.out + "/key/families.json.gz"))
z = np.load(a.names); epos = np.full(g.n, -1); epos[z["nodes"]] = np.arange(len(z["nodes"])); E = z["E"].astype(np.float32)
W = key["worlds"]; byb = {}
for wid, w in W.items():
    byb.setdefault(w["batch"], {})[w["kind"]] = wid
intact, null = byb[0]["INTACT"], byb[0]["NULL"]
foot = np.zeros(g.n, bool)
for c, f in fams.items():
    foot[f["ni1"]] = True
    foot[A[f["nd"]].indices] = True
bg_pool = np.flatnonzero((deg >= 2) & ~foot)
dbin = np.digitize(np.log(np.maximum(deg, 1)), np.linspace(0, 10, 41))

def matched(nodes, k):
    out = []
    for v in nodes:
        cand = bg_pool[dbin[bg_pool] == dbin[v]]
        out += list(rng.choice(cand, size=k, replace=len(cand) < k)) if len(cand) else []
    return out

seeded, skey, pools, pkey = [], {}, {}, {}
for c, kc in key["concepts"].items():
    node = kc["node"]; fam = set(fams[c]["ni1"])
    prof = lambda v: [int(x) for x in A[v].indices]
    # decoys
    el = np.flatnonzero(~foot & (deg >= 2)); dd = np.abs(np.log(deg[el]) - np.log(deg[node]))
    dc = el[dd < 0.2] if (dd < 0.2).sum() >= 19 else el[np.argsort(dd)[:19]]  # degree-matched random decoys
    rand = rng.choice(dc, size=19, replace=False).tolist()
    nb = A[node].indices
    co = np.asarray(A[nb].sum(0)).ravel(); co[list(fam)] = 0; co[node] = 0
    jac = co / (deg + len(nb) - co + 1e-9); jac[~(deg >= 2)] = 0
    hard_g = [int(x) for x in np.argsort(-jac)[:5]]
    sims = E @ E[epos[node]]; order = z["nodes"][np.argsort(-sims)]
    hard_l = [int(x) for x in order if x not in fam and x not in hard_g and deg[x] >= 2][:4]
    for kind in ("ND0", "ND", "NI1", "NI2", "NI3"):
        wid = byb[kc["batch"]][kind]
        tg = list(kc["targets"][wid])
        for k in (1, 3):
            if len(tg) < k + 2:
                continue
            seeds = [int(x) for x in rng.choice(tg, size=k, replace=False)]
            cands = [("true", node)] + [("rand", x) for x in rand] + [("hard", x) for x in hard_g + hard_l]
            perm = rng.permutation(len(cands))
            tid = f"T{len(seeded):05d}"
            cand_profiles = [[x for x in prof(cands[i][1]) if x not in seeds] for i in perm]
            seeded.append({"task": tid, "world": wid, "seeds": seeds, "candidates": cand_profiles,
                           "candidate_names": [g.ids[cands[i][1]].replace("_", " ") for i in perm]})
            skey[tid] = {"concept": c, "kind": kind, "k": k, "labels": [cands[i][0] for i in perm],
                         "cand_nodes": [int(cands[i][1]) for i in perm]}
# detection pools: the same seed nodes in every world of a batch (paired comparison)
for b, kinds in byb.items():
    aff, who = [], []
    for c, kc in key["concepts"].items():
        if kc["batch"] != b:
            continue
        tg = [int(x) for x in kc["targets"][kinds["ND"]]]
        s = rng.choice(tg, size=min(a.pool_per_concept, len(tg)), replace=False).tolist()
        aff += s; who += [c] * len(s)
    bg = matched(aff, 5)
    nodes = np.array(aff + bg); lab = who + [None] * len(bg)
    perm = rng.permutation(len(nodes))
    nodes, lab = nodes[perm].tolist(), [lab[i] for i in perm]
    for kind, wid in kinds.items():
        if kind not in ("INTACT", "NULL"):
            pools[wid] = nodes
    pkey[str(b)] = {"nodes": nodes, "concept": lab}
pools[intact] = pools[null] = sorted(set().union(*(set(p["nodes"]) for p in pkey.values())))
json.dump({"seeded": seeded, "pools": pools}, open(a.out + "/blind/tasks.json", "w"))
json.dump({"seeded": skey, "pools": pkey}, open(a.out + "/key/tasks_key.json", "w"))
print(len(seeded), "seeded tasks;", {w: len(p) for w, p in pools.items()})
