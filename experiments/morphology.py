"""Structural gaps in the ConceptNet graph, tested against null models and WikiText-reweighted graphs.

Neighbourhoods use conceptual relations only (FormOf, DerivedFrom, Etymologically*, HasContext are lexical
and excluded) restricted to corpus-visible ideas (unigram count >= --min-unigram in every corpus), so
neighbourhoods are not dominated by Wiktionary-only leaves. A pair counts as "linked" if any ConceptNet
link joins it.

Families
  missing_link   unlinked pair whose neighbourhoods look like those of pairs that usually are linked
  nested         unlinked pair where one neighbourhood sits inside the other (one-way asymmetry)
  hole           an idea whose neighbourhood splits into clusters with no links between them although
                 cross-cluster pairs look like pairs that usually are linked
  unnamed_group  ideas that are mutually unlinked missing-link gaps, share a frame of neighbours, and
                 have no common category (IsA/InstanceOf/MannerOf/PartOf target) naming most of them

Evidence
  * comparable-neighbourhood model: logistic P(conceptually linked | log Jaccard, log typed Jaccard,
    log common neighbours, log degrees), fitted on all candidate pairs. Refitted with weighted Jaccard
    under the original weights and each WikiText half (evidence mode). Gap score = min over the weightings
    of -log2(1 - P), so a gap must hold under every weighting.
  * null models (degree-preserving target shuffle; relation-type-preserving shuffle; reciprocity- and
    relation-preserving shuffle): common-neighbour count of the same pair in each null graph, and the
    number of high-similarity pairs among a fixed sample of ideas.
  * WikiText co-occurrence of the pair in each half (observed vs independence expectation).
  * "explained": the gap disappears through an alias - a Synonym/FormOf/DerivedFrom/SimilarTo of one end
    is linked to the other end. Explained gaps are kept in the output but excluded from the rankings.

Gaps are characterised, not filled: no edges are added.
"""
from __future__ import annotations

import argparse
import difflib
import gzip
import json
import os
import time
from collections import Counter, defaultdict
from multiprocessing import Pool
from pathlib import Path

import numpy as np
import scipy.sparse as sp
from scipy.sparse.csgraph import connected_components

LEX = {"FormOf", "DerivedFrom", "EtymologicallyRelatedTo", "EtymologicallyDerivedFrom", "HasContext"}
ALIAS = {"Synonym", "FormOf", "DerivedFrom", "SimilarTo"}
CATEGORY = {"IsA", "InstanceOf", "MannerOf", "PartOf"}
SHIFT = 21
HUB = 2000
TOPK = 40
NULL_MODES = ("global", "relation", "reciprocal")


def log(*a):
    print(time.strftime("%H:%M:%S"), *a, flush=True)


def pair_key(a, b):
    a, b = np.asarray(a, np.int64), np.asarray(b, np.int64)
    return (np.minimum(a, b) << SHIFT) | np.maximum(a, b)


def unkey(k):
    return (k >> SHIFT).astype(np.int64), (k & ((1 << SHIFT) - 1)).astype(np.int64)


def binary(n, s, t, keep=None):
    ok = s != t
    if keep is not None:
        ok &= keep[s] & keep[t]
    M = sp.coo_matrix((np.ones(ok.sum(), np.float32), (s[ok], t[ok])), shape=(n, n)).tocsr()
    M = (M + M.T).tocsr()
    M.data[:] = 1
    return M


def weighted(n, s, t, w, keep):
    """|weight| of the strongest conceptual link between two ideas (either direction)."""
    ok = (s != t) & keep[s] & keep[t]
    k = pair_key(s[ok], t[ok])
    ww = np.abs(w[ok])
    order = np.lexsort((-ww, k))
    k, ww = k[order], ww[order]
    first = np.r_[True, k[1:] != k[:-1]]
    a, b = unkey(k[first])
    ww = ww[first].astype(np.float32)
    return sp.coo_matrix((np.r_[ww, ww], (np.r_[a, b], np.r_[b, a])), shape=(n, n)).tocsr()


