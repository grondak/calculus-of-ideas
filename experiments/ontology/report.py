"""Aggregate experiments/ontology/results/runs.jsonl into tables (mean and 95% bootstrap CI over seeds)."""
import json
import sys
from collections import Counter, defaultdict

import numpy as np

METHODS = ["invent", "oracle_primitive", "L0_d3", "L0_d5", "conj_only", "stat_lr", "stat_gbm", "gbm_plus_invented"]
NON_INVENT = ["L0_d3", "L0_d4", "L0_d5", "conj_only", "stat_lr", "stat_gbm"]


def ci(xs, reps=4000, seed=0):
    xs = np.asarray(xs, float)
    if len(xs) == 0:
        return "–"
    rng = np.random.default_rng(seed)
    bs = rng.choice(xs, (reps, len(xs))).mean(1)
    lo, hi = np.percentile(bs, [2.5, 97.5])
    return f"{xs.mean():.3f} [{lo:.3f}, {hi:.3f}]"


def main(path, out):
    recs = [json.loads(l) for l in open(path)]
    fams = list(dict.fromkeys(r["family"] for r in sorted(recs, key=lambda r: ["positive", "out-of-menu", "negative"].index(r["kind"]))))
    by = defaultdict(list)
    for r in recs:
        by[r["family"]].append(r)
    L = [f"# Ontology-expansion results ({len(recs)} runs, {len(set(r['seed'] for r in recs))} seeds)", ""]
    L += ["Each cell: mean over seeds [95% bootstrap CI]. MCC on pooled held-out pairs.", ""]
    for split in ("large", "iid"):
        L += [f"## Held-out MCC, test split `{split}`", "", "| family | kind | " + " | ".join(METHODS) + " |",
              "|" + "---|" * (len(METHODS) + 2)]
        for f in fams:
            row = [f, by[f][0]["kind"]]
            for m in METHODS:
                xs = [r["results"][m][split]["mcc"] for r in by[f] if m in r["results"]]
                row.append(ci(xs) if xs else "–")
            L.append("| " + " | ".join(row) + " |")
        L.append("")
    L += ["## Fraction of held-out worlds predicted exactly (`large`)", "", "| family | " + " | ".join(METHODS) + " |",
          "|" + "---|" * (len(METHODS) + 1)]
    for f in fams:
        row = [f]
        for m in METHODS:
            xs = [r["results"][m]["large"]["exact"] for r in by[f] if m in r["results"]]
            row.append(f"{np.mean(xs):.2f}" if xs else "–")
        L.append("| " + " | ".join(row) + " |")
    L += ["", "## Paired advantage of invention over the best non-inventing method (per seed, `large` MCC)", "",
          "Best non-inventing method chosen per seed post hoc (favours baselines).", "",
          "| family | invent − best baseline | seeds invent > best + 0.01 | seeds invent < best − 0.01 |", "|---|---|---|---|"]
    for f in fams:
        d = [r["results"]["invent"]["large"]["mcc"] - max(r["results"][m]["large"]["mcc"] for m in NON_INVENT) for r in by[f]]
        L.append(f"| {f} | {ci(d)} | {sum(x > 0.01 for x in d)}/{len(d)} | {sum(x < -0.01 for x in d)}/{len(d)} |")
    L += ["", "## Invention decisions (training worlds only)", "",
          "| family | kind | seeds with any invention | operators accepted | withheld primitive recovered | CONJ-only menu accepted | L0 val MCC | GBM val MCC |",
          "|---|---|---|---|---|---|---|---|"]
    for f in fams:
        rs = by[f]
        ops = Counter(o for r in rs for o in r["accepted_ops"])
        tf = [r["true_found"] for r in rs if r["true_found"] is not None]
        L.append(f"| {f} | {rs[0]['kind']} | {sum(bool(r['accepted_ops']) for r in rs)}/{len(rs)} | "
                 f"{', '.join(f'{k}×{v}' for k, v in ops.most_common()) or '–'} | "
                 f"{f'{sum(tf)}/{len(tf)}' if tf else '–'} | {sum(r['conj_only_accepted'] > 0 for r in rs)}/{len(rs)} | "
                 f"{np.mean([r['diag_val_mcc_L0'] for r in rs]):.3f} | {np.mean([r['diag_val_mcc_gbm'] for r in rs]):.3f} |")
    L += ["", "## Definability probe: can depth-5 L0 rules reproduce each accepted invented relation?", "",
          "Target = the invented relation itself; learned on training worlds, scored on held-out worlds.", "",
          "| family | operator | n | probe MCC train | probe MCC iid | probe MCC large | large worlds reproduced exactly |", "|---|---|---|---|---|---|---|"]
    for f in fams:
        per_seed = defaultdict(list)
        for r in by[f]:
            for s, p in r.get("probe", {}).items():
                per_seed[(s.split(",")[0].strip("(' "), r["seed"])].append(p)
        g = defaultdict(list)
        for (op, _), ps in per_seed.items():
            g[op].append({k: {m: float(np.mean([p[k][m] for p in ps])) for m in ("mcc", "exact")}
                          for k in ("train", "iid", "large")})
        for op, ps in sorted(g.items()):
            L.append(f"| {f} | {op} | {len(ps)} | {ci([p['train']['mcc'] for p in ps])} | {ci([p['iid']['mcc'] for p in ps])} | "
                     f"{ci([p['large']['mcc'] for p in ps])} | {np.mean([p['large']['exact'] for p in ps]):.2f} |")
    L += ["", "## Ablation (`large` MCC; runs that accepted an invention)", "",
          "| family | n | with invention | refit without (L0 d3) | invented relation scrambled | GBM + invented features | GBM alone |",
          "|---|---|---|---|---|---|---|"]
    for f in fams:
        rs = [r for r in by[f] if r["accepted_ops"]]
        if not rs:
            continue
        g = lambda m: ci([r["results"][m]["large"]["mcc"] for r in rs])
        L.append(f"| {f} | {len(rs)} | {g('invent')} | {g('ablate_refit')} | {g('ablate_scramble')} | {g('gbm_plus_invented')} | {g('stat_gbm')} |")
    L += ["", "## L0 depth sweep (`large` MCC)", "", "| family | d3 | d4 | d5 | d5 rules |", "|---|---|---|---|---|"]
    for f in fams:
        rs = by[f]
        L.append(f"| {f} | " + " | ".join(ci([r["results"][f"L0_d{d}"]["large"]["mcc"] for r in rs]) for d in (3, 4, 5))
                 + f" | {np.mean([r['L0_d5_rules'] for r in rs]):.1f} |")
    open(out, "w").write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main(*(sys.argv[1:] or ["experiments/ontology/results/runs.jsonl", "experiments/ontology/results/SUMMARY.md"]))
