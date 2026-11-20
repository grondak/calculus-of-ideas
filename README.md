# ideanet: activation dynamics over an idea graph

Prototype for the "calculus of ideas": ideas are nodes, relationships are signed,
weighted, delayed links, and activation propagates through a deterministic
discrete-event queue. Human words are only an output projection; ideas may have
several approximate words or none.

Pure Python 3.10+, no runtime deps (matplotlib optional for plots).

## Model
- **Idea**: decaying potential (`decay_tau`), `threshold`, `refractory`, `labels` (empty = no human word).
- **Link**: `weight` (+ excitatory / - inhibitory), `delay`, optional `context` gate.
- **Engine**: heap-ordered events `(time, seq)`; deterministic for a given seed.
  Convergent sub-threshold inputs can fire an idea that no single input could.
  Optional spontaneous noise and an `interpreter` callback that reads recent fires
  and injects stimuli back (the human/LLM feedback loop; off by default).
- **Trace**: every delivered event (potential before/after, fired) is kept, not just words.

## Analysis
- `characterize`: extinct / periodic / persistent / runaway, attractor set and period,
  recurrent window states, path diversity (same idea re-firing via different input sets),
  fires of unnamed ideas.
- `null_comparison`: degree-preserving rewired graphs (same in/out degree and weights) -> z and p.
- `perturb_links`: knock out each link, rank by how much the dynamics change.
- `random_ontology` / `inject_unfamiliar`: community-structured graphs at 500-2000+ ideas,
  plus "bee-axle" links between ideas with no path of length <= 2.

## Usage
```
pip install -e .[plot,dev]
ideanet run ontologies/harbor.json -s harbor:2 --until 300 --plot raster.png --trace trace.jsonl
ideanet run ontologies/harbor.json -s cell:2 --context biology
ideanet null ontologies/harbor.json -s harbor:2 --until 80 --samples 100
ideanet perturb ontologies/harbor.json -s harbor:2 --until 300
ideanet generate big.json --nodes 1500 --unfamiliar 30
ideanet run big.json -s i0:3 -s i1:3 --gain 2
pytest
```

## Large ontology: ConceptNet 5.7 (English)
```
curl -O https://s3.amazonaws.com/conceptnet/downloads/2019/edges/conceptnet-assertions-5.7.0.csv.gz
ideanet import-conceptnet conceptnet-assertions-5.7.0.csv.gz conceptnet-en.pkl   # ~3.5 min -> 1.12M ideas, 4.34M links
ideanet run conceptnet-en.pkl -t "bee" --gain 2 --top-k 10 --inhibition 0.1 --until 100 --plot bee.png
```
Relation types map to base weights (`ideanet/conceptnet.py`); Antonym/DistinctFrom/Not* are inhibitory.
`-t/--text` matches words and phrases (longest first, simple plural stripping) to idea labels.
At this scale the graph has no middle ground without regulation: gain 1 is silent, gain 1.5 ignites 50k+ ideas.
`--top-k` (a firing idea uses only its k strongest links) and `--inhibition` (a shared pool that raises
every threshold with recent global activity) keep the cascade bounded and self-sustaining.
`--fanout-alpha` damps hub links instead.

Ontology JSON: `{"defaults": {...}, "ideas": [{"id", "labels", ...}], "links": [{"source", "target", "weight", "delay", "context"}]}`.

## Experiments
`PYTHONPATH=. python experiments/brutality.py conceptnet-en.pkl out.json --samples 20`
tests whether the attractor reached from "bee" is reproducible, how large its basin is,
and whether it survives degree-preserving rewiring (global and within-relation-type).
Results from the first run: `experiments/brutality-results.json`.

### Attractor identity, basin map, paired stimuli
- `ideanet.attractor`: `signature()` is the firing distribution over idea ids in a late window.
  `weighted_jaccard()` / `jensen_shannon()` compare signatures. `AttractorMap` groups them
  into attractors, and `classify_pair()` labels a joint-stimulus outcome.
- `ideanet.analysis.shuffle_targets(mode="global"|"relation"|"reciprocal")` rewires a large graph in place.
  The `reciprocal` mode keeps reciprocal pairs and per-relation in/out degree.
- `experiments/brutality.py --modes reciprocal`: the reciprocity-controlled null.
- `experiments/basins.py`: a 10k random-start basin map plus pair interactions.
- `experiments/novel_controls.py`: checks whether a "novel" joint outcome still appears with a doubled single stimulus or a random partner.

### Corpus-learned weights (fixed topology)
- `ideanet.corpus`: `ConceptMatcher` matches text to idea ids. `count_cooccurrence` counts concepts within 10 matched concepts in the same sentence. `ppmi_weights` turns PPMI into weights by rank, keeping the original |weight| distribution and signs.
  - `evidence` mode reweights only links seen ≥3 times.
  - `replace` mode reranks every link.