def rowdot(M, a, b, N=None, batch=50_000):
    N = M if N is None else N
    out = np.empty(len(a), np.float64)
    for i in range(0, len(a), batch):
        out[i:i + batch] = np.asarray(M[a[i:i + batch]].multiply(N[b[i:i + batch]]).sum(1)).ravel()
    return out


def wjaccard(M, a, b, batch=50_000):
    """Weighted Jaccard sum(min)/sum(max), and sum(min)/sum(row a)."""
    rs = np.asarray(M.sum(1)).ravel()
    wj, cont = np.empty(len(a)), np.empty(len(a))
    for i in range(0, len(a), batch):
        aa, bb = a[i:i + batch], b[i:i + batch]
        d = np.asarray(abs(M[aa] - M[bb]).sum(1)).ravel()
        s = rs[aa] + rs[bb]
        mn = (s - d) / 2
        wj[i:i + batch] = np.where(s + d > 0, (s - d) / np.maximum(s + d, 1e-12), 0)
        cont[i:i + batch] = mn / np.maximum(rs[aa], 1e-12)
    return wj, cont


def shuffle_dst(src, dst, rel, mode, rng, n):
    """numpy version of ideanet.analysis.shuffle_targets (same three modes)."""
    d = dst.copy()
    if mode == "global":
        return rng.permutation(d)
    R = int(rel.max()) + 1
    rec = np.zeros(len(src), bool)
    if mode == "reciprocal":
        key = (src.astype(np.int64) * n + dst) * R + rel
        rkey = (dst.astype(np.int64) * n + src) * R + rel
        rec = np.isin(rkey, key) & (src != dst)
    for r in range(R):
        idx = np.flatnonzero((rel == r) & ~rec)
        d[idx] = rng.permutation(dst[idx])
        idx = rng.permutation(np.flatnonzero((rel == r) & rec))
        x, y = idx[0:len(idx) - 1:2], idx[1::2]
        d[x], d[y] = src[y], src[x]
    return d


def global_stats(A, rows, min_deg=5):
    deg = np.asarray(A.sum(1)).ravel()
    S = (A[rows] @ A.T).tocoo()
    r, c, v = rows[S.row], S.col, S.data
    keep = (r < c) & (deg[c] >= min_deg)
    r, c, v = r[keep], c[keep], v[keep]
    J = v / (deg[r] + deg[c] - v)
    linked = np.asarray(A[r, c]).ravel() > 0
    out = {}
    for t in (0.1, 0.2, 0.3):
        m = (J >= t) & (v >= 3)
        out[f"J>={t}"] = int(m.sum())
        out[f"J>={t}_unlinked"] = int((m & ~linked).sum())
    return out


_G: dict = {}


def _null_init(src, dst, rel, cmask, vis, n, pa, pb, rows):
    _G.update(src=src, dst=dst, rel=rel, cmask=cmask, vis=vis, n=n, pa=pa, pb=pb, rows=rows)


def _null_task(args):
    mode, seed = args
    g = _G
    rng = np.random.default_rng(1000 * (NULL_MODES.index(mode) + 1) + seed)
    d = shuffle_dst(g["src"], g["dst"], g["rel"], mode, rng, g["n"])
    A = binary(g["n"], g["src"][g["cmask"]], d[g["cmask"]], g["vis"])
    return mode, seed, rowdot(A, g["pa"], g["pb"]).astype(np.float32), global_stats(A, g["rows"])


# ---- comparable-neighbourhood model -------------------------------------------

def features(sim, tsim, cn, d1, d2):
    lo, hi = np.minimum(d1, d2), np.maximum(d1, d2)
    return np.column_stack([np.ones(len(sim)), np.log(sim + 1e-3), np.log(tsim + 1e-3),
                            np.log1p(cn), np.log(lo), np.log(hi)])


def fit_logistic(X, y, iters=25, ridge=1e-6):
    beta = np.zeros(X.shape[1])
    for _ in range(iters):
        p = 1 / (1 + np.exp(-np.clip(X @ beta, -30, 30)))
        wv = p * (1 - p)
        H = X.T @ (X * wv[:, None]) + ridge * np.eye(X.shape[1])
        step = np.linalg.solve(H, X.T @ (y - p))
        beta += step
        if np.abs(step).max() < 1e-8:
            break
    return beta


