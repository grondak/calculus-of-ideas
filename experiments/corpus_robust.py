"""Where does a stimulus land under each weight configuration, allowing for small perturbations?

A single deterministic run can sit on a basin boundary. For each configuration this script
runs the stimulus under N copies of its weights with multiplicative log-normal jitter
(sigma, seeded), then groups the late-window signatures into attractors (AttractorMap) shared by all
configurations. Output: per-configuration attractor occupancy distributions, plus a figure.

usage: python experiments/corpus_robust.py GRAPH.pkl OUTDIR --weights NAME=FILE ... [--stimulus bee] [--n 30] [--sigma 0.05]
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from collections import Counter
from pathlib import Path

import numpy as np

from ideanet import AttractorMap, IdeaGraph, TextStimulus, signature
from ideanet.corpus import apply_weights, load_weights

sys.path.insert(0, str(Path(__file__).parent))
from brutality import LATE, UNTIL, run  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("graph")
    ap.add_argument("outdir")
    ap.add_argument("--weights", nargs="+", default=[])
    ap.add_argument("--stimulus", default="bee")
    ap.add_argument("--n", type=int, default=30)
    ap.add_argument("--sigma", type=float, default=0.05)
    a = ap.parse_args()
    out = Path(a.outdir)
    out.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    log = lambda *m: print(f"[{time.time() - t0:6.1f}s]", *m, flush=True)
    g = IdeaGraph.load(a.graph)
    stim = TextStimulus(g).stimuli(a.stimulus)
    orig = np.array([l.weight for l in g.links], dtype=np.float32)
    configs = {"original": orig}
    for spec in a.weights:
        name, path = spec.split("=", 1)
        configs[name] = load_weights(path, g)["weights"]
    amap = AttractorMap(threshold=0.5)
    runs = {}
    for name, w in configs.items():
        rows = []
        for k in range(a.n + 1):
            jit = w if k == 0 else w * np.exp(np.random.default_rng(10_000 + k).normal(0, a.sigma, len(w))).astype(np.float32)
            restore = apply_weights(g, jit)
            e = run(g, stim)
            restore()
            sig = signature(e.fires, LATE, UNTIL)
            aid = amap.assign(sig, f"{name}:{k}")
            rows.append({"k": k, "attractor": aid, "fires": len(e.fires),
                         "top": [i for i, _ in Counter(f.idea for f in e.fires if f.time >= LATE).most_common(4)]})
        runs[name] = rows
        occ = Counter(r["attractor"] for r in rows[1:])
        log(f"{name}: unjittered -> {rows[0]['attractor']} {rows[0]['top']}; jittered occupancy {occ.most_common(6)}")
    labels = {aid: [i for i, _ in sorted(rep.items(), key=lambda kv: -kv[1])[:4]] for aid, rep in enumerate(amap.reps)}
    occupancy = {name: {str(k): v / a.n for k, v in Counter(r["attractor"] for r in rows[1:]).items()} for name, rows in runs.items()}
    res = {"stimulus": a.stimulus, "n": a.n, "sigma": a.sigma, "labels": {str(k): v for k, v in labels.items()},
           "occupancy": occupancy, "runs": runs}
    (out / f"robust-{a.stimulus}.json").write_text(json.dumps(res, indent=1))
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        aids = sorted({k for o in occupancy.values() for k in o}, key=lambda k: -sum(o.get(k, 0) for o in occupancy.values()))
        top = aids[:9]
        fig, ax = plt.subplots(figsize=(11, 0.5 * len(configs) + 2.5))
        left = np.zeros(len(configs))
        names = list(configs)
        for aid in top + ["other"]:
            vals = np.array([sum(v for k, v in occupancy[n].items() if k not in top) if aid == "other" else occupancy[n].get(aid, 0)
                             for n in names])
            lab = "other" if aid == "other" else ("extinct" if aid == "0" else f"{aid}: " + ", ".join(labels[int(aid)][:3]))
            ax.barh(names, vals, left=left, label=lab)
            left += vals
        ax.invert_yaxis()
        ax.set_xlabel(f"share of {a.n} jittered runs (weights x lognormal, sigma={a.sigma})")
        ax.set_title(f"'{a.stimulus}': attractor reached per weight configuration")
        ax.legend(fontsize=7, loc="upper center", bbox_to_anchor=(0.5, -0.18), ncol=3)
        fig.tight_layout()
        fig.savefig(out / f"robust-{a.stimulus}.png", dpi=120)
    except ImportError:
        pass
    log("done")


if __name__ == "__main__":
    main()
