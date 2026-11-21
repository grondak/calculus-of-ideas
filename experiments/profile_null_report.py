"""Markdown report for profile_null.py: real vs re-mined null groups, survivors, anomaly 18."""
import gzip, json, re, sys

import numpy as np

A18 = {"swimming", "surfing", "skating", "skiing", "dancing", "singing", "playing_cards"}


STOP = {"the", "and", "for", "with", "get", "getting", "going", "have", "having", "take", "taking", "buy", "buying",
        "use", "using", "make", "making", "see", "seeing", "one", "out", "off", "into", "onto", "about"}


def tokens(x):
    return {t[:3] for t in re.split(r"[_\W]+", x) if len(t) >= 3 and t not in STOP}


def frame_kind(g, linked):
    """'paraphrase' when every pair of frame neighbours shares a content-word stem (3-letter prefix) or is directly linked in the full graph
    (light_fire / start_fire, cow / heifer); otherwise 'distinct'. Paraphrase frames are typical of crowd prompts
    asked twice in different words, which no degree- or profile-preserving null reproduces."""
    nodes = sorted({b for _, b in g["frame"]})
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            a, b = nodes[i], nodes[j]
            if not (tokens(a) & tokens(b)) and (a, b) not in linked:
                return "distinct"
    return "paraphrase"


