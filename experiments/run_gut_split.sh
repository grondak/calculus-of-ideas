#!/usr/bin/env bash
# Between-book vs within-book Gutenberg splits, WikiText halves and shuffle controls at 5% and 1% weight noise.
set -euo pipefail
G=${G:-$HOME/data/conceptnet-en.pkl}; L=${L:-$HOME/data/learned}
[ -f $L/wikitext103-half0.evidence.shuf1.weights.npz ] || \
  PYTHONPATH=. python3 experiments/make_shuffled_weights.py "$G" $L/wikitext103-half0.evidence.weights.npz $L/wikitext103-half0.evidence --seeds 1
for S in 05 01; do
  PYTHONPATH=. python3 experiments/corpus_ensemble.py "$G" experiments/results-gut-split-s$S --sigma 0.$S \
    --n 200 --starts 1000 --basin-seeds 0,1,2 --workers 8 \
    --weights wiki_half0=$L/wikitext103-half0.evidence.weights.npz wiki_half1=$L/wikitext103-half1.evidence.weights.npz \
              wiki_half0_shuf=$L/wikitext103-half0.evidence.shuf1.weights.npz \
              gut_half0=$L/gut-half0.evidence.weights.npz gut_half1=$L/gut-half1.evidence.weights.npz \
              gut_half0_shuf=$L/gut-half0.evidence.shuf1.weights.npz \
              gut_within0=$L/gut-within0.evidence.weights.npz gut_within1=$L/gut-within1.evidence.weights.npz \
    --corpus-of wiki_half0_shuf=wiki_half0 gut_half0_shuf=gut_half0
done
