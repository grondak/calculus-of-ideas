# Final round: relational primitive invention (ontology expansion)

This round is documented separately from the original *Calculus of Ideas* experiment. Nothing here revises or
reinterprets those findings: no evidence that ConceptNet's geometry reveals missing concepts. See the top-level
README sections and the conceptual-ablation work in PR #1. This round uses only synthetic data and does not touch
ConceptNet.

- Literature review: [LITERATURE.md](LITERATURE.md)
- Raw tables: [results/SUMMARY.md](results/SUMMARY.md); per-run records: `results/runs.jsonl`
- Project-level summary and disposition: [FINAL_SUMMARY.md](FINAL_SUMMARY.md)

## 1. Revised hypothesis and how it differs from the original

| | Original round | This round |
|---|---|---|
| Unit of novelty | a missing **concept** (node) | a missing **kind of relationship** (primitive) |
| Representation | fixed relation vocabulary, new nodes/edges | vocabulary itself may be extended |
| Claim tested | graph geometry points at unthought ideas | a learner can detect that its vocabulary is inadequate and add a primitive that improves held-out prediction |

Enumerating new combinations of existing predicates cannot answer the new question: every combination is
expressible by construction. The question is whether a system can (a) notice that no theory in its language
explains the observations well, and (b) add a relation whose extension no formula in the old language reproduces.

## 2. Experimental design

**Worlds** (`worlds.py`). Every world has the same anonymous shape: *n* entities, 2 unary predicates, 3 binary
relations and a binary target *T(x, y)*. The runner (`run.py`) permutes the relation slots once per seed and the
entity order in every world. The discovery code (`discover.py`) never imports the generators. It sees only boolean
arrays, so family names, slot order and entity order carry no signal. There are 10 families:

| family | kind | hidden rule | logical expressibility in L0 (first-order chain rules) |
|---|---|---|---|
| closure | positive | T = ancestor = transitive closure of a parent relation | not FO-definable (Aho & Ullman 1979); finite depth *d* needs ~*d* disjuncts |
| parity | positive, temporal/process | T(a, t) = odd number of a's events at times ≤ t | not FO[<]-definable (McNaughton & Papert 1971); bounded length needs ~2^(T−1) patterns |
| block | positive, latent | T = U ∧ same-hidden-class; class only visible through an assortative relation | not definable at all: the class is not a function of the observed structure, only statistically inferable |
| count | out-of-menu | T(x, y) = outdeg_R(x) > outdeg_R(y) | needs counting quantifiers; no invention operator can build it |
| closure_shallow | negative | ancestor, but trees of depth ≤ 2 (train and test) | definable: parent ∨ parent∘parent |
| closure_shuffled | negative/leakage | ancestor of an *independent* forest | unrelated to the observations; the target is still transitive |
| temporal_local | negative | event now ∧ event at the previous step | definable, depth 2 |
| compose2, compose3 | negative | T = A∘B, T = A∘B∘C | definable, depth 2 and 3 |
| noise | negative | random T, density 0.08 | nothing to explain |

Per seed and family: 16 training worlds (small), 16 held-out worlds from the same distribution (`iid`), and 16
held-out **larger** worlds (`large`). In `large`, trees and timelines are about twice as deep or long, with 2× the
entities. There are 20 independent seeds, 200 runs in total. The full run takes about 10 minutes on 8 cores:

```bash
PYTHONPATH=. python experiments/ontology/run.py --seeds 20 --out experiments/ontology/results
PYTHONPATH=. python experiments/ontology/report.py
```

**Base vocabulary L0.**
- A theory is a disjunction of up to 8 rules, each with up to 3 literals.
- A literal is a chain R1∘…∘Rd(x, y) of base relations or their converses (depth *d* ≤ 3), a negated single
  relation, or a unary predicate or its negation on x or y.
