"""Fixed-core sparse-region test with many null graphs (no re-mining).

The real typed groups and candidate pairs are built exactly as in boundaries.py. Each null graph (generated at the
original-ID level, then contracted with the same class map) is only used to count links between the fixed real cores,
so thousands of nulls are affordable. For every dominant-relation stratum the real linked share is compared with the
null distribution: empirical p (one-sided, real <= null), z-score, and Benjamini-Hochberg q across strata per mode.
No edges are proposed and nothing is named.
"""
import argparse, gzip, json
from multiprocessing import Pool
from pathlib import Path

import numpy as np

from experiments.boundaries import MODES, adjacency, score, _G, _init
from experiments.morphology import CATEGORY, LEX, log, shuffle_dst, null_strata
from experiments.typed_groups import UNTYPED, features, Space, mine
from experiments.profile_null import profile_classes, profile_plan, profile_shuffle


def bh(p):
    p = np.asarray(p, float); o = np.argsort(p); q = np.empty_like(p)
    q[o] = np.minimum.accumulate((p[o] * len(p) / np.arange(1, len(p) + 1))[::-1])[::-1]
    return np.minimum(q, 1)


def _fixed(args):
    mode, seed = args
    g = _G
    rng = np.random.default_rng(71000 + 100000 * MODES.index(mode) + seed)
    if mode in ("profile", "profile2"):
        s, d = profile_shuffle(g["src"], g["dst"], g["plans"][mode], rng)
    else:
        s, d = g["src"], shuffle_dst(g["src"], g["dst"], g["rel"], mode, rng, g["n"], g["strata"], g["rec"])
    s, d = g["mp"][s], g["mp"][d]
    A = adjacency(g["n"], s, d, g["crel"][g["rel"]])
    Co, bi, bj = g["Co"], g["bi"], g["bj"]
    x = np.asarray((Co[bi] @ A).multiply(Co[bj]).sum(1)).ravel() > 0
    return mode, seed, np.array([x[w].mean() for w in g["W"]])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("arrays"); ap.add_argument("real", help="typed-groups.json.gz (settings)"); ap.add_argument("out")
    ap.add_argument("--keep"); ap.add_argument("--sources", required=True); ap.add_argument("--merge")
    ap.add_argument("--nulls", type=int, default=1000); ap.add_argument("--modes", default=",".join(MODES))
    ap.add_argument("--workers", type=int, default=2); ap.add_argument("--min-pairs", type=int, default=20)
    ap.add_argument("--s-min", type=float, default=0.99); ap.add_argument("--k-min", type=float, default=2)
    a = ap.parse_args()
    modes = a.modes.split(",")
    st = json.load(gzip.open(a.real, "rt"))["summary"]["settings"]
    z = np.load(a.arrays)
    ids, rels = [str(x) for x in z["ids"]], [str(x) for x in z["rels"]]
    n, R = len(ids), len(rels)
    keep = np.load(a.keep)["keep"] if a.keep else np.ones(len(z["src"]), bool)
    src, dst, rel = z["src"][keep], z["dst"][keep], z["rel"][keep]
    ds = np.load(a.sources)["mask"][keep]
    frame_rel = np.array([r not in UNTYPED and r not in CATEGORY for r in rels])
    crel = np.array([r not in LEX for r in rels])
    vis = np.ones(n, bool)
    mp = np.load(a.merge)["cls"] if a.merge else np.arange(n)
    ms, md = mp[src], mp[dst]
    rows, codes = features(n, ms, md, rel, frame_rel, vis, None)
    space = Space(n, rows, codes, st["min_df"], st["max_df"])
    X = space.matrix(rows, codes); space.set_members(X, st["max_member_features"]); X = space.matrix(rows, codes)
    A = adjacency(n, ms, md, crel[rel])
    groups = mine(X)
    r = score(groups, space.codes, A, n, a.s_min, a.k_min)
    keys = [k for k in np.unique(r["rp"]) if (r["rp"] == k).sum() >= a.min_pairs]
    W = [r["rp"] == k for k in keys]
    real = np.array([(r["cross"][w] > 0).mean() for w in W])
    log(f"real: {len(groups):,} groups, {len(r['i']):,} candidate pairs, {len(keys)} strata")
    strata, rec = null_strata(src, dst, rel, n, R, ds)
    plans = {}
    for lv, mname in ((1, "profile"), (2, "profile2")):
        if mname in modes:
            plans[mname] = profile_plan(n, src, dst, rel, ds, profile_classes(n, src, dst, rel, frame_rel, R, lv), R)
    kw = dict(src=src, dst=dst, rel=rel, n=n, strata=strata, rec=rec, plans=plans, crel=crel, mp=mp,
              Co=r["Co"], bi=r["i"], bj=r["j"], W=W)
    res = {m: np.zeros((a.nulls, len(keys))) for m in modes}
    with Pool(a.workers, initializer=_init, initargs=(kw,)) as pool:
        for k_, (m, s_, x) in enumerate(pool.imap_unordered(_fixed, [(m, s_) for s_ in range(a.nulls) for m in modes], chunksize=4)):
            res[m][s_] = x
            if k_ % 200 == 0:
                log(f"  null {k_}/{a.nulls * len(modes)}")
    N = a.nulls
    out = []
    for t, k in enumerate(keys):
        out.append(dict(relations=f"{rels[k // 1000]} x {rels[k % 1000]}", pairs=int(W[t].sum()), linked_share=round(float(real[t]), 3)))
    for m in modes:
        sh = res[m]
        p_lo = (1 + (sh <= real).sum(0)) / (1 + N)
        p_hi = (1 + (sh >= real).sum(0)) / (1 + N)
        zs = (real - sh.mean(0)) / np.maximum(sh.std(0), 1e-9)
        q_lo = bh(p_lo)
        for t, d in enumerate(out):
            d[m] = dict(mean=round(float(sh[:, t].mean()), 3), sd=round(float(sh[:, t].std()), 4),
                        min=round(float(sh[:, t].min()), 3), z=round(float(zs[t]), 2),
                        p_real_le_null=round(float(p_lo[t]), 5), q_bh_sparse=round(float(q_lo[t]), 5),
                        p_real_ge_null=round(float(p_hi[t]), 5))
    out.sort(key=lambda d: -d["pairs"])
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(a.out, "wt") as f:
        json.dump(dict(settings=vars(a), strata=out), f)
    hdr = "| dominant relations | pairs | real linked | " + " | ".join(f"{m} mean±sd (z) [p, q]" for m in modes) + " |"
    L = [hdr, "|" + "---|" * (3 + len(modes))]
    for d in out:
        L.append(f"| {d['relations']} | {d['pairs']} | {d['linked_share']:.2f} | " + " | ".join(
            f"{d[m]['mean']:.2f}±{d[m]['sd']:.3f} ({d[m]['z']:+.1f}) [{d[m]['p_real_le_null']:.4f}, {d[m]['q_bh_sparse']:.3f}]" for m in modes) + " |")
    Path(a.out.replace(".json.gz", ".md")).write_text("\n".join(L) + "\n")
    log("done")


if __name__ == "__main__":
    main()
