# Conceptual ablation and recovery — results

Can the geometry of the remaining graph reveal the shape of a removed idea? Design: [../PROTOCOL.md](../PROTOCOL.md).

**No, not in ConceptNet with these methods.** Across 80 curated (Stage 1) and 200 blind held-out (Stage 2) concepts:

| question | geometry (GEO) | best ordinary baseline | what carries the baseline |
|---|---|---|---|
| Does the graph show something is missing? | no (≈ background, ≈ sham) | none; degree reacts almost equally to sham deletions | deletion mechanics |
| Where does it belong? | no better than before deletion | PPR, but worse after deletion than before | neighbourhood density |
| What links would it have? (AP, ND, 3 seeds; S1 / S2) | 0.010 / 0.008 | PPR 0.028 / 0.037 | triangle density, common neighbours |
| Which candidate is it? (top-1 vs 9 hard decoys; chance 0.10) | 0.12 / 0.06 | name similarity 0.31 / 0.21 | words in neighbours' names |

- [STAGE1.md](STAGE1.md) — feasibility; [STAGE2.md](STAGE2.md) — blind evaluation; `stage*-tables.md` — all tables with CIs.
- Predictions are kept in `~/data/abl/*/preds` (pickled per world); nothing was written back to the graph.
- Scoring: method rankings, targets and the RANDOM baseline all use ideas with surviving degree ≥ 2; RANDOM is the exact expected AP@200 of a random ranking. Sham controls are only approximately degree-matched (see STAGE1 caveats).