def predict(beta, X):
    return 1 / (1 + np.exp(-np.clip(X @ beta, -30, 30)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("arrays", help="graph-arrays.npz (src,dst,rel,w,ids,rels aligned to graph.links)")
    ap.add_argument("out")
    ap.add_argument("--weights", nargs="+", default=[], help="name=path.weights.npz (evidence mode)")
    ap.add_argument("--counts", nargs="+", default=[], help="name=path.allpairs.npz from count_pairs.py")
    ap.add_argument("--nulls", type=int, default=20)
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--min-degree", type=int, default=5)
    ap.add_argument("--min-unigram", type=int, default=20)
    ap.add_argument("--top", type=int, default=60)
    a = ap.parse_args()
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)

    z = np.load(a.arrays)
    src, dst, rel, w0 = z["src"], z["dst"], z["rel"], z["w"]
    ids, rels = [str(x) for x in z["ids"]], [str(x) for x in z["rels"]]
    n, R = len(ids), len(rels)
    cmask = ~np.isin(rel, [rels.index(r) for r in LEX if r in rels])
    amask = np.isin(rel, [rels.index(r) for r in ALIAS if r in rels])

    C = {}
    for spec in a.counts:
        name, path = spec.split("=", 1)
        zc = np.load(path, allow_pickle=True)
        C[name] = {k: zc[k] for k in ("unigram", "marg", "link_keys", "link_cnt", "prop_keys", "prop_cnt")}
        C[name]["total"] = C[name]["marg"].sum() / 2
        C[name]["provenance"] = json.loads(str(zc["meta"]))["provenance"]
    corpus_names = list(C)
    vis = np.ones(n, bool)
    for c in C.values():
        vis &= c["unigram"] >= a.min_unigram

    cs, ct, crel = src[cmask], dst[cmask], rel[cmask]
    A = binary(n, cs, ct, vis)
    deg = np.asarray(A.sum(1)).ravel()
    any_keys = np.unique(pair_key(src[src != dst], dst[src != dst]))
    Aany = binary(n, src, dst)
    Syn = binary(n, src[amask], dst[amask])
    log(f"{n:,} ideas, {vis.sum():,} corpus-visible, {cmask.sum():,} conceptual links, "
        f"{A.nnz // 2:,} visible undirected conceptual edges")

    W = {"original": weighted(n, cs, ct, w0[cmask], vis)}
    for spec in a.weights:
        name, path = spec.split("=", 1)
        W[name] = weighted(n, cs, ct, np.load(path, allow_pickle=True)["weights"][cmask], vis)

    ci = np.flatnonzero(vis & (deg >= a.min_degree))
    log(f"core: {len(ci):,} ideas (visible conceptual degree >= {a.min_degree})")

    ok = vis[cs] & vis[ct] & (cs != ct)
    F = sp.coo_matrix((np.ones(2 * ok.sum(), np.float32),
                       (np.r_[cs[ok], ct[ok]],
                        np.r_[ct[ok].astype(np.int64) * R * 2 + crel[ok] * 2,
                              cs[ok].astype(np.int64) * R * 2 + crel[ok] * 2 + 1])),
                      shape=(n, n * R * 2)).tocsr()
    F.data[:] = 1
    tdeg = np.asarray(F.sum(1)).ravel()

    # ---- candidates ------------------------------------------------------------------
    iw = np.where(deg > HUB, 0.0, 1.0 / np.log(np.maximum(deg, 2))).astype(np.float32)
    Ac = A[ci]
    AcW = Ac @ sp.diags(iw)
    AcT = Ac.T.tocsr()
    pa, pb = [], []
    for i in range(0, len(ci), 1000):
        S = (AcW[i:i + 1000] @ AcT).tocsr()
        for r in range(S.shape[0]):
            lo, hi = S.indptr[r], S.indptr[r + 1]
            cols, vals = S.indices[lo:hi], S.data[lo:hi]
            keep = cols != i + r
            cols, vals = cols[keep], vals[keep]
            if len(cols) > TOPK:
                cols = cols[np.argpartition(-vals, TOPK)[:TOPK]]
            pa.append(np.full(len(cols), ci[i + r]))
            pb.append(ci[cols])
    k = np.unique(pair_key(np.concatenate(pa), np.concatenate(pb)))
    pa, pb = unkey(k)
    log(f"{len(pa):,} candidate pairs")

    def pair_stats(x, y):
        cn_ = rowdot(A, x, y)
        tcn_ = rowdot(F, x, y)
        return dict(cn=cn_, J=cn_ / np.maximum(deg[x] + deg[y] - cn_, 1),
                    tJ=tcn_ / np.maximum(tdeg[x] + tdeg[y] - tcn_, 1))

    st = pair_stats(pa, pb)
    cn, J, tJ = st["cn"], st["J"], st["tJ"]
    linked = np.isin(k, any_keys)
    clinked = np.asarray(A[pa, pb]).ravel() > 0
    train = clinked | ~linked          # drop pairs linked only lexically
    wj, wc = {}, {}
    for name, M in W.items():
        wj[name], c1 = wjaccard(M, pa, pb)
        _, c2 = wjaccard(M, pb, pa)
        wc[name] = (c1, c2)
    beta, p_link = {}, {}
    for name in W:
        X = features(wj[name], tJ, cn, deg[pa], deg[pb])
        beta[name] = fit_logistic(X[train], clinked[train].astype(float))
        p_link[name] = predict(beta[name], X)
        log(f"  model {name}: beta {np.round(beta[name], 3).tolist()}")
    surpr = {nm: -np.log2(1 - p_link[nm]) for nm in W}
    gap_score = np.min(np.vstack([surpr[nm] for nm in W]), axis=0)

    def lexvar(x, y):
        tx, ty = set(x.split("_")), set(y.split("_"))
        if tx & ty:
            return True
        pre = len(os.path.commonprefix([x, y]))
        return pre >= max(4, int(0.6 * min(len(x), len(y)))) or difflib.SequenceMatcher(None, x, y).ratio() >= 0.75

    small = np.where(deg[pa] <= deg[pb], 0, 1)
    cont_s = cn / np.minimum(deg[pa], deg[pb])
    cont_l = cn / np.maximum(deg[pa], deg[pb])
    nested_ok = (cont_s >= 0.5) & (cont_l <= 0.25) & (np.minimum(deg[pa], deg[pb]) >= 8)
    interesting = ~linked & ((p_link["original"] >= 0.05) | nested_ok)
    lex = np.zeros(len(pa), bool)
    for i in np.flatnonzero(interesting):
        lex[i] = lexvar(ids[pa[i]], ids[pb[i]])
    explained = np.zeros(len(pa), bool)
    ii = np.flatnonzero(interesting & ~lex)
    explained[ii] = (rowdot(Syn, pa[ii], pb[ii], Aany) + rowdot(Syn, pb[ii], pa[ii], Aany)) > 0
    gap_mask = interesting & ~lex & ~explained
    log(f"{(~linked).sum():,} unlinked candidates; {interesting.sum():,} similar or nested; "
        f"{lex[interesting].sum():,} lexical variants; {explained.sum():,} explained by an alias; "
        f"{gap_mask.sum():,} gap pairs")

    # ---- holes ---------------------------------------------------------------------------
    holes, hpa, hpb, hown = [], [], [], []
    for v in ci[(deg[ci] >= 20) & (deg[ci] <= 500)]:
        nb = A.indices[A.indptr[v]:A.indptr[v + 1]]
        nb = nb[deg[nb] >= 3]
        if len(nb) < 12:
            continue
        nc, lab = connected_components(A[nb][:, nb], directed=False)
        sizes = np.bincount(lab)
        big = np.flatnonzero(sizes >= 4)
        if len(big) < 2:
            continue
        big = big[np.argsort(-sizes[big])][:4]
        comps = [nb[lab == b_][np.argsort(-deg[nb[lab == b_]])][:25] for b_ in big]
        holes.append(dict(v=int(v), comps=comps, sizes=sorted(sizes.tolist(), reverse=True)[:6],
                          frag=float(1 - sizes.max() / len(nb)), n_nb=int(len(nb))))
        for x in range(len(comps)):
            for y in range(x + 1, len(comps)):
                X_, Y_ = np.meshgrid(comps[x], comps[y])
                hpa.append(X_.ravel()); hpb.append(Y_.ravel())
                hown.append(np.full(X_.size, (len(holes) - 1) * 100 + x * 10 + y))
    hpa, hpb, hown = np.concatenate(hpa), np.concatenate(hpb), np.concatenate(hown)
    hk = pair_key(hpa, hpb)
    hlinked = np.isin(hk, any_keys)
    hst = pair_stats(hpa, hpb)
    hex_ = {}
    for name, M in W.items():
        hw, _ = wjaccard(M, hpa, hpb)
        p = predict(beta[name], features(hw, hst["tJ"], hst["cn"], deg[hpa], deg[hpb]))
        p0 = predict(beta[name], features(np.zeros(len(hpa)), np.zeros(len(hpa)), np.ones(len(hpa)), deg[hpa], deg[hpb]))
        hex_[name] = np.where(hlinked, 0.0, np.maximum(0, -np.log2(1 - p) + np.log2(1 - p0)))
    hscore = np.min(np.vstack([hex_[nm] for nm in W]), axis=0)
    log(f"{len(holes):,} fragmented neighbourhoods, {len(hpa):,} cross-cluster pairs")

    # ---- nulls -----------------------------------------------------------------------------
    test_idx = np.flatnonzero(gap_mask)
    hsel = np.flatnonzero(hscore > 0.05)
    na, nbb = np.r_[pa[test_idx], hpa[hsel]], np.r_[pb[test_idx], hpb[hsel]]
    obs_cn = np.r_[cn[test_idx], hst["cn"][hsel]]
    rows = np.sort(np.random.default_rng(7).choice(ci, size=min(3000, len(ci)), replace=False))
    real_glob = global_stats(A, rows)
    log(f"nulls: {len(na):,} pairs x {a.nulls} x {len(NULL_MODES)}; real {real_glob}")
    null_cn = {m: np.zeros((a.nulls, len(na)), np.float32) for m in NULL_MODES}
    null_glob = {m: [] for m in NULL_MODES}
    with Pool(a.workers, initializer=_null_init, initargs=(src, dst, rel, cmask, vis, n, na, nbb, rows)) as pool:
        for mode, seed, cnv, glob in pool.imap_unordered(_null_task, [(m, s) for m in NULL_MODES for s in range(a.nulls)]):
            null_cn[mode][seed] = cnv
            null_glob[mode].append(glob)
            log(f"  null {mode} {seed}: {glob}")
    null_p = {m: (1 + (null_cn[m] >= obs_cn[None]).sum(0)) / (1 + a.nulls) for m in NULL_MODES}
    null_z = {m: (obs_cn - null_cn[m].mean(0)) / np.maximum(null_cn[m].std(0), 0.5) for m in NULL_MODES}
    pmax = np.max(np.vstack([null_p[m] for m in NULL_MODES]), axis=0)
    zmin = np.min(np.vstack([null_z[m] for m in NULL_MODES]), axis=0)
    floor = 1.5 / (1 + a.nulls)

    # ---- corpus ------------------------------------------------------------------------------
    def cooc(name, keys):
        c = C[name]
        obs = np.zeros(len(keys), np.int64)
        for kk, cc in ((c["link_keys"], c["link_cnt"]), (c["prop_keys"], c["prop_cnt"])):
            pos = np.searchsorted(kk, keys)
            pos[pos == len(kk)] = 0
            hit = kk[pos] == keys
            obs[hit] = cc[pos[hit]]
        x, y = unkey(keys)
        return obs, c["marg"][x].astype(float) * c["marg"][y] / c["total"]

    def corpus_class(o, e):
        if all(oo >= 3 and oo > 2 * ee for oo, ee in zip(o, e)):
            return "attested"
        if all(oo == 0 for oo in o) and all(ee >= 1 for ee in e):
            return "silent"
        if all(oo <= ee for oo, ee in zip(o, e)):
            return "under"
        return "mixed"

    # ---- description helpers ---------------------------------------------------------------
    order_s, order_d = np.argsort(src, kind="stable"), np.argsort(dst, kind="stable")
    ss, ds = src[order_s], dst[order_d]

    def links_of(u):
        return (order_s[np.searchsorted(ss, u):np.searchsorted(ss, u, "right")],
                order_d[np.searchsorted(ds, u):np.searchsorted(ds, u, "right")])

    def neighbourhood(u, conceptual=True):
        o_, i_ = links_of(u)
        d = defaultdict(set)
        for i in o_:
            if cmask[i] or not conceptual:
                d[int(dst[i])].add(f"{rels[rel[i]]}>")
        for i in i_:
            if cmask[i] or not conceptual:
                d[int(src[i])].add(f"<{rels[rel[i]]}")
        d.pop(u, None)
        return d

    tidx = {int(t): j for j, t in enumerate(test_idx)}
    cg = {nm: cooc(nm, k[test_idx]) for nm in corpus_names}

    def describe_pair(t, kind):
        x, y = int(pa[t]), int(pb[t])
        if deg[x] > deg[y]:
            x, y = y, x
        nx, ny = neighbourhood(x), neighbourhood(y)
        vis_shared = [q for q in set(nx) & set(ny) if vis[q]]
        shared = sorted(vis_shared, key=lambda q: deg[q])
        j = tidx[t]
        o = [int(cg[nm][0][j]) for nm in corpus_names]
        e = [float(cg[nm][1][j]) for nm in corpus_names]
        return dict(
            kind=kind, a=ids[x], b=ids[y], deg=[int(deg[x]), int(deg[y])],
            common_neighbours=int(cn[t]), jaccard=round(float(J[t]), 3), typed_jaccard=round(float(tJ[t]), 3),
            containment=[round(float(cn[t] / deg[x]), 3), round(float(cn[t] / deg[y]), 3)],
            weighted_jaccard={nm: round(float(wj[nm][t]), 3) for nm in W},
            p_linked_comparable={nm: round(float(p_link[nm][t]), 3) for nm in W},
            gap_score=round(float(gap_score[t]), 3),
            null={m: dict(p=round(float(null_p[m][j]), 4), z=round(float(null_z[m][j]), 1),
                          mean_cn=round(float(null_cn[m][:, j].mean()), 2)) for m in NULL_MODES},
            corpus={nm: dict(observed=o[i], expected=round(e[i], 2)) for i, nm in enumerate(corpus_names)},
            corpus_class=corpus_class(o, e),
            shared=[[ids[q], sorted(nx[q]), sorted(ny[q]), int(deg[q])] for q in shared[:16]],
            only_a=[[ids[q], sorted(nx[q])] for q in sorted(set(nx) - set(ny) - {y}, key=lambda q: -deg[q]) if vis[q]][:10],
            only_b=[[ids[q], sorted(ny[q])] for q in sorted(set(ny) - set(nx) - {x}, key=lambda q: -deg[q]) if vis[q]][:10],
            shared_relation_profile=Counter(r_ for q in vis_shared for r_ in nx[q] | ny[q]).most_common(6),
        )

    results = {
        "settings": dict(vars(a), HUB=HUB, TOPK=TOPK, LEX=sorted(LEX), ALIAS=sorted(ALIAS)),
        "corpus_provenance": {nm: C[nm]["provenance"] for nm in corpus_names},
        "graph": dict(ideas=n, visible=int(vis.sum()), conceptual_links=int(cmask.sum()), core=len(ci),
                      candidates=len(pa), unlinked=int((~linked).sum()), interesting=int(interesting.sum()),
                      lexical=int(lex[interesting].sum()), explained=int(explained.sum()), gap_pairs=int(gap_mask.sum()),
                      gap_pairs_null_significant=int((pmax[:len(test_idx)] <= floor).sum()),
                      holes=len(holes)),
        "model": {nm: np.round(beta[nm], 4).tolist() for nm in W},
        "global": {"real": real_glob, **null_glob},
    }

    def nbset(u):
        return set(A.indices[A.indptr[u]:A.indptr[u + 1]].tolist())

    def diverse(order, limit, max_overlap=0.2):
        """Greedy redundancy suppression: skip a pair if an endpoint was already used or its shared
        neighbourhood overlaps (Jaccard >= max_overlap) the shared neighbourhood of a selected pair."""
        chosen, sets, ends, skipped = [], [], set(), 0
        end_sets = []
        for t in order:
            x, y = int(pa[t]), int(pb[t])
            if x in ends or y in ends:
                skipped += 1
                continue
            nx_, ny_ = nbset(x), nbset(y)
            if any(len(e & q) / max(1, len(e | q)) >= 0.1 for e in (nx_, ny_) for q in end_sets):
                skipped += 1
                continue
            sh = nbset(x) & nbset(y)
            if any(len(sh & o) / max(1, len(sh | o)) >= max_overlap for o in sets):
                skipped += 1
                continue
            chosen.append(t); sets.append(sh); ends.update((x, y)); end_sets += [nx_, ny_]
            if len(chosen) >= limit:
                break
        return chosen, skipped

    sig = pmax[:len(test_idx)] <= floor
    log("describing pairs")
    ml = test_idx[sig & ~nested_ok[test_idx]]
    ml = ml[np.argsort(-gap_score[ml])]
    chosen, skipped = diverse(ml, a.top)
    results["graph"]["missing_link_redundant_skipped"] = skipped
    results["missing_link"] = [describe_pair(t, "missing_link") for t in chosen]
    wcmin = np.min(np.vstack([np.where(small == 0, wc[nm][0], wc[nm][1]) for nm in W]), axis=0)
    ns = test_idx[sig & nested_ok[test_idx]]
    nscore = wcmin * (1 - cont_l)
    ns = ns[np.argsort(-nscore[ns])]
    results["nested"] = []
    chosen, skipped = diverse(ns, a.top)
    results["graph"]["nested_redundant_skipped"] = skipped
    for t in chosen:
        r_ = describe_pair(t, "nested")
        r_["nested_score"] = round(float(nscore[t]), 3)
        results["nested"].append(r_)

    log("scoring holes")
    hp = np.ones(len(hpa))
    hp[hsel] = pmax[len(test_idx):]
    owners, inv = np.unique(hown, return_inverse=True)
    members = np.split(np.argsort(inv, kind="stable"), np.cumsum(np.bincount(inv))[:-1])
    ch = {nm: cooc(nm, hk) for nm in corpus_names}
    rows_h = []
    for o, m in zip(owners.tolist(), members):
        rows_h.append((float(hscore[m].sum()), o, m))
    rows_h.sort(key=lambda r_: -r_[0])
    results["hole"] = []
    hsets, csets = [], []
    for score, o, m in rows_h:
        if len(results["hole"]) >= a.top:
            break
        h = holes[o // 100]
        xs = set(h["comps"][(o % 100) // 10].tolist()) | set(h["comps"][o % 10].tolist()) | {h["v"]}
        cv = nbset(h["v"])
        if any(len(xs & q) / len(xs | q) >= 0.2 for q in hsets) or any(len(cv & q) / max(1, len(cv | q)) >= 0.1 for q in csets):
            continue
        hsets.append(xs); csets.append(cv)
        x, y = (o % 100) // 10, o % 10
        v, X_, Y_ = h["v"], h["comps"][x], h["comps"][y]
        nv = neighbourhood(v)
        best = m[np.argsort(-hscore[m])][:10]
        bx = np.asarray(A[X_].sum(0)).ravel() > 0
        by = np.asarray(A[Y_].sum(0)).ravel() > 0
        bridge = [q for q in np.flatnonzero(bx & by) if q != v and q not in nv]
        o_ = [int(ch[nm][0][m].sum()) for nm in corpus_names]
        e_ = [float(ch[nm][1][m].sum()) for nm in corpus_names]
        results["hole"].append(dict(
            kind="hole", centre=ids[v], deg=int(deg[v]), neighbourhood_sizes=h["sizes"],
            fragmentation=round(h["frag"], 3), score=round(score, 2),
            score_by_weights={nm: round(float(hex_[nm][m].sum()), 2) for nm in W},
            cross_pairs=int(len(m)), cross_pairs_null_significant=int(((hp[m] <= floor) & (hscore[m] > 0.05)).sum()),
            cluster_x=[[ids[q], sorted(nv[q])] for q in X_[:12]], cluster_y=[[ids[q], sorted(nv[q])] for q in Y_[:12]],
            bridges_outside=[ids[q] for q in sorted(bridge, key=lambda q: deg[q])[:12]],
            strongest_missing=[[ids[hpa[i]], ids[hpb[i]], int(hst["cn"][i]), round(float(hst["J"][i]), 3),
                                round(float(hscore[i]), 3)] for i in best],
            corpus={nm: dict(observed=o_[i], expected=round(e_[i], 1)) for i, nm in enumerate(corpus_names)},
            corpus_class=corpus_class(o_, e_),
        ))

    log("unnamed groups")
    strong = ml[np.min(np.vstack([p_link[nm][ml] for nm in W]), axis=0) >= 0.25]
    adj = defaultdict(dict)
    for t in strong:
        adj[int(pa[t])][int(pb[t])] = float(gap_score[t])
        adj[int(pb[t])][int(pa[t])] = float(gap_score[t])
    used, groups = set(), []
    for t in strong:
        x, y = int(pa[t]), int(pb[t])
        if x in used or y in used:
            continue
        grp = [x, y]
        while True:
            cand = Counter(q for g_ in grp for q in adj[g_] if q not in grp)
            best = [q for q, c_ in cand.most_common() if c_ >= max(2, 0.6 * len(grp)) and q not in used]
            if not best or len(grp) >= 30:
                break
            grp.append(best[0])
        if len(grp) < 4:
            continue
        used.update(grp)
        mem = np.array(grp)
        gap_edges = sum(1 for i_ in grp for j_ in grp if i_ < j_ and j_ in adj[i_])
        dens = A[mem][:, mem].nnz / (len(mem) * (len(mem) - 1))
        frame = np.asarray(A[mem].sum(0)).ravel()
        fr = np.flatnonzero(frame >= max(3, 0.6 * len(mem)))
        fr = fr[np.argsort(-frame[fr])][:15]
        named = []
        full = [neighbourhood(int(mm), False) for mm in mem]
        for q in fr:
            cover = sum(any(r_.endswith(">") and r_[:-1] in CATEGORY for r_ in nb_.get(int(q), ())) for nb_ in full)
            if cover >= 0.75 * len(mem):
                named.append(ids[q])
        nbs = [neighbourhood(int(mm)) for mm in mem]
        groups.append(dict(
            kind="unnamed_group", members=[ids[q] for q in mem], size=len(mem), gap_edges=gap_edges,
            gap_density=round(2 * gap_edges / (len(mem) * (len(mem) - 1)), 3),
            internal_link_density=round(float(dens), 3), named_by=named,
            score=round(gap_edges * (1 - dens) * float(np.mean([adj[i_][j_] for i_ in grp for j_ in adj[i_] if j_ in grp])), 2),
            frame=[[ids[q], int(frame[q]), Counter(r_ for nb_ in nbs for r_ in nb_.get(int(q), ())).most_common(3)] for q in fr],
        ))
    groups.sort(key=lambda g_: (bool(g_["named_by"]), -g_["score"]))
    kept, fsets = [], []
    for g_ in groups:
        fs = {f_[0] for f_ in g_["frame"]}
        if fs and any(len(fs & q) / len(fs | q) >= 0.15 for q in fsets):
            continue
        fsets.append(fs)
        kept.append(g_)
    results["unnamed_group"] = kept[:a.top]
    results["graph"]["groups"] = len(groups)
    results["graph"]["groups_unnamed"] = sum(not g_["named_by"] for g_ in groups)

    with gzip.open(out / "morphology-results.json.gz", "wt") as f:
        json.dump(results, f, default=lambda o: o.tolist() if hasattr(o, "tolist") else str(o))
    np.savez_compressed(out / "candidates.npz", a=pa, b=pb, cn=cn, J=J, tJ=tJ, linked=linked, lex=lex,
                        explained=explained, gap_score=gap_score,
                        **{f"wj_{k_}": v_ for k_, v_ in wj.items()}, **{f"p_{k_}": v_ for k_, v_ in p_link.items()})
    log("done")


if __name__ == "__main__":
    main()
