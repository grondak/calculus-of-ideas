"""Compare activation under original vs corpus-learned link weights (fixed topology).

For each weight configuration run the same stimuli with identical settings and record
stats, attractor signature, emitted words, causal path and full trace.
Controls per learned configuration:
  shuffle_sign: learned weights permuted across links of the same sign
  shuffle_rel:  learned weights permuted within relation type (keeps relation-level reweighting)
In "evidence" mode only the corpus-reweighted links are permuted; the rest keep original weights.

usage: python experiments/corpus_compare.py GRAPH.pkl OUTDIR --weights NAME=FILE.weights.npz ... [--stimulus bee] [--samples 20]
"""
from __future__ import annotations

import argparse
import gzip
import json
import random
import statistics
import sys
import time
from collections import defaultdict
from dataclasses import asdict
from pathlib import Path

import numpy as np

from ideanet import Engine, IdeaGraph, TextStimulus, signature, weighted_jaccard
from ideanet.corpus import apply_weights, load_weights

sys.path.insert(0, str(Path(__file__).parent))
from brutality import LATE, PARAMS, UNTIL, late_stats, run  # noqa: E402


def causal_path(fires, target: str) -> list[str]:
    """Backtrack from the first fire of `target` through the earliest-firing input each step."""
    first = {}
    for f in fires:
        first.setdefault(f.idea, f)
    path, cur, seen = [], first.get(target), set()
    while cur is not None and cur.idea not in seen:
        path.append(cur.idea)
        seen.add(cur.idea)
        prior = [first[i] for i in cur.inputs if i in first and first[i].time < cur.time]
        cur = min(prior, key=lambda f: f.time) if prior else None
    return path[::-1]


def describe(eng, ref_sigs: dict) -> dict:
    sig = signature(eng.fires, LATE, UNTIL)
    s = late_stats(eng, set(ref_sigs.get("original", sig)))
    s["sim"] = {k: round(weighted_jaccard(sig, v), 3) for k, v in ref_sigs.items()}
    top = s["top_late"][0][0] if s["top_late"] else None
    s["path_to_top_late"] = causal_path(eng.fires, top) if top else []
    s["words"] = eng.emissions[:80]
    return s, sig


