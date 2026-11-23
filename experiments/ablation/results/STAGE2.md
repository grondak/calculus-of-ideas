# Stage 2 (blind, held out): 200 concepts, 66 worlds

Concepts: the first 200 eligible entries of `stage2.txt` (log-degree quartiles q0–q3 of ideas with intact degree 10–500;
Stage 1, dev and tuning ideas and their name families excluded). Method, sample and scoring were committed before any
Stage 1 result was seen; recovery read only `blind/` (worlds, seeds, unlabeled candidates and pools), never `key/`.
Full tables with 95% concept-bootstrap CIs: [stage2-tables.md](stage2-tables.md); raw scores `stage2-results.json.gz`.

## Verdict: Stage 1's negative result replicates; geometry is the weakest graph method on every task

| task | result (ND = family deletion, 3 surviving-neighbour seeds unless stated) |
|---|---|
| Detection | **No signal beyond the deletion mechanics.** DEG flags 100% of affected seeds in ND/NI worlds and 90% in degree-matched sham worlds. GEO: 51% of affected vs 50% of background seeds rise (sham 51%); within-world AUC 0.45–0.52. RA/PPR rise more for *background* than affected seeds (graph-wide renormalisation). |
| Localization | **Fails.** GEO's and RA's best-ranked hypotheses almost never overlap the concept's surviving neighbourhood (median 1.00 = never, intact graph also 1.00). PPR gets 0.69 after ND vs 0.42 before deletion: deletion makes the spot harder, not easier, to find. |
| Relationship reconstruction | GEO AP 0.008 [0.005, 0.010] vs RANDOM 0.0005, RA 0.020, PPR 0.034, LANG 0.010. GEO beats the best baseline for 13–31 of 200 concepts depending on world (Wilcoxon p ≈ 1). Relation+direction of recovered neighbours: GEO 32% vs 55% for most-frequent-relation. |
| Candidate identification | vs 9 hard decoys: GEO top-1 0.06 (11/200; *below* the 0.10 chance level, binomial p = 0.02), RA 0.10, PPR 0.14, LANG 0.15, LANG-NAME 0.21. vs 19 degree-matched decoys: GEO 0.20, RA 0.46, PPR 0.51, LANG 0.40, LANG-NAME 0.59, chance 0.05. |
| Never-invented approximations | NI1/NI2 change little; NI3 (also cutting links among former neighbours) drives RA to chance (AP 0.001, hard top-1 0.01) and halves PPR, while LANG and LANG-NAME keep most of their signal. |

## What explains recoverability

- PPR/RA succeed for concepts whose surviving neighbours are interlinked: PPR AP vs triangle density ρ = +0.52, common neighbours +0.30, neighbour name coherence +0.35; PPR does worse for broad concepts (surviving degree −0.35).
- GEO's AP rises with degree (+0.27), surviving degree (+0.25) and neighbour degree (+0.29): it does better where there are more targets and hub-like neighbours — base rate, not shape.
- LANG's AP tracks name coherence (+0.31); identification is dominated by name similarity (LANG-NAME) in every world.
- Baselines + log properties explain only R² = 0.14 of GEO's per-concept AP (0.57 in Stage 1) — GEO's residual variation is mostly noise at these AP levels (mean 0.008), not an independent signal: it never exceeds the best baseline on average.

## Changes vs Stage 1

Stage 2 concepts are smaller (median intact degree 11–50 by quartile vs 20–113 by category), so random AP is lower and
localization (≥30% overlap of a 10-idea hypothesis with the neighbourhood) is rarely achievable; detection pools have 10 seeds/concept (Stage 1: 30).
