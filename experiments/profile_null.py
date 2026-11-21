"""Profile-preserving nulls for typed-relation groups, with every null graph re-mined.

Nulls (all keep each idea's in/out link counts per relation type and source dataset, and keep two-way pairs two-way):
  strict    targets shuffled within relation x dataset x reciprocity x degree class (morphology.null_strata)
  profile   targets shuffled only between links whose endpoints have the same relation profile class:
            dominant (relation, direction) of the idea's typed links + log2 typed degree
  profile2  as profile, with the two most frequent (relation, direction) pairs in the class
Two-way pairs are rewired as pairs (a<->b, c<->d  ->  a<->d, c<->b) within the same endpoint classes.
Every null graph is mined with the identical procedure (typed_groups.mine). Real groups are compared with
null-mined groups by count, size, shape cluster, naming tier and member overlap. No edges are proposed.
--merge cls.npz (anchor_classes.py): ideas are contracted to their paraphrase class before features are built, in
the real graph and in every null graph (nulls are drawn on the original graph, then contracted the same way).
The original arrays are never modified, so every merged group expands back to original ids and links.
"""
import argparse, gzip, json, math
from collections import Counter
from multiprocessing import Pool
from pathlib import Path

import numpy as np
import scipy.sparse as sp

from experiments.morphology import CATEGORY, LEX, log, shuffle_dst, null_strata
from experiments.typed_groups import UNTYPED, FRAC, features, Space, mine, support

MODES = ("relation", "strict", "profile", "profile2")
_G = {}


def profile_classes(n, src, dst, rel, frame_rel, R, level):
    m = frame_rel[rel] & (src != dst)
    rows = np.r_[src[m], dst[m]]
    cols = np.r_[2 * rel[m], 2 * rel[m] + 1]
    P = sp.csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(n, 2 * R)).toarray() if n * 2 * R < 4e8 else None
    tot = P.sum(1)
    o = np.argsort(-P, 1, kind="stable")
    d1 = np.where(tot > 0, o[:, 0], -1)
    d2 = np.where(P[np.arange(n), o[:, 1]] > 0, o[:, 1], -1)
    b = np.minimum(np.log2(tot + 1).astype(np.int64), 12)
    cls = (d1 + 1) * 13 + b
    if level == 2:
        cls = cls * (2 * R + 1) + (d2 + 1)
    return cls


def profile_plan(n, src, dst, rel, ds, cls, R):
    """Precompute strata for one-way links and canonical two-way pairs."""
    key = (src.astype(np.int64) * n + dst) * R + rel
    rkey = (dst.astype(np.int64) * n + src) * R + rel
    order = np.argsort(key); ks = key[order]
    pos = np.searchsorted(ks, rkey); pos[pos == len(ks)] = 0
    rec = (ks[pos] == rkey) & (src != dst)
    partner = np.where(rec, order[pos], -1)
    dcode = np.unique(ds, return_inverse=True)[1]
    ow = np.flatnonzero(~rec)
    st_ow = np.unique(np.stack([rel[ow], dcode[ow], cls[src[ow]], cls[dst[ow]]], 1), axis=0, return_inverse=True)[1].ravel()
    can = np.flatnonzero(rec & (src < dst))
    st_rc = np.unique(np.stack([rel[can], dcode[can], dcode[partner[can]], cls[src[can]], cls[dst[can]]], 1),
                      axis=0, return_inverse=True)[1].ravel()
    return dict(ow=ow, st_ow=st_ow, can=can, part=partner[can], st_rc=st_rc)


def permute_within(idx, st, vals, rng):
    o = np.lexsort((rng.random(len(idx)), st))
    out = np.empty_like(vals)
    out[np.argsort(st, kind="stable")] = vals[o]
    return out


def profile_shuffle(src, dst, plan, rng):
    s, d = src.copy(), dst.copy()
    ow, can, part = plan["ow"], plan["can"], plan["part"]
    d[ow] = permute_within(ow, plan["st_ow"], dst[ow], rng)
    nb = permute_within(can, plan["st_rc"], dst[can], rng)
    d[can] = nb
    s[part], d[part] = nb, src[can]
    return s, d


def cover(Mat, M):
    cnt = np.asarray(Mat[M].sum(0)).ravel()
    cnt[M] = 0
    c = int(cnt.argmax())
    return c, cnt[c] / len(M)


