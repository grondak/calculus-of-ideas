"""Markdown report for typed_groups.py: shape clusters and diversified examples per naming tier."""
import argparse, gzip, json

ap = argparse.ArgumentParser()
ap.add_argument("results"); ap.add_argument("out")
ap.add_argument("--per-tier", type=int, default=6)
ap.add_argument("--find", nargs="*", default=["swimming", "writing", "chair"])
a = ap.parse_args()
r = json.load(gzip.open(a.results, "rt"))
S, G = r["summary"], r["groups"]
modes = list(G[0]["null"])
zmin = lambda g: min(v["z"] for v in g["null"].values())
rank = lambda g: g["size"] * zmin(g)
L = ["# Typed-relation groups (Wiktionary-only links removed)\n"]
L.append(f"Variant: {S['variant']['links']:,} of {S['variant']['all_links']:,} links; datasets {S['variant']['datasets_in_variant']}. "
         f"Typed features {S['features']['columns']:,} columns / {S['features']['incidences']:,} incidences.")
L.append(f"Groups mined {S['groups']:,}; significant under all nulls ({', '.join(modes)}) {S['significant_all']:,}; "
         f"robust (all nulls + recovered in ≥60% of 80% edge subsamples + still present with Wiktionary restored) {S['robust']:,}.")
L.append(f"Robust tiers: {S['tiers_robust']}. Subsample re-mining group counts: {S['subsample_group_counts']}.")
L.append("Selection control (re-mining null graphs): " + json.dumps(S["selection_control"]) + "\n")
L.append("## Shapes (clusters of relation profiles)\n")
L.append("| shape | relation profile (share of member–frame incidences) | groups | robust | robust tiers |")
L.append("|---|---|---|---|---|")
for s in r["shapes"][:15]:
    L.append(f"| {s['shape']} | {', '.join(f'{k} {v}' for k, v in s['relation_profile'])} | {s['groups']} | {s['robust_groups']} | {s['robust_tiers']} |")


def show(g):
    c = g["category"]
    out = [f"### group {g['id']} — {g['size']} members, shape {g.get('shape')}, tier {g['tier']}",
           "members: " + ", ".join(g["members"][:24]) + (" …" if g["size"] > 24 else ""),
           "frame: " + "; ".join(f"{rl} {nd}" for rl, nd in g["frame"][:12]),
           f"density {g['density']}; support {g['support']} (with Wiktionary {g['support_full_graph']}); "
           + "nulls " + ", ".join(f"{m} p={v['p']} z={v['z']} (null mean {v['mean']})" for m, v in g["null"].items())
           + f"; BH q {g['q_bh']}; subsample recovery {g['subsample_recovery']}",
           f"category: best direct {c['best_direct']} ({c['direct_coverage']}), best within 2 IsA-steps {c['best_within_2']} "
           f"({c['within_2_coverage']}), members with any category {c['members_with_any_category']}",
           "member categories: " + "; ".join(f"{k}→{','.join(v) or '–'}" for k, v in list(c["member_categories"].items())[:10]),
           f"internal links among members {g['internal_links']} (configuration expectation {g['internal_expected']}); "
           f"relative weight of member–frame links {g['relative_weight']}",
           "WikiText (obs/exp): " + "; ".join(f"{nm} member–frame {v['member_frame'][0]}/{v['member_frame'][1]}, member–member "
                                             f"{v['member_member'][0]}/{v['member_member'][1]}" for nm, v in g["corpus"].items()), ""]
    return out


TIERS = [("Easy to name: an existing category covers ≥50% of members", ["named"]),
         ("Hard to name: partial category (33–50%, or ≥50% only at 2 IsA-steps), or members mostly uncategorised",
          ["partly_named", "uncategorised"]),
         ("Coherent but resisting: members are categorised, but no category within 2 steps covers ≥33%", ["crosscutting"])]
for title, tiers in TIERS:
    L.append(f"\n## {title}\n")
    chosen, seen_m, seen_f = [], [], []
    for g in sorted((g for g in G if g["robust"] and g["tier"] in tiers), key=lambda g: -rank(g)):
        m, f = set(g["members"]), set(g["frame_nodes"])
        if any(len(m & x) / len(m | x) >= 0.15 for x in seen_m) or any(len(f & y) / len(f | y) >= 0.5 for y in seen_f):
            continue
        chosen.append(g); seen_m.append(m); seen_f.append(f)
        if len(chosen) >= a.per_tier * len(tiers):
            break
    for g in chosen:
        L += show(g)
L.append("\n## Earlier groups 18–20, located\n")
for w in a.find:
    hits = sorted((g for g in G if w in g["members"]), key=lambda g: -rank(g))[:2]
    for g in hits:
        L += show(g)
open(a.out, "w").write("\n".join(L))
print(a.out)
