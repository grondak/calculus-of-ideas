"""Shared machinery for fixed-core sparse-region tests (collection-preserving nulls, merge sensitivity).

A null mode is a base shuffle ("relation", "strict", "profile", "profile2"), optionally with a set of links held
fixed ("profile|units"): fixed links keep their endpoints, every other link is shuffled by the base procedure
restricted to the free links (its strata and profile classes are computed on the full graph). Nulls are generated
on original IDs and then contracted with the class map, as in profile_null.py / boundaries.py.
"""
import gzip, json

import numpy as np
import scipy.sparse as sp

from experiments.boundaries import adjacency, score
from experiments.morphology import CATEGORY, LEX, shuffle_dst, null_strata
from experiments.typed_groups import UNTYPED, features, Space, mine
from experiments.profile_null import profile_classes, profile_plan, profile_shuffle

_G = {}


def load_graph(arrays, keep, sources):
    z = np.load(arrays)
    ids, rels = [str(x) for x in z["ids"]], [str(x) for x in z["rels"]]
    k = np.load(keep)["keep"] if keep else np.ones(len(z["src"]), bool)
    g = dict(ids=ids, rels=rels, n=len(ids), R=len(rels), src=z["src"][k].astype(np.int64),
             dst=z["dst"][k].astype(np.int64), rel=z["rel"][k].astype(np.int64), ds=np.load(sources)["mask"][k])
    g["frame_rel"] = np.array([r not in UNTYPED and r not in CATEGORY for r in rels])
    g["crel"] = np.array([r not in LEX for r in rels])
    return g


def settings(typed_groups_json):
    return json.load(gzip.open(typed_groups_json, "rt"))["summary"]["settings"]


def real_regions(g, mp, st, s_min=0.99, k_min=2, min_pairs=20):
    n, rel = g["n"], g["rel"]
    ms, md = mp[g["src"]], mp[g["dst"]]
    rows, codes = features(n, ms, md, rel, g["frame_rel"], np.ones(n, bool), None)
    space = Space(n, rows, codes, st["min_df"], st["max_df"])
    X = space.matrix(rows, codes); space.set_members(X, st["max_member_features"]); X = space.matrix(rows, codes)
    A = adjacency(n, ms, md, g["crel"][rel])
    groups = mine(X)
    r = score(groups, space.codes, A, n, s_min, k_min)
    keys = [int(k) for k in np.unique(r["rp"]) if (r["rp"] == k).sum() >= min_pairs]
    W = [r["rp"] == k for k in keys]
    real = np.array([(r["cross"][w] > 0).mean() for w in W])
    return dict(groups=groups, r=r, keys=keys, W=W, real=real, space=space,
                names=[f"{g['rels'][k // 1000]} x {g['rels'][k % 1000]}" for k in keys])


def prepare(g, modes, fixed=None):
    """Precompute strata / plans for every mode. fixed: name -> bool mask over links."""
    fixed = fixed or {}
    n, R, src, dst, rel, ds = g["n"], g["R"], g["src"], g["dst"], g["rel"], g["ds"]
    cls = {}
    spec = {}
    for m in modes:
        base, _, fx = m.partition("|")
        free = ~fixed[fx] if fx else np.ones(len(src), bool)
        f = np.flatnonzero(free)
        if base in ("profile", "profile2"):
            lv = 1 if base == "profile" else 2
            if lv not in cls:
                cls[lv] = profile_classes(n, src, dst, rel, g["frame_rel"], R, lv)
            spec[m] = ("profile", f, profile_plan(n, src[f], dst[f], rel[f], ds[f], cls[lv], R))
        elif base == "strict":
            spec[m] = ("strict", f, null_strata(src[f], dst[f], rel[f], n, R, ds[f]))
        else:
            spec[m] = (base, f, None)
    return spec


def null_graph(g, spec, mode, rng):
    kind, f, plan = spec[mode]
    s, d = g["src"].copy(), g["dst"].copy()
    if kind == "profile":
        s[f], d[f] = profile_shuffle(g["src"][f], g["dst"][f], plan, rng)
    elif kind == "strict":
        d[f] = shuffle_dst(g["src"][f], g["dst"][f], g["rel"][f], "strict", rng, g["n"], plan[0], plan[1])
    else:
        d[f] = shuffle_dst(g["src"][f], g["dst"][f], g["rel"][f], kind, rng, g["n"])
    return s, d


