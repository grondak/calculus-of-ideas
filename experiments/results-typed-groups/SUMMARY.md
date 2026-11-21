# Wiktionary removal, strict null, typed-relation groups

No edges added, no labels invented. Graph variant: links with only Wiktionary provenance removed (689,944 of 4,341,307 links kept).
Nulls: global, relation-type, reciprocity, and strict (relation x source dataset x reciprocity x log-degree class), 100 samples each; floor p = 1/101.

## Earlier top-20 after Wiktionary removal (morphology.py --keep, 4 nulls)
| anomaly | survives all 4 nulls | note |
|---|---|---|
| shelf – table, zoo – mammal, play_music – orchestra, coach – player, s.a – company, blisters – exercise | yes | |
| silk – cotton | no | strict p = 0.64 (shared neighbours are RelatedTo) |
| new_york – county_seat, diminutive – given_name, chemical_element – atomic_number, minor_key – root, classical_greek – letter, austro_hungarian – europe | gone | no shared neighbours left; they were Wiktionary structure |
| holes nebraska, coffee, web, transformation | no cross-cluster evidence | nebraska shrinks to degree 12 |
Graph level: overlap J >= 0.2 pairs in the 3,000-idea sample: real 395; null means global 3.8, relation 1.9, reciprocity 2.8, strict 89.1.

## Typed groups
Member = idea sharing >= 60% of a frame of typed (relation, direction, neighbour) features; category relations excluded from frames and used only to test naming.
Robust = all 4 nulls at floor, recovered in >= 60% of 5 re-mined 80% edge subsamples, frame support not lower with Wiktionary restored.

| member cap (typed features) | groups | size >= 10 | relation-null re-mined size >= 10 | strict-null re-mined size >= 10 | robust |
|---|---|---|---|---|---|
| 30 (results-typed-groups) | 1,511 | 155 | 14–16 | 2–7 | 434 |
| 150 (results-typed-groups-cap150) | 4,009 | 459 | 543–620 | 48–60 | 986 |

With hub ideas allowed as members (cap 150), mining relation-preserving shuffles yields as many large groups as the real graph: group existence there is not evidence. Per-frame support tests still pass, but they are post-selection.
Anomaly 18 core (swimming, dancing, skiing, ...) has 70–130 typed features each, so it appears only in the cap-150 run: a family of overlapping UsedFor> fun / pleasure / enjoyment / entertainment / exercise frames (strict-null mean support 7–20 vs observed 23–62).

Tiers measure ConceptNet's IsA coverage, not human nameability: most "uncategorised" groups are verb-phrase events (prerequisites, causes, capabilities) which ConceptNet never categorises; most "crosscutting" groups are things AtLocation one place.
See report.md for per-group members, frames, nulls, categories, corpus counts and weight consistency.
