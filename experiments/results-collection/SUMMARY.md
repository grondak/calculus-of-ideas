# Collection artifacts and merge sensitivity of the sparse regions

No edges were added and nothing was named.

## Collection-unit null (`collection-null.md`, 1,000 nulls per mode, paraphrase-merged graph)

Collection unit of an event = the event plus its HasPrerequisite answers (1,272 units). "fixing hp" holds every
HasPrerequisite link fixed (each event keeps its exact list); "fixing units" also holds every other link inside a unit
(26,664 of 689,944 links); everything else is shuffled exactly as in the earlier nulls.

| HasPrerequisite x HasPrerequisite (543 pairs, real linked 0.46) | null mean | z | BH q |
|---|---|---|---|
| strict | 0.54 | -3.2 | 0.023 |
| profile | 0.59 | -5.8 | 0.023 |
| profile2 | 0.57 | -5.9 | 0.023 |
| profile fixing hp | 0.52 | -4.2 | 0.023 |
| strict fixing units | 0.49 | -2.4 | 0.14 |
| profile fixing units | 0.49 | -2.3 | 0.14 |
| profile2 fixing units | 0.48 | -2.5 | 0.069 |

- Holding the units intact removes about 80% of the deficit (0.13 -> 0.03); the remainder is not significant after
  correction. In the profile nulls the extra cross-links are mainly HasPrerequisite links moved between lists
  (0.39 of pairs vs 0.33 real).
- Causes x Causes (164 pairs, 0.60): holding Causes units fixed gives null means 0.58-0.61 (`../results-collection-causes`).
- Provenance: 81% of answer phrases occur in one event's list only; 64% of the links use the template "If you want to X
  then you should Y". A reused answer comes from the same contributor in 9.7% of cases (2.8% for random link pairs).
  89% of HasPrerequisite candidate pairs share at least one contributor, so contributor overlap does not separate them.

## Merge sensitivity (`../results-merge-sensitivity/merge-sensitivity.md`, 200 nulls per mode and map)

Every class map is applied to the real graph and its nulls, and groups and candidate pairs are rebuilt. Maps: none,
final, strong evidence only (3,309 merged), region-unmerged, 5 x random detachment of 16 / 33 / 50% of merged ideas,
5 x injection of 1,400 false merges from related NLI-rejected pairs.

- HasPrerequisite x HasPrerequisite is underlinked relative to the profile nulls in all 24 maps (profile p <= 0.025,
  profile2 p = 0.005), including no merging (0.43 vs 0.51-0.52).
- Against the collection-unit null it is not underlinked without merging (0.43 vs 0.42), with strong merges only
  (0.44 vs 0.44) or region-unmerged (0.38 vs 0.38); 5 of 24 maps give p < 0.05. The residual after fixing units is
  therefore a merge artifact.
- Causes x Causes is not underlinked without merging (0.73, above every null) or with strong merges only; the
  sparsity appears only with merging.

## Dense-group survivors (`dense-survivors.md`)

The frame links of the 32 (cap 30) and 19 (cap 150) selection survivors are not concentrated on one contributor
(median top-contributor share 0.14 and 0.10 vs random 0.14 and 0.13; 3 of 51 groups concentrated). They are lists
written by many contributors answering the same prompt, often under paraphrased anchors the merge kept apart
(watch_movie / enjoy_film, getting_onto_web / go_on_internet, take_shower / having_bath).

## Reading

Every sparse region found so far is reproduced by graph construction once each event's answer list is kept intact and
merges are restricted to well-supported ones. Within ConceptNet no unexplained sparse geometry remains under these controls.
