"""Distribution-level comparison of weight configurations with paired perturbations.

Every configuration (original ConceptNet weights and each learned weight file) is run under the
same set of perturbation seeds; seed k multiplies each link's weight by the *same* log-normal
factor in every configuration (k=0 is unperturbed). Two experiments:

  stimulus ensembles  N perturbed runs of each named stimulus per configuration
  basin maps          a common set of random starts (the first S starts of the 10,000-start map)
                      per configuration, at seeds --basin-seeds

Attractor identity uses the existing late-window signatures and weighted-Jaccard overlap.
Raw per-run rows are appended to OUT/raw-*.jsonl so an interrupted run resumes.

  PYTHONPATH=. python experiments/corpus_ensemble.py GRAPH.pkl OUTDIR \
      --weights wiki_evidence=PATH ... --corpus-of wiki_evidence=wiki ...
"""
from __future__ import annotations

import argparse
import gzip
import json
import multiprocessing as mp
import sys
import time
from collections import Counter
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ideanet import Engine, IdeaGraph  # noqa: E402
from ideanet.attractor import AttractorMap, signature, weighted_jaccard  # noqa: E402
from ideanet.corpus import WeightTable, load_weights  # noqa: E402
from ideanet.text import TextStimulus  # noqa: E402
from brutality import LATE, PARAMS, UNTIL  # noqa: E402

DEFAULT_STIMULI = ["bee", "honey", "ant", "flower", "wolf", "computer worm"]
G = WT = None
CONFIGS: dict = {}
EVMASK: dict = {}
CORPUS_OF: dict = {}
STIMS: dict = {}
STARTS: list = []
SIGMA = 0.05


def _run(weight_of, stimuli, mask):
    eng = Engine(G, seed=0, max_events=300_000, weight_of=weight_of, **PARAMS)
    for idea, s in stimuli:
        eng.stimulate(idea, s)
    eng.run(UNTIL)
    sig = signature(eng.fires, LATE, UNTIL)
    used = ev = 0
    if mask is not None:
        idx = WT.index
        per_idea = {}
        for f in eng.fires:
            if f.idea not in per_idea:
                out = eng._outgoing(f.idea)
                per_idea[f.idea] = (len(out), int(sum(mask[idx[id(l)]] for l in out)))
            u, e = per_idea[f.idea]
            used += u
            ev += e
    late = Counter(f.idea for f in eng.fires if f.time >= LATE)
    return {"sig": {k: round(v, 5) for k, v in sig.items()}, "fires": len(eng.fires),
            "distinct": len({f.idea for f in eng.fires}), "late_fires": sum(late.values()),
            "runaway": eng.hit_event_limit, "top": [i for i, _ in late.most_common(4)],
            "ev_share": round(ev / used, 4) if used else None}


def _weight_of(config, k):
    return WT.weight_fn(CONFIGS[config], k, SIGMA)


def task_stim(args):
    config, k = args
    wo, mask = _weight_of(config, k), EVMASK.get(CORPUS_OF.get(config))
    return [{"exp": "stim", "config": config, "k": k, "stim": name, **_run(wo, st, mask)} for name, st in STIMS.items()]


def task_basin(args):
    config, k, lo, hi = args
    wo, mask = _weight_of(config, k), EVMASK.get(CORPUS_OF.get(config))
    return [{"exp": "basin", "config": config, "k": k, "start": s, **_run(wo, [(s, 2.0)], mask)} for s in STARTS[lo:hi]]


def agree(a, b, thr=0.5):
    if not a and not b:
        return True
    return weighted_jaccard(a, b) >= thr


def top10_evidence_share(links_w, groups, mask, k=10):
    """Share of top-k propagation slots (per source with > k links) held by evidence links."""
    order = np.lexsort((-np.abs(links_w), groups))
    g = groups[order]
    starts = np.r_[0, np.flatnonzero(np.diff(g)) + 1]
    sizes = np.diff(np.r_[starts, len(g)])
    rank = np.arange(len(g)) - np.repeat(starts, sizes)
    big = np.repeat(sizes > k, sizes)
    sel = order[(rank < k) & big]
    return float(mask[sel].mean())


