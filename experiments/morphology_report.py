"""Select the top structural anomalies from morphology-results.json.gz and write a Markdown report."""
import argparse, gzip, json

ap = argparse.ArgumentParser()
ap.add_argument("results"); ap.add_argument("out")
ap.add_argument("--quota", default="missing_link=7,nested=4,hole=5,unnamed_group=4")
ap.add_argument("--pick", default="", help="explicit picks, e.g. missing_link=0,3;hole=1 (indices into ranked lists)")
a = ap.parse_args()
r = json.load(gzip.open(a.results, "rt"))
quota = {k: int(v) for k, v in (x.split("=") for x in a.quota.split(","))}
fmt_rel = lambda rs: ",".join(rs)
L = []
g = r["graph"]
L.append("# Structural anomalies in ConceptNet (original weights + WikiText halves)\n")
L.append(f"Visible ideas {g['visible']:,}; core {g['core']:,}; candidate pairs {g['candidates']:,}; "
         f"gap pairs {g['gap_pairs']:,} (lexical variants {g['lexical']:,} and alias-explained {g['explained']:,} removed); "
         f"null-significant gap pairs {g['gap_pairs_null_significant']:,}; fragmented neighbourhoods {g['holes']:,}; "
         f"groups {g['groups']} ({g['groups_unnamed']} unnamed).\n")
gl = r["global"]
L.append("Global similarity structure (3,000 sampled core ideas): real " + json.dumps(gl["real"]))
for m in ("global", "relation", "reciprocal"):
    vals = gl[m]
    keys = vals[0].keys()
    L.append(f"- {m} null mean: " + ", ".join(f"{k} {sum(v[k] for v in vals)/len(vals):.1f}" for k in keys))
L.append("")
n = 0
picks = {f: [int(i) for i in v.split(",")] for f, v in (x.split("=") for x in a.pick.split(";"))} if a.pick else None
for fam, q in (picks or quota).items():
    for x in ([r[fam][i] for i in q] if picks else r[fam][:q]):
        n += 1
        if fam in ("missing_link", "nested"):
            cor = "; ".join(f"{k} {v['observed']} obs / {v['expected']} exp" for k, v in x["corpus"].items())
            nul = "; ".join(f"{k} p={v['p']} z={v['z']}" for k, v in x["null"].items())
            L.append(f"## {n}. {fam}: {x['a']} — {x['b']}")
            L.append(f"degrees {x['deg']}, common neighbours {x['common_neighbours']}, Jaccard {x['jaccard']}, "
                     f"typed Jaccard {x['typed_jaccard']}, containment {x['containment']}; "
                     f"P(linked | comparable) {x['p_linked_comparable']}; gap score {x['gap_score']}"
                     + (f"; nested score {x['nested_score']}" if 'nested_score' in x else ""))
            L.append(f"nulls: {nul}")
            L.append(f"WikiText: {cor} → {x['corpus_class']}")
            L.append("shared relation profile: " + ", ".join(f"{k} {v}" for k, v in x["shared_relation_profile"]))
            L.append("shared neighbours (relation from a | from b): " + "; ".join(
                f"{s[0]} ({fmt_rel(s[1])} | {fmt_rel(s[2])})" for s in x["shared"][:12]))
            L.append(f"only {x['a']}: " + "; ".join(f"{s[0]} ({fmt_rel(s[1])})" for s in x["only_a"][:8]))
            L.append(f"only {x['b']}: " + "; ".join(f"{s[0]} ({fmt_rel(s[1])})" for s in x["only_b"][:8]))
        elif fam == "hole":
            cor = "; ".join(f"{k} {v['observed']} obs / {v['expected']} exp" for k, v in x["corpus"].items())
            L.append(f"## {n}. hole around {x['centre']}")
            L.append(f"degree {x['deg']}, neighbourhood component sizes {x['neighbourhood_sizes']}, fragmentation {x['fragmentation']}, "
                     f"score {x['score']} by weights {x['score_by_weights']}; cross pairs {x['cross_pairs']}, "
                     f"null-significant {x['cross_pairs_null_significant']}")
            L.append(f"WikiText cross-cluster co-occurrence: {cor} → {x['corpus_class']}")
            L.append("cluster X: " + "; ".join(f"{s[0]} ({fmt_rel(s[1])})" for s in x["cluster_x"]))
            L.append("cluster Y: " + "; ".join(f"{s[0]} ({fmt_rel(s[1])})" for s in x["cluster_y"]))
            L.append("ideas outside the neighbourhood touching both: " + ", ".join(x["bridges_outside"]))
            L.append("strongest missing cross pairs (common nbrs, J, excess surprisal): " + "; ".join(
                f"{p[0]}–{p[1]} ({p[2]}, {p[3]}, {p[4]})" for p in x["strongest_missing"][:6]))
        else:
            L.append(f"## {n}. unnamed group ({x['size']} ideas)")
            L.append(f"gap density {x['gap_density']}, internal link density {x['internal_link_density']}, score {x['score']}, named by {x['named_by'] or 'none'}")
            L.append("members: " + ", ".join(x["members"]))
            L.append("frame (neighbour, members touching it, relations): " + "; ".join(
                f"{f[0]} {f[1]} [{', '.join(f'{k}×{v}' for k, v in f[2])}]" for f in x["frame"][:10]))
        L.append("")
open(a.out, "w").write("\n".join(L))
print(a.out, n)
