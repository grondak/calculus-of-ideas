"""Summarise results-ensemble-corpora: within-corpus split floors vs cross-corpus agreement."""
import itertools
import json
import sys

import numpy as np

sys.path.insert(0, ".")
from ideanet.attractor import weighted_jaccard  # noqa: E402

D = sys.argv[1] if len(sys.argv) > 1 else "experiments/results-ensemble-corpora"
r = json.load(open(f"{D}/ensemble-results.json"))
rows = [json.loads(line) for line in open(f"{D}/raw.jsonl") if '"basin"' in line[:20]]
S = {(x["config"], x["k"], x["start"]): x["sig"] for x in rows}
starts = sorted({x["start"] for x in rows})
C = r["configs"]


def live(a, b, ka, kb):
    v = [weighted_jaccard(S[(a, ka, s)], S[(b, kb, s)]) >= 0.5 for s in starts if S.get((a, ka, s)) and S.get((b, kb, s))]
    return float(np.mean(v))


def basin(a, b):
    return np.mean([live(a, b, k, k) for k in (0, 1, 2)])


groups = {
    "split: wiki 48M": [("wiki_half0", "wiki_half1")],
    "split: gut 48M": [("gut_half0", "gut_half1")],
    "cross: wiki~gut 48M": list(itertools.product(["wiki_half0", "wiki_half1"], ["gut_half0", "gut_half1"])),
    "shuffle: gut_half0~shuf": [("gut_half0", "gut_half0_shuf")],
    "shuffle: shuf~gut_half1": [("gut_half0_shuf", "gut_half1")],
    "split: wiki 0.6M": [("wiki_s0", "wiki_s1")],
    "split: gut 0.6M": [("gut_s0", "gut_s1")],
    "split: dd 0.7M": [("dd_s0", "dd_s1")],
    "cross: wiki~gut 0.6M": list(itertools.product(["wiki_s0", "wiki_s1"], ["gut_s0", "gut_s1"])),
    "cross: wiki~dd 0.6M": list(itertools.product(["wiki_s0", "wiki_s1"], ["dd_s0", "dd_s1"])),
    "cross: gut~dd 0.6M": list(itertools.product(["gut_s0", "gut_s1"], ["dd_s0", "dd_s1"])),
    "orig~wiki 48M": [("original", "wiki_half0"), ("original", "wiki_half1")],
    "orig~gut 48M": [("original", "gut_half0"), ("original", "gut_half1")],
    "orig~small (all)": [("original", c) for c in ("wiki_s0", "wiki_s1", "gut_s0", "gut_s1", "dd_s0", "dd_s1")],
}
stims = list(r["stim"])
print(f"{'group':28s} basin  " + " ".join(f"{s[:8]:>8s}" for s in stims))
for name, pairs in groups.items():
    b = np.mean([basin(a, c) for a, c in pairs])
    ov = [np.mean([r["stim"][s]["distribution_overlap"][a][c] for a, c in pairs]) for s in stims]
    print(f"{name:28s} {b:.3f}  " + " ".join(f"{x:8.2f}" for x in ov))
print("self-agreement across seeds (live):")
for c in C:
    print(f"  {c:16s} {np.mean([live(c, c, a, b) for a, b in ((0, 1), (0, 2), (1, 2))]):.3f}"
          f"  basin attractors {r['basin']['0']['summary'][c]['attractors']}  ev_share {r['basin']['0']['summary'][c]['ev_share_mean']:.3f}")
for s in stims:
    st = r["stim"][s]["stats"]
    print(s, {c: st[c]["unperturbed_top"][:2] for c in C})
print(json.dumps({k: v["evidence_links"] for k, v in r["topk_diagnostic"].items()}))
