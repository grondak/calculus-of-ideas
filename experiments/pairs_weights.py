"""The 847 paired-stimulus experiments under several weight configurations with paired perturbations.

Pairs (a, b, group) come from basins-results.json.gz. For every configuration and perturbation seed k
(seed k applies the same per-link factor in every configuration; k=0 is unperturbed):
  - run A alone, B alone and A+B; classify the joint outcome with classify_pair
    (dominate / coexist / alternate / novel / same / extinct);
  - for 'novel' outcomes run the controls of novel_controls.py: A x2, B x2, A+R, B+R
    (R is a random live start, fixed per pair across configurations and seeds);
    the outcome counts as an interaction only if no control reaches the joint region (wj >= 0.5);
  - check whether the joint region is reached by any single start of the common basin map
    for the same configuration and seed (--basin-raw, from corpus_ensemble.py).
Raw rows are appended to OUT/raw.jsonl (resumable); the summary goes to OUT/pairs-results.json.

  PYTHONPATH=. python experiments/pairs_weights.py GRAPH.pkl OUTDIR --sigma 0.01 --seeds 0,1,2 \
      --weights wiki_half0=PATH ... [--basin-raw experiments/results-gut-split-s01/raw.jsonl]
"""
from __future__ import annotations

import argparse
import gzip
import itertools
import json
import multiprocessing as mp
import random
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ideanet import Engine, IdeaGraph  # noqa: E402
from ideanet.attractor import AttractorMap, classify_pair, signature, weighted_jaccard  # noqa: E402
from ideanet.corpus import WeightTable, load_weights  # noqa: E402
from ideanet.text import TextStimulus  # noqa: E402
from basins import NAMED, STRENGTH  # noqa: E402
from brutality import LATE, PARAMS, UNTIL  # noqa: E402

G = WT = TS = None
CONFIGS: dict = {}
PAIRS: list = []
PARTNER: list = []
SIGMA = 0.01


def rsig(s):
    return {k: round(v, 5) for k, v in s.items()}


def stim(x, s=STRENGTH):
    return TS.stimuli(x, s) if x in NAMED else [(x, s)]


def task(args):
    config, k, lo, hi = args
    wo = WT.weight_fn(CONFIGS[config], k, SIGMA)

    def run(st):
        eng = Engine(G, seed=0, max_events=300_000, weight_of=wo, **PARAMS)
        for idea, s in st:
            eng.stimulate(idea, s)
        eng.run(UNTIL)
        return eng.fires

    single = {}

    def sig1(x):
        if x not in single:
            single[x] = signature(run(stim(x)), LATE, UNTIL)
        return single[x]

    rows = []
    for i in range(lo, hi):
        p = PAIRS[i]
        a, b = p["a"], p["b"]
        sa, sb = sig1(a), sig1(b)
        res, sab = classify_pair(sa, sb, run(stim(a) + stim(b)), LATE, UNTIL)
        ctrl = None
        if res["kind"] == "novel":
            r = PARTNER[i]
            ctrl = {name: round(weighted_jaccard(sab, signature(run(st), LATE, UNTIL)), 3) for name, st in
                    [("A x2", stim(a, 2 * STRENGTH)), ("B x2", stim(b, 2 * STRENGTH)),
                     ("A + R", stim(a) + [(r, STRENGTH)]), ("B + R", stim(b) + [(r, STRENGTH)])]}
        rows.append({"config": config, "k": k, "pair": i, "group": p["group"], "a": a, "b": b, **res,
                     "controls": ctrl, "interaction": bool(ctrl) and max(ctrl.values()) < 0.5,
                     "sig_ab": rsig(sab), "sig_a": rsig(sa), "sig_b": rsig(sb)})
    return rows


def _top(sig, n=5):
    return [x for x, _ in sorted(sig.items(), key=lambda kv: -kv[1])[:n]]


