"""Sensitivity of the sparse-region result to paraphrase-merging errors.

Each variant class map is applied identically to the real graph and its nulls; real typed groups, candidate pairs
and the fixed-core null test are rebuilt from scratch for every map.
  none            no merging
  final           the class map used in results-merged
  strong          only evidence with mutual entailment >= --strong-entail in both directions and name cosine
                  >= --strong-cos; members stay merged only through such evidence
  detach-f        each merged-away idea independently detached to its own class with probability f
                  (removes a random share of merges, including the wrong ones; f = 0.16 matches the hand-check rate)
  inject-f        f x (merged-away ideas) extra false merges drawn from NLI candidate pairs the merge rejected
                  (cosine >= --inject-cos, related but not equivalent: the observed error type)
  region-unmerged final map, but every idea in a core of a HasPrerequisite x HasPrerequisite candidate pair is
                  detached (no merge touches the region)
No edges are proposed and nothing is named.
"""
import argparse, gzip, json
from pathlib import Path

import numpy as np

from experiments.morphology import log
from experiments.sparse_core import load_graph, settings, real_regions, run_nulls, class_map_from_classes
from experiments.collection_null import units


def relabel(mp):
    """Canonical labels: each class labelled by its smallest member."""
    u, inv = np.unique(mp, return_inverse=True)
    mn = np.full(len(u), len(mp)); np.minimum.at(mn, inv, np.arange(len(mp)))
    return mn[inv]


def detach(mp, nodes):
    mp = mp.copy(); mp[nodes] = -1 - np.asarray(nodes)
    return relabel(mp)


def union(mp, pairs):
    par = relabel(mp).copy()
    def find(x):
        while par[x] != x:
            par[x] = par[par[x]]; x = par[x]
        return x
    for p, q in pairs:
        a, b = find(par[p]), find(par[q])
        if a != b:
            par[max(a, b)] = min(a, b)
    return relabel(np.array([find(x) for x in range(len(par))]))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("arrays"); ap.add_argument("real"); ap.add_argument("out")
    ap.add_argument("--keep"); ap.add_argument("--sources", required=True); ap.add_argument("--classes", required=True)
    ap.add_argument("--pairs", required=True, help="nli-pairs.npz"); ap.add_argument("--nulls", type=int, default=200)
    ap.add_argument("--reps", type=int, default=5); ap.add_argument("--fracs", default="0.16,0.33,0.5")
    ap.add_argument("--strong-entail", type=float, default=0.97); ap.add_argument("--strong-cos", type=float, default=0.7)
    ap.add_argument("--inject-cos", type=float, default=0.6); ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--modes", default="strict,profile,profile2,profile|units")
    a = ap.parse_args()
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    g = load_graph(a.arrays, a.keep, a.sources)
    st = settings(a.real)
    n = g["n"]
    final = relabel(np.load(a.classes + ".npz")["cls"])
    classes = json.load(gzip.open(a.classes + ".json.gz", "rt"))["classes"]
    merged = np.flatnonzero(final != np.arange(n))
    strong = class_map_from_classes(classes, g["ids"], drop=lambda ci, ev: [
        e for e in ev if e[2] == "mutual_entailment" and min(e[3], e[4]) >= a.strong_entail and e[5] >= a.strong_cos])
    P = np.load(a.pairs)
    cand = P["pairs"][(P["cos"] >= a.inject_cos)]
    cand = cand[final[cand[:, 0]] != final[cand[:, 1]]]
    rng = np.random.default_rng(5)
    variants = [("none", np.arange(n)), ("final", final), ("strong", relabel(strong))]
    hpk = g["rels"].index("HasPrerequisite") * 1001
    reg_f = real_regions(g, final, st)
    r = reg_f["r"]; w = r["rp"] == hpk
    gi = np.unique(np.r_[r["i"][w], r["j"][w]])
    core_nodes = np.unique(r["Co"][gi].indices)
    region = np.flatnonzero(np.isin(final, core_nodes))
    variants.append(("region-unmerged", detach(final, region)))
    for f in map(float, a.fracs.split(",")):
        for k in range(a.reps):
            variants.append((f"detach-{f:g}#{k}", detach(final, merged[rng.random(len(merged)) < f])))
    for k in range(a.reps):
        pick = cand[rng.choice(len(cand), int(0.16 * len(merged)), replace=False)]
        variants.append((f"inject-0.16#{k}", union(final, pick)))
    modes = a.modes.split(",")
    rows = []
    for vi, (name, mp) in enumerate(variants):
        reg = reg_f if name == "final" else real_regions(g, mp, st)
        hp, un, _ = units(g, mp)
        stt = run_nulls(g, mp, reg, modes, a.nulls, fixed=dict(units=un), workers=a.workers, seed0=91000 + 977 * vi)
        row = dict(variant=name, merged_away=int((mp != np.arange(n)).sum()), groups=len(reg["groups"]),
                   pairs=int(len(reg["r"]["i"])), strata={})
        for t, key in enumerate(reg["keys"]):
            row["strata"][reg["names"][t]] = dict(pairs=int(reg["W"][t].sum()), linked=round(float(reg["real"][t]), 3), **{
                m: dict(mean=round(float(stt[m]["mean"][t]), 3), z=round(float(stt[m]["z"][t]), 2),
                        p=round(float(stt[m]["p"][t]), 4), q=round(float(stt[m]["q"][t]), 4)) for m in modes})
        rows.append(row)
        h = row["strata"].get("HasPrerequisite x HasPrerequisite")
        log(name, row["merged_away"], row["pairs"], json.dumps(h))
        with gzip.open(out / "merge-sensitivity.json.gz", "wt") as fh:
            json.dump(dict(settings=vars(a), variants=rows), fh)
    L = []
    for S in ("HasPrerequisite x HasPrerequisite", "Causes x Causes"):
        L += [f"\n## {S}\n", "| variant | merged away | pairs | real linked | " + " | ".join(
            m.replace("|", " fixing ") + " mean (z, p)" for m in modes) + " |", "|" + "---|" * (4 + len(modes))]
        for row in rows:
            h = row["strata"].get(S)
            if h is None:
                L.append(f"| {row['variant']} | {row['merged_away']:,} | <20 | | " + " | " * len(modes)); continue
            L.append(f"| {row['variant']} | {row['merged_away']:,} | {h['pairs']} | {h['linked']:.2f} | " + " | ".join(
                f"{h[m]['mean']:.2f} ({h[m]['z']:+.1f}, {h[m]['p']:.3f})" for m in modes) + " |")
    (out / "merge-sensitivity.md").write_text("# Merge sensitivity of sparse regions\n" + "\n".join(L) + "\n")
    log("done")


if __name__ == "__main__":
    main()