- The learner uses FOIL-style sequential covering and minimises a two-part MDL code: L(H) plus a binomial code of
  the errors, with the constraint that each rule has precision ≥ ½.

**Invention menu** (generic operators, applied blindly to every base relation and direction):

| operator | builds | parameters | expressive status relative to L0 |
|---|---|---|---|
| `TC(R)` | transitive closure | – | fixpoint; beyond FO |
| `FOLD(O, E, δ)` | 2-state automaton run along any relation O that is a chain, reading E(a, t) | 16 transition tables | fold/recursion; beyond FO[<] |
| `BLOCK(R)` | same-community relation from the spectral modularity split of R ∪ Rᵀ | – | latent variable; not a formula over observations |
| `CONJ(A, B)` | A∘B | – | **definable abbreviation** (control: complexity without a new primitive) |

**Discovery procedure** (`discover`):
1. Split the training worlds into fit (8) and validation (8).
2. Fit L0 on the fit worlds. Screen every candidate (about 600 before deduplication), discarding any whose extension
   equals an existing L0 literal.
3. Refit with each of the top 6 candidates. Accept one only if the validation description length, including the
   cost of encoding the operator choice, drops below that of the current theory. At most 2 inventions.
4. Refit on all training worlds.

Held-out worlds are never seen during discovery.

**Baselines.** All are trained on the same 16 training worlds.
- `L0_d3`, `L0_d4`, `L0_d5`: existing-predicate composition at increasing depth. d5 has about 9,300 literals; this
  is "more complexity, no new primitive".
- `conj_only`: the same invention loop restricted to `CONJ`.
- `stat_lr`: logistic regression on 58 pair features: relation indicators, in/out degrees, unary attributes and all
  depth-2 path counts.
- `stat_gbm`: gradient boosting on those features plus all 216 depth-3 path counts (feature construction).
- `oracle_primitive`: L0 plus the generator's true primitive. This is an upper bound used for evaluation only.

**Controls.**
- **Definability probe:** relabel the training worlds with the invented relation as target, fit L0 at depth 5, and
  test whether it reproduces that relation on held-out worlds.
- **Ablation:**
  - refit without the invention;
  - keep the learned theory but feed it an entity-permuted ("scrambled") invented relation;
  - give the invented relation to gradient boosting as a feature.
- **Inadequacy diagnostic:** on the discovery split only, compare L0 validation MCC with gradient-boosting validation
  MCC.

The metric is MCC on all ordered pairs, pooled over held-out worlds, plus the fraction of held-out worlds predicted
exactly. Uncertainty is a 95% bootstrap CI over the 20 seeds.

## 3. Observations

All numbers are from `results/SUMMARY.md`: held-out `large` MCC, mean [95% CI] over 20 seeds.

| family | invent | L0 d3 | L0 d5 | conj_only | LR | GBM | invention accepted | correct primitive |
|---|---|---|---|---|---|---|---|---|
| parity | **1.000** [1.000, 1.000] | 0.615 | 0.662 | 0.615 | 0.495 | 0.501 | 20/20 (FOLD) | 20/20 |
| closure | **1.000** [1.000, 1.000] | 0.677 | 0.835 | 0.677 | 0.559 | 0.673 | 20/20 (TC) | 20/20 |
| block | **1.000** [1.000, 1.000] | 0.678 | 0.678 | 0.678 | 0.871 | 0.850 | 20/20 (BLOCK) | 20/20 |
| count (out-of-menu) | 0.391 [0.364, 0.418] | 0.303 | 0.350 | 0.303 | **1.000** | **1.000** | 16/20 (BLOCK×17, TC×13) | – |
| closure_shallow | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | **20/20 (TC)** | – |
| closure_shuffled | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0/20 | – |
| temporal_local, compose2, compose3 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 / 1.000 / 0.192 | 1.000 | 0/20 each | – |
| noise | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0/20 | – |

