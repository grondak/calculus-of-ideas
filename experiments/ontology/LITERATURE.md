# Literature review: relational primitive invention and ontology expansion

Scope: work that bears on whether a learner can detect that its vocabulary is inadequate and add a new relational
primitive. Citations are to the primary sources as best known; page-level claims were not re-checked for this round.

## 1. Predicate invention in inductive logic programming (ILP)

- **Inverse resolution.** Muggleton & Buntine (1988, *Machine invention of first-order predicates by inverting
  resolution*, ICML) introduced the W-operator (CIGOL), which proposes a new predicate when two clauses share a body
  pattern. The earlier propositional system DUCE (Muggleton, 1987) did the same for propositional theories.
- **Necessity of invention.** Stahl (1993, *Predicate invention in ILP — an overview*, ECML) and Stahl (1995, *The
  appropriateness of predicate invention as bias shift operation in ILP*, Machine Learning 20) separate
  invention that only compresses from invention that extends the language. Non-recursive invented predicates can be
  unfolded away, so for function-free definite programs only recursive invented predicates change what is learnable.
  This is the formal version of our "novelty" control: a non-recursive abbreviation is a renaming.
- **Demand-driven invention.** Wrobel (1994, *Concept formation during interactive theory revision*, Machine
  Learning 14; MOBAL) invents a new concept when a rule has exceptions that the current vocabulary cannot separate.
  This is the closest prior answer to "recognising the limits of one's ontology": the trigger is an irreducible
  residual. Kramer (1995, *Predicate invention: a comprehensive view*, tech. report OFAI-TR-95-32) surveys this line.
- **Bias shift.** Utgoff (1986, *Shift of bias for inductive concept learning*, in Machine Learning II; the STABB
  system) adds new terms when the hypothesis space can no longer fit the data.
- **Meta-interpretive learning.** Muggleton, Lin & Tamaddoni-Nezhad (2015, *Meta-interpretive learning of
  higher-order dyadic Datalog: predicate invention revisited*, Machine Learning 100; Metagol) invents recursive
  predicates via metarules (chain, identity, tail-recursion). Cropper & Muggleton (2016+) and Cropper, Morel &
  Muggleton (2020, *Learning higher-order logic programs*, Machine Learning 109) add higher-order operators such as
  map, fold and until. These are explicitly a menu of second-order templates, which is also what our operator menu
  is.
- **Learning from failures.** Cropper & Morel (2021, *Learning programs by learning from failures*, Machine Learning
  110; Popper) and Cropper & Morel (2021, *Predicate invention by learning from failures*, arXiv:2104.14426).
  Cropper & Dumančić (2022, *Inductive logic programming at 30: a new introduction*, JAIR 74) is the current survey.
  It names predicate invention as a central open problem, mainly on search cost rather than on the question of
  whether new primitives exist.
- **Differentiable ILP.** Evans & Grefenstette (2018, *Learning explanatory rules from noisy data*, JAIR 61; ∂ILP)
  uses program templates with invented auxiliary predicates. Yang, Yang & Cohen (2017, *Differentiable learning of
  logical rules for knowledge base reasoning*, NeurIPS; Neural LP) learns chain rules (our L0) differentiably.
  Dong et al. (2019, *Neural Logic Machines*, ICLR) learn bounded-depth relational reasoning.
- **Rule learning with MDL.** Quinlan (1990, *Learning logical definitions from relations*, Machine Learning 5; FOIL)
  is the sequential-covering learner our L0 baseline imitates. Its stopping rule is an encoding-length criterion.
  Muggleton (1995, *Inverse entailment and Progol*, New Generation Computing 13) uses compression to score clauses.

## 2. Statistical predicate invention and relational representation learning

- Kemp, Tenenbaum, Griffiths, Yamada & Ueda (2006, *Learning systems of concepts with an infinite relational model*,
  AAAI): latent classes of entities that explain several relations. This is our `BLOCK` operator in nonparametric
  Bayesian form, and our block world is a stochastic block model (Holland, Laskey & Leinhardt, 1983).
- Kok & Domingos (2007, *Statistical predicate invention*, ICML; MRC) invent predicates by clustering entities and
  relations jointly in Markov logic.
- Dumančić & Blockeel (2017, *Clustering-based relational unsupervised representation learning with an explicit
  distributed representation*, IJCAI) build new relational features by clustering.
- Kemp & Tenenbaum (2008, *The discovery of structural form*, PNAS) choose among a grammar of structural forms (chain,
  ring, tree, cluster) by Bayesian model selection. This is structurally the same as our experiment: a fixed
  meta-grammar of forms, with selection by marginal likelihood.
- Newman (2006, *Modularity and community structure in networks*, PNAS) gives the spectral modularity split used by
  `BLOCK`.
- Bengio, Courville & Vincent (2013, *Representation learning: a review and new perspectives*, IEEE TPAMI) is the
  general framing: learned latent variables are new "primitives" for a downstream predictor.