def analyse(rows, configs, seeds, basin_raw, log):
    R = {(r["config"], r["k"], r["pair"]): r for r in rows}
    pairs = sorted({r["pair"] for r in rows})
    groups = sorted({r["group"] for r in rows})
    # reachable from a single start of the common basin map (same config and seed)?
    reach = {}
    if basin_raw:
        bmaps = defaultdict(lambda: AttractorMap(threshold=0.5))
        for line in open(basin_raw):
            b = json.loads(line)
            if b["exp"] == "basin" and b["sig"] and b["config"] in configs and b["k"] in seeds:
                bmaps[(b["config"], b["k"])].assign(b["sig"], b["start"])
        for key, r in R.items():
            m = bmaps.get(key[:2])
            if m is not None and r["sig_ab"]:
                aid, sim = m.lookup(r["sig_ab"])
                reach[key] = aid is not None
    res = {"configs": configs, "seeds": seeds, "per_config": {}, "cross": {}, "robust_interactions": {}}
    for c in configs:
        res["per_config"][c] = {}
        for k in seeds:
            rs = [R[(c, k, i)] for i in pairs if (c, k, i) in R]
            d = {}
            for g in groups + ["all"]:
                gs = [r for r in rs if g == "all" or r["group"] == g]
                nov = [r for r in gs if r["kind"] == "novel"]
                inter = [r for r in nov if r["interaction"]]
                d[g] = {"n": len(gs), "kinds": dict(Counter(r["kind"] for r in gs).most_common()),
                        "novel": len(nov), "interaction": len(inter),
                        "interaction_unreached_by_basin_map": sum(1 for r in inter if reach.get((c, k, r["pair"])) is False)}
            res["per_config"][c][str(k)] = d
        log(f"{c}: " + "; ".join(f"k{k} novel {res['per_config'][c][str(k)]['all']['novel']} "
                                 f"inter {res['per_config'][c][str(k)]['all']['interaction']}" for k in seeds))
    # cross-configuration agreement per pair at the same seed: outcome kind, joint region, interaction status
    for c, d in itertools.combinations(configs, 2):
        kind, region, both_inter, any_inter = [], [], 0, 0
        for k in seeds:
            for i in pairs:
                x, y = R.get((c, k, i)), R.get((d, k, i))
                if not x or not y:
                    continue
                kind.append(x["kind"] == y["kind"])
                region.append((not x["sig_ab"] and not y["sig_ab"]) or weighted_jaccard(x["sig_ab"], y["sig_ab"]) >= 0.5)
                both_inter += x["interaction"] and y["interaction"]
                any_inter += x["interaction"] or y["interaction"]
        res["cross"][f"{c}~{d}"] = {"same_kind": float(np.mean(kind)), "same_joint_region": float(np.mean(region)),
                                    "interaction_jaccard": both_inter / any_inter if any_inter else None}
    # same configuration, different seeds: intrinsic sensitivity
    res["self"] = {}
    for c in configs:
        kind, region = [], []
        for k1, k2 in itertools.combinations(seeds, 2):
            for i in pairs:
                x, y = R.get((c, k1, i)), R.get((c, k2, i))
                if x and y:
                    kind.append(x["kind"] == y["kind"])
                    region.append((not x["sig_ab"] and not y["sig_ab"]) or weighted_jaccard(x["sig_ab"], y["sig_ab"]) >= 0.5)
        res["self"][c] = {"same_kind": float(np.mean(kind)) if kind else None,
                          "same_joint_region": float(np.mean(region)) if region else None}
    # interactions that survive the controls under every seed of a configuration
    for c in configs:
        rob = []
        for i in pairs:
            rs = [R.get((c, k, i)) for k in seeds]
            if all(r and r["interaction"] for r in rs):
                stable = all(weighted_jaccard(rs[0]["sig_ab"], r["sig_ab"]) >= 0.5 for r in rs[1:])
                rob.append({"pair": i, "a": rs[0]["a"], "b": rs[0]["b"], "group": rs[0]["group"],
                            "a_top": _top(rs[0]["sig_a"], 3), "b_top": _top(rs[0]["sig_b"], 3),
                            "joint_top": _top(rs[0]["sig_ab"], 5), "same_region_all_seeds": stable,
                            "reached_by_basin_map": [reach.get((c, k, i)) for k in seeds]})
        res["robust_interactions"][c] = rob
        log(f"{c}: {len(rob)} interactions survive controls at every seed "
            f"({sum(r['same_region_all_seeds'] for r in rob)} in the same region at every seed)")
    return res


def main():
    global G, WT, TS, SIGMA
    ap = argparse.ArgumentParser()
    ap.add_argument("graph")
    ap.add_argument("outdir")
    ap.add_argument("--weights", nargs="+", default=[])
    ap.add_argument("--basins", default="experiments/basins-results.json.gz")
    ap.add_argument("--basin-raw", default=None)
    ap.add_argument("--sigma", type=float, default=0.01)
    ap.add_argument("--seeds", default="0,1,2")
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--limit", type=int, default=None, help="only the first N pairs (smoke test)")
    a = ap.parse_args()
    SIGMA = a.sigma
    out = Path(a.outdir)
    out.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    log = lambda *m: print(f"[{time.time() - t0:7.1f}s]", *m, flush=True)
    G = IdeaGraph.load(a.graph)
    WT, TS = WeightTable(G), TextStimulus(G)
    CONFIGS["original"] = WT.original
    prov = {}
    for spec in a.weights:
        name, path = spec.split("=", 1)
        d = load_weights(path, G)
        CONFIGS[name] = d["weights"].astype(np.float64)
        prov[name] = {**d["provenance"], "path": path}
    data = json.load(gzip.open(a.basins, "rt"))
    PAIRS[:] = [{"a": p["a"], "b": p["b"], "group": p["group"]} for p in data["pairs"]][: a.limit]
    live = [r["start"] for r in data["starts"] if r["attractor"] != 0]
    PARTNER[:] = [random.Random(7_000 + i).choice(live) for i in range(len(PAIRS))]
    seeds = [int(x) for x in a.seeds.split(",")]
    log(f"loaded; configs {list(CONFIGS)}; {len(PAIRS)} pairs; seeds {seeds}; sigma {SIGMA}")

    raw = out / "raw.jsonl"
    done = set()
    if raw.exists():
        done = {(r["config"], r["k"], r["pair"]) for r in map(json.loads, raw.open())}
    chunk = 20
    tasks = [(c, k, lo, min(lo + chunk, len(PAIRS))) for k in seeds for c in CONFIGS
             for lo in range(0, len(PAIRS), chunk) if (c, k, lo) not in done]
    log(f"{len(tasks)} chunks to run")
    with mp.get_context("fork").Pool(a.workers) as pool, raw.open("a") as fh:
        for n, rows in enumerate(pool.imap_unordered(task, tasks), 1):
            for r in rows:
                fh.write(json.dumps(r) + "\n")
            fh.flush()
            if n % 25 == 0 or n == len(tasks):
                log(f"{n}/{len(tasks)} chunks")
    rows = [r for r in map(json.loads, raw.open()) if r["config"] in CONFIGS and r["k"] in seeds]
    res = analyse(rows, list(CONFIGS), seeds, a.basin_raw, log)
    res.update({"params": PARAMS, "until": UNTIL, "late": LATE, "strength": STRENGTH, "sigma": SIGMA,
                "provenance": prov, "partners": PARTNER})
    (out / "pairs-results.json").write_text(json.dumps(res, indent=1))
    log("done")


if __name__ == "__main__":
    main()