def main():
    global G, WT, STIMS, STARTS, SIGMA
    ap = argparse.ArgumentParser()
    ap.add_argument("graph")
    ap.add_argument("outdir")
    ap.add_argument("--weights", nargs="+", default=[])
    ap.add_argument("--corpus-of", nargs="+", default=[], help="config=corpus; configs sharing a corpus share its evidence mask")
    ap.add_argument("--stimuli", default=",".join(DEFAULT_STIMULI))
    ap.add_argument("--n", type=int, default=200)
    ap.add_argument("--starts", type=int, default=1000)
    ap.add_argument("--basin-seeds", default="0,1")
    ap.add_argument("--basins-file", default="experiments/basins-results.json.gz")
    ap.add_argument("--sigma", type=float, default=0.05)
    ap.add_argument("--workers", type=int, default=7)
    a = ap.parse_args()
    SIGMA = a.sigma
    out = Path(a.outdir)
    out.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    log = lambda *m: print(f"[{time.time() - t0:7.1f}s]", *m, flush=True)

    G = IdeaGraph.load(a.graph)
    WT = WeightTable(G)
    CONFIGS["original"] = WT.original
    prov = {}
    for spec in a.weights:
        name, path = spec.split("=", 1)
        d = load_weights(path, G)
        CONFIGS[name] = d["weights"].astype(np.float64)
        prov[name] = {**d["provenance"], "path": path}
        corpus = dict(s.split("=", 1) for s in a.corpus_of).get(name, name)
        CORPUS_OF[name] = corpus
        EVMASK.setdefault(corpus, d["joint"] >= d["provenance"]["min_count"])
    default_corpus = next(iter(EVMASK), None)
    CORPUS_OF["original"] = default_corpus
    ts = TextStimulus(G)
    STIMS.update({s: ts.stimuli(s) for s in a.stimuli.split(",")})
    STARTS[:] = [r["start"] for r in json.load(gzip.open(a.basins_file))["starts"][: a.starts]]
    seeds = [int(x) for x in a.basin_seeds.split(",")]
    log(f"loaded; configs {list(CONFIGS)}; stimuli {STIMS}; {len(STARTS)} starts")

    # static diagnostic: how much of the top-k propagation evidence links control
    src = [l.source for l in WT.links]
    groups = np.cumsum([0] + [int(src[i] != src[i - 1]) for i in range(1, len(src))])
    diag = {}
    for corpus, mask in EVMASK.items():
        diag[corpus] = {"evidence_links": int(mask.sum()), "evidence_fraction": float(mask.mean()),
                        "top10_share": {c: top10_evidence_share(w, groups, mask) for c, w in CONFIGS.items()
                                        if CORPUS_OF.get(c) == corpus or c == "original"}}
    log("top-k diagnostic", json.dumps(diag))

    raw_path = out / "raw.jsonl"
    done = set()
    if raw_path.exists():
        for line in raw_path.open():
            r = json.loads(line)
            done.add((r["exp"], r["config"], r["k"], r.get("start") or "*"))
    stim_tasks = [(c, k) for k in range(a.n + 1) for c in CONFIGS if ("stim", c, k, "*") not in done]
    chunk = 50
    basin_tasks = [(c, k, lo, min(lo + chunk, len(STARTS))) for k in seeds for c in CONFIGS
                   for lo in range(0, len(STARTS), chunk) if ("basin", c, k, STARTS[lo]) not in done]
    log(f"{len(stim_tasks)} stimulus groups, {len(basin_tasks)} basin chunks to run")
    with mp.get_context("fork").Pool(a.workers) as pool, raw_path.open("a") as fh:
        n = 0
        jobs = [(task_basin, t) for t in basin_tasks] + [(task_stim, t) for t in stim_tasks]
        for rows in pool.imap_unordered(_dispatch, jobs):
            for r in rows:
                fh.write(json.dumps(r) + "\n")
            fh.flush()
            n += 1
            if n % 50 == 0 or n == len(jobs):
                log(f"{n}/{len(jobs)} task groups")

    rows = [json.loads(line) for line in raw_path.open()]
    res = analyse(rows, list(CONFIGS), list(STIMS), seeds, a.n, log)
    res.update({"params": PARAMS, "until": UNTIL, "late": LATE, "sigma": a.sigma, "n": a.n,
                "stimuli": {k: v for k, v in STIMS.items()}, "starts": STARTS, "basin_seeds": seeds,
                "provenance": prov, "corpus_of": CORPUS_OF, "topk_diagnostic": diag})
    (out / "ensemble-results.json").write_text(json.dumps(res, indent=1))
    plot(res, out)
    log("done")