- Learned weights live in `.weights.npz` files aligned to `graph.links`, with a fingerprint and provenance. `apply_weights` swaps them in temporarily; the graph file is never changed.
- `experiments/learn_weights.py GRAPH wikitext103 OUT FILES...` writes the counts, both weight modes and provenance.
- `experiments/corpus_compare.py` runs single deterministic runs per configuration. It records traces, fires, words and causal paths, plus shuffled-learned-weight controls.
- `experiments/corpus_robust.py` gives each configuration's attractor occupancy across 30 weight-jittered runs (×lognormal, σ=0.05).
- `experiments/make_shuffled_weights.py` builds controls: it permutes a learned file's values among the same evidence links, within sign.
- `experiments/corpus_ensemble.py` compares configurations as distributions, using paired perturbations: seed k multiplies each link by the same log-normal factor in every configuration.
  - It runs N perturbed runs per named stimulus, plus basin maps over the first S starts of the 10,000-start map.
  - Outputs: attractor-distribution overlap with bootstrap CIs, per-seed paired agreement, basin summaries, self-agreement across seeds, and how much of the top-k propagation goes through evidence links.
  - Raw rows go to `raw.jsonl` (resumable; not committed). Summaries go to `ensemble-results.json` and `ensemble-overview.png`.

Example (WikiText-103; the data files are not in the repo):
```
python experiments/learn_weights.py ~/data/conceptnet-en.pkl wikitext103 ~/data/learned/wikitext103 ~/data/wikitext/train-*.parquet
PYTHONPATH=. python experiments/corpus_ensemble.py ~/data/conceptnet-en.pkl experiments/results-ensemble \
    --n 200 --starts 1000 --basin-seeds 0,1,2 \
    --weights wiki_evidence=~/data/learned/wikitext103.evidence.weights.npz ... --corpus-of wiki_evidence=wiki ...
```

### Cross-corpus comparison (WikiText-103, Project Gutenberg, DailyDialog)
- Readers: `read_wikitext`, `read_gutenberg` (books split into 20-sentence chunks) and `read_dailydialog` (one utterance per paragraph). `learn_weights.py --sample-mod/--sample-rem` takes disjoint paragraph subsamples; `--max-tokens` caps the size.
- `experiments/train_matched.sh` trains two size-matched samples per corpus:
  - about 0.6M tokens each, because DailyDialog has only 1.4M tokens;
  - 48M tokens each for WikiText and Gutenberg, where each Gutenberg half comes from a different parquet shard (a different set of books).
- `experiments/run_corpora_ensemble.sh` runs the paired-perturbation ensemble over all of them plus a shuffled Gutenberg control.
- `experiments/summarize_corpora.py` compares within-corpus split agreement (the noise floor) with cross-corpus agreement. Output: `experiments/results-ensemble-corpora/summary.txt`.

### Between-book vs within-book Gutenberg splits; tie-breaking sensitivity
- `gut-within0/1` alternate 20-sentence chunks of the same books (both shards), so they share books; `gut-half0/1` use disjoint book sets. `experiments/run_gut_split.sh` runs both, the WikiText halves and shuffle controls at 5% and 1% weight noise. `experiments/summarize_gut_split.py` reports per-start agreement and attractor-occupancy (distribution) overlap, with and without extinction and with bootstrap CIs, plus same-config/different-seed baselines (`experiments/gut-split-summary.txt`).
- Weight noise mostly breaks ties: 65% of ConceptNet links have |w| = 0.35, and 84.5% of ideas with more than 10 links have a tie at the top-10 cut. Per-start self-agreement is about the same at 5%, 1% and 0.1% noise (`experiments/results-sigma0001`). Treat perturbation seeds as samples of tie order.
- `experiments/pairs_weights.py` reruns the 847 paired stimuli under each weight configuration and seed, with the A×2 / B×2 / A+R / B+R controls and a basin-map reachability check.
- `experiments/summarize_pairs.py` summarises a pairs run (`experiments/results-pairs-s01/summary.txt`): outcome rates, agreement within a configuration across seeds and between configurations at the same seed, and interactions that recur in the same region across seeds.

## Graph morphology (structural gaps)

`experiments/count_pairs.py` counts WikiText co-occurrence for all concept pairs (linked or not). `experiments/morphology.py` ranks unlinked pairs with near-identical neighbourhoods (`missing_link`), one-way nested neighbourhoods (`nested`), split neighbourhoods (`hole`) and mutually unlinked look-alike groups with no shared category (`unnamed_group`). Scoring uses a logistic model of P(linked | similarity, degrees) fitted on comparable pairs, and takes the minimum over the original and both WikiText-half weightings. Each candidate is also tested against degree-, relation- and reciprocity-preserving nulls and checked for WikiText co-occurrence. Lexical variants and alias-explained gaps are removed, and redundant (same-region) candidates are suppressed. `experiments/morphology_report.py` writes the selected anomalies to `experiments/results-morphology/top20.md`. No edges are added.