def linked(Co, bi, bj, A):
    return np.asarray((Co[bi] @ A).multiply(Co[bj]).sum(1)).ravel() > 0


def by_relation(g, mp, s, d, Co, bi, bj, W):
    """Share of candidate pairs in each stratum joined by at least one link of each relation (rows: relations)."""
    ms, md = mp[s], mp[d]
    out = np.zeros((g["R"], len(W)))
    for r in range(g["R"]):
        m = (g["rel"] == r)
        if not g["crel"][r] or not m.any():
            continue
        A = adjacency(g["n"], ms[m], md[m], np.ones(m.sum(), bool))
        x = linked(Co, bi, bj, A)
        out[r] = [x[w].mean() for w in W]
    return out


def _init(kw):
    _G.clear(); _G.update(kw)


def _work(args):
    mode, seed = args
    g = _G
    rng = np.random.default_rng(g["seed0"] + 100003 * g["modes"].index(mode) + seed)
    s, d = null_graph(g["g"], g["spec"], mode, rng)
    mp = g["mp"]
    A = adjacency(g["g"]["n"], mp[s], mp[d], g["g"]["crel"][g["g"]["rel"]])
    x = linked(g["Co"], g["bi"], g["bj"], A)
    sh = np.array([x[w].mean() for w in g["W"]])
    rel = by_relation(g["g"], mp, s, d, g["Co"], g["bi"], g["bj"], g["W"]) if seed < g["n_rel"] else None
    return mode, seed, sh, rel


def bh(p):
    p = np.asarray(p, float); o = np.argsort(p); q = np.empty_like(p)
    q[o] = np.minimum.accumulate((p[o] * len(p) / np.arange(1, len(p) + 1))[::-1])[::-1]
    return np.minimum(q, 1)


def run_nulls(g, mp, reg, modes, nulls, fixed=None, workers=6, n_rel=0, seed0=81000):
    from multiprocessing import Pool
    spec = prepare(g, modes, fixed)
    r = reg["r"]
    kw = dict(g=g, spec=spec, mp=mp, Co=r["Co"], bi=r["i"], bj=r["j"], W=reg["W"], modes=list(modes),
              n_rel=n_rel, seed0=seed0)
    res = {m: np.zeros((nulls, len(reg["W"]))) for m in modes}
    rel = {m: [] for m in modes}
    with Pool(workers, initializer=_init, initargs=(kw,)) as pool:
        for m, s_, x, rr in pool.imap_unordered(_work, [(m, s_) for s_ in range(nulls) for m in modes], chunksize=2):
            res[m][s_] = x
            if rr is not None:
                rel[m].append(rr)
    stats = {}
    real = reg["real"]
    for m in modes:
        sh = res[m]
        p_lo = (1 + (sh <= real).sum(0)) / (1 + nulls)
        stats[m] = dict(mean=sh.mean(0), sd=sh.std(0), z=(real - sh.mean(0)) / np.maximum(sh.std(0), 1e-9),
                        p=p_lo, q=bh(p_lo), rel=np.mean(rel[m], 0) if rel[m] else None)
    return stats


def class_map_from_classes(classes, ids, drop=None):
    """Class map from classes.json.gz entries; drop(cls_index, evidence_list) -> evidence list kept.
    Members of a class stay merged only through kept evidence (connected components)."""
    from scipy.sparse.csgraph import connected_components
    idx = {x: i for i, x in enumerate(ids)}
    mp = np.arange(len(ids))
    for ci, c in enumerate(classes):
        mem = [idx[x] for x in c["members"]]
        ev = c["evidence"] if drop is None else drop(ci, c["evidence"])
        loc = {x: k for k, x in enumerate(c["members"])}
        if not ev:
            continue
        a = [loc[e[0]] for e in ev]; b = [loc[e[1]] for e in ev]
        M = sp.csr_matrix((np.ones(len(a)), (a, b)), shape=(len(mem), len(mem)))
        _, lab = connected_components(M, directed=False)
        mem = np.array(mem)
        for l_ in np.unique(lab):
            grp = mem[lab == l_]
            if len(grp) > 1:
                mp[grp] = grp.min()
    return mp