def _dispatch(job):
    fn, args = job
    return fn(args)


def overlap(p, q):
    return sum(min(p.get(x, 0), q.get(x, 0)) for x in set(p) | set(q))


def analyse(rows, configs, stims, seeds, n, log):
    res = {"configs": configs, "stim": {}, "basin": {}}
    rng = np.random.default_rng(0)
    for stim in stims:
        R = {(r["config"], r["k"]): r for r in rows if r["exp"] == "stim" and r["stim"] == stim}
        amap = AttractorMap(threshold=0.5)
        aid = {key: amap.assign(R[key]["sig"], f"{key[0]}:{key[1]}") if R[key]["sig"] else 0
               for key in sorted(R, key=lambda x: (x[1], configs.index(x[0])))}
        ks = list(range(1, n + 1))
        A = {c: np.array([aid[(c, k)] for k in ks]) for c in configs}
        occ = {c: {str(x): v / n for x, v in Counter(A[c].tolist()).most_common()} for c in configs}
        paired = {c: {d: float(np.mean([agree(R[(c, k)]["sig"], R[(d, k)]["sig"]) for k in ks])) for d in configs} for c in configs}
        ov, ci = {}, {}
        for c in configs:
            ov[c], ci[c] = {}, {}
            for d in configs:
                ov[c][d] = overlap(occ[c], occ[d])
                boots = []
                for _ in range(500):
                    idx = rng.integers(0, n, n)
                    pc, pd = Counter(A[c][idx].tolist()), Counter(A[d][idx].tolist())
                    boots.append(sum(min(pc[x], pd[x]) for x in pc) / n)
                ci[c][d] = [float(np.percentile(boots, 2.5)), float(np.percentile(boots, 97.5))]
        stats = {c: {"unperturbed_attractor": aid[(c, 0)], "unperturbed_top": R[(c, 0)]["top"],
                     "attractors": len(set(A[c].tolist())),
                     "persist": float(np.mean([R[(c, k)]["late_fires"] > 0 for k in ks])),
                     "fires_mean": float(np.mean([R[(c, k)]["fires"] for k in ks])),
                     "distinct_mean": float(np.mean([R[(c, k)]["distinct"] for k in ks])),
                     "ev_share_mean": float(np.mean([R[(c, k)]["ev_share"] or 0 for k in ks]))} for c in configs}
        labels = {str(i): [x for x, _ in sorted(rep.items(), key=lambda kv: -kv[1])[:4]] for i, rep in enumerate(amap.reps)}
        used = {x for o in occ.values() for x in o} | {str(s["unperturbed_attractor"]) for s in stats.values()}
        res["stim"][stim] = {"occupancy": occ, "paired_agreement": paired, "distribution_overlap": ov,
                             "overlap_ci95": ci, "stats": stats, "labels": {k: v for k, v in labels.items() if k in used},
                             "runs": {f"{c}:{k}": {"attractor": aid[(c, k)], "top": R[(c, k)]["top"], "fires": R[(c, k)]["fires"]}
                                      for (c, k) in R}}
        log(f"{stim}: " + "; ".join(f"{c} {stats[c]['attractors']} attr, top {list(occ[c].items())[:2]}" for c in configs))
    for k in seeds:
        R = {(r["config"], r["start"]): r for r in rows if r["exp"] == "basin" and r["k"] == k}
        starts = sorted({s for _, s in R})
        amap = AttractorMap(threshold=0.5)
        summ = {}
        assign = {}
        for c in configs:
            live = [s for s in starts if R[(c, s)]["sig"]]
            for s in live:
                assign[(c, s)] = amap.assign(R[(c, s)]["sig"], f"{c}:{s}")
            sizes = sorted(Counter(assign[(c, s)] for s in live).values(), reverse=True)
            cum = np.cumsum(sizes) / max(1, len(live))
            summ[c] = {"live": len(live), "extinct": len(starts) - len(live), "attractors": len(sizes),
                       "singletons": sum(1 for x in sizes if x == 1),
                       "cover50": int(np.searchsorted(cum, 0.5) + 1) if sizes else 0,
                       "cover80": int(np.searchsorted(cum, 0.8) + 1) if sizes else 0,
                       "largest": sizes[:10],
                       "fires_mean": float(np.mean([R[(c, s)]["fires"] for s in starts])),
                       "ev_share_mean": float(np.mean([R[(c, s)]["ev_share"] or 0 for s in starts]))}
        paired = {c: {d: float(np.mean([agree(R[(c, s)]["sig"], R[(d, s)]["sig"]) for s in starts])) for d in configs} for c in configs}
        live_paired = {c: {d: float(np.mean([agree(R[(c, s)]["sig"], R[(d, s)]["sig"]) for s in starts
                                             if R[(c, s)]["sig"] and R[(d, s)]["sig"]] or [np.nan])) for d in configs} for c in configs}
        top = Counter(assign.values()).most_common(15)
        labels = {str(i): [x for x, _ in sorted(amap.reps[i].items(), key=lambda kv: -kv[1])[:4]] for i, _ in top}
        by_cfg = {str(i): {c: sum(1 for s in starts if assign.get((c, s)) == i) for c in configs} for i, _ in top}
        res["basin"][str(k)] = {"summary": summ, "paired_agreement": paired, "paired_agreement_live": live_paired,
                                "top_attractors": {i: {"labels": labels[i], "basin_by_config": by_cfg[i]} for i in labels},
                                "assign": {f"{c}:{s}": assign.get((c, s), 0) for c in configs for s in starts}}
        log(f"basins seed {k}: " + "; ".join(f"{c} live {summ[c]['live']} attr {summ[c]['attractors']}" for c in configs))
    # intrinsic sensitivity: same configuration, two perturbation seeds
    if len(seeds) > 1:
        a, b = seeds[:2]
        Ra = {(r["config"], r["start"]): r["sig"] for r in rows if r["exp"] == "basin" and r["k"] == a}
        Rb = {(r["config"], r["start"]): r["sig"] for r in rows if r["exp"] == "basin" and r["k"] == b}
        res["basin_self_agreement"] = {c: float(np.mean([agree(Ra[key], Rb[key]) for key in Ra if key[0] == c and key in Rb]))
                                       for c in configs}
        log("basin self-agreement across seeds", res["basin_self_agreement"])
    return res


