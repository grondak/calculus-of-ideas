"""Between-book vs within-book Gutenberg splits at two noise levels: per-start and distribution-level agreement."""
import json
from collections import Counter
import sys

import numpy as np

sys.path.insert(0, ".")
from ideanet.attractor import AttractorMap  # noqa: E402


def self_distribution(d, configs, seeds):
    """Same configuration, different perturbation seeds: live attractor-occupancy overlap (shared map)."""
    rows = [json.loads(line) for line in open(f"{d}/raw.jsonl")]
    rows = [r for r in rows if r["exp"] == "basin" and r["config"] in configs and r["sig"]]
    out = {}
    for c in configs:
        amap, occ = AttractorMap(threshold=0.5), {}
        for r in sorted((r for r in rows if r["config"] == c), key=lambda r: (r["k"], r["start"])):
            occ.setdefault(r["k"], Counter())[amap.assign(r["sig"], r["start"])] += 1
        ps = [{x: v / sum(o.values()) for x, v in o.items()} for o in (occ[int(k)] for k in seeds)]
        out[c] = float(np.mean([sum(min(p.get(x, 0), q.get(x, 0)) for x in p) for i, p in enumerate(ps) for q in ps[i + 1:]]))
    return out

GROUPS = {
    "wiki halves": [("wiki_half0", "wiki_half1")],
    "wiki half0 ~ its shuffle": [("wiki_half0", "wiki_half0_shuf")],
    "gut between-book": [("gut_half0", "gut_half1")],
    "gut within-book": [("gut_within0", "gut_within1")],
    "gut within ~ between": [(a, b) for a in ("gut_within0", "gut_within1") for b in ("gut_half0", "gut_half1")],
    "gut half0 ~ its shuffle": [("gut_half0", "gut_half0_shuf")],
    "wiki ~ gut (between)": [(a, b) for a in ("wiki_half0", "wiki_half1") for b in ("gut_half0", "gut_half1")],
    "wiki ~ gut (within)": [(a, b) for a in ("wiki_half0", "wiki_half1") for b in ("gut_within0", "gut_within1")],
    "original ~ wiki": [("original", "wiki_half0"), ("original", "wiki_half1")],
    "original ~ gut within": [("original", "gut_within0"), ("original", "gut_within1")],
}


def m(f, pairs):
    return float(np.nanmean([f(a, b) for a, b in pairs]))


out = {}
for d in sys.argv[1:]:
    r = json.load(open(f"{d}/ensemble-results.json"))
    B, seeds, stims = r["basin"], list(r["basin"]), list(r["stim"])
    print(f"\n== {d}  sigma={r['sigma']}")
    print(f"{'group':26s} start  dist  distL  ci95(dist)    " + " ".join(f"{s[:7]:>7s}" for s in stims))
    out[d] = {}
    for g, pairs in GROUPS.items():
        st = m(lambda a, b: np.mean([B[k]["paired_agreement_live"][a][b] for k in seeds]), pairs)
        dv = m(lambda a, b: np.mean([B[k]["distribution_overlap"][a][b] for k in seeds]), pairs)
        dl = m(lambda a, b: np.mean([B[k]["distribution_overlap_live"][a][b] for k in seeds]), pairs)
        lo = m(lambda a, b: np.mean([B[k]["distribution_overlap_ci95"][a][b][0] for k in seeds]), pairs)
        hi = m(lambda a, b: np.mean([B[k]["distribution_overlap_ci95"][a][b][1] for k in seeds]), pairs)
        so = [m(lambda a, b: r["stim"][s]["distribution_overlap"][a][b], pairs) for s in stims]
        out[d][g] = {"start": st, "dist": dv, "dist_live": dl, "dist_ci": [lo, hi], "stim": dict(zip(stims, so))}
        print(f"{g:26s} {st:.3f} {dv:.3f} {dl:.3f}  [{lo:.2f},{hi:.2f}]   " + " ".join(f"{x:7.2f}" for x in so))
    sd = self_distribution(d, r["configs"], seeds)
    out[d]["self_distribution_live"] = sd
    print("self distL (same config, across seeds):", {c: round(v, 3) for c, v in sd.items()})
    print("self (start, seeds 0v1):", {c: round(v, 3) for c, v in r["basin_self_agreement"].items()})
    print("live/attractors seed0:", {c: (s["live"], s["attractors"]) for c, s in B[seeds[0]]["summary"].items()})
    print("evidence links:", {k: v["evidence_links"] for k, v in r["topk_diagnostic"].items()})
    for s in ("bee", "ant", "flower"):
        print(s, {c: r["stim"][s]["stats"][c]["unperturbed_top"][:2] for c in r["configs"]})
json.dump(out, open("experiments/gut-split-summary.json", "w"), indent=1)
