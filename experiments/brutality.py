"""Is the 'brutality trap' reached from 'bee' structural or an artifact?

1. Repeatability: identical reruns, plus small parameter jitter.
2. Basin: many start concepts; how often do they end in the same cluster?
3. Null models: rewire link endpoints (degree-preserving; global and
   within-relation-type) and compare trap metrics.

Cluster = ideas firing in the late window [late, until] of the baseline bee run.
Occupancy = fraction of late-window fires that land in the cluster.
Late diversity = distinct ideas / fires in the late window (low = trapped/recurrent).

usage: python experiments/brutality.py conceptnet-en.pkl out.json [--samples 20]
"""
from __future__ import annotations

import argparse
import json
import random
import statistics
import sys
import time
from collections import Counter, defaultdict

from ideanet import Engine, IdeaGraph, TextStimulus, shuffle_targets, signature, weighted_jaccard

PARAMS = dict(fire_gain=2.0, top_k=10, global_inhibition=0.1)
UNTIL, LATE = 100.0, 50.0
NAMED_STARTS = ["bee", "ant", "flower", "honey", "computer worm", "wasp", "wolf",
                "harbor", "violin", "mathematics", "democracy", "rain", "kitchen", "justice", "ocean", "sugar"]


def run(g, stimuli, params=PARAMS, seed=0):
    eng = Engine(g, seed=seed, max_events=300_000, **params)
    for idea, s in stimuli:
        eng.stimulate(idea, s)
    eng.run(UNTIL)
    return eng


def late_stats(eng, cluster: set[str] | None):
    late = [f for f in eng.fires if f.time >= LATE]
    ideas = [f.idea for f in late]
    fc = Counter(f.idea for f in eng.fires)
    inputs = defaultdict(set)
    for f in eng.fires:
        inputs[f.idea].add(tuple(sorted(f.inputs)))
    return {
        "fires": len(eng.fires),
        "distinct": len(fc),
        "late_fires": len(late),
        "late_distinct": len(set(ideas)),
        "late_diversity": round(len(set(ideas)) / len(ideas), 3) if ideas else None,
        "reactivation": round(len(eng.fires) / len(fc), 2) if fc else 0,
        "max_path_diversity": max((len(v) for k, v in inputs.items() if fc[k] > 1), default=0),
        "persistent": bool(eng.fires) and eng.fires[-1].time >= UNTIL - 5,
        "runaway": eng.hit_event_limit,
        "occupancy": round(sum(i in cluster for i in ideas) / len(ideas), 3) if cluster and ideas else 0.0,
        "top_late": Counter(ideas).most_common(5),
    }


