#!/usr/bin/env bash
# Matched-size corpus samples for WikiText-103, Project Gutenberg and DailyDialog (see README).
set -euo pipefail
G=${G:-$HOME/data/conceptnet-en.pkl}; L=${L:-$HOME/data/learned}; D=${D:-$HOME/data}
DD="$D/dailydialog/train.parquet $D/dailydialog/validation.parquet $D/dailydialog/test.parquet"
WT="$D/wikitext/train-00000-of-00002.parquet $D/wikitext/train-00001-of-00002.parquet"
SMALL=580000      # ~half of DailyDialog (1,172,606 tokens)
LARGE=48409656    # WikiText-103 half0 token count
run() { PYTHONPATH=. python3 experiments/learn_weights.py "$G" "$@"; }
run dailydialog $L/dd-s0 $DD --sample-mod 2 --sample-rem 0
run dailydialog $L/dd-s1 $DD --sample-mod 2 --sample-rem 1
run dailydialog $L/dd-full $DD
run wikitext103 $L/wiki-s0 $WT --sample-mod 64 --sample-rem 0 --max-tokens $SMALL
run wikitext103 $L/wiki-s1 $WT --sample-mod 64 --sample-rem 1 --max-tokens $SMALL
run gutenberg $L/gut-s0 $D/gutenberg/g0.parquet --sample-mod 64 --sample-rem 0 --max-tokens $SMALL
run gutenberg $L/gut-s1 $D/gutenberg/g0.parquet --sample-mod 64 --sample-rem 1 --max-tokens $SMALL
run gutenberg $L/gut-half0 $D/gutenberg/g0.parquet --max-tokens $LARGE
run gutenberg $L/gut-half1 $D/gutenberg/g1.parquet --max-tokens $LARGE
# Within-book Gutenberg split: alternate 20-sentence chunks of the same books (both shards), same size cap.
run gutenberg $L/gut-within0 $D/gutenberg/g0.parquet $D/gutenberg/g1.parquet --sample-mod 2 --sample-rem 0 --max-tokens $LARGE
run gutenberg $L/gut-within1 $D/gutenberg/g0.parquet $D/gutenberg/g1.parquet --sample-mod 2 --sample-rem 1 --max-tokens $LARGE
