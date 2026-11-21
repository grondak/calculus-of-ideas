#!/bin/bash
# Paraphrase-merged pipeline (see experiments/results-merged/SUMMARY.md). Run from the repo root.
set -e
export PYTHONPATH=.
D=/home/ubuntu/data; G=$D/morph/graph-arrays.npz; K="--keep $D/morph/keep-no-wiktionary.npz"; S="--sources $D/morph/link-datasets.npz"
[ -f $D/merge/emb-mpnet.npz ] || python experiments/embed_ideas.py $G $D/merge/emb-mpnet.npz $K
[ -f $D/merge/nli-pairs.npz ] || python experiments/paraphrase_pairs.py $G $D/merge/emb-mpnet.npz $D/merge/nli-pairs.npz $K
[ -f $D/merge/nli-base.npz ] || python experiments/paraphrase_rescore.py $G $D/merge/nli-pairs.npz $D/merge/nli-base.npz
python experiments/anchor_classes.py $G $D/merge/emb-mpnet.npz $D/merge/nli-pairs.npz $D/merge/classes $K --entail 0.6 \
  --judge $D/merge/nli-base.npz
python experiments/profile_null.py $G experiments/results-typed-groups/typed-groups.json.gz experiments/results-merged \
  $K $S --merge $D/merge/classes.npz --emb $D/merge/emb-mpnet.npz --nulls 100
python experiments/boundaries.py $G experiments/results-typed-groups/typed-groups.json.gz experiments/results-boundaries-merged \
  $K $S --merge $D/merge/classes.npz --nulls 100
python experiments/profile_null.py $G experiments/results-typed-groups-cap150/typed-groups.json.gz experiments/results-merged-cap150 \
  $K $S --merge $D/merge/classes.npz --emb $D/merge/emb-mpnet.npz --nulls 100
python experiments/fixed_regions.py $G experiments/results-typed-groups/typed-groups.json.gz \
  experiments/results-boundaries-merged/fixed-regions.json.gz $K $S --merge $D/merge/classes.npz --nulls 1000
python experiments/boundary_report.py experiments/results-boundaries-merged/report.md \
  unmerged=experiments/results-boundaries/boundaries.json.gz merged=experiments/results-boundaries-merged/boundaries.json.gz
python experiments/merged_report.py experiments/results-merged/profile-null.json.gz experiments/results-profile-null/profile-null.json.gz \
  experiments/results-typed-groups/typed-groups.json.gz $G $D/merge/classes experiments/results-merged/report.md --title " (cap 30)"
python experiments/merged_report.py experiments/results-merged-cap150/profile-null.json.gz \
  experiments/results-profile-null-cap150/profile-null.json.gz experiments/results-typed-groups-cap150/typed-groups.json.gz \
  $G $D/merge/classes experiments/results-merged-cap150/report.md --title " (cap 150)"
