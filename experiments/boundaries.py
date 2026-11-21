"""Unexpected sparse boundaries between structured neighbourhoods (paraphrase-merged graph).

Units are the typed groups mined by typed_groups.mine (members + frame anchors = the group's core). Two groups
form a *boundary* when their cores are disjoint, their surroundings overlap strongly (idf-weighted cosine of the
ideas adjacent to each group's members outside the two cores, top 1% of core-disjoint pairs in that graph), and yet no link joins the two cores, while comparable pairs in the same graph
(same bin of context overlap x core-size product x core-degree product) usually are joined.
The identical procedure (contract classes -> mine -> score boundaries) is run on every null graph; real counts are
compared with null counts. For each real boundary, the fixed pair of cores is also checked in every null graph:
p_absent is the share of null graphs in which the two cores are also unlinked (small = construction predicts links).
No edges are proposed and nothing is named.
"""
import argparse, gzip, json
from multiprocessing import Pool
from pathlib import Path

import numpy as np
import scipy.sparse as sp

from experiments.morphology import CATEGORY, LEX, log, shuffle_dst, null_strata
from experiments.typed_groups import UNTYPED, features, Space, mine
from experiments.profile_null import profile_classes, profile_plan, profile_shuffle

MODES = ("relation", "strict", "profile", "profile2")
_G = {}


def adjacency(n, s, d, crel):
    m = crel & (s != d)
    A = sp.csr_matrix((np.ones(m.sum(), np.float32), (s[m], d[m])), shape=(n, n))
    A = (A + A.T).tocsr(); A.data[:] = 1
    return A


def cores(groups, codes, n, members_only=False):
    r, c = [], []
    for gi, (M, F) in enumerate(groups):
        nodes = np.unique(M if members_only else np.r_[M, codes[F] % n])
        r.append(np.full(len(nodes), gi)); c.append(nodes)
    r, c = np.concatenate(r), np.concatenate(c)
    return sp.csr_matrix((np.ones(len(r), np.float32), (r, c)), shape=(len(groups), n))


