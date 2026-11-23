"""Frozen Stage 2 sampler: stratified (4 log-degree strata) random single-word concepts with intact degree 10-500,
excluding Stage 1, dev and tuning concepts and every idea in their name families. Writes an oversampled ordered list;
ablate.py --limit keeps the first N that pass its checks (>= 5 surviving neighbours, family size <= 200)."""
import json, sys
import numpy as np
from experiments.ablation.common import load, undirected
from experiments.ablation.families import variants

g = load(sys.argv[1]); out = sys.argv[2]; N = int(sys.argv[3]) if len(sys.argv) > 3 else 300
deg = np.asarray(undirected(g.n, g.src, g.dst).sum(1)).ravel()
used = {l.split()[1] for f in ("stage1.txt", "dev.txt") for l in open(f"experiments/ablation/{f}") if l.strip() and not l.startswith("#")}
used |= set(json.load(open("experiments/ablation/tuning_nodes.json")))
ban = set()
for u in used:
    ban |= variants(u)
ok = np.array([deg[i] >= 10 and deg[i] <= 500 and g.ids[i].isalpha() and g.ids[i] not in ban
               and not any(b in g.ids[i] for b in used if len(b) >= 4) for i in range(g.n)])
cand = np.flatnonzero(ok)
edges = np.quantile(np.log(deg[cand]), [0.25, 0.5, 0.75])
strata = np.digitize(np.log(deg[cand]), edges)
rng = np.random.default_rng(20261122)
picks = [rng.permutation(cand[strata == s])[: N // 4] for s in range(4)]
order = [x for tup in zip(*picks) for x in tup]
with open(out, "w") as fh:
    fh.write("# Stage 2 held-out sample (stage2_sample.py, seed 20261122); stratum = log-degree quartile\n")
    for i in order:
        fh.write(f"q{int(np.digitize(np.log(deg[i]), edges))} {g.ids[i]}\n")
print(len(cand), "eligible;", len(order), "written; quartile edges", np.exp(edges).round(1))
