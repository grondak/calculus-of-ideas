"""Shuffled-learned-weight control files for corpus_ensemble.py.

Permutes a learned weight file's values among its corpus-evidence links (joint >= min_count),
within sign, so the same links are reweighted with the same multiset of values but without the
corpus's assignment of values to links.

  PYTHONPATH=. python experiments/make_shuffled_weights.py GRAPH.pkl IN.weights.npz OUT_PREFIX --seeds 1 2
"""
import argparse
import numpy as np
from ideanet import IdeaGraph
from ideanet.corpus import load_weights, save_weights

ap = argparse.ArgumentParser()
ap.add_argument("graph")
ap.add_argument("weights")
ap.add_argument("out_prefix")
ap.add_argument("--seeds", type=int, nargs="+", default=[1])
a = ap.parse_args()
g = IdeaGraph.load(a.graph)
d = load_weights(a.weights, g)
w, joint, prov = d["weights"], d["joint"], d["provenance"]
mask = joint >= prov["min_count"]
for seed in a.seeds:
    rng = np.random.default_rng(seed)
    out = w.copy()
    for sgn in (-1, 1):
        idx = np.flatnonzero(mask & (np.sign(w) == sgn))
        out[idx] = w[rng.permutation(idx)]
    p = {**prov, "control": "shuffle_within_evidence_by_sign", "shuffle_seed": seed, "source_weights": a.weights}
    save_weights(f"{a.out_prefix}.shuf{seed}.weights.npz", g, out, {"joint": joint}, p)
    print("wrote", f"{a.out_prefix}.shuf{seed}.weights.npz", int(mask.sum()), "links permuted")