## 3. Program synthesis and library learning

- Dechter, Malmaud, Adams & Tenenbaum (2013, *Bootstrap learning via modular concept discovery*, IJCAI; EC) and Ellis
  et al. (2021, *DreamCoder*, PLDI) grow a library of reusable abstractions by compression. Bowers et al. (2023,
  *Top-down synthesis for library learning*, POPL; Stitch) do the same faster.
- New library functions are lambda-abstractions over the base DSL. They are definable by construction: they change
  description length and search cost, not expressivity. This is the analogue of our `CONJ` control.

## 4. Scientific theory formation and theoretical terms

- Langley, Simon, Bradshaw & Zytkow (1987, *Scientific Discovery: Computational Explorations of the Creative
  Processes*): BACON introduces "intrinsic properties" (e.g. mass, specific heat). These are latent per-object
  numbers postulated when a law holds only after assigning each object a constant. This is a historical example of
  primitive invention driven by residual structure.
- Schmidt & Lipson (2009, *Distilling free-form natural laws from experimental data*, Science) search over
  expressions in a fixed operator set.
- Philosophy of theoretical terms: Ramsey sentences, Lewis (1970, *How to define theoretical terms*, J. Philosophy),
  and Craig's interpolation/elimination results. **Beth's definability theorem** (Beth, 1953) states that in
  first-order logic, a predicate implicitly fixed by a theory is explicitly definable from the old vocabulary. So
  within FO, a genuinely new primitive has to be one the observations do *not* pin down from the old vocabulary,
  i.e. a latent (theoretical) term, or it has to leave FO (fixpoints, counting).

## 5. Expressibility (finite model theory)

- Aho & Ullman (1979, *Universality of data retrieval languages*, POPL) and Fagin (1975): transitive closure is not
  expressible in relational algebra or first-order logic. Gaifman (1982) locality and Ehrenfeucht–Fraïssé games give
  the standard proofs (Libkin, 2004, *Elements of Finite Model Theory*; Immerman, 1999, *Descriptive Complexity*).
- McNaughton & Papert (1971, *Counter-Free Automata*): FO[<] over strings defines exactly the star-free languages.
  Parity is not star-free, so "an odd number of events so far" is not FO-definable even with a linear order.
- Counting comparisons (|R(x)| > |R(y)|) need counting quantifiers (FO+C).
- On finite worlds with bounded size or depth, all of these become FO-definable by finite disjunctions. That is the
  difference between *logical* expressibility (unbounded worlds) and *practical* expressibility (description length
  growing with world size). Closure needs about d disjuncts for depth d, while parity over T steps needs on the
  order of 2^(T−1) conjunctive patterns.

## 6. Cognitive science: learning new representational resources

- Fodor (1975, *The Language of Thought*; 1980 Piaget–Chomsky debate): hypothesis-testing learners cannot acquire
  concepts more expressive than the language in which they frame hypotheses ("the paradox of concept learning").
- Carey (2009, *The Origin of Concepts*) proposes "Quinian bootstrapping" as a way around it.
- Piantadosi, Tenenbaum & Goodman (2016, *The logical primitives of thought*, Psychological Review) infer *which*
  primitive set best explains human concept learning, by model comparison across candidate grammars.
- Ullman, Goodman & Tenenbaum (2012, *Theory learning as stochastic search in the language of thought*, Cognitive
  Development) learn theories that introduce new latent predicates.
- Chiang (1998, *Story of Your Life*; the basis of *Arrival*) is the motivating fiction. Nothing above bears on it
  directly.

## What is and is not novel about our question

- **Already established.**
  - Inventing a predicate that compresses a theory is old (1987–1995).
  - Inventing a *recursive* predicate, which provably extends a non-recursive language (Stahl), is standard in MIL
    and Popper.
  - Inventing a latent class that no rule over observed relations defines is standard in statistical predicate
    invention and SBM/IRM.
  - Triggering invention from an irreducible residual is Wrobel's demand-driven approach and Utgoff's bias shift.
  - Choosing among structural forms by model selection is Kemp & Tenenbaum's approach.
- **Standing objection.** All of these invent *within a meta-language fixed in advance*: metarules, higher-order
  templates, a clustering model, a form grammar. Fodor's argument and Beth's theorem jointly predict this. Such a
  system can move from FO to a fixpoint or latent-variable extension only if that extension is already in its
  meta-vocabulary.
- **What this round adds.** It is a methodological contribution, not a new capability:
  - a small, controlled test that separates logical expressibility from description length;
  - invention scored by held-out prediction rather than self-assessment;
  - negative controls where invention is permitted but unnecessary;
  - an "out-of-menu" world that tests whether the system can recognise inadequacy it cannot repair.

  We found no prior work framed exactly this way. Each ingredient has precedents, and we do not claim novelty for
  any of them.
