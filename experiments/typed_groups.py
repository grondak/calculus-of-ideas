"""Recurring typed-relation patterns that outline groups of ideas with no category.

A *group* is a member set M plus a frame F of typed features (relation, direction, neighbour), e.g.
UsedFor> having_fun. Every member carries at least 60% of F. Category relations (IsA, InstanceOf, MannerOf,
PartOf) are excluded from frames and used only to ask whether an existing concept already covers the
members. Groups are mined on the chosen graph variant (default: Wiktionary-only links removed). They are
tested against null graphs, edge subsamples and the full graph. Their relation profiles (shapes) are then
clustered. No edges or labels are created.
"""
import argparse, gzip, json, math, os
from collections import Counter
from multiprocessing import Pool
from pathlib import Path

import numpy as np
import scipy.sparse as sp
from scipy.cluster.hierarchy import fcluster, linkage

from experiments.morphology import LEX, ALIAS, CATEGORY, ALL_MODES, log, pair_key, shuffle_dst, null_strata

UNTYPED = {"RelatedTo", "Antonym", "DistinctFrom"} | ALIAS | LEX
FRAC = 0.6


def features(n, src, dst, rel, frame_rel, vis, ncols_rel):
    """Binary rows x typed-feature matrix; column code = (2*rel + dir) * n + neighbour."""
    m = frame_rel[rel] & vis[src] & vis[dst] & (src != dst)
    s, d, r = src[m].astype(np.int64), dst[m].astype(np.int64), rel[m].astype(np.int64)
    rows = np.r_[s, d]
    codes = np.r_[(2 * r) * n + d, (2 * r + 1) * n + s]
    return rows, codes


class Space:
    """Maps feature codes to columns (df filter fixed on the real graph)."""

    def __init__(self, n, rows, codes, min_df, max_df):
        u, inv, df = np.unique(codes, return_inverse=True, return_counts=True)
        keep = (df >= min_df) & (df <= max_df)
        self.codes = u[keep]
        self.n = n
        self.elig = None

    def set_members(self, X, max_feats):
        """Rows with more than max_feats typed features (hubs such as house, table) may sit in frames but not
        be members: under target-shuffling nulls they otherwise form large spurious groups."""
        self.elig = np.diff(X.indptr) <= max_feats

    def matrix(self, rows, codes):
        pos = np.searchsorted(self.codes, codes)
        pos[pos == len(self.codes)] = 0
        ok = self.codes[pos] == codes
        if self.elig is not None:
            ok &= self.elig[rows]
        X = sp.csr_matrix((np.ones(ok.sum(), np.float32), (rows[ok], pos[ok])), shape=(self.n, len(self.codes)))
        X.sum_duplicates()
        X.data[:] = 1
        return X


def mine(X, max_seeds=40000, min_support=4, max_row_feats=200, min_lift=4.0):
    """Seeded frame growth. Returns list of (members array, frame cols array)."""
    rf = np.diff(X.indptr)
    Xr = X[np.flatnonzero((rf >= 2) & (rf <= max_row_feats))]
    df = np.asarray(X.sum(0)).ravel()
    C = (Xr.T @ Xr).tocoo()
    m = (C.row < C.col) & (C.data >= min_support)
    i, j, s = C.row[m], C.col[m], C.data[m]
    N = X.shape[0]
    lift = s * float((rf >= 1).sum()) / (df[i] * df[j])
    m = lift >= min_lift
    i, j, s, lift = i[m], j[m], s[m], lift[m]
    order = np.argsort(-(s * np.log(lift)))[:max_seeds]
    Xc = X.tocsc()
    groups, owner = [], {}
    for o in order:
        a, b = int(i[o]), int(j[o])
        ra = Xc.indices[Xc.indptr[a]:Xc.indptr[a + 1]]
        rb = Xc.indices[Xc.indptr[b]:Xc.indptr[b + 1]]
        M = np.intersect1d(ra, rb)
        F = np.array([a, b])
        for _ in range(3):
            cnt = np.asarray(X[M].sum(0)).ravel()
            F = np.flatnonzero(cnt >= max(2, FRAC * len(M)))
            if len(F) < 2:
                break
            thr = max(2, math.ceil(FRAC * len(F)))
            hits = np.asarray(Xc[:, F].sum(1)).ravel()
            M2 = np.flatnonzero(hits >= thr)
            if np.array_equal(M2, M):
                break
            M = M2
        if len(F) < 2 or len(M) < min_support:
            continue
        # redundancy: skip when most members already belong to one accepted group
        votes = {g for x in M for g in owner.get(int(x), ())}
        if votes and max(len(np.intersect1d(groups[g][0], M)) / len(np.union1d(groups[g][0], M)) for g in votes) >= 0.5:
            continue
        gid = len(groups)
        groups.append((M, F))
        for x in M:
            owner.setdefault(int(x), []).append(gid)
    return groups


