#!/usr/bin/env bash
# Matched-size cross-corpus ensemble (evidence mode). Run after train_matched.sh.
set -euo pipefail
G=${G:-$HOME/data/conceptnet-en.pkl}; L=${L:-$HOME/data/learned}
PYTHONPATH=. python3 experiments/make_shuffled_weights.py "$G" $L/gut-half0.evidence.weights.npz $L/gut-half0.evidence --seeds 1
PYTHONPATH=. python3 experiments/corpus_ensemble.py "$G" experiments/results-ensemble-corpora \
  --n 200 --starts 1000 --basin-seeds 0,1,2 --workers 7 \
  --weights wiki_half0=$L/wikitext103-half0.evidence.weights.npz wiki_half1=$L/wikitext103-half1.evidence.weights.npz \
            gut_half0=$L/gut-half0.evidence.weights.npz gut_half1=$L/gut-half1.evidence.weights.npz \
            gut_half0_shuf=$L/gut-half0.evidence.shuf1.weights.npz \
            wiki_s0=$L/wiki-s0.evidence.weights.npz wiki_s1=$L/wiki-s1.evidence.weights.npz \
            gut_s0=$L/gut-s0.evidence.weights.npz gut_s1=$L/gut-s1.evidence.weights.npz \
            dd_s0=$L/dd-s0.evidence.weights.npz dd_s1=$L/dd-s1.evidence.weights.npz dd_full=$L/dd-full.evidence.weights.npz \
  --corpus-of gut_half0_shuf=gut_half0