def tier_of(M, Cat, Cat12):
    _, c1 = cover(Cat, M)
    _, c2 = cover(Cat12, M)
    par = (np.asarray(Cat[M].sum(1)).ravel() > 0).mean()
    if c1 >= 0.5:
        return "named"
    if c1 >= 1 / 3 or c2 >= 0.5:
        return "partly_named"
    return "uncategorised" if par < 0.5 else "crosscutting"


def describe(X, groups, n, R, cent, Cat, Cat12):
    """size, shape (nearest real centroid), tier for each group."""
    out = []
    for M, F in groups:
        prof = np.zeros(2 * R)
        np.add.at(prof, (_G["codes"][F] // n), np.asarray(X[M][:, F].sum(0)).ravel())
        v = prof / max(np.linalg.norm(prof), 1e-9)
        shape = int(_G["shape_ids"][int(np.argmax(cent @ v))])
        out.append((len(M), shape, tier_of(M, Cat, Cat12)))
    return out


def best_match(real, ng):
    """Per real group: best member Jaccard and best frame Jaccard among null-mined groups."""
    own, fown = {}, {}
    for h, (M, F) in enumerate(ng):
        for x in M:
            own.setdefault(int(x), []).append(h)
        for c in F:
            fown.setdefault(int(c), []).append(h)
    bm, bf = np.zeros(len(real)), np.zeros(len(real))
    for gi, (M, F) in enumerate(real):
        cand = {h for x in M for h in own.get(int(x), ())}
        bm[gi] = max((len(np.intersect1d(M, ng[h][0])) / len(np.union1d(M, ng[h][0])) for h in cand), default=0)
        cand = {h for c in F for h in fown.get(int(c), ())}
        bf[gi] = max((len(np.intersect1d(F, ng[h][1])) / len(np.union1d(F, ng[h][1])) for h in cand), default=0)
    return bm, bf


def _null(args):
    mode, seed = args
    g = _G
    rng = np.random.default_rng(91000 + 1000 * MODES.index(mode) + seed)
    if mode in ("profile", "profile2"):
        s, d = profile_shuffle(g["src"], g["dst"], g["plans"][mode], rng)
    else:
        s, d = g["src"], shuffle_dst(g["src"], g["dst"], g["rel"], mode, rng, g["n"], g["strata"], g["rec"])
    s, d = g["mp"][s], g["mp"][d]
    rows, codes = features(g["n"], s, d, g["rel"], g["frame_rel"], g["vis"], None)
    X = g["space"].matrix(rows, codes)
    retained = X.multiply(g["X"]).nnz / g["X"].nnz
    sup = support(X, g["Fs"], g["thr"])
    ng = mine(X)
    desc = describe(X, ng, g["n"], g["R"], g["cent"], g["Cat"], g["Cat12"])
    bm, bf = best_match(g["groups"], ng)
    big = sorted(range(len(ng)), key=lambda h: -len(ng[h][0]))[:40] if seed < 3 else []
    examples = [dict(members=ng[h][0].tolist(), frame=ng[h][1].tolist(), size=desc[h][0], shape=desc[h][1], tier=desc[h][2])
                for h in big]
    return mode, seed, dict(sup=sup, desc=desc, bm=bm, bf=bf, retained=retained, examples=examples)


def independence(A, M, anchors, E=None, pos=None, jac=0.1, cmin=0.6):
    """Number of independent neighbourhoods among frame anchors: anchors are joined when directly linked, when
    their neighbourhoods outside the group overlap (Jaccard >= jac), or when their names embed close (cos >= cmin)."""
    anchors = list(dict.fromkeys(anchors))
    k = len(anchors)
    Ms = set(int(x) for x in M)
    nb = [set(A.indices[A.indptr[x]:A.indptr[x + 1]].tolist()) - Ms - {x} for x in anchors]
    par = list(range(k))

    def find(i):
        while par[i] != i:
            par[i] = par[par[i]]; i = par[i]
        return i
    for i in range(k):
        for j in range(i + 1, k):
            x, y = anchors[i], anchors[j]
            join = y in nb[i] or len(nb[i] & nb[j]) >= jac * max(1, len(nb[i] | nb[j]))
            if not join and E is not None and pos[x] >= 0 and pos[y] >= 0:
                join = float(E[pos[x]] @ E[pos[y]]) >= cmin
            if join:
                par[find(i)] = find(j)
    return len({find(i) for i in range(k)})


def _init(kw):
    _G.update(kw)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("arrays"); ap.add_argument("real", help="typed-groups.json.gz from typed_groups.py (same settings)")
    ap.add_argument("out")
    ap.add_argument("--keep"); ap.add_argument("--sources", required=True)
    ap.add_argument("--nulls", type=int, default=100)
    ap.add_argument("--modes", default=",".join(MODES))
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--merge", help="cls.npz from anchor_classes.py: contract paraphrase classes before mining")
    ap.add_argument("--emb", help="embeddings npz (embed_ideas.py), for anchor independence")
    a = ap.parse_args()
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    modes = a.modes.split(",")
    real = json.load(gzip.open(a.real, "rt"))
    st = real["summary"]["settings"]

    z = np.load(a.arrays)
    ids, rels = [str(x) for x in z["ids"]], [str(x) for x in z["rels"]]
    n, R = len(ids), len(rels)
    keep = np.load(a.keep)["keep"] if a.keep else np.ones(len(z["src"]), bool)
    src, dst, rel = z["src"][keep], z["dst"][keep], z["rel"][keep]
    ds = np.load(a.sources)["mask"][keep]
    frame_rel = np.array([r not in UNTYPED and r not in CATEGORY for r in rels])
    cat_rel = np.array([r in CATEGORY for r in rels])
    assert st["min_unigram"] == 0
    vis = np.ones(n, bool)
    mp = np.load(a.merge)["cls"] if a.merge else np.arange(n)
    msrc, mdst = mp[src], mp[dst]

    rows, codes = features(n, msrc, mdst, rel, frame_rel, vis, None)
    space = Space(n, rows, codes, st["min_df"], st["max_df"])
    X = space.matrix(rows, codes)
    space.set_members(X, st["max_member_features"])
    X = space.matrix(rows, codes)
    groups = mine(X)
    if not a.merge:
        assert len(groups) == len(real["groups"]), (len(groups), len(real["groups"]))
        assert all(sorted(ids[x] for x in M) == sorted(g["members"]) for (M, _), g in zip(groups, real["groups"]))
        log(f"re-mined {len(groups):,} real groups (identical to {a.real})")
    else:
        log(f"merged graph: {X.nnz:,} incidences, {X.shape[1]:,} feature columns; mined {len(groups):,} groups")
    Fs = [F for _, F in groups]
    thr = np.array([max(2, math.ceil(FRAC * len(F))) for F in Fs])
    obs = support(X, Fs, thr)

    # shape centroids in (relation, direction) space, from the real clustering
    rdname = [rels[i // 2] + (">" if i % 2 == 0 else "<") for i in range(2 * R)]
    V = np.zeros((len(real["groups"]), 2 * R))
    for gi, g in enumerate(real["groups"]):
        for k, v in g["profile"]:
            V[gi, rdname.index(k)] = v
    V /= np.maximum(V.sum(1, keepdims=True), 1)
    shp = np.array([g["shape"] for g in real["groups"]])
    shape_ids = np.unique(shp)
    cent = np.array([V[shp == s_].mean(0) for s_ in shape_ids])
    cent /= np.linalg.norm(cent, axis=1, keepdims=True)

    fm = cat_rel[z["rel"]] & (mp[z["src"]] != mp[z["dst"]])
    Cat = sp.csr_matrix((np.ones(fm.sum(), np.float32), (mp[z["src"][fm]], mp[z["dst"][fm]])), shape=(n, n)); Cat.data[:] = 1
    Cat12 = Cat + Cat @ Cat; Cat12.data[:] = 1
    Cat, Cat12 = Cat.tocsr(), Cat12.tocsr()

    strata, rec = null_strata(src, dst, rel, n, R, ds)
    plans, pinfo = {}, {}
    for lv, mname in ((1, "profile"), (2, "profile2")):
        if mname in modes:
            cls = profile_classes(n, src, dst, rel, frame_rel, R, lv)
            plans[mname] = p = profile_plan(n, src, dst, rel, ds, cls, R)
            fr_ow = frame_rel[rel[p["ow"]]]
            sz = np.bincount(p["st_ow"])[p["st_ow"]]
            szr = np.bincount(p["st_rc"])[p["st_rc"]]
            pinfo[mname] = dict(classes=int(len(np.unique(cls))), one_way_strata=int(p["st_ow"].max() + 1),
                                two_way_strata=int(p["st_rc"].max() + 1) if len(p["st_rc"]) else 0,
                                typed_one_way_links_in_singleton_strata=round(float((sz[fr_ow] == 1).mean()), 3),
                                two_way_pairs_in_singleton_strata=round(float((szr == 1).mean()), 3) if len(szr) else None)
            log(mname, pinfo[mname])

    kw = dict(src=src, dst=dst, rel=rel, n=n, R=R, strata=strata, rec=rec, plans=plans, frame_rel=frame_rel, vis=vis,
              space=space, codes=space.codes, X=X, Fs=Fs, thr=thr, groups=groups, cent=cent, shape_ids=shape_ids,
              Cat=Cat, Cat12=Cat12, mp=mp)
    _G.update(kw)
    real_desc = describe(X, groups, n, R, cent, Cat, Cat12) if a.merge else \
        [(g["size"], g["shape"], g["tier"]) for g in real["groups"]]
    info = None
    if a.merge:
        cm = np.array([r_ not in LEX for r_ in rels])[rel] & (msrc != mdst)
        A = sp.csr_matrix((np.ones(cm.sum(), np.float32), (msrc[cm], mdst[cm])), shape=(n, n))
        A = (A + A.T).tocsr(); A.data[:] = 1
        E = pos = None
        if a.emb:
            e = np.load(a.emb); E = e["E"].astype(np.float32); pos = -np.ones(n, np.int64); pos[e["nodes"]] = np.arange(len(e["nodes"]))
        order = np.argsort(mp, kind="stable"); ms = mp[order]

        def expand(x):
            lo, hi = np.searchsorted(ms, [x, x + 1])
            return [ids[y] for y in order[lo:hi]]
        # reversible provenance: original links realising each (member, frame) incidence of a merged group
        dsn = [str(x) for x in np.load(a.sources)["names"]]
        lk = np.flatnonzero(frame_rel[rel] & (msrc != mdst))
        lkey = (msrc[lk].astype(np.int64) * n + mdst[lk]) * R + rel[lk]
        lo_ = np.argsort(lkey, kind="stable"); lk, lkey = lk[lo_], lkey[lo_]

        def prov(M, cd):
            outp = []
            for m_ in M:
                for c in cd:
                    r_, dr, nb = int(c) // n // 2, int(c) // n % 2, int(c) % n
                    k_ = ((int(m_) * n + nb) if dr == 0 else (nb * n + int(m_))) * R + r_
                    i0, i1 = np.searchsorted(lkey, [k_, k_ + 1])
                    for li in lk[i0:i1]:
                        outp.append([ids[src[li]], rels[r_], ids[dst[li]],
                                     "+".join(dsn[b] for b in range(len(dsn)) if ds[li] >> b & 1)])
            return outp
        info = []
        for (M, F), (sz, sh, tr) in zip(groups, real_desc):
            cd = space.codes[F]
            fr_ = [[rdname[int(c) // n], ids[int(c) % n], expand(int(c) % n)] for c in cd]
            info.append(dict(members=[ids[x] for x in M], expanded=[expand(int(x)) for x in M], frame=fr_, size=sz,
                             shape=sh, tier=tr, rel_types=len({f_[0][:-1] for f_ in fr_}),
                             anchors=len({int(c) % n for c in cd}),
                             independent=independence(A, M, [int(c) % n for c in cd], E, pos),
                             provenance=prov(M, cd)))
    res = {m: [None] * a.nulls for m in modes}
    tasks = [(m, s_) for s_ in range(a.nulls) for m in modes]
    with Pool(a.workers, initializer=_init, initargs=(kw,)) as pool:
        for i_, (m, s_, r_) in enumerate(pool.imap_unordered(_null, tasks)):
            res[m][s_] = r_
            if i_ % 20 == 0:
                log(f"  null {i_}/{len(tasks)}")

    # ---- statistics ------------------------------------------------------------------------
    N = a.nulls
    floor = 1.5 / (1 + N)
    size_bins = (4, 6, 10, 20)

    def counts(desc):
        c = {f"size_ge_{k}": sum(s_ >= k for s_, _, _ in desc) for k in size_bins}
        for t in ("named", "partly_named", "uncategorised", "crosscutting"):
            c[f"{t}_ge_6"] = sum(s_ >= 6 and t_ == t for s_, _, t_ in desc)
        c["unnamed_ge_6"] = c["uncategorised_ge_6"] + c["crosscutting_ge_6"]
        return c

    rc = counts(real_desc)
    count_cmp = {"real": rc}
    for m in modes:
        cs = [counts(r_["desc"]) for r_ in res[m]]
        count_cmp[m] = {k: dict(mean=round(float(np.mean([c[k] for c in cs])), 1), min=int(min(c[k] for c in cs)),
                                max=int(max(c[k] for c in cs)),
                                p_real_le_null=round((1 + sum(c[k] >= rc[k] for c in cs)) / (1 + N), 4)) for k in rc}
        count_cmp[m]["retained_incidences"] = round(float(np.mean([r_["retained"] for r_ in res[m]])), 3)

    shape_cmp = []
    for s_ in shape_ids:
        row = dict(shape=int(s_), real_ge_6=sum(sz >= 6 and sh == s_ for sz, sh, _ in real_desc),
                   real_unnamed_ge_6=sum(sz >= 6 and sh == s_ and t in ("uncategorised", "crosscutting") for sz, sh, t in real_desc),
                   real_max=max([sz for sz, sh, _ in real_desc if sh == s_], default=0))
        for m in modes:
            row[m] = dict(mean_ge_6=round(float(np.mean([sum(sz >= 6 and sh == s_ for sz, sh, _ in r_["desc"]) for r_ in res[m]])), 1),
                          mean_unnamed_ge_6=round(float(np.mean([sum(sz >= 6 and sh == s_ and t in ("uncategorised", "crosscutting")
                                                                     for sz, sh, t in r_["desc"]) for r_ in res[m]])), 1),
                          mean_max=round(float(np.mean([max([sz for sz, sh, _ in r_["desc"] if sh == s_], default=0) for r_ in res[m]])), 1))
        shape_cmp.append(row)
    shape_cmp.sort(key=lambda r_: -r_["real_ge_6"])

    # per-group: frame support vs null, selection-corrected size (max size of null-mined group in the same shape),
    # and reproduction (null-mined group with member Jaccard >= 0.5)
    maxsize = {m: np.array([[max([sz for sz, sh, _ in r_["desc"] if sh == s_], default=0) for s_ in shape_ids] for r_ in res[m]])
               for m in modes}
    sidx = {int(s_): i for i, s_ in enumerate(shape_ids)}
    per = []
    for gi, (gsize, gshape, _) in enumerate(real_desc):
        d = dict(id=gi)
        for m in modes:
            ns = np.array([r_["sup"][gi] for r_ in res[m]])
            d[m] = dict(p=round(float((1 + (ns >= obs[gi]).sum()) / (1 + N)), 4),
                        z=round(float((obs[gi] - ns.mean()) / max(ns.std(), 0.5)), 1), mean=round(float(ns.mean()), 2),
                        p_selection=round(float((1 + (maxsize[m][:, sidx[gshape]] >= gsize).sum()) / (1 + N)), 4),
                        reproduced=round(float(np.mean([r_["bm"][gi] >= 0.5 for r_ in res[m]])), 3),
                        frame_reproduced=round(float(np.mean([r_["bf"][gi] >= 0.5 for r_ in res[m]])), 3),
                        best_member_jaccard=round(float(np.mean([r_["bm"][gi] for r_ in res[m]])), 3))
        pm = [m for m in modes if m.startswith("profile")]
        d["survives_profile"] = bool(all(d[m]["p"] <= floor and d[m]["reproduced"] <= 0.05 for m in pm))
        d["survives_selection"] = bool(d["survives_profile"] and all(d[m]["p_selection"] <= 0.05 for m in pm))
        per.append(d)

    examples = {m: [dict(e, members=[ids[x] for x in e["members"][:25]],
                         frame=[[rdname[int(space.codes[c]) // n], ids[int(space.codes[c]) % n]] for c in e["frame"]])
                    for r_ in res[m] for e in r_["examples"]] for m in modes}
    summary = dict(settings=dict(vars(a), real_settings=st), profile_classes=pinfo, counts=count_cmp, shapes=shape_cmp,
                   survives_profile=int(sum(d["survives_profile"] for d in per)),
                   survives_selection=int(sum(d["survives_selection"] for d in per)),
                   survives_by_tier={k: dict(Counter(real_desc[d["id"]][2] for d in per if d[k]))
                                     for k in ("survives_profile", "survives_selection")})
    log(json.dumps(summary["counts"]))
    log(f"survive profile nulls {summary['survives_profile']}, + selection {summary['survives_selection']}; {summary['survives_by_tier']}")
    with gzip.open(out / "profile-null.json.gz", "wt") as f:
        json.dump(dict(summary=summary, groups=per, null_examples=examples, merged_groups=info), f,
                  default=lambda o: o.item() if hasattr(o, "item") else str(o))
    log("done")


if __name__ == "__main__":
    main()