- **O1.** In parity, closure and block, the selected primitive was exactly the withheld one in 20/20 seeds. The
  learned theories are one or two literals: `T = a6` (the invented relation) for closure and parity, and
  `T = a2 ∧ a6` (U ∧ same-block) for block. Every `large` held-out world was predicted exactly (1.00). No baseline
  predicted any of them exactly.
- **O2.** Paired against the best non-inventing method chosen per seed (post hoc, which favours the baselines), the
  invention advantage on `large` worlds is +0.337 for parity, +0.165 for closure and +0.115 for block, in 20/20
  seeds each.
- **O3.** On `iid` worlds (same size as training), depth-5 L0 nearly matches closure (0.994 vs 1.000). The gap
  opens only on larger worlds (0.835): closure is *practically* expressible at the training scale, and L0 fails to
  extrapolate. Parity shows no such recovery (L0 d5 iid 0.646); block is flat across depth (0.678 at d3, d4 and d5).
- **O4 (definability probe).** Depth-5 L0 trained to reproduce the invented relation reached held-out `large` MCC
  0.662 (FOLD), 0.835 (TC in closure) and 0.604 (BLOCK), with 0% of worlds exact. For the TC accepted in
  closure_shallow, the probe reached 1.000 with 100% of worlds exact: that invention is definable in L0.
- **O5 (ablation).** Scrambling the invented relation drops MCC to 0.002 (parity), 0.000 (closure) and 0.443
  (block). Refitting without it returns to the L0 numbers. Adding the invented relation to gradient boosting raises
  GBM from 0.501 to 1.000 (parity), 0.673 to 1.000 (closure) and 0.850 to 0.969 (block). The advantage sits in the
  primitive, not in the rule learner.
- **O6 (negative controls).** No invention was accepted in temporal_local, compose2, compose3, noise or
  closure_shuffled (0/20 each). The `CONJ`-only loop accepted nothing in any family (0/200). In closure_shallow, `TC`
  was accepted in 20/20 seeds even though the base vocabulary suffices. It brought no predictive gain (1.000 vs
  1.000), and the definability probe flagged it as definable.
- **O7 (out-of-menu).** In count, the system accepted wrong operators in 16/20 seeds. It gained only modestly over
  L0 (0.391 vs 0.350 for d5) and stayed far below logistic regression and gradient boosting, which reach 1.000 from
  ordinary degree features. The definability probe rated the spurious TC as largely definable (0.895). The
  inadequacy diagnostic did show the gap: L0 validation MCC 0.351 vs GBM 1.000.
- **O8 (inadequacy diagnostic).** The L0-vs-GBM validation gap was large for block (0.759 vs 0.940) and count, near
  zero for closure (0.891 vs 0.884), and negative for parity (0.616 vs 0.477). A low L0 residual-fit score also
  appears in noise and closure_shuffled (0.000), where there is nothing to find.

## 4. Interpretation (separate from the observations)

- **I1.** Within its menu, the system discovered relational structure that its base vocabulary could not reproduce
  on held-out worlds (O1, O2, O4), and the gain disappears under ablation (O5). In the restricted sense of this
  design, it detected that its vocabulary was inadequate: no L0 theory compressed the validation worlds as well as
  one using a new primitive. It repaired the vocabulary with a relation that generalises to larger worlds.
- **I2.** This is **conventional predicate invention**. Each successful primitive is one of four operators placed in
  the menu by the designer: a fixpoint, a 2-state fold, a latent 2-block partition, and an abbreviation.
  - TC and FOLD are recursive invented predicates, exactly the case Stahl (1995) showed to extend non-recursive
    languages. Metagol and Popper invent them routinely.
  - BLOCK is statistical predicate invention in the IRM/SBM sense.
  - The search is model selection over a meta-grammar fixed in advance, as in Kemp & Tenenbaum's structural forms.
  - "Inadequacy" was detected only relative to that meta-grammar.
