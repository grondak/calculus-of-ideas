# Paraphrase-merged typed groups and sparse boundaries

No edges are added and nothing is named. Structural anomalies here are evidence about graph geometry, not discoveries.

## Equivalence classes (`classes.json.gz`)

- Candidates: 186,443 pairs from embedding neighbours (all-mpnet-base-v2) plus ConceptNet Synonym / SimilarTo / FormOf.
- Evidence: mutual entailment under nli-deberta-v3-small and nli-deberta-v3-base (stricter below cosine 0.55), or FormOf.
- Excluded: Antonym / DistinctFrom, NLI contradiction, asymmetric negation, one-way entailment, entity vs activity extensions.
- Complete linkage (every member pair joined by evidence or name cosine ≥ 0.75), class size ≤ 40.
- Result: 6,621 classes with ≥ 2 ideas, 8,747 ideas merged away, largest class 10; about half of within-class pairs share no word.
- Known errors: in a hand check of 80 random evidence pairs (seed 7), 13 (16%) are clearly not equivalent (prosecutor = prosecution, betrayal = traitor, buy_dvd = buy_vcr, bed = bedding) and 6 more are borderline (stop_vehicles = stop_car, book_ticket = make_reservations); some true paraphrases are missed (light_fire / start_fire, go_on_internet / get_onto_web).
- Nulls are generated on original IDs and contracted with the same map; link-level source datasets are kept.

## Dense groups after merging (cap 30, `report.md`)

- 1,166 real groups (unmerged 1,511); 580 pass both profile nulls; 32 pass the full selection control (unmerged 89).
- Of the 89 earlier selection survivors: 25 survive, 46 pass profile nulls only, 3 found but not significant, 15 have no matching group.
- Anomaly 18: no merged group contains ≥ 2 of its activities.
- Only one survivor spans ≥ 2 relation types and ≥ 2 independent anchor neighbourhoods: musical instruments AtLocation band / orchestra / music_store and UsedFor making_music.
- Most other survivors are answer lists to one event; the "independent neighbourhood" count still overstates independence where anchor paraphrases were missed.

## Dense groups after merging (cap 150, `../results-merged-cap150/report.md`)

- 5,050 real groups (unmerged 4,009); size ≥ 10: real 651 vs profile 377 [max 421], profile2 463 [508], relation null 971 (the relation null still produces more large groups than the real graph).
- 1,405 pass both profile nulls; 19 pass the full selection control (unmerged 53). Of the 53 earlier selection survivors: 10 survive, 29 pass profile nulls only, 13 found but not significant, 1 gone.
- Survivors are almost all exercise/fitness/health answer lists, movie/TV/internet prerequisites, city locations and military prerequisites; one spans ≥ 2 relation types and ≥ 2 independent neighbourhoods (lose_weight / stay_fit / maintain_good_health: HasPrerequisite exercise, UsedFor< going_for_run / eating_healthily).
- Anomaly 18: 69 merged groups contain ≥ 2 of its activities (UsedFor fun / enjoyment / entertainment / relaxation); 3 pass the profile nulls, none passes selection.
- 264 groups pass the profile nulls with ≥ 2 relation types and ≥ 2 independent neighbourhoods but fail selection (the null-mined groups of the same shape are as large), e.g. instruments at band / orchestra / music store; activities that Cause injury, need practice and skill, and are UsedFor pleasure / earning money.

## Sparse boundaries (`../results-boundaries-merged/`)

- Real: 4,667 candidate pairs (top 1% context similarity, disjoint cores), 227 boundaries (no links where comparable pairs are linked).
- Boundary rate 0.049 vs null means 0.031 (relation, p = 0.03), 0.051 (strict), 0.039 (profile, p = 0.18), 0.046 (profile2): no excess beyond construction. No single boundary or unlinked pair has BH q ≤ 0.10.
- Fixed real pairs re-checked in 1,000 nulls per mode (`fixed-regions.md`, BH across 23 relation strata):

| stratum | pairs | real linked | relation | strict | profile | profile2 |
|---|---|---|---|---|---|---|
| HasPrerequisite x HasPrerequisite | 543 | 0.46 | 0.51 (z −2.1, q 0.37) | 0.54 (z −3.1, q 0.023) | 0.59 (z −5.9, q 0.023) | 0.57 (z −6.1, q 0.023) |
| Causes x Causes | 164 | 0.60 | 0.57 | 0.66 (z −1.5) | 0.69 (z −2.4, q 0.18) | 0.73 (z −3.8, q 0.023) |

- Every other stratum is as linked or more linked than the nulls (location and UsedFor strata strongly so).
- The HasPrerequisite sparsity was present before merging (0.43 vs 0.51–0.52) and is stronger after it.
- Leading construction explanation (not yet tested): prerequisite lists were elicited one event at a time, so answer phrases are rarely reused across events; the nulls redistribute them across events with similar profiles.