def summarize(rows, keys=("fires", "distinct", "late_diversity", "reactivation", "max_path_diversity", "occupancy")):
    out = {}
    for k in keys:
        vals = [r[k] for r in rows if r[k] is not None]
        out[k] = {"mean": round(statistics.fmean(vals), 3), "sd": round(statistics.pstdev(vals), 3)} if vals else None
    out["persistent_frac"] = round(sum(r["persistent"] for r in rows) / len(rows), 3)
    out["reach_frac"] = round(sum(r["occupancy"] >= 0.5 for r in rows) / len(rows), 3)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("graph")
    ap.add_argument("out")
    ap.add_argument("--samples", type=int, default=20)
    ap.add_argument("--random-starts", type=int, default=30)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--modes", nargs="+", default=["global", "relation", "reciprocal"])
    ap.add_argument("--skip-basin", action="store_true")
    a = ap.parse_args()
    rng = random.Random(a.seed)
    t0 = time.time()
    log = lambda *m: print(f"[{time.time() - t0:6.1f}s]", *m, flush=True)

    g = IdeaGraph.load(a.graph)
    ts = TextStimulus(g)
    log(f"loaded {len(g.ideas):,} ideas")
    results: dict = {"params": PARAMS, "until": UNTIL, "late": LATE}

    # --- baseline + cluster
    base = run(g, ts.stimuli("bee"))
    cluster = {f.idea for f in base.fires if f.time >= LATE}
    results["cluster"] = sorted(cluster)
    results["baseline"] = late_stats(base, cluster)
    log(f"baseline: {len(cluster)} cluster ideas, {results['baseline']}")

    if a.skip_basin:
        results['repeatability'] = 'skipped'
    # --- 1. repeatability + jitter
    sig = lambda e: [(r.time, r.target, round(r.potential_after, 9)) for r in e.trace]
    rep = {"identical_rerun": sig(run(g, ts.stimuli("bee"))) == sig(base),
           "identical_other_seed": sig(run(g, ts.stimuli("bee"), seed=99)) == sig(base)}
    jitter = []
    for name, delta in [("fire_gain", 1.8), ("fire_gain", 1.9), ("fire_gain", 2.1), ("fire_gain", 2.2),
                        ("top_k", 8), ("top_k", 12), ("top_k", 15),
                        ("global_inhibition", 0.07), ("global_inhibition", 0.13), ("global_inhibition", 0.2)]:
        p = PARAMS | {name: delta}
        s = late_stats(run(g, ts.stimuli("bee"), p), cluster)
        jitter.append({"param": name, "value": delta, **s})
    rep["jitter"] = jitter
    results["repeatability"] = rep
    log("repeatability", {k: v for k, v in rep.items() if k != "jitter"},
        [(j["param"], j["value"], j["occupancy"]) for j in jitter])

    # --- 2. basin: named + random starts
    candidates = sorted(i for i, ls in g.out_links.items() if len(ls) >= 10)
    random_starts = rng.sample(candidates, a.random_starts)
    basin = []
    for label in NAMED_STARTS + random_starts:
        stim = ts.stimuli(label) if label in NAMED_STARTS else [(label, 2.0)]
        if not stim:
            basin.append({"start": label, "matched": None})
            continue
        s = late_stats(run(g, stim), cluster)
        basin.append({"start": label, "kind": "named" if label in NAMED_STARTS else "random",
                      "matched": [i for i, _ in stim], **s})
    results["basin"] = basin
    for kind in ("named", "random"):
        rows = [b for b in basin if b.get("kind") == kind]
        results[f"basin_{kind}_summary"] = summarize(rows)
    log("basin", [(b["start"], b.get("occupancy")) for b in basin if b.get("kind") == "named"])
    log("basin random summary", results["basin_random_summary"])

    # --- 3. null models (in-place endpoint shuffles, restored afterwards)
    links = g.links
    orig_targets = [l.target for l in links]
    base_sig = signature(base.fires, LATE, UNTIL)

    nulls = {}
    panel = ["bee", "ant", "flower", "honey", "wolf"]
    for mode in a.modes:
        rows_bee, rows_panel = [], []
        for k in range(a.samples):
            restore, info = shuffle_targets(g, random.Random(a.seed * 1000 + k + {"global": 0, "relation": 500, "reciprocal": 900}[mode]), mode)
            if k == 0:
                log(f"null {mode} shuffle stats {info}")
            e = run(g, ts.stimuli("bee"))
            row = late_stats(e, cluster)
            row["sig_similarity"] = round(weighted_jaccard(signature(e.fires, LATE, UNTIL), base_sig), 3)
            rows_bee.append(row)
            for w in panel[1:]:
                rows_panel.append(late_stats(run(g, ts.stimuli(w)), cluster))
            restore()
        nulls[mode] = {"bee": summarize(rows_bee), "panel": summarize(rows_panel),
                       "bee_samples": rows_bee}
        log(f"null {mode}: bee {nulls[mode]['bee']}")
    results["null"] = nulls
    assert [l.target for l in links] == orig_targets

    # observed-vs-null table for bee
    obs = results["baseline"]
    table = {}
    for mode in nulls:
        for m in ("late_diversity", "reactivation", "max_path_diversity", "occupancy", "distinct", "fires"):
            vals = [r[m] for r in nulls[mode]["bee_samples"] if r[m] is not None]
            if not vals:
                continue
            mu, sd = statistics.fmean(vals), statistics.pstdev(vals)
            lower_is_trap = m == "late_diversity"
            extreme = sum((v <= obs[m]) if lower_is_trap else (v >= obs[m]) for v in vals)
            table[f"{mode}:{m}"] = {"observed": obs[m], "null_mean": round(mu, 3), "null_sd": round(sd, 3),
                                    "z": round((obs[m] - mu) / sd, 2) if sd else None,
                                    "p": round((1 + extreme) / (1 + len(vals)), 3)}
    results["bee_vs_null"] = table
    for k, v in table.items():
        log(k, v)

    with open(a.out, "w") as fh:
        json.dump(results, fh, indent=1, default=str)
    log(f"wrote {a.out}")


if __name__ == "__main__":
    sys.exit(main())
