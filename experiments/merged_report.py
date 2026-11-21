"""Markdown report: paraphrase-merged typed groups vs the unmerged profile-null run.

Inputs: merged profile-null output (profile_null.py --merge), the unmerged profile-null output and its typed-groups
file, and the class mapping. For every previously surviving group the members are mapped to their classes and
matched to the best merged group (member Jaccard); we report whether that merged group still survives.
"""
import argparse, gzip, json
from collections import Counter
import numpy as np

A18 = {"swimming", "surfing", "skating", "skiing", "dancing", "singing", "playing_cards"}


def fmt_frame(fr):
    out = []
    for rd, rep, exp in fr:
        extra = [x for x in exp if x != rep]
        out.append(f"{rd} {rep}" + (f" (= {', '.join(extra[:4])}{'…' if len(extra) > 4 else ''})" if extra else ""))
    return "; ".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("merged"); ap.add_argument("prior"); ap.add_argument("prior_groups"); ap.add_argument("arrays")
    ap.add_argument("classes"); ap.add_argument("out"); ap.add_argument("--title", default="")
    a = ap.parse_args()
    M = json.load(gzip.open(a.merged, "rt")); P = json.load(gzip.open(a.prior, "rt"))
    PG = json.load(gzip.open(a.prior_groups, "rt"))["groups"]
    z = np.load(a.arrays); ids = [str(x) for x in z["ids"]]; ix = {x: i for i, x in enumerate(ids)}
    cls = np.load(a.classes + ".npz")["cls"]; C = json.load(gzip.open(a.classes + ".json.gz", "rt"))
    mg, per, sm = M["merged_groups"], M["groups"], M["summary"]
    modes = [m for m in ("relation", "strict", "profile", "profile2") if m in sm["counts"]]
    L = [f"# Paraphrase-merged typed groups{a.title}\n"]
    nc = len(C["classes"]); merged_away = sum(len(c["members"]) - 1 for c in C["classes"])
    L.append(f"Classes with ≥ 2 ideas: {nc:,}; ideas merged into another: {merged_away:,}. "
             f"Settings: {C['settings']}.\n")
    L.append("Largest classes by typed degree (evidence = mutual NLI entailment or FormOf):\n")
    for c in C["classes"][:25]:
        L.append(f"- {c['rep']}: {', '.join(c['members'][:12])}{' …' if len(c['members']) > 12 else ''}")
    L.append("\n## Real vs re-mined null graphs (both contracted with the same classes)\n")
    keys = ["size_ge_4", "size_ge_6", "size_ge_10", "size_ge_20", "unnamed_ge_6"]
    L.append("| | " + " | ".join(keys) + " |"); L.append("|---" * (len(keys) + 1) + "|")
    L.append("| real | " + " | ".join(str(sm["counts"]["real"][k]) for k in keys) + " |")
    for m in modes:
        c = sm["counts"][m]
        L.append(f"| {m} | " + " | ".join(f"{c[k]['mean']} [{c[k]['max']}]" for k in keys) + " |")
    L.append(f"\nSurvive both profile nulls (frame support at floor, reproduced ≤ 5%): {sm['survives_profile']}; "
             f"+ selection control: {sm['survives_selection']}. By tier: {sm['survives_by_tier']}\n")

    # prior survivors -> merged
    own = {}
    for gi, g in enumerate(mg):
        for x in g["members"]:
            own.setdefault(x, []).append(gi)
    rows = []
    for d in P["groups"]:
        if not d["survives_profile"]:
            continue
        g = PG[d["id"]]
        mm = {ids[cls[ix[x]]] for x in g["members"]}
        cand = {h for x in mm for h in own.get(x, ())}
        best, bj = None, 0
        for h in cand:
            s = set(mg[h]["members"]); j = len(mm & s) / len(mm | s)
            if j > bj:
                best, bj = h, j
        st = "gone" if best is None or bj < 0.3 else ("survives_selection" if per[best]["survives_selection"]
                                                       else "survives_profile" if per[best]["survives_profile"] else "found_not_significant")
        rows.append(dict(prior=d["id"], sel=d["survives_selection"], status=st, best=best, j=bj, collapsed=len(g["members"]) - len(mm)))
    L.append("## What happened to previously surviving groups\n")
    L.append("| prior status | n | still survive selection | survive profile only | found, not significant | gone (no merged group with member Jaccard ≥ 0.3) |")
    L.append("|---|---|---|---|---|---|")
    for lab, f in (("survived selection", True), ("survived profile only", False)):
        rs = [r for r in rows if r["sel"] == f]
        c = Counter(r["status"] for r in rs)
        L.append(f"| {lab} | {len(rs)} | {c['survives_selection']} | {c['survives_profile']} | {c['found_not_significant']} | {c['gone']} |")
    L.append("")
    L.append("Previous selection survivors, one line each (prior members → status):\n")
    for r in rows:
        if r["sel"]:
            g = PG[r["prior"]]
            L.append(f"- {', '.join(g['members'][:6])} … [{'; '.join(f[0] + ' ' + f[1] for f in g['frame'][:3])}] → **{r['status']}**"
                     f" (members merged away {r['collapsed']}; match J={r['j']:.2f})")

    def line(gi):
        g, d = mg[gi], per[gi]
        pm = "; ".join(f"{m} p={d[m]['p']} sel={d[m]['p_selection']} rep={d[m]['reproduced']}" for m in modes if m.startswith("profile"))
        mem = [m_ + (f"(+{len(e) - 1})" if len(e) > 1 else "") for m_, e in zip(g["members"], g["expanded"])]
        return (f"- **m{gi}** n={g['size']}, {g['tier']}, relation types {g['rel_types']}, anchor classes {g['anchors']}, "
                f"independent neighbourhoods {g['independent']}: {', '.join(mem[:16])}{' …' if len(mem) > 16 else ''}\n"
                f"  - frame: {fmt_frame(g['frame'])}\n  - {pm}")
    surv = [i for i, d in enumerate(per) if d["survives_selection"]]
    L.append(f"\n## Merged groups surviving the selection control ({len(surv)})\n")
    L.append(f"By relation types in frame: {dict(Counter(mg[i]['rel_types'] for i in surv))}; "
             f"by independent anchor neighbourhoods: {dict(Counter(mg[i]['independent'] for i in surv))}\n")
    multi = [i for i in surv if mg[i]["rel_types"] >= 2 and mg[i]["independent"] >= 2]
    L.append(f"### ≥ 2 relation types and ≥ 2 independent neighbourhoods ({len(multi)})\n")
    for i in sorted(multi, key=lambda i: -mg[i]["size"]):
        L.append(line(i))
    one = [i for i in surv if i not in multi]
    L.append(f"\n### Other selection survivors ({len(one)})\n")
    for i in sorted(one, key=lambda i: (-mg[i]["independent"], -mg[i]["rel_types"], -mg[i]["size"])):
        L.append(line(i))
    pr = [i for i, d in enumerate(per) if d["survives_profile"] and not d["survives_selection"] and mg[i]["rel_types"] >= 2 and mg[i]["independent"] >= 2]
    L.append(f"\n### Pass profile nulls but not the selection control, ≥ 2 relation types and ≥ 2 independent neighbourhoods ({len(pr)}; largest 25)\n")
    for i in sorted(pr, key=lambda i: -mg[i]["size"])[:25]:
        L.append(line(i))
    a18 = [i for i, g in enumerate(mg) if len(A18 & {x for e in g["expanded"] for x in e}) >= 2]
    L.append(f"\n## Anomaly 18 ({len(a18)} merged groups with ≥ 2 of its activities; "
             f"{sum(per[i]['survives_selection'] for i in a18)} survive selection, {sum(per[i]['survives_profile'] for i in a18)} survive profile)\n")
    for i in sorted(a18, key=lambda i: -mg[i]["size"])[:8]:
        L.append(line(i))
    open(a.out, "w").write("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
