"""Markdown tables from score.py's results.json (+ per-concept bootstrap CIs and property analysis)."""
import json, sys
from collections import defaultdict
import numpy as np
from scipy.stats import spearmanr, wilcoxon

r = json.load(open(sys.argv[1])); out = open(sys.argv[2], "w") if len(sys.argv) > 2 else sys.stdout
M = ["GEO", "RA", "PPR", "SPEC", "LANG"]; KINDS = ["ND0", "ND", "NI1", "NI2", "NI3"]
per = defaultdict(dict)
for k, v in r["per"].items():
    c, kind, kk = k.split("|"); per[(kind, kk)][c] = v
rng = np.random.default_rng(0)


def ci(x):
    x = np.asarray(x, float)
    if len(x) == 0:
        return "–"
    b = [rng.choice(x, len(x)).mean() for _ in range(2000)]
    return f"{x.mean():.3f} [{np.percentile(b, 2.5):.3f}, {np.percentile(b, 97.5):.3f}]"


def p(*a):
    print(*a, file=out)


P = r["props"]
p("## Ablation sizes (median per concept)\n")
p("| category | n | intact degree | surviving neighbours | ND removed ideas | NI1 removed ideas |\n|---|---|---|---|---|---|")
for cat in sorted({v["cat"] for v in P.values()}):
    vs = [v for v in P.values() if v["cat"] == cat]
    p(f"| {cat} | {len(vs)} | " + " | ".join(f"{np.median([v[f] for v in vs]):.0f}" for f in ("deg", "surv_deg", "family_nd", "family_ni1")) + " |")

p("\n## Detection: paired fraction of seeds whose gap score rose vs the unablated graph (affected / background), and AUC affected vs background in the world\n")
p("| world | " + " | ".join(M + ["DEG"]) + " |\n|---|" + "---|" * 6)
for kind in ["ND0", "ND", "NI1", "NI2", "NI3", "SHAM-ND", "SHAM-NI2", "NULL-ND"]:
    row = []
    for m in M + ["DEG"]:
        v = r["det"].get(f"{kind}|{m}")
        row.append("–" if v is None else f"{v[0]:.2f} / {v[1]:.2f} · {v[2]:.2f}")
    p(f"| {kind} | " + " | ".join(row) + " |")

p("\n## Localization: median fraction of background hypotheses ranked above the first hypothesis that lands on the concept's surviving neighbours (lower = better; INTACT = same search before ablation)\n")
p("| world | " + " | ".join(M) + " |\n|---|" + "---|" * 5)
for kind in ["ND0", "ND", "NI1", "NI2", "NI3", "SHAM-ND"]:
    row = []
    for m in M:
        a_, b_ = r["loc"].get(f"{kind}|{kind}|{m}"), r["loc"].get(f"{kind}|INTACT|{m}")
        row.append("–" if a_ is None else f"{a_[0]:.2f} (intact {b_[0]:.2f})")
    p(f"| {kind} | " + " | ".join(row) + " |")

p("\n## Relationship reconstruction: AP of the concept's surviving neighbours (top 200), mean [95% bootstrap CI over concepts]\n")
p("| world | seeds | RANDOM | " + " | ".join(M) + " | GEO > best baseline (Wilcoxon p) |\n|---|---|---|" + "---|" * 6)
for kind in KINDS:
    for kk in ("1", "3"):
        d = per.get((kind, kk), {})
        if not d:
            continue
        rnd = r["recon"].get(f"{kind}|{kk}|RANDOM", [float("nan")])[0]
        cols = [ci([v[f"{m}:ap"] for v in d.values()]) for m in M]
        geo = np.array([v["GEO:ap"] for v in d.values()]); best = np.array([max(v[f"{m}:ap"] for m in M[1:]) for v in d.values()])
        try:
            pv = wilcoxon(geo, best, alternative="greater").pvalue
        except ValueError:
            pv = float("nan")
        p(f"| {kind} | {kk} | {rnd:.4f} | " + " | ".join(cols) + f" | {pv:.3g} |")