def support(X, Fs, thr):
    """Rows carrying >= thr[g] of frame g, for all groups at once."""
    G = sp.csr_matrix((np.ones(sum(len(f) for f in Fs), np.float32),
                       (np.concatenate(Fs), np.repeat(np.arange(len(Fs)), [len(f) for f in Fs]))),
                      shape=(X.shape[1], len(Fs)))
    S = (X @ G).tocoo()
    return np.bincount(S.col[S.data >= thr[S.col]], minlength=len(Fs))


_G = {}


def _null(args):
    mode, seed, do_mine = args
    g = _G
    rng = np.random.default_rng(7000 + 1000 * ALL_MODES.index(mode) + seed)
    d = shuffle_dst(g["src"], g["dst"], g["rel"], mode, rng, g["n"], g["strata"], g["rec"])
    rows, codes = features(g["n"], g["src"], d, g["rel"], g["frame_rel"], g["vis"], None)
    X = g["space"].matrix(rows, codes)
    sup = support(X, g["Fs"], g["thr"])
    sizes = [len(M) for M, _ in mine(X)] if do_mine else None
    return mode, seed, sup, sizes


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("arrays"); ap.add_argument("out")
    ap.add_argument("--keep", help="npz 'keep' mask over links (graph variant to mine on)")
    ap.add_argument("--sources", help="link-datasets.npz (strict-null strata, dataset report)")
    ap.add_argument("--counts", nargs="+", default=[])
    ap.add_argument("--weights", nargs="+", default=[])
    ap.add_argument("--nulls", type=int, default=100)
    ap.add_argument("--null-mine", type=int, default=4, help="nulls per mode that are also re-mined (selection control)")
    ap.add_argument("--modes", default="global,relation,reciprocal,strict")
    ap.add_argument("--subsamples", type=int, default=5)
    ap.add_argument("--subsample-frac", type=float, default=0.8)
    ap.add_argument("--min-unigram", type=int, default=20)
    ap.add_argument("--min-df", type=int, default=3)
    ap.add_argument("--max-df", type=int, default=1000)
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--max-member-features", type=int, default=30)
    a = ap.parse_args()
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    modes = tuple(a.modes.split(","))

    z = np.load(a.arrays)
    ids, rels = [str(x) for x in z["ids"]], [str(x) for x in z["rels"]]
    n, R = len(ids), len(rels)
    fsrc, fdst, frel = z["src"], z["dst"], z["rel"]
    keep = np.load(a.keep)["keep"] if a.keep else np.ones(len(fsrc), bool)
    dsm = np.load(a.sources) if a.sources else None
    src, dst, rel = fsrc[keep], fdst[keep], frel[keep]
    frame_rel = np.array([r not in UNTYPED and r not in CATEGORY for r in rels])
    cat_rel = np.array([r in CATEGORY for r in rels])
    concept_rel = np.array([r not in LEX for r in rels])

    C = {}
    for spec in a.counts:
        nm, path = spec.split("=", 1)
        zc = np.load(path, allow_pickle=True)
        C[nm] = {k: zc[k] for k in ("unigram", "marg", "link_keys", "link_cnt", "prop_keys", "prop_cnt")}
        C[nm]["total"] = C[nm]["marg"].sum() / 2
    vis = np.ones(n, bool)
    for c in C.values():
        vis &= c["unigram"] >= a.min_unigram
    log(f"variant links {keep.sum():,} of {len(keep):,}; visible ideas {vis.sum():,}; "
        f"frame relations {[r for r, f in zip(rels, frame_rel) if f]}")

    rows, codes = features(n, src, dst, rel, frame_rel, vis, None)
    space = Space(n, rows, codes, a.min_df, a.max_df)
    X = space.matrix(rows, codes)
    space.set_members(X, a.max_member_features)
    X = space.matrix(rows, codes)
    log(f"members limited to ideas with <= {a.max_member_features} typed features: {space.elig.sum():,} eligible")
    log(f"typed features: {X.shape[1]:,} columns, {X.nnz:,} incidences, {(np.diff(X.indptr) > 0).sum():,} rows")
    groups = mine(X)
    log(f"mined {len(groups):,} groups")
    Fs = [F for _, F in groups]
    thr = np.array([max(2, math.ceil(FRAC * len(F))) for F in Fs])
    obs = support(X, Fs, thr)

    # ---- graph variants -------------------------------------------------------------------
    rows_f, codes_f = features(n, fsrc, fdst, frel, frame_rel, vis, None)
    sup_full = support(space.matrix(rows_f, codes_f), Fs, thr)
    rng = np.random.default_rng(11)
    recov = np.zeros(len(groups))
    sub_sizes = []
    for k in range(a.subsamples):
        m = rng.random(len(src)) < a.subsample_frac
        r_, c_ = features(n, src[m], dst[m], rel[m], frame_rel, vis, None)
        sg = mine(space.matrix(r_, c_))
        sub_sizes.append(len(sg))
        owner = {}
        for gi, (M, _) in enumerate(sg):
            for x in M:
                owner.setdefault(int(x), []).append(gi)
        for gi, (M, _) in enumerate(groups):
            cand = {h for x in M for h in owner.get(int(x), [])}
            best = max((len(np.intersect1d(M, sg[h][0])) / len(np.union1d(M, sg[h][0])) for h in cand), default=0)
            recov[gi] += best >= 0.5
        log(f"  subsample {k}: {len(sg):,} groups")
    recov /= max(1, a.subsamples)

    # ---- nulls ----------------------------------------------------------------------------
    strata, rec = null_strata(src, dst, rel, n, R, dsm["mask"][keep] if dsm is not None else None) if "strict" in modes else (None, None)
    null_sup = {m: np.zeros((a.nulls, len(groups)), np.int32) for m in modes}
    null_sizes = {m: [] for m in modes}
    tasks = [(m, s, s < a.null_mine) for m in modes for s in range(a.nulls)]
    with Pool(a.workers, initializer=_init_kw, initargs=(dict(src=src, dst=dst, rel=rel, n=n, strata=strata, rec=rec,
                                                                 frame_rel=frame_rel, vis=vis, space=space, Fs=Fs, thr=thr),)) as pool:
        for i_, (m, s, sup, sizes) in enumerate(pool.imap_unordered(_null, tasks)):
            null_sup[m][s] = sup
            if sizes is not None:
                null_sizes[m].append(sizes)
            if i_ % 50 == 0:
                log(f"  null {i_}/{len(tasks)}")
    pval = {m: (1 + (null_sup[m] >= obs[None]).sum(0)) / (1 + a.nulls) for m in modes}
    zval = {m: (obs - null_sup[m].mean(0)) / np.maximum(null_sup[m].std(0), 0.5) for m in modes}
    pmax = np.max(np.vstack([pval[m] for m in modes]), 0)
    order_p = np.argsort(pmax); mtests = len(pmax)
    q = np.empty(mtests); q[order_p] = np.minimum.accumulate((pmax[order_p] * mtests / np.arange(1, mtests + 1))[::-1])[::-1]
    floor = 1.5 / (1 + a.nulls)

    # ---- naming (full graph incl. Wiktionary) and internal structure -------------------------
    cm = cat_rel[frel] & (fsrc != fdst)
    Cat = sp.csr_matrix((np.ones(cm.sum(), np.float32), (fsrc[cm], fdst[cm])), shape=(n, n)); Cat.data[:] = 1
    Cat2 = (Cat @ Cat); Cat2.data[:] = 1
    Cat12 = Cat + Cat2; Cat12.data[:] = 1
    km = concept_rel[rel] & (src != dst)
    Akeep = sp.csr_matrix((np.ones(km.sum(), np.float32), (src[km], dst[km])), shape=(n, n))
    Akeep = Akeep + Akeep.T; Akeep.data[:] = 1
    dkeep = np.asarray(Akeep.sum(1)).ravel(); E2 = dkeep.sum()
    W = {"original": None}
    wts = {nm: np.load(p, allow_pickle=True)["weights"][keep] for nm, p in (s_.split("=", 1) for s_ in a.weights)}
    w0 = z["w"][keep]

    def cover(Mat, M):
        cnt = np.asarray(Mat[M].sum(0)).ravel()
        cnt[M] = 0
        c = int(cnt.argmax())
        return c, cnt[c] / len(M)

    def cooc(nm, keys):
        c = C[nm]
        o = np.zeros(len(keys), np.int64)
        for kk, cc in ((c["link_keys"], c["link_cnt"]), (c["prop_keys"], c["prop_cnt"])):
            pos = np.searchsorted(kk, keys); pos[pos == len(kk)] = 0
            hit = kk[pos] == keys; o[hit] = cc[pos[hit]]
        x, y = keys >> 21, keys & ((1 << 21) - 1)
        return o.sum(), float((c["marg"][x].astype(float) * c["marg"][y] / c["total"]).sum())

    lk = (src.astype(np.int64) * n + dst)
    lorder = np.argsort(lk); lks = lk[lorder]

    def link_ids(us, vs):
        k = us.astype(np.int64) * n + vs
        pos = np.searchsorted(lks, k); pos[pos == len(lks)] = 0
        return lorder[pos[lks[pos] == k]]

    def feat(col):
        code = int(space.codes[col]); rd, node = divmod(code, n)
        r, d = divmod(rd, 2)
        return rels[r] + (">" if d == 0 else "<"), node

    res = []
    for gi, (M, F) in enumerate(groups):
        fr = [feat(c) for c in F]
        frame_nodes = sorted({nd for _, nd in fr})
        sub = X[M][:, F].toarray()
        prof = Counter()
        for (rl, _), colsum in zip(fr, sub.sum(0)):
            prof[rl] += int(colsum)
        c1, cov1 = cover(Cat, M)
        c2, cov2 = cover(Cat12, M)
        par = np.asarray(Cat[M].sum(1)).ravel() > 0
        internal = int(Akeep[M][:, M].sum() // 2)
        dm = dkeep[M]; exp_int = float((dm.sum() ** 2 - (dm ** 2).sum()) / 2 / E2)
        if cov1 >= 0.5:
            tier = "named"
        elif cov1 >= 1 / 3 or cov2 >= 0.5:
            tier = "partly_named"
        elif par.mean() < 0.5:
            tier = "uncategorised"
        else:
            tier = "crosscutting"
        # weighted consistency: mean |w| of member-frame links relative to all links of the same relations
        us, vs = [], []
        for c in F:
            rl, nd = feat(c)
            mm = M[X[M][:, c].toarray().ravel() > 0]
            if rl.endswith(">"):
                us.append(mm); vs.append(np.full(len(mm), nd))
            else:
                us.append(np.full(len(mm), nd)); vs.append(mm)
        li = link_ids(np.concatenate(us), np.concatenate(vs))
        rel_here = np.unique(rel[li])
        wrel = {}
        for nm, ww in [("original", w0)] + list(wts.items()):
            base = np.abs(ww[np.isin(rel, rel_here)]).mean()
            wrel[nm] = round(float(np.abs(ww[li]).mean() / base), 3) if len(li) else None
        mf = pair_key(np.repeat(M, len(frame_nodes)), np.tile(frame_nodes, len(M)))
        mf = mf[(np.repeat(M, len(frame_nodes)) != np.tile(frame_nodes, len(M)))]
        iu = np.triu_indices(len(M), 1)
        mmk = pair_key(M[iu[0]], M[iu[1]])
        corp = {nm: dict(member_frame=[int(cooc(nm, mf)[0]), round(cooc(nm, mf)[1], 1)],
                         member_member=[int(cooc(nm, mmk)[0]), round(cooc(nm, mmk)[1], 1)]) for nm in C}
        res.append(dict(
            id=gi, members=[ids[x] for x in M], size=len(M), frame=[[rl, ids[nd]] for rl, nd in fr],
            frame_size=len(F), frame_nodes=[ids[x] for x in frame_nodes], density=round(float(sub.mean()), 3),
            profile=prof.most_common(), support=int(obs[gi]), support_full_graph=int(sup_full[gi]),
            null={m: dict(p=round(float(pval[m][gi]), 4), z=round(float(zval[m][gi]), 1),
                          mean=round(float(null_sup[m][:, gi].mean()), 2)) for m in modes},
            p_max=round(float(pmax[gi]), 4), q_bh=round(float(q[gi]), 4), significant_all=bool(pmax[gi] <= floor),
            subsample_recovery=round(float(recov[gi]), 2),
            category={"best_direct": ids[c1], "direct_coverage": round(float(cov1), 2),
                      "best_within_2": ids[c2], "within_2_coverage": round(float(cov2), 2),
                      "members_with_any_category": round(float(par.mean()), 2),
                      "member_categories": {ids[x]: [ids[y] for y in Cat[x].indices[:4]] for x in M[:12]}},
            tier=tier, internal_links=internal, internal_expected=round(exp_int, 2),
            relative_weight=wrel, corpus=corp))

    # ---- shape clustering --------------------------------------------------------------------
    rd = sorted({rl for g in res for rl, _ in g["profile"]})
    V = np.array([[dict(g["profile"]).get(r_, 0) for r_ in rd] for g in res], float)
    V /= np.maximum(V.sum(1, keepdims=True), 1)
    lab = fcluster(linkage(V, "average", metric="cosine"), 0.3, "distance") if len(res) > 1 else np.ones(len(res), int)
    robust = np.array([g["significant_all"] and g["subsample_recovery"] >= 0.6 and g["support_full_graph"] >= g["support"]
                       for g in res])
    shapes = []
    for c in np.unique(lab):
        mem = np.flatnonzero(lab == c)
        centroid = V[mem].mean(0)
        top = [[rd[i], round(float(centroid[i]), 2)] for i in np.argsort(-centroid)[:4] if centroid[i] > 0.05]
        tiers = Counter(res[i]["tier"] for i in mem[robust[mem]])
        shapes.append(dict(shape=int(c), relation_profile=top, groups=int(len(mem)), robust_groups=int(robust[mem].sum()),
                           robust_tiers=dict(tiers),
                           examples=sorted((int(i) for i in mem[robust[mem]]),
                                           key=lambda i: -(res[i]["size"] * min(res[i]["null"][m]["z"] for m in modes)))[:12]))
        for i in mem:
            res[i]["shape"] = int(c)
            res[i]["robust"] = bool(robust[i])
    shapes.sort(key=lambda s_: -s_["robust_groups"])

    ds_report = {}
    if dsm is not None:
        names = [str(x) for x in dsm["names"]]
        mk = dsm["mask"][keep]
        ds_report = {nm: int(((mk >> i) & 1).sum()) for i, nm in enumerate(names)}
    real_sizes = [len(M) for M, _ in groups]
    summary = dict(
        settings=dict(vars(a), FRAC=FRAC, UNTYPED=sorted(UNTYPED), CATEGORY=sorted(CATEGORY)),
        variant=dict(links=int(keep.sum()), all_links=int(len(keep)), datasets_in_variant=ds_report),
        features=dict(columns=int(X.shape[1]), incidences=int(X.nnz)),
        groups=len(groups), significant_all=int(sum(g["significant_all"] for g in res)), robust=int(robust.sum()),
        subsample_group_counts=sub_sizes,
        selection_control={"real": dict(groups=len(real_sizes), size_ge_6=int(sum(s_ >= 6 for s_ in real_sizes)),
                                         size_ge_10=int(sum(s_ >= 10 for s_ in real_sizes))),
                           **{m: dict(groups=[len(x) for x in null_sizes[m]],
                                      size_ge_6=[int(sum(s_ >= 6 for s_ in x)) for x in null_sizes[m]],
                                      size_ge_10=[int(sum(s_ >= 10 for s_ in x)) for x in null_sizes[m]]) for m in modes}},
        tiers_all=dict(Counter(g["tier"] for g in res)), tiers_robust=dict(Counter(g["tier"] for g, r_ in zip(res, robust) if r_)),
    )
    log(json.dumps(summary["selection_control"]))
    log(f"significant in all nulls {summary['significant_all']}, robust {summary['robust']}, tiers {summary['tiers_robust']}")
    with gzip.open(out / "typed-groups.json.gz", "wt") as f:
        json.dump(dict(summary=summary, shapes=shapes, groups=res), f)
    log("done")


def _init_kw(kw):
    _G.update(kw)


if __name__ == "__main__":
    main()
