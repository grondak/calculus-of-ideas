"""Contributor concentration of the frame links of dense-group selection survivors.

For each survivor, the original frame links (provenance) are matched to ConceptNet contributors. top = share of
the group's frame links entered by its single most frequent contributor; base = mean top share of random link sets
of the same size and relation mix (200 draws); p = share of draws with top >= observed.
High concentration means the group is largely one person's answers. No edges are proposed and nothing is named.
"""
import argparse, gzip, json
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("provenance"); ap.add_argument("out"); ap.add_argument("runs", nargs="+", help="label=profile-null.json.gz")
    a = ap.parse_args()
    con, byrel = {}, defaultdict(list)
    for line in gzip.open(a.provenance, "rt"):
        r, s, e, _, c, _, _ = line.rstrip("\n").split("\t")
        cs = tuple(sorted(set(c.split("|")) - {""}))
        if cs:
            con[(s, r, e)] = cs; byrel[r].append(cs)
    rng = np.random.default_rng(3)

    def top(sets):
        cnt = Counter(x for cs in sets for x in cs)
        return max(cnt.values()) / len(sets) if cnt else 0.0

    L = ["| run | group | size | relations / anchors (frame) | frame links with contributor | contributors | top contributor share | random base | p |",
         "|---|---|---|---|---|---|---|---|---|"]
    summ = {}
    for spec in a.runs:
        lab, path = spec.split("=", 1)
        d = json.load(gzip.open(path, "rt"))
        tops = []
        for g, m in zip(d["groups"], d["merged_groups"]):
            if not g["survives_selection"]:
                continue
            sets = [con[(s, r, e)] for s, r, e, _ in m["provenance"] if (s, r, e) in con]
            if not sets:
                continue
            rels = Counter(r for s, r, e, _ in m["provenance"] if (s, r, e) in con)
            t = top(sets)
            draws = []
            for _ in range(200):
                smp = [byrel[r][k] for r, c in rels.items() for k in rng.integers(0, len(byrel[r]), c)]
                draws.append(top(smp))
            draws = np.array(draws)
            p = (1 + (draws >= t).sum()) / 201
            tops.append((t, float(draws.mean()), p))
            fr = "; ".join(f"{f[0]} {f[1]}" for f in m["frame"][:4])
            L.append(f"| {lab} | {g['id']} | {m['size']} | {fr} | {len(sets)} | {len(set(x for cs in sets for x in cs))} | "
                     f"{t:.2f} | {draws.mean():.2f} | {p:.3f} |")
        tt = np.array(tops)
        summ[lab] = dict(survivors=len(tops), median_top=float(np.median(tt[:, 0])), median_base=float(np.median(tt[:, 1])),
                         top_ge_half=int((tt[:, 0] >= 0.5).sum()), p_le_005=int((tt[:, 2] <= 0.05).sum()))
    Path(a.out).write_text("# Contributor concentration of dense-group survivors\n\n" + json.dumps(summ, indent=1) + "\n\n" + "\n".join(L) + "\n")
    print(json.dumps(summ, indent=1))


if __name__ == "__main__":
    main()