def score(groups, codes, A, n, s_min, k_min, bins=(4, 3, 3)):
    """Core-disjoint group pairs whose context cosine is in the top (1 - s_min) of all core-disjoint pairs of this
    graph, their cross-link counts and boundary flags. Comparable pairs share a bin of context similarity, core sizes,
    core degree and the unordered pair of the two groups' dominant frame relations (so location groups are compared
    with location groups, prerequisite lists with prerequisite lists)."""
    Co = cores(groups, codes, n)
    deg = np.asarray(A.sum(1)).ravel()
    Ctx = (cores(groups, codes, n, True) @ A); Ctx.data[:] = 1
    Ctx = Ctx - Ctx.multiply(Co); Ctx.eliminate_zeros()
    Ctx = Ctx @ sp.diags(1 / np.log(2 + deg))
    nrm = np.sqrt(np.asarray(Ctx.multiply(Ctx).sum(1)).ravel()); nrm[nrm == 0] = 1
    Ctx = sp.diags(1 / nrm) @ Ctx
    S = (Ctx @ Ctx.T).tocoo()
    i, j, s = S.row, S.col, S.data
    m = i < j
    i, j, s = i[m], j[m], s[m]
    ov = np.asarray(Co[i].multiply(Co[j]).sum(1)).ravel()
    m = ov == 0
    i, j, s = i[m], j[m], s[m]
    m = s >= np.quantile(s, s_min) if len(s) else np.zeros(0, bool)
    i, j, s = i[m], j[m], s[m]
    X = (Co @ A).tocsr()
    cross = np.asarray(X[i].multiply(Co[j]).sum(1)).ravel()
    size = np.asarray(Co.sum(1)).ravel()
    dsum = np.asarray(Co @ deg).ravel()
    feats = [s, np.log(size[i] * size[j]), np.log1p(dsum[i]) + np.log1p(dsum[j])]
    dom = np.array([np.bincount(codes[F] // n // 2).argmax() for _, F in groups], np.int64)
    a_, b_ = np.minimum(dom[i], dom[j]), np.maximum(dom[i], dom[j])
    key = np.unique(a_ * 1000 + b_, return_inverse=True)[1].ravel().astype(np.int64)
    for f, b in zip(feats, bins):
        q = np.quantile(f, np.linspace(0, 1, b + 1)[1:-1]) if len(f) else []
        key = key * b + np.searchsorted(q, f, "right")
    med = np.zeros(len(i)); linked = np.zeros(len(i))
    for k in np.unique(key):
        w = key == k
        med[w] = np.median(cross[w]); linked[w] = (cross[w] > 0).mean()
    bnd = (cross == 0) & (med >= k_min)
    return dict(i=i, j=j, s=s, cross=cross, med=med, linked=linked, bnd=bnd, Co=Co, key=key, rp=a_ * 1000 + b_)


def strata_linked(r):
    """Per unordered dominant-relation pair: [candidate pairs, linked pairs]."""
    out = {}
    for k in np.unique(r["rp"]):
        w = r["rp"] == k
        out[int(k)] = [int(w.sum()), int((r["cross"][w] > 0).sum())]
    return out


def _null(args):
    mode, seed = args
    g = _G
    rng = np.random.default_rng(93000 + 1000 * MODES.index(mode) + seed)
    if mode in ("profile", "profile2"):
        s, d = profile_shuffle(g["src"], g["dst"], g["plans"][mode], rng)
    else:
        s, d = g["src"], shuffle_dst(g["src"], g["dst"], g["rel"], mode, rng, g["n"], g["strata"], g["rec"])
    s, d = g["mp"][s], g["mp"][d]
    rows, codes = features(g["n"], s, d, g["rel"], g["frame_rel"], g["vis"], None)
    X = g["space"].matrix(rows, codes)
    A = adjacency(g["n"], s, d, g["crel"][g["rel"]])
    ng = mine(X)
    r = score(ng, g["space"].codes, A, g["n"], g["s_min"], g["k_min"])
    # fixed real pairs in this null graph
    Co, bi, bj = g["Co"], g["bi"], g["bj"]
    fixed = np.asarray((Co[bi] @ A).multiply(Co[bj]).sum(1)).ravel() if len(bi) else np.zeros(0)
    sz = np.array([len(M) for M, _ in ng])
    return mode, seed, dict(groups=len(ng), pairs=len(r["i"]), bnd=int(r["bnd"].sum()),
                            strata=strata_linked(r), bnd_s=r["s"][r["bnd"]].tolist(), fixed=fixed, cand_linked=float((r["cross"] > 0).mean()) if len(r["i"]) else 0,
                            bnd_min_size=[int(min(sz[x], sz[y])) for x, y in zip(r["i"][r["bnd"]], r["j"][r["bnd"]])])


def _init(kw):
    _G.update(kw)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("arrays"); ap.add_argument("real", help="typed-groups.json.gz (settings)"); ap.add_argument("out")
    ap.add_argument("--keep"); ap.add_argument("--sources", required=True); ap.add_argument("--merge")
    ap.add_argument("--nulls", type=int, default=100); ap.add_argument("--modes", default=",".join(MODES))
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--s-min", type=float, default=0.99, help="context-cosine quantile (among core-disjoint pairs) for candidates")
    ap.add_argument("--k-min", type=float, default=2, help="minimum median cross-links of comparable pairs")
    a = ap.parse_args()
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
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
    log(f"real: {len(groups):,} groups, {len(r['i']):,} candidate pairs, {int(r['bnd'].sum())} boundaries; "
        f"share of candidate pairs linked {np.mean(r['cross'] > 0):.3f}")
    bi, bj = r["i"], r["j"]  # every real candidate pair is re-checked (fixed cores) in every null graph

    strata, rec = null_strata(src, dst, rel, n, R, ds)
    plans = {}
    for lv, mname in ((1, "profile"), (2, "profile2")):
        if mname in modes:
            plans[mname] = profile_plan(n, src, dst, rel, ds, profile_classes(n, src, dst, rel, frame_rel, R, lv), R)
    kw = dict(src=src, dst=dst, rel=rel, n=n, strata=strata, rec=rec, plans=plans, frame_rel=frame_rel, crel=crel,
              vis=vis, space=space, mp=mp, s_min=a.s_min, k_min=a.k_min, Co=r["Co"], bi=bi, bj=bj)
    res = {m: [None] * a.nulls for m in modes}
    with Pool(a.workers, initializer=_init, initargs=(kw,)) as pool:
        for k_, (m, s_, x) in enumerate(pool.imap_unordered(_null, [(m, s_) for s_ in range(a.nulls) for m in modes])):
            res[m][s_] = x
            if k_ % 20 == 0:
                log(f"  null {k_}/{a.nulls * len(modes)}")

    N = a.nulls
    rb = int(r["bnd"].sum())
    rrate = rb / max(1, len(r["i"]))
    cmp_ = {"real": dict(groups=len(groups), pairs=len(r["i"]), boundaries=rb, rate=round(rrate, 4),
                         cand_linked=round(float(np.mean(r["cross"] > 0)), 3))}
    for m in modes:
        b = np.array([x["bnd"] for x in res[m]])
        rate = np.array([x["bnd"] / max(1, x["pairs"]) for x in res[m]])
        cmp_[m] = dict(groups=float(np.mean([x["groups"] for x in res[m]])), pairs=float(np.mean([x["pairs"] for x in res[m]])),
                       boundaries_mean=round(float(b.mean()), 1), boundaries_max=int(b.max()),
                       p_real_le_null=round((1 + (b >= rb).sum()) / (1 + N), 4),
                       rate_mean=round(float(rate.mean()), 4), rate_min=round(float(rate.min()), 4), rate_max=round(float(rate.max()), 4),
                       p_rate_real_ge_null=round((1 + (rate >= rrate).sum()) / (1 + N), 4),
                       p_rate_real_le_null=round((1 + (rate <= rrate).sum()) / (1 + N), 4),
                       cand_linked=round(float(np.mean([x["cand_linked"] for x in res[m]])), 3),
                       p_unlinked_real_ge_null=round((1 + sum(x["cand_linked"] <= float(np.mean(r["cross"] > 0)) for x in res[m])) / (1 + N), 4))
    fixed = {m: np.array([x["fixed"] for x in res[m]]) for m in modes}
    # sparse regions: dominant-relation strata whose context-similar group pairs are linked less often than in nulls
    rs = strata_linked(r)
    regions = []
    for k, (np_, nl) in rs.items():
        if np_ < 20:
            continue
        d = dict(relations=f"{rels[k // 1000]} x {rels[k % 1000]}", pairs=np_, linked_share=round(nl / np_, 3))
        for m in modes:
            sh = [x["strata"][k][1] / x["strata"][k][0] for x in res[m] if k in x["strata"] and x["strata"][k][0] >= 5]
            d[m] = dict(null_graphs_with_stratum=len(sh), linked_share_mean=round(float(np.mean(sh)), 3) if sh else None,
                        p_real_le_null=round((1 + sum(v <= nl / np_ for v in sh)) / (1 + len(sh)), 4) if sh else None)
        regions.append(d)
    regions.sort(key=lambda d: -d["pairs"])
    rdname = [rels[k // 2] + (">" if k % 2 == 0 else "<") for k in range(2 * R)]

    order_ = np.argsort(mp, kind="stable"); mps = mp[order_]

    def expand(x):
        lo, hi = np.searchsorted(mps, [x, x + 1])
        return [ids[y] for y in order_[lo:hi]]

    def gdesc(gi):
        M, F = groups[gi]
        return dict(size=len(M), members=[ids[x] for x in M[:20]],
                    expanded={ids[x]: expand(int(x)) for x in M[:20] if len(expand(int(x))) > 1},
                    frame=[[rdname[int(c) // n], ids[int(c) % n], expand(int(c) % n)] for c in space.codes[F]])
    Co = r["Co"]
    # relation mix of cross links among linked comparable pairs (same bin), and of links from each core to the
    # shared surroundings: the typed shape that is present elsewhere and absent here
    cm = crel[rel] & (ms != md)
    ls, ld, lr = ms[cm], md[cm], rel[cm]
    Xi = (Co[r["i"]]).tocsr(); Xj = (Co[r["j"]]).tocsr()
    relcross = {}
    for k in np.unique(lr):
        w = lr == k
        Ak = sp.csr_matrix((np.ones(w.sum(), np.float32), (ls[w], ld[w])), shape=(n, n))
        relcross[rels[k] + ">"] = np.asarray((Xi @ Ak).multiply(Xj).sum(1)).ravel()
        relcross[rels[k] + "<"] = np.asarray((Xj @ Ak).multiply(Xi).sum(1)).ravel()
    bidx = np.flatnonzero(r["bnd"])

    def core_rels(core, shared):
        inc, insh = np.zeros(n, bool), np.zeros(n, bool)
        inc[core] = True; insh[shared] = True
        c = {}
        for x, y, k in ((ls, ld, ">"), (ld, ls, "<")):
            w = inc[x] & insh[y]
            for rr, cc in zip(*np.unique(lr[w], return_counts=True)):
                c[rels[rr] + k] = c.get(rels[rr] + k, 0) + int(cc)
        return sorted(c.items(), key=lambda kv: -kv[1])[:5]
    def pair_desc(t):
        x, y = int(bi[t]), int(bj[t])
        d = dict(a=x, b=y, context=round(float(r["s"][t]), 3), cross_links=int(r["cross"][t]),
                 comparable_median=float(r["med"][t]), comparable_linked=round(float(r["linked"][t]), 3), A=gdesc(x), B=gdesc(y))
        ctx = np.asarray((Co[x] @ A).multiply(Co[y] @ A).todense()).ravel()
        ctx[Co[x].indices] = 0; ctx[Co[y].indices] = 0
        top = np.argsort(-ctx)[:12]
        shared = [int(v) for v in top if ctx[v] > 0]
        d["shared_surroundings"] = [ids[v] for v in shared]
        sh_all = np.flatnonzero(ctx > 0)
        d["A_to_surroundings"] = core_rels(Co[x].indices, sh_all)
        d["B_to_surroundings"] = core_rels(Co[y].indices, sh_all)
        w = (r["key"] == r["key"][t]) & (r["cross"] > 0)
        mix = sorted(((k, float(v[w].sum())) for k, v in relcross.items()), key=lambda kv: -kv[1])
        tot = sum(v for _, v in mix) or 1
        d["comparable_cross_relations"] = [[k, round(v / tot, 3)] for k, v in mix[:4] if v > 0]
        d["comparable_pairs"] = int(w.sum())
        for m in modes:
            f = fixed[m][:, t]
            d[m] = dict(p_absent=round(float((1 + (f == 0).sum()) / (1 + N)), 4), null_mean_links=round(float(f.mean()), 2))
        return d
    pairs = [pair_desc(t) for t in bidx]
    pm = [m for m in modes if m.startswith("profile")]
    for d in pairs:
        d["unexpected"] = bool(all(d[m]["p_absent"] <= 0.05 for m in pm))
    pmax = np.array([max(d[m]["p_absent"] for m in pm) for d in pairs]) if pairs else np.zeros(0)
    o = np.argsort(pmax); q = np.minimum.accumulate((pmax[o] * len(pmax) / np.arange(1, len(pmax) + 1))[::-1])[::-1]
    for k_, t in enumerate(o):
        pairs[t]["q_bh"] = round(float(min(1, q[k_])), 4)
    pairs.sort(key=lambda d: (not d["unexpected"], -d["context"]))
    # every unlinked candidate pair (not only flagged boundaries): fixed-core absence test under both profile nulls
    pm_ = [m for m in modes if m.startswith("profile")]
    ul = np.flatnonzero(r["cross"] == 0)
    pa = np.max([(1 + (fixed[m][:, ul] == 0).sum(0)) / (1 + N) for m in pm_], 0) if len(ul) and pm_ else np.ones(len(ul))
    o = np.argsort(pa, kind="stable"); qq = np.empty(len(pa))
    if len(pa):
        qq[o] = np.minimum(1, np.minimum.accumulate((pa[o] * len(pa) / np.arange(1, len(pa) + 1))[::-1])[::-1])
    unlinked = []
    for t in sorted(range(len(ul)), key=lambda k: (pa[k], -r["s"][ul[k]]))[:60]:
        d = pair_desc(int(ul[t])); d["p_absent_max"] = round(float(pa[t]), 4); d["q_bh"] = round(float(qq[t]), 4)
        unlinked.append(d)
    # sparse regions with the same (real) group pairs: linked share of real candidate pairs per dominant-relation
    # stratum vs the share of those same core pairs that are linked in each null graph
    fixed_regions = []
    for k in np.unique(r["rp"]):
        w = r["rp"] == k
        if w.sum() < 20:
            continue
        real_sh = float((r["cross"][w] > 0).mean())
        d = dict(relations=f"{rels[k // 1000]} x {rels[k % 1000]}", pairs=int(w.sum()), linked_share=round(real_sh, 3))
        for m in modes:
            sh = (fixed[m][:, w] > 0).mean(1)
            d[m] = dict(linked_share_mean=round(float(sh.mean()), 3), p_real_le_null=round((1 + (sh <= real_sh).sum()) / (1 + N), 4),
                        p_real_ge_null=round((1 + (sh >= real_sh).sum()) / (1 + N), 4))
        if pm_ and all(d[m]["p_real_le_null"] <= 0.05 for m in pm_):
            # unlinked real pairs of this stratum that the profile nulls link most often
            wu = np.flatnonzero(w & (r["cross"] == 0))
            lk = np.min([(fixed[m][:, wu] > 0).mean(0) for m in pm_], 0)
            d["examples"] = []
            for t in wu[np.argsort(-lk, kind="stable")][:12]:
                e = pair_desc(int(t)); e["null_linked_share_min"] = round(float(lk[list(wu).index(t)]), 3)
                d["examples"].append(e)
        fixed_regions.append(d)
    fixed_regions.sort(key=lambda d: -d["pairs"])
    summary = dict(settings=vars(a), counts=cmp_, unexpected=int(sum(d["unexpected"] for d in pairs)),
                   unexpected_q10=int(sum(d["q_bh"] <= 0.1 for d in pairs)),
                   unlinked_pairs=int(len(ul)), unlinked_unexpected=int((pa <= 0.05).sum()), unlinked_q10=int((qq <= 0.1).sum()) if len(ul) else 0)
    log(json.dumps(summary["counts"]))
    log(f"boundaries unexpected under both profile nulls: {summary['unexpected']} of {len(pairs)}")
    with gzip.open(out / "boundaries.json.gz", "wt") as f:
        json.dump(dict(summary=summary, boundaries=pairs, unlinked=unlinked, regions=regions, fixed_regions=fixed_regions,
                       null={m: [{k: v for k, v in x.items() if k != "fixed"} for x in res[m]] for m in modes}), f, default=lambda o: o.tolist() if hasattr(o, "tolist") else str(o))
    log("done")


if __name__ == "__main__":
    main()