def permute(weights: np.ndarray, groups: np.ndarray, rng: np.random.Generator) -> np.ndarray:
    out = weights.copy()
    for gval in np.unique(groups):
        if gval < 0:
            continue
        idx = np.flatnonzero(groups == gval)
        out[idx] = weights[rng.permutation(idx)]
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("graph")
    ap.add_argument("outdir")
    ap.add_argument("--weights", nargs="+", default=[], help="NAME=path.weights.npz")
    ap.add_argument("--stimulus", nargs="+", default=["bee"])
    ap.add_argument("--samples", type=int, default=20)
    a = ap.parse_args()
    out = Path(a.outdir)
    out.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    log = lambda *m: print(f"[{time.time() - t0:6.1f}s]", *m, flush=True)
    g = IdeaGraph.load(a.graph)
    ts = TextStimulus(g)
    links = g.links
    sign = np.sign([l.weight for l in links]).astype(int)
    rel_names = sorted({l.relation or "" for l in links})
    rel = np.array([rel_names.index(l.relation or "") for l in links])
    configs = {"original": None}
    masks: dict = {}
    prov = {}
    for spec in a.weights:
        name, path = spec.split("=", 1)
        d = load_weights(path, g)
        configs[name] = d["weights"]
        prov[name] = d["provenance"]
        if d["provenance"].get("mode") == "evidence":  # only corpus-reweighted links are shuffled
            masks[name] = d["joint"] >= d["provenance"]["min_count"]
    log(f"loaded; configs {list(configs)}")

    results = {"params": PARAMS, "until": UNTIL, "late": LATE, "provenance": prov, "stimuli": {}}
    for text in a.stimulus:
        stim = ts.stimuli(text)
        R = {"matched": stim, "configs": {}, "controls": {}}
        sigs: dict = {}
        for name, w in configs.items():
            restore = apply_weights(g, w) if w is not None else (lambda: None)
            eng = run(g, stim)
            rerun = run(g, stim, seed=99)
            s, sigs[name] = describe(eng, sigs)
            s["identical_rerun"] = [(f.time, f.idea) for f in eng.fires] == [(f.time, f.idea) for f in rerun.fires]
            slug = f"{text.replace(' ', '_')}-{name}"
            eng.write_trace(out / f"{slug}.trace.jsonl")
            with open(out / f"{slug}.trace.jsonl", "rb") as src, gzip.open(out / f"{slug}.trace.jsonl.gz", "wb") as dst:
                dst.write(src.read())
            (out / f"{slug}.trace.jsonl").unlink()
            (out / f"{slug}.fires.json").write_text(json.dumps([asdict(f) for f in eng.fires]))
            try:
                from ideanet.plot import raster
                raster(eng, str(out / f"{slug}.png"), f"{text} — {name} weights")
            except Exception as e:  # matplotlib optional
                log("plot skipped", e)
            restore()
            R["configs"][name] = s | {"signature": dict(sorted(sigs[name].items(), key=lambda kv: -kv[1])[:40])}
            log(f"{text} [{name}] fires={s['fires']} distinct={s['distinct']} react={s['reactivation']} "
                f"persist={s['persistent']} sim={s['sim']} top={s['top_late'][:3]} path={s['path_to_top_late']}")
        # pairwise similarity matrix
        names = list(sigs)
        R["similarity"] = {x: {y: round(weighted_jaccard(sigs[x], sigs[y]), 3) for y in names} for x in names}
        for name, w in configs.items():
            if w is None:
                continue
            for kind, groups in (("shuffle_sign", sign + 1), ("shuffle_rel", rel * 3 + sign + 1)):
                if name in masks:
                    groups = np.where(masks[name], groups, -1)
                rows = []
                for k in range(a.samples):
                    restore = apply_weights(g, permute(w, groups, np.random.default_rng(k)))
                    e = run(g, stim)
                    restore()
                    sig = signature(e.fires, LATE, UNTIL)
                    st = late_stats(e, set(sigs["original"]))
                    rows.append({k2: st[k2] for k2 in ("fires", "distinct", "reactivation", "late_diversity", "persistent", "occupancy", "max_path_diversity")}
                                | {"sim_original": round(weighted_jaccard(sig, sigs["original"]), 3),
                                   "sim_learned": round(weighted_jaccard(sig, sigs[name]), 3),
                                   "top_late": st["top_late"][:3]})
                obs = R["configs"][name]
                summ = {}
                for m, obs_v in (("sim_original", obs["sim"]["original"]), ("fires", obs["fires"]),
                                 ("reactivation", obs["reactivation"]), ("distinct", obs["distinct"])):
                    vals = [r[m] for r in rows]
                    summ[m] = {"observed": obs_v, "mean": round(statistics.fmean(vals), 3), "sd": round(statistics.pstdev(vals), 3),
                               "p_le": round((1 + sum(v <= obs_v for v in vals)) / (1 + len(vals)), 3),
                               "p_ge": round((1 + sum(v >= obs_v for v in vals)) / (1 + len(vals)), 3)}
                summ["sim_learned_mean"] = round(statistics.fmean(r["sim_learned"] for r in rows), 3)
                summ["persistent_frac"] = sum(r["persistent"] for r in rows) / len(rows)
                R["controls"][f"{name}:{kind}"] = {"summary": summ, "samples": rows}
                log(f"{text} control {name}:{kind} {summ}")
        results["stimuli"][text] = R
    (out / "results.json").write_text(json.dumps(results, indent=1, default=str))
    log(f"wrote {out / 'results.json'}")


if __name__ == "__main__":
    main()
