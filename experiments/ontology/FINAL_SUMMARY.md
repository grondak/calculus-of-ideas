# Calculus of Ideas: final round summary (ontology expansion)

**Question.** Can a system recognise the limits of its own ontology and discover a relationship that its existing
conceptual vocabulary could not adequately express?

**Relation to the original round.** The original round asked whether relationships among known ideas (ConceptNet
geometry) reveal missing ideas. Its negative findings stand unchanged. This round moved the hypothesis from missing
*concepts* to missing *kinds of relation*, and tested it only on synthetic worlds.

**Experiment.**
- 10 anonymised synthetic world families with hidden relational rules: transitive closure, temporal parity, a latent
  partition, a counting comparison outside the menu, and 6 negative or leakage controls.
- 20 seeds, with held-out worlds at the training size and at about 2× that size.
- Discovery uses an MDL rule learner over a restricted first-order vocabulary. It may add primitives from 4 generic
  operators: closure, 2-state fold, 2-block partition, and composition as an abbreviation control.
- It is compared with deeper composition, composition-only invention, logistic regression and gradient boosting,
  plus definability probes and ablations.
- Pure NumPy/scikit-learn with no paid API calls. A full run takes about 10 minutes on 8 cores.

**Result.**
- In the 3 in-menu positive families, the system selected the withheld primitive in 60/60 runs. It predicted every
  larger held-out world exactly, beating the best baseline by +0.12 to +0.34 MCC.
- The gain vanished when the primitive was ablated.
- It invented nothing in 100/100 definable, noise and shuffled-target runs.
- It did invent an unnecessary but definable closure in all 20 shallow-tree runs, with no predictive gain. MDL alone
  does not separate compression from new capability.
- In the out-of-menu counting world, it accepted wrong primitives and lost to ordinary statistics: 0.39 vs 1.00 MCC.

**Disposition: Already understood.** The system performs conventional predicate invention: recursive predicates,
statistical (latent) predicates, and model selection over a fixed meta-grammar of forms. This is well covered by ILP
(Stahl 1995; Metagol; Popper), statistical predicate invention (IRM; Kok & Domingos 2007) and structural-form
discovery (Kemp & Tenenbaum 2008). It recognises vocabulary inadequacy only relative to a meta-vocabulary its designer
supplied. When the needed primitive lay outside that meta-vocabulary, it neither repaired the gap nor reported it
reliably.

**Open question (not pursued; out of scope by decision).** Whether a system can extend its meta-vocabulary, inventing
an *operator* rather than an instance of one. Beth's definability theorem and Fodor's concept-learning argument suggest
this cannot be done by hypothesis testing within a fixed language.

The project is closed after this round.

Details: [README.md](README.md) · [LITERATURE.md](LITERATURE.md) · [results/SUMMARY.md](results/SUMMARY.md)
