"""Are 'novel' joint outcomes interactions, or just A (or B) under any extra perturbation?

For every pair classified 'novel' by basins.py, rerun the joint stimulus and compare
its signature with four controls:
  A x2   : A alone at double strength       B x2 : B alone at double strength
  A + R  : A plus a random unrelated idea   B + R: B plus a random unrelated idea
If any control lands in the same region (weighted Jaccard >= 0.5), the novel region is
reachable without the specific partner and is not evidence of an A-B interaction.

usage: PYTHONPATH=. python experiments/novel_controls.py conceptnet-en.pkl basins.json.gz out.json
"""
import gzip
import json
import random
import sys
from collections import Counter

from ideanet import IdeaGraph, TextStimulus, signature, weighted_jaccard
from basins import LATE, NAMED, STRENGTH, UNTIL, run

g = IdeaGraph.load(sys.argv[1])
ts = TextStimulus(g)
data = json.load(gzip.open(sys.argv[2], "rt"))
rng = random.Random(7)
live = [r["start"] for r in data["starts"] if r["attractor"] != 0]
stim = lambda x, s=STRENGTH: ts.stimuli(x, s) if x in NAMED else [(x, s)]
sig = lambda st: signature(run(g, st).fires, LATE, UNTIL)

out = []
for p in data["pairs"]:
    if p["kind"] != "novel":
        continue
    a, b = p["a"], p["b"]
    joint = sig(stim(a) + stim(b))
    ctrl = {}
    for name, st in [("A x2", stim(a, 2 * STRENGTH)), ("B x2", stim(b, 2 * STRENGTH)),
                     ("A + R", stim(a) + [(rng.choice(live), STRENGTH)]),
                     ("B + R", stim(b) + [(rng.choice(live), STRENGTH)])]:
        ctrl[name] = round(weighted_jaccard(joint, sig(st)), 3)
    explained = [k for k, v in ctrl.items() if v >= 0.5]
    out.append({**{k: p[k] for k in ("group", "a", "b", "a_top", "b_top", "joint_top", "joint_attractor")},
                "controls": ctrl, "explained_by": explained, "interaction": not explained})

n = len(out)
inter = [o for o in out if o["interaction"]]
print(f"novel pairs: {n}; survive all controls: {len(inter)}")
print("explained by:", Counter(k for o in out for k in o["explained_by"]))
print("participants in surviving pairs:", Counter(x for o in inter for x in (o["a"], o["b"])).most_common(8))
for o in inter:
    print(f"  {o['a']}({o['a_top'][:2]}) + {o['b']}({o['b_top'][:2]}) -> {o['joint_top'][:5]} attr={o['joint_attractor']} ctrl={o['controls']}")
json.dump(out, open(sys.argv[3], "w"), indent=1)
