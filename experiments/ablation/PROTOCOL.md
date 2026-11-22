# Conceptual ablation and recovery: protocol (written before any recovery result was seen)

Question: if a known idea is removed from ConceptNet, does the remaining geometry show that something is missing,
where it belongs, what relationships it had, and which candidate it was? No speculative node or edge is ever added
to the source graph; inferred structures are written only to prediction files.

## Graph
ConceptNet 5.7 English, importer filters (`build_graph.py`); analysis graph drops lexical relations (FormOf,
DerivedFrom, Etymologically*, HasContext) and Wiktionary-only links (gazetteer noise). 351k ideas, 683k links.
Lexical links are used only to build name families, never by a detector. Core = ideas with intact degree >= 2.

## Ablation worlds (per batch of concepts with disjoint families and neighbourhoods)
| world | removed |
|---|---|
| ND0 (leak control) | the bare node only |
| ND (node deletion) | name family: the node, morphological variants, FormOf/DerivedFrom relatives, paraphrase-class members (results-merged/classes.json.gz), Synonym/SimilarTo neighbours that are names (text cosine >= 0.6 or degree <= the concept's), and compounds containing any family name as a token sequence; all incident links |
| NI1 (dependents) | ND + ideas that would hardly exist without it: >= 50% of their links go to removed ideas, or a hyponym/part/instance/manner/material of a family member with >= 25% of links to removed ideas (two rounds) |
| NI2 (references) | NI1 + links among survivors whose ConceptNet surface text mentions a family name |
| NI3 (closure, upper bound) | NI2 + every link between two surviving former neighbours (triangles closed through the concept); also removes independent knowledge, so it is a stress test, not a world |
| SHAM-ND, SHAM-NI2 (artifact control) | nothing removed from the family; every survivor that lost k links in ND / NI2 loses k other random links instead (exact degree deficits, no coherent missing idea) |
| NULL / NULL-ND (artifact control) | relation- and reciprocity-preserving target shuffle of the whole graph; then the same family node IDs removed (same deletion mechanics, incoherent neighbourhood) |
The intact graph is shared by all batches.

## Blinding
The recovery program reads only: world edge lists (anonymous world IDs), idea names, a shuffled pool of seed ideas,
seeded-task hints and anonymous candidate profiles. It never reads the intact graph, the family files or the answer
key. Ideas with no link in a world are invisible to it (vocabulary entries are never enumerated). Identification
scores only (inferred profile, candidate profile) pairs, so it cannot test which candidate is absent from the graph.

## Methods (fixed before Stage 1; no tuning on Stage 1 or 2 outcomes)
- GEO (geometry): typed low-rank geometry. Matrix of ideas x typed features (relation, direction, partner),
  column-normalised by 1/sqrt(df), truncated SVD d=128. A hypothetical idea linked to seed set S is folded in as
  x = sum over s in S and (relation,direction) of prior(r,dir) * feature(r,dir,s); predicted profile x V V^T gives a
  score and a relation for every (r, dir, v). Two mean-shift refolds on the top 10 predictions.
  Pre-Stage-1 change (made on a tuning world: 150 random non-Stage-1 ideas removed as bare nodes, listed in
  `tuning_nodes.json`, excluded from Stage 2): the fold-in projection above scored rare typed columns highest
  (AP 0.0006 for 3 seeds; e.g. food-recipe ideas for "water"). Of three geometric variants (cosine to the folded point,
  same with refolds, analog ideas) the analog variant scored best and is the frozen GEO: fold the hypothetical idea
  in, take the 50 ideas nearest to it in the typed low-rank space, and predict its typed links as their
  similarity-weighted typed links. On the tuning world GEO (AP 0.011) is still below RA (0.036), LANG (0.028) and
  PPR (0.062); this was fixed before any Stage 1 run.
- LP baselines (ordinary link prediction): resource allocation over 2 hops from S (RA), personalised PageRank
  (restart 0.3, 10 iterations, PPR), untyped spectral embedding (normalised adjacency SVD d=128, cosine to seed
  centroid, SPEC). Relation baseline: the candidate idea's most frequent relation.
- LANG (language): all-MiniLM-L6-v2 name embeddings, cosine to the seed-name centroid; no graph.
- RANDOM: uniform guessing among matched candidates / pool order.

## Questions and metrics
1. Detection. Every method turns each pool seed s into a hypothesis H_s (s plus its top-10 predictions) with
   gap(H) = coherence_M(H) x (1 - coverage(H)): coherence = mean pairwise cosine in the method's own space
   (RA: adjacency rows), coverage = largest fraction of H adjacent to one existing idea. Pool = surviving former
   neighbours of every ablated concept plus 5x background ideas matched on world degree, shuffled.
   Reported: paired AUC of gap(s) ablated vs intact for affected seeds, in ND/NI vs SHAM vs NULL-ND vs NULL;
   percentile of affected seeds among background. A method detects missing knowledge only if the ablated
   effect exceeds the SHAM and NULL effects.
2. Localization (blind). Rank of the first pool hypothesis with >= 30% of H in the concept's surviving neighbours,
   as a percentile of the pool background (estimated fraction of the graph scanned before reaching it).
3. Relationship reconstruction (seeded hints: k = 1 or 3 random surviving former neighbours). AP and recall@50
   of the remaining surviving core neighbours among all core ideas; relation-type accuracy of recovered true
   neighbours vs the majority/most-frequent-relation baseline.
4. Candidate identification. True concept vs 19 random decoys matched on surviving degree, and vs 9 hard decoys
   (most similar ideas in the intact graph by neighbourhood Jaccard and by name, excluding the family).
   Score = cosine between the inferred profile (top 200) and the candidate's known neighbours; LANG uses name
   cosine to the seeds. Top-1 and MRR vs 1/20 and 1/10.
5. Properties. Per concept: intact and surviving degree, family size, triangle density and mean common neighbours
   among surviving neighbours, name coherence of neighbours, relation entropy, category. Spearman with each
   method's success, and a regression of GEO success on baseline success plus properties.

## Stages
- Dev: 20 random concepts outside both stages, for debugging only.
- Stage 1 (feasibility): 80 hand-chosen concepts, 20 each of physical objects, mechanisms, processes, abstract ideas.
- Stage 2 (blind): stratified random sample (by intact degree) of held-out concepts with intact degree 10-500,
  >= 5 surviving core neighbours and family size <= 200, excluding Stage 1 and dev concepts and their families;
  sampler, seed and analysis frozen and committed before the run.
