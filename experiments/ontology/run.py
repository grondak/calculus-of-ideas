"""Run the ontology-expansion experiment: discovery, baselines, controls, ablation.

PYTHONPATH=. python experiments/ontology/run.py --seeds 10 --out experiments/ontology/results
"""
import argparse
import json
import os
import time
from multiprocessing import Pool

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import numpy as np

from experiments.ontology import baselines as B
from experiments.ontology import discover as D
from experiments.ontology import worlds as W


def mcc(preds, worlds):
    p = np.concatenate([D.flat(x) for x in preds])
    y = np.concatenate([D.flat(w["target"]) for w in worlds])
    tp, fp = float((p & y).sum()), float((p & ~y).sum())
    fn, tn = float((~p & y).sum()), float((~p & ~y).sum())
    den = np.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))
    return (tp * tn - fp * fn) / den if den else 0.0


def exact(preds, worlds):
    return float(np.mean([(D.flat(p) == D.flat(w["target"])).all() for p, w in zip(preds, worlds)]))


def scores(preds, sets):
    return {k: {"mcc": mcc(preds[k], ws), "exact": exact(preds[k], ws)} for k, ws in sets.items()}


def anonymize(w, rng, pu, pb):
    p = rng.permutation(w["target"].shape[0])
    return {"unary": w["unary"][pu][:, p], "binary": w["binary"][pb][:, p][:, :, p],
            "target": w["target"][np.ix_(p, p)]}


def true_spec(family, pb):
    """Generator-side label of the withheld primitive in anonymous coordinates (evaluation only)."""
    if family not in W.TRUE_SOURCE:
        return None
    src = W.TRUE_SOURCE[family]
    k = [int(np.flatnonzero(pb == s)[0]) for s in src[1:]]
    if src[0] == "TC":
        return [("TC", 2 * k[0])]
    if src[0] == "FOLD":
        return [("FOLD", 2 * k[0], 2 * k[1], (0, 1, 1, 0))]
    return [("BLOCK", k[0])]


def theory_scores(th, sets, cache):
    return scores({k: [th.predict(w, cache) for w in ws] for k, ws in sets.items()}, sets)


def probe_definability(spec, train, sets, depth, cache):
    """Can the base vocabulary (no inventions) reproduce the invented relation on held-out worlds?"""
    def relabel(w):
        t = D.invent(w, spec).copy()
        np.fill_diagonal(t, False)
        return {"unary": w["unary"], "binary": w["binary"], "target": t}
    ptrain = [relabel(w) for w in train]
    psets = {k: [relabel(w) for w in ws] for k, ws in sets.items()}
    th, _ = D.fit(ptrain, [], depth, {})
    out = theory_scores(th, psets, {})
    out["train"] = theory_scores(th, {"train": ptrain}, {})["train"]
    out["rules"] = len(th.rules)
    return out


def scrambled(th, sets, rng):
    """Ablation: keep the learned theory but feed it entity-permuted invented relations."""
    cache = {}
    for ws in sets.values():
        for w in ws:
            c = cache.setdefault(id(w), {})
            for spec in th.inv:
                n = w["target"].shape[0]
                p = rng.permutation(n)
                c[spec] = D.invent(w, spec)[np.ix_(p, p)]
    return theory_scores(th, sets, cache)