- **I3.** The out-of-menu world is the critical test of the round's question, and the system failed it (O7). Facing a
  rule outside its meta-vocabulary, it did not report "my vocabulary cannot express this". It grabbed the closest
  menu items, accepted them by MDL, and gained little. Ordinary statistics with hand-chosen degree features solved
  the task. The only signal of the deeper inadequacy was the gap between L0 and the black-box model (O8). That
  signal is unreliable in both directions: it misses closure and parity, and the residual alone cannot tell
  structure from noise.
- **I4.** MDL acceptance does not separate *new capability* from *compression* (O6, closure_shallow). The
  definability probe does, but only relative to the probe's own depth bound and the held-out sizes tested. It is an
  empirical check, not a proof of inexpressibility. The logical inexpressibility claims in the design table come
  from the cited theorems, not from these runs.
- **I5.** On closure, the advantage over composition is mostly *extrapolation to larger worlds* (O3). At the training
  scale, the difference is description length, not expressibility.

## 5. Assessment: is there evidence for useful ontology expansion?

| success criterion | met? | evidence |
|---|---|---|
| not a relabeling or trivial abbreviation | yes for TC/FOLD/BLOCK in positive worlds; **no** for TC in closure_shallow and count | O4, O6 |
| measurable advantage over matched baselines | yes in positive worlds; **no** in count (LR/GBM win) | O2, O7 |
| generalises to held-out observations and worlds | yes (iid and 2× larger worlds, all exact) | O1 |
| survives leakage and complexity controls | yes: no acceptance in shuffled-target, noise or definable worlds; the CONJ-only and depth-5 baselines do not close the gap | O6, table |
| interpretable account of the new relation | yes: "ancestor", "toggled an odd number of times so far" and "same community" | O1 |
| evidence of discovering representational inadequacy beyond conventional fitting | **no**: inadequacy is detected only relative to a designer-supplied meta-language, and the system fails when the needed primitive is outside it | I2, I3 |

**Disposition: Already understood.** The positive results are real and robust (20/20 seeds, exact held-out
generalisation, clean ablations and negative controls). They are what established predicate invention
(recursive-predicate invention, statistical predicate invention, MDL model selection over structural forms) predicts.
No result shows a capability beyond those techniques. The one test that probed beyond them (count) came out
negative: ordinary feature-based statistics outperformed the inventor.

**What was demonstrated.** Under anonymised, leakage-controlled synthetic conditions, an MDL learner with a fixed
4-operator meta-vocabulary did the following:
- selected the correct withheld primitive (closure, 2-state fold, latent partition) in 60/60 positive runs;
- rejected invention in 100/100 definable, noise and shuffled-target runs;
- generalised exactly to larger held-out worlds where bounded composition and gradient boosting did not.

**What remains unknown.**
- Whether any system can extend its *meta*-vocabulary: invent an operator such as counting that was not supplied.
- Whether the results hold with noisy observations, richer worlds, ternary or higher-arity targets (not tested), or
  real data.
- How to certify inexpressibility from data rather than borrowing it from theorems.

## 6. Limitations

- The menu and the positive worlds were designed together. That is unavoidable for a controlled test and is the
  main reason the disposition is not "Demonstrated".
- The worlds are noise-free. Positives use fixed generator parameters. There is one out-of-menu family, and no
  ternary or higher-arity target.
- `BLOCK` assumes 2 communities. `FOLD` assumes 2 states and requires a relation that is an exact chain. The spectral
  split is imperfect on small worlds (block `iid` MCC 0.982).
- The statistical baselines use hand-picked features. Giving them degree features is why they solve count; giving
  them closure or parity features would solve those. "Feature construction" and "primitive invention" differ here
  only in who chooses the operator.
- The definability probe is bounded (depth 5, at most 8 rules with up to 3 literals). Failure to reproduce a relation
  is evidence of practical inexpressibility at that bound, not of logical inexpressibility.