def plot(res, out):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    cfgs = res["configs"]
    short = [c.replace("wiki_", "w:") for c in cfgs]
    stims = list(res["stim"])
    fig, axes = plt.subplots(2, max(3, (len(stims) + 3) // 2 + 1), figsize=(26, 10))
    axes = axes.ravel()
    for ax, stim in zip(axes, stims):
        m = np.array([[res["stim"][stim]["distribution_overlap"][c][d] for d in cfgs] for c in cfgs])
        ax.imshow(m, vmin=0, vmax=1, cmap="viridis")
        for i in range(len(cfgs)):
            for j in range(len(cfgs)):
                ax.text(j, i, f"{m[i, j]:.2f}", ha="center", va="center", fontsize=7, color="w" if m[i, j] < 0.6 else "k")
        ax.set_xticks(range(len(cfgs)), short, rotation=60, fontsize=7)
        ax.set_yticks(range(len(cfgs)), short, fontsize=7)
        ax.set_title(f"'{stim}': attractor-distribution overlap", fontsize=9)
    rest = axes[len(stims):]
    for ax, (k, b) in zip(rest, res["basin"].items()):
        m = np.array([[b["paired_agreement"][c][d] for d in cfgs] for c in cfgs])
        ax.imshow(m, vmin=0, vmax=1, cmap="magma")
        for i in range(len(cfgs)):
            for j in range(len(cfgs)):
                ax.text(j, i, f"{m[i, j]:.2f}", ha="center", va="center", fontsize=7, color="w" if m[i, j] < 0.6 else "k")
        ax.set_xticks(range(len(cfgs)), short, rotation=60, fontsize=7)
        ax.set_yticks(range(len(cfgs)), short, fontsize=7)
        ax.set_title(f"basin map seed {k}: per-start same-attractor rate", fontsize=9)
    for ax in rest[len(res["basin"]):]:
        ax.axis("off")
    fig.tight_layout()
    fig.savefig(out / "ensemble-overview.png", dpi=110)


if __name__ == "__main__":
    main()