def run_one(args):
    seed, fam, n_train, n_test = args
    t0 = time.time()
    fi = list(W.FAMILIES).index(fam)
    srng = np.random.default_rng([seed, 999])
    pu, pb = srng.permutation(W.N_UNARY), srng.permutation(W.N_BINARY)
    rng = np.random.default_rng([seed, fi])
    gen = lambda size, k: [anonymize(W.make(fam, rng, size), rng, pu, pb) for _ in range(k)]
    train, iid, large = gen("small", n_train), gen("small", n_test), gen("large", n_test)
    sets = {"iid": iid, "large": large}
    rec = {"seed": seed, "family": fam, "kind": W.FAMILIES[fam][1]}
    cache = {}

    th, acc, trace = D.discover(train)
    rec["accepted"] = [list(map(str, s)) for s in acc]
    rec["accepted_ops"] = [s[0] for s in acc]
    rec["theory"] = th.describe()
    rec["trace"] = [{k: (str(v) if k == "candidate" else v) for k, v in t.items()} for t in trace]
    ts = true_spec(fam, pb)
    rec["true_found"] = None if ts is None else any(s in acc for s in ts)
    res = {"invent": theory_scores(th, sets, cache)}

    for depth in (3, 4, 5):
        th0, _ = D.fit(train, [], depth, cache)
        res[f"L0_d{depth}"] = theory_scores(th0, sets, cache)
        if depth == 5:
            rec["L0_d5_rules"] = len(th0.rules)
    thc, accc, _ = D.discover(train, ops=("CONJ",))
    res["conj_only"] = theory_scores(thc, sets, cache)
    rec["conj_only_accepted"] = len(accc)
    if ts is not None:
        tho, _ = D.fit(train, ts, 3, cache, D.inv_extra_chains(ts, 6))
        res["oracle_primitive"] = theory_scores(tho, sets, cache)

    lr = B.fit_lr(train)
    res["stat_lr"] = scores({k: B.predict(lr, ws, False) for k, ws in sets.items()}, sets)
    gbm = B.fit_gbm(train)
    res["stat_gbm"] = scores({k: B.predict(gbm, ws, True) for k, ws in sets.items()}, sets)
    if acc:
        ex = lambda w: [D.invent(w, s) for s in acc]
        g2 = B.fit_gbm(train, ex)
        res["gbm_plus_invented"] = scores({k: B.predict(g2, ws, True, ex) for k, ws in sets.items()}, sets)
        res["ablate_scramble"] = scrambled(th, sets, np.random.default_rng([seed, fi, 7]))
        res["ablate_refit"] = res["L0_d3"]
        rec["probe"] = {str(s): probe_definability(s, train, sets, 5, cache) for s in acc}

    # inadequacy diagnostic visible to the discovery system (training worlds only)
    half = n_train // 2
    th_fit, _ = D.fit(train[:half], [], 3, {})
    g_fit = B.fit_gbm(train[:half])
    rec["diag_val_mcc_L0"] = mcc([th_fit.predict(w, {}) for w in train[half:]], train[half:])
    rec["diag_val_mcc_gbm"] = mcc(B.predict(g_fit, train[half:], True), train[half:])
    rec["target_density"] = float(np.mean([D.flat(w["target"]).mean() for w in train]))
    rec["results"] = res
    rec["secs"] = time.time() - t0
    return rec


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seeds", type=int, default=10)
    ap.add_argument("--n-train", type=int, default=16)
    ap.add_argument("--n-test", type=int, default=16)
    ap.add_argument("--families", default=",".join(W.FAMILIES))
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--out", default="experiments/ontology/results")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    jobs = [(s, f, a.n_train, a.n_test) for s in range(a.seeds) for f in a.families.split(",")]
    path = os.path.join(a.out, "runs.jsonl")
    tmp = path + ".partial"
    with Pool(a.workers) as pool, open(tmp, "w") as fh:
        for rec in pool.imap_unordered(run_one, jobs):
            fh.write(json.dumps(rec) + "\n")
            fh.flush()
            r = rec["results"]
            print(f"seed {rec['seed']} {rec['family']:17s} inv={rec['accepted_ops']} "
                  f"invent={r['invent']['large']['mcc']:.3f} L0d5={r['L0_d5']['large']['mcc']:.3f} "
                  f"gbm={r['stat_gbm']['large']['mcc']:.3f} ({rec['secs']:.0f}s)", flush=True)
    os.replace(tmp, path)


if __name__ == "__main__":
    main()
