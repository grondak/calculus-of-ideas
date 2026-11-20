"""Summarise results-pairs-*: outcome rates, seed/config agreement and interactions recurring across seeds."""
import itertools
import json
import sys
from collections import Counter

import numpy as np

sys.path.insert(0, ".")
from ideanet.attractor import weighted_jaccard  # noqa: E402

D = sys.argv[1] if len(sys.argv) > 1 else "experiments/results-pairs-s01"
r = json.load(open(f"{D}/pairs-results.json"))
C, S = r["configs"], [str(k) for k in r["seeds"]]
print("outcome rates (all pairs, pooled over seeds); interactions and those unreached by the basin map, per seed:")
for c in C:
    tot = Counter()
    for k in S:
        tot.update(r["per_config"][c][k]["all"]["kinds"])
    n = sum(tot.values())
    print(f"  {c:16s}", {k: round(v / n, 3) for k, v in tot.most_common()},
          "inter", [r["per_config"][c][k]["all"]["interaction"] for k in S],
          "unreached", [r["per_config"][c][k]["all"]["interaction_unreached_by_basin_map"] for k in S])
print("same config, different seeds:", {c: {k: round(v, 3) for k, v in d.items()} for c, d in r["self"].items()})
print("different configs, same seed:")
for k, v in r["cross"].items():
    print("  ", k, {a: (round(b, 3) if b is not None else None) for a, b in v.items()})
rows = [json.loads(line) for line in open(f"{D}/raw.jsonl")]
R = {(x["config"], x["k"], x["pair"]): x for x in rows}
P = sorted({x["pair"] for x in rows})
top = lambda s: [t for t, _ in sorted(s.items(), key=lambda kv: -kv[1])[:4]]
for c in C:
    sets = [{i for i in P if R[(c, int(k), i)]["interaction"]} for k in S]
    js = [len(a & b) / len(a | b) for a, b in itertools.combinations(sets, 2)]
    p = [len(s) / len(P) for s in sets]
    exp = [pa * pb / (pa + pb - pa * pb) for pa, pb in itertools.combinations(p, 2)]
    rec = []
    for i in P:
        inter = [x for x in (R[(c, int(k), i)] for k in S) if x["interaction"]]
        if any(weighted_jaccard(a["sig_ab"], b["sig_ab"]) >= 0.5 for a, b in itertools.combinations(inter, 2)):
            rec.append((inter[0]["a"], inter[0]["b"], top(inter[0]["sig_ab"])))
    print(f"{c:16s} interaction-set Jaccard across seeds {np.round(js, 3)} (independence {np.round(exp, 3)}); "
          f"same-region interaction at >=2 seeds: {len(rec)}")
    for x in rec:
        print("     ", x)
