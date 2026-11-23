# Stage 1 (feasibility): 80 curated concepts, 90 worlds

Full tables with 95% concept-bootstrap CIs: [stage1-tables.md](stage1-tables.md). Raw scores: `stage1-results.json.gz`.
GEO is the analog-geometry method frozen on the tuning world before this run; nothing was changed after seeing these results.

## Verdict: no concept is recovered by geometry beyond ordinary baselines

| question | result |
|---|---|
| Unexpected structural feature (detection) | **No.** Only degree "detects" deletions (DEG: 100% of affected seeds change in ND/NI worlds) and it fires almost as often for degree-matched *sham* deletions (92%), i.e. it sees the mechanical signature. GEO's gap score rises for 53% of affected vs 50% of background seeds (sham: 52%); within-world AUC affected-vs-background is 0.42–0.45 for GEO and below 0.5 for RA/PPR/SPEC. (Sham worlds are only approximately degree-matched: exact per-node loss for ~80% of affected survivors, ~2× total loss; see caveats.) |
| Locate where it belongs | **No better than before deletion.** Median fraction of background hypotheses ranked above the first one landing on the concept's neighbourhood: GEO 0.28 in ND vs 0.29 in the intact graph (PPR 0.31 vs 0.22: deletion makes the spot *harder* to find). NI3 is worse (0.63); bare-node (ND0) neighbourhoods are never reached by any method (1.00). |
| Infer its relationships | **Weakly, and worse than baselines.** From 3 surviving neighbours, GEO AP 0.010 [0.005, 0.015] in ND vs RANDOM 0.0001, RA 0.019, PPR 0.028, LANG 0.020. GEO beats the best baseline for 4–14 of 80 concepts depending on world; Wilcoxon GEO > best baseline p ≈ 1 everywhere. GEO's predicted relation+direction for recovered neighbours is right 33% of the time in ND vs 55% for "most frequent relation". |
| Identify it among candidates | **Name similarity wins.** ND, 3 seeds, vs 9 hard decoys: GEO top-1 0.12, RA 0.15, PPR 0.15, LANG 0.15, LANG-NAME 0.31, random 0.10. vs 19 degree-matched decoys: GEO 0.21, PPR 0.55, LANG-NAME 0.68, random 0.05. |

## What explains the (small) recoverability that exists

- Reconstruction AP rises with the number of surviving family neighbours (Spearman +0.37 for GEO, +0.43 RA, +0.33 PPR): more targets, higher AP — a base-rate effect, not geometry.
- GEO AP is *negatively* related to the neighbours' name coherence (−0.32); LANG's is positive (+0.15, n.s.).
- The baselines' AP plus log degree / family size / triangle density / common neighbours / neighbour degree / name coherence / relation entropy explain R² = 0.51 of GEO's per-concept AP.
- Identification against degree-matched decoys is mostly degree/neighbourhood and name similarity: PPR and LANG-NAME, not GEO, carry it; against hard decoys (graph- or name-neighbours) every graph method is near chance.
- Stricter never-invented approximations remove most remaining signal (NI3 3-seed AP: GEO 0.004, RA 0.003, PPR 0.005); only LANG (0.016) and LANG-NAME survive, because surviving neighbours still carry words related to the removed name.

## A typical failure (pump, ND, 3 seeds)

Seeds given to recovery: `pirate`, `auto_part`, `pour` (random surviving neighbours; ConceptNet's RelatedTo neighbourhoods are heterogeneous).
GEO's top predictions: website, airplane, west_indies, **ship**, transsexual, wiki, … ; PPR: sailor, automotive_product, captain, …, **film**, **boat**, …, **ship**; LANG: inflections of the seed names.
None of the methods reconstruct "a device that moves fluid"; GEO follows the seeds' typed-link shape into unrelated regions.

## Caveats

- Families are approximations: broad concepts (`time`, `language`, `war`) lose hundreds of ideas in ND (median 235 for abstracts), which also removes much of what could identify them.
- Detection pools differ in size between Stage 1 (30 seeds/concept) and Stage 2 (10).
- Sham controls cut a random link whenever *either* endpoint still owes degree, so they remove about twice the real total degree and touch ~3k otherwise unaffected ideas; they are a stronger-than-matched mechanical control. Since no method detects the real ablations above background either, this does not change the detection verdict.
- Seeds are random surviving neighbours; a curated seed set would be easier but would leak the answer.