def main(real_path, pn_path, out_path, arrays=None):
    R = json.load(gzip.open(real_path, "rt"))
    P = json.load(gzip.open(pn_path, "rt"))
    G, per, S = R["groups"], P["groups"], P["summary"]
    modes = [m for m in ("relation", "strict", "profile", "profile2") if m in per[0]]
    pm = [m for m in modes if m.startswith("profile")]
    linked = set()
    if arrays:
        z = np.load(arrays)
        ids = [str(x) for x in z["ids"]]
        need = {b for g in G for _, b in g["frame"]}
        idx = np.array([i for i, x in enumerate(ids) if x in need])
        m = np.isin(z["src"], idx) & np.isin(z["dst"], idx)
        for a, b in zip(z["src"][m], z["dst"][m]):
            linked |= {(ids[a], ids[b]), (ids[b], ids[a])}
    for g in G:
        g["frame_kind"] = frame_kind(g, linked)
        g["frame_relations"] = len({a for a, _ in g["frame"]})
    L = []
    w = L.append
    st = S["settings"]
    w(f"# Profile-preserving nulls, re-mined (member cap {st['real_settings']['max_member_features']} typed features)\n")
    w(f"{st['nulls']} null graphs per mode, every one mined with the identical procedure. No edges or labels added.\n")
    w("| null | what is kept besides per-relation in/out counts, dataset, two-way pairs | typed incidences of the real graph still present |")
    w("|---|---|---|")
    desc = dict(relation="nothing else (two-way pairs not kept)", strict="log2 degree class of both ends",
                profile="each end's dominant (relation, direction) + log2 typed degree",
                profile2="each end's top-2 (relation, direction) + log2 typed degree")
    for m in modes:
        w(f"| {m} | {desc[m]} | {S['counts'][m]['retained_incidences']:.1%} |")
    for m, v in S["profile_classes"].items():
        w(f"\n{m}: {v['classes']} endpoint classes; {v['typed_one_way_links_in_singleton_strata']:.1%} of typed one-way links and "
          f"{v['two_way_pairs_in_singleton_strata']:.1%} of two-way pairs sit in strata of one (cannot move).")
    w("\n## Group counts: real vs re-mined nulls (null mean [min–max])\n")
    keys = list(S["counts"]["real"])
    w("| | real | " + " | ".join(modes) + " |")
    w("|---|---|" + "---|" * len(modes))
    for k in keys:
        w(f"| {k} | {S['counts']['real'][k]} | " + " | ".join(
            f"{S['counts'][m][k]['mean']} [{S['counts'][m][k]['min']}–{S['counts'][m][k]['max']}]" for m in modes) + " |")
    w("\n## Shapes: groups of size ≥ 6 (null mean) and largest group (null mean of the largest)\n")
    w("| shape | relation profile | real ≥6 | real unnamed ≥6 | real max | " + " | ".join(f"{m} ≥6 / unnamed / max" for m in modes) + " |")
    w("|---|---|---|---|---|" + "---|" * len(modes))
    prof = {s["shape"]: s["relation_profile"] for s in R["shapes"]}
    for s in S["shapes"][:16]:
        w(f"| {s['shape']} | {', '.join(f'{a} {b:.0%}' for a, b in prof[s['shape']])} | {s['real_ge_6']} | {s['real_unnamed_ge_6']} | {s['real_max']} | "
          + " | ".join(f"{s[m]['mean_ge_6']} / {s[m]['mean_unnamed_ge_6']} / {s[m]['mean_max']}" for m in modes) + " |")
    w(f"\n## Survival\n")
    w(f"- frame support at the p floor under {', '.join(pm)} and reproduced (member Jaccard ≥ 0.5) in ≤ 5% of re-mined nulls: "
      f"**{S['survives_profile']}** of {len(G)} groups; by tier {S['survives_by_tier']['survives_profile']}")
    w(f"- and, in addition, larger than the largest re-mined null group of the same shape in ≥ 95% of nulls: "
      f"**{S['survives_selection']}**; by tier {S['survives_by_tier']['survives_selection']}")
    from collections import Counter
    for k in ("survives_profile", "survives_selection"):
        c = Counter((G[i]["frame_kind"], G[i]["frame_relations"] > 1) for i, d in enumerate(per) if d[k])
        w(f"- {k} by frame kind (kind, >1 relation type): {dict(sorted(c.items()))}")
    c = Counter((g["frame_kind"], g["frame_relations"] > 1) for g in G)
    w(f"- all groups by frame kind: {dict(sorted(c.items()))}")
    was_rob = [d for d, g in zip(per, G) if g.get("robust")]
    w(f"- of the {len(was_rob)} groups robust in the earlier run, {sum(d['survives_profile'] for d in was_rob)} survive the profile nulls and "
      f"{sum(d['survives_selection'] for d in was_rob)} also the selection control\n")

    def line(gi):
        g, d = G[gi], per[gi]
        fr = "; ".join(f"{a} {b}" for a, b in g["frame"][:6])
        nl = ", ".join(f"{m} z {d[m]['z']} (null {d[m]['mean']}), sel p {d[m]['p_selection']}, repro {d[m]['reproduced']:.0%}" for m in pm)
        return (f"- **g{gi}** n={g['size']}, {g['tier']}, shape {g['shape']}, {g['frame_kind']} frame: {', '.join(g['members'][:14])}{' …' if g['size'] > 14 else ''}\n"
                f"  - frame: {fr}\n  - support {g['support']}; {nl}; strict z {d['strict']['z']}")

    def zmin(gi):
        return min(per[gi][m]["z"] for m in pm)

    w("## Survivors of the selection control, by tier (largest size × min profile z first, ≤ 2 per shape)\n")
    for tier in ("named", "partly_named", "uncategorised", "crosscutting"):
        ids = sorted((i for i, d in enumerate(per) if d["survives_selection"] and G[i]["tier"] == tier),
                     key=lambda i: -G[i]["size"] * zmin(i))
        w(f"### {tier} ({len(ids)})\n")
        seen = {}
        for i in ids:
            if seen.get(G[i]["shape"], 0) >= 2:
                continue
            seen[G[i]["shape"]] = seen.get(G[i]["shape"], 0) + 1
            w(line(i))
            if sum(seen.values()) >= 8:
                break
        w("")
    w("## Selection survivors with distinct (non-paraphrase) frame neighbours\n")
    dist = sorted((i for i, d in enumerate(per) if d["survives_selection"] and G[i]["frame_kind"] == "distinct"),
                  key=lambda i: -G[i]["size"] * zmin(i))
    w(f"{len(dist)} groups.\n")
    for i in dist[:25]:
        w(line(i))
    w("")
    w("## Disappeared: earlier robust unnamed groups that the profile nulls explain\n")
    gone = sorted((i for i, d in enumerate(per) if G[i].get("robust") and not d["survives_profile"]
                   and G[i]["tier"] in ("uncategorised", "crosscutting")), key=lambda i: -G[i]["size"])
    w(f"{len(gone)} groups. Largest:\n")
    for i in gone[:10]:
        w(line(i))
    w("\n## Anomaly 18 family (groups with ≥ 2 of swimming, surfing, skating, skiing, dancing, singing, playing_cards)\n")
    fam = sorted((i for i, g in enumerate(G) if len(A18 & set(g["members"])) >= 2), key=lambda i: -G[i]["size"])
    w(f"{len(fam)} groups.\n")
    w("| g | n | anomaly-18 members | frame | tier | " + " | ".join(f"{m} z / sel p / repro" for m in modes) + " | survives profile | + selection |")
    w("|---|---|---|---|---|" + "---|" * len(modes) + "---|---|")
    for i in fam:
        g, d = G[i], per[i]
        w(f"| {i} | {g['size']} | {', '.join(sorted(A18 & set(g['members'])))} | {'; '.join(f'{a} {b}' for a, b in g['frame'][:4])} | {g['tier']} | "
          + " | ".join(f"{d[m]['z']} / {d[m]['p_selection']} / {d[m]['reproduced']:.0%}" for m in modes)
          + f" | {d['survives_profile']} | {d['survives_selection']} |")
    w("\n## What construction alone produces: largest unnamed groups mined from profile nulls (seeds 0–2)\n")
    ex = [e for e in P["null_examples"].get("profile", []) if e["tier"] in ("uncategorised", "crosscutting")]
    seenf = set()
    for e in sorted(ex, key=lambda e: -e["size"]):
        f = tuple(sorted(b for _, b in e["frame"]))
        if f in seenf:
            continue
        seenf.add(f)
        w(f"- n={e['size']}, {e['tier']}, shape {e['shape']}: {', '.join(e['members'][:12])} …\n  - frame: {'; '.join(f'{a} {b}' for a, b in e['frame'][:6])}")
        if len(seenf) >= 8:
            break
    open(out_path, "w").write("\n".join(L) + "\n")


if __name__ == "__main__":
    main(*sys.argv[1:5])
