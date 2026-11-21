"""Markdown report for boundaries.py output (one or more runs, e.g. unmerged and paraphrase-merged)."""
import argparse, gzip, json
from collections import Counter
import numpy as np

LOC = {"AtLocation", "LocatedNear", "PartOf", "HasA"}


def rtypes(frame):
    return {f[0][:-1] for f in frame}


def bh(p):
    p = np.asarray(p, float); o = np.argsort(p)
    q = np.minimum.accumulate((p[o] * len(p) / np.arange(1, len(p) + 1))[::-1])[::-1]
    out = np.empty_like(q); out[o] = np.minimum(q, 1); return out


def fr(frame):
    return "; ".join(f"{f[0]} {f[1]}" + (f" (= {', '.join(x for x in f[2] if x != f[1])})" if len(f) > 2 and len(f[2]) > 1 else "")
                     for f in frame[:5]) + (" …" if len(frame) > 5 else "")


def mem(g):
    return ", ".join(m + (f" (= {', '.join(x for x in g.get('expanded', {}).get(m, []) if x != m)})" if m in g.get("expanded", {}) else "")
                     for m in g["members"][:10]) + (" …" if g["size"] > 10 else "")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out"); ap.add_argument("runs", nargs="+", help="label=path/boundaries.json.gz")
    ap.add_argument("--top", type=int, default=15)
    a = ap.parse_args()
    L = ["# Sparse boundaries between structured neighbourhoods\n",
         "A candidate pair is two typed groups with disjoint cores whose member neighbourhoods (outside both cores) are in "
         "the top 1% of context similarity among all core-disjoint group pairs of the same graph. It is a *boundary* when "
         "the two cores (members + frame anchors) have no conceptual link at all while comparable candidate pairs (same "
         "similarity, size, degree and dominant-relation bins) have a median of at least 2 links. Every null graph is generated at the original-id "
         "level, contracted with the same class map, re-mined, and scored the same way. No edges are proposed.\n"]
    for lab_path in a.runs:
        lab, path = lab_path.split("=", 1)
        d = json.load(gzip.open(path, "rt")); c = d["summary"]["counts"]; B = d["boundaries"]
        modes = [m for m in ("relation", "strict", "profile", "profile2") if m in c]
        pm = [m for m in modes if m.startswith("profile")]
        L.append(f"## {lab}\n")
        L.append("| graph | groups | candidate pairs | boundaries | boundary rate | p (rate real ≥ null) | candidate pairs linked | p (real unlinked share ≥ null) |")
        L.append("|---|---|---|---|---|---|---|---|")
        r = c["real"]
        L.append(f"| real | {r['groups']} | {r['pairs']} | {r['boundaries']} | {r['rate']:.3f} | | {r['cand_linked']:.2f} | |")
        for m in modes:
            x = c[m]
            L.append(f"| {m} null (mean) | {x['groups']:.0f} | {x['pairs']:.0f} | {x['boundaries_mean']} [max {x['boundaries_max']}] | "
                     f"{x['rate_mean']:.3f} [{x['rate_min']:.3f}–{x['rate_max']:.3f}] | {x['p_rate_real_ge_null']} | {x['cand_linked']:.2f} | {x.get('p_unlinked_real_ge_null', '')} |")
        if d.get("regions"):
            L.append("\nSparse regions: candidate pairs grouped by the two groups' dominant frame relations. Linked share in the real "
                     "graph vs re-mined nulls (strata with ≥ 20 real pairs; null graphs where the stratum has ≥ 5 pairs).\n")
            L.append("| dominant relations | real pairs | real linked | " + " | ".join(f"{m} linked [p real ≤ null, graphs]" for m in modes) + " |")
            L.append("|---" * (3 + len(modes)) + "|")
            for g in d["regions"]:
                L.append(f"| {g['relations']} | {g['pairs']} | {g['linked_share']:.2f} | " + " | ".join(
                    f"{g[m]['linked_share_mean']} [{g[m]['p_real_le_null']}, {g[m]['null_graphs_with_stratum']}]" if g[m]['linked_share_mean'] is not None else "—"
                    for m in modes) + " |")
        if d.get("fixed_regions"):
            sm = d["summary"]
            L.append(f"\nSame real group pairs re-checked in every null graph (cores fixed). Unlinked real candidate pairs: "
                     f"{sm.get('unlinked_pairs')}; unlinked in ≤ 5% of graphs of both profile nulls: {sm.get('unlinked_unexpected')}; "
                     f"BH q ≤ 0.10: {sm.get('unlinked_q10')}.\n")
            L.append("| dominant relations | real pairs | real linked | " + " | ".join(f"{m} linked [p real ≤ null]" for m in modes) + " |")
            L.append("|---" * (3 + len(modes)) + "|")
            for g in d["fixed_regions"]:
                L.append(f"| {g['relations']} | {g['pairs']} | {g['linked_share']:.2f} | " + " | ".join(
                    f"{g[m]['linked_share_mean']:.2f} [{g[m]['p_real_le_null']}]" for m in modes) + " |")
        for g in d.get("fixed_regions", []):
            if not g.get("examples"):
                continue
            L.append(f"\n### Sparse region {g['relations']}: unlinked real pairs that both profile nulls link most often\n")
            for b in g["examples"][:a.top]:
                L.append(f"- linked in ≥ {b['null_linked_share_min']:.0%} of graphs of each profile null; context {b['context']}; "
                         + "; ".join(f"{m} null mean links {b[m]['null_mean_links']}" for m in modes))
                L.append(f"  - A ({b['A']['size']}): {mem(b['A'])} — frame {fr(b['A']['frame'])}")
                L.append(f"  - B ({b['B']['size']}): {mem(b['B'])} — frame {fr(b['B']['frame'])}")
                L.append(f"  - shared surroundings: {', '.join(b['shared_surroundings'][:10])}")
                L.append(f"  - A→surroundings {b['A_to_surroundings']}; B→surroundings {b['B_to_surroundings']}")
        if d.get("unlinked"):
            L.append(f"\n### Unlinked context-similar group pairs least expected under both profile nulls (top {a.top})\n")
            for b in d["unlinked"][:a.top]:
                L.append(f"- p_absent (worst profile) {b['p_absent_max']}, q={b['q_bh']}, context {b['context']}; "
                         + "; ".join(f"{m} null mean links {b[m]['null_mean_links']}" for m in modes))
                L.append(f"  - A ({b['A']['size']}): {mem(b['A'])} — frame {fr(b['A']['frame'])}")
                L.append(f"  - B ({b['B']['size']}): {mem(b['B'])} — frame {fr(b['B']['frame'])}")
                L.append(f"  - shared surroundings: {', '.join(b['shared_surroundings'][:10])}")
                L.append(f"  - A→surroundings {b['A_to_surroundings']}; B→surroundings {b['B_to_surroundings']}")
        pmax = [max(b[m]["p_absent"] for m in pm) for b in B]
        q = bh(pmax) if B else []
        for b, q_ in zip(B, q):
            b["q"] = float(q_); b["pmax"] = max(b[m]["p_absent"] for m in pm)
            ta, tb = rtypes(b["A"]["frame"]), rtypes(b["B"]["frame"])
            b["kind"] = "location-only" if (ta | tb) <= LOC else ("different relation types" if ta != tb else "same relation types")
        L.append(f"\nBoundaries by frame kind: {dict(Counter(b['kind'] for b in B))}. "
                 f"Fixed-pair test (both profile nulls leave the pair unlinked in ≤ 5% of graphs): {sum(b['pmax'] <= 0.05 for b in B)} of {len(B)}; "
                 f"BH q ≤ 0.10: {sum(b['q'] <= 0.1 for b in B)}.\n")
        L.append(f"### Most unexpected boundaries (smallest worst-case profile p; ties by context similarity), top {a.top}\n")
        for b in sorted(B, key=lambda b: (b["pmax"], b["kind"] == "location-only", -b["context"]))[:a.top]:
            L.append(f"- **{b['kind']}**, context {b['context']}, comparable pairs {b['comparable_pairs']} with median "
                     f"{b['comparable_median']:.0f} links ({b['comparable_linked']:.0%} linked); "
                     + "; ".join(f"{m} p_absent={b[m]['p_absent']} (null mean links {b[m]['null_mean_links']})" for m in modes)
                     + f"; q={b['q']:.2f}")
            L.append(f"  - A ({b['A']['size']}): {mem(b['A'])} — frame {fr(b['A']['frame'])}")
            L.append(f"  - B ({b['B']['size']}): {mem(b['B'])} — frame {fr(b['B']['frame'])}")
            L.append(f"  - shared surroundings: {', '.join(b['shared_surroundings'][:10])}")
            L.append(f"  - A→surroundings {b['A_to_surroundings']}; B→surroundings {b['B_to_surroundings']}; "
                     f"links between comparable linked pairs are mostly {b['comparable_cross_relations']}")
        L.append("")
    open(a.out, "w").write("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
