# Profile-preserving nulls (no edges added, no labels)

Every null keeps each idea's in/out link counts per relation type and source dataset, and two-way pairs stay two-way.
`profile` additionally only swaps links whose endpoints share the same dominant (relation, direction) and log2 typed degree; `profile2` uses the top-2 (relation, direction). 100 nulls per mode, **every null re-mined** with the identical procedure.
Note: relation/strict already preserved per-relation in/out counts exactly; profile nulls add endpoint-class mixing. profile2 keeps 32% of the real typed incidences in place, so it is partly the real graph.

| | cap 30 real | profile null mean [max] | profile2 | cap 150 real | profile | profile2 |
|---|---|---|---|---|---|---|
| groups ≥ 6 | 571 | 146 [168] | 245 [269] | 1,690 | 780 [851] | 1,045 [1,118] |
| groups ≥ 10 | 155 | 14 [21] | 38 [50] | 459 | 123 [144] | 215 [237] |
| unnamed groups ≥ 6 | 423 | 116 [144] | 174 [199] | 1,141 | 542 [592] | 677 [733] |

Group-level survival (frame support at p floor under both profile nulls, reproduced in ≤ 5% of re-mined nulls, and larger than the largest same-shape null-mined group in ≥ 95% of nulls):
cap 30: 89 of 1,511 (uncategorised 68, crosscutting 17, partly named 4, named 0). cap 150: 53 of 4,009.

- **Anomaly 18 disappears.** 58 cap-150 groups contain ≥ 2 of its terms; none passes the selection control (selection p 0.05–1.0). Profile nulls mine UsedFor> fun / enjoyment / entertainment groups of 30–52 members by themselves.
- **Survivors** are almost all HasPrerequisite<, Causes<, UsedFor< shapes (answer lists to one event), for which null graphs produce essentially no groups ≥ 6. Most have paraphrase frames (light_fire / start_fire, watch_movie / see_movie): consistent with the same crowd prompt asked in different words, which these nulls cannot model.
- See report.md for every table, survivor lists, disappeared groups and the anomaly-18 family.