p("\nRelation types of recovered true neighbours (GEO's predicted relation+direction vs the neighbour's most frequent relation):\n")
p("| world | GEO rel+dir | MFR rel+dir | GEO rel | MFR rel | n |\n|---|---|---|---|---|---|")
for kind in KINDS:
    g_ = r["rel"].get(f"{kind}|GEO")
    if g_:
        p(f"| {kind} | {g_[0]:.2f} | {r['rel'][kind + '|MFR'][0]:.2f} | {r['rel'][kind + '|GEO-reltype'][0]:.2f} | {r['rel'][kind + '|MFR-reltype'][0]:.2f} | {g_[1]} |")

p("\n## Candidate identification: top-1 accuracy (MRR) — true concept vs 19 degree-matched random decoys / vs 9 hard decoys\n")
MI = M + ["LANG-NAME", "RANDOM"]
p("| world | seeds | decoys | " + " | ".join(MI) + " |\n|---|---|---|" + "---|" * len(MI))
for kind in KINDS:
    for kk in ("1", "3"):
        for lab in ("rand", "hard"):
            row = [r["ident"].get(f"{kind}|{kk}|{lab}|{m}") for m in MI]
            if row[0]:
                p(f"| {kind} | {kk} | {lab} | " + " | ".join(f"{x[0]:.2f} ({x[1]:.2f})" for x in row) + " |")

p("\n## What predicts success? Spearman rho over concepts (ND world, 3 seeds; * = p < 0.01)\n")
feats = ["deg", "surv_deg", "family_nd", "tri_density", "mean_common_nbrs", "nbr_mean_deg", "name_coherence", "rel_entropy"]
d = per.get(("ND", "3"), {}); cs = sorted(d)
outcomes = {f"{m} AP": [d[c][f"{m}:ap"] for c in cs] for m in M}
outcomes.update({f"{m} hard top-1": [d[c][f"{m}:hard"] for c in cs] for m in ("GEO", "PPR", "LANG-NAME")})
p("| outcome | " + " | ".join(feats) + " |\n|---|" + "---|" * len(feats))
for o, y in outcomes.items():
    cells = []
    for f in feats:
        rho, pv = spearmanr([P[c][f] for c in cs], y)
        cells.append(f"{rho:+.2f}{'*' if pv < 0.01 else ''}")
    p(f"| {o} | " + " | ".join(cells) + " |")
if cs:
    X = np.column_stack([np.ones(len(cs))] + [np.asarray([d[c][f"{m}:ap"] for c in cs]) for m in M[1:]] +
                        [np.log1p([P[c][f] for c in cs]) for f in feats])
    y = np.asarray(outcomes["GEO AP"])
    beta, res, *_ = np.linalg.lstsq(X, y, rcond=None)
    r2 = 1 - ((y - X @ beta) ** 2).sum() / max(((y - y.mean()) ** 2).sum(), 1e-12)
    p(f"\nOLS of GEO AP on the four baselines' AP + log properties: R^2 = {r2:.2f} (n = {len(cs)}).")
p("\n## Per category (ND world, 3 seeds): mean AP, hard-decoy top-1\n")
p("| category | " + " | ".join(f"{m} AP" for m in M) + " | GEO hard | PPR hard | LANG-NAME hard |\n|---|" + "---|" * 8)
for cat in sorted({P[c]["cat"] for c in cs}):
    cc = [c for c in cs if P[c]["cat"] == cat]
    p(f"| {cat} | " + " | ".join(f"{np.mean([d[c][f'{m}:ap'] for c in cc]):.3f}" for m in M) + " | " +
      " | ".join(f"{np.mean([d[c][f'{m}:hard'] for c in cc]):.2f}" for m in ("GEO", "PPR", "LANG-NAME")) + " |")
