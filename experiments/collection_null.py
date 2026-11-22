"""Does one-event-at-a-time collection explain the sparse HasPrerequisite region?

Collection unit of an event E (merged class level): E plus every answer y with E HasPrerequisite y.
Null modes (fixed real cores and candidate pairs from boundaries.py, nulls on original IDs then contracted):
  <base>        the earlier strict / profile / profile2 nulls
  <base>|hp     every HasPrerequisite link held fixed (each event keeps its exact list); the rest shuffled
  <base>|units  HasPrerequisite links and every other link inside one unit held fixed (lists and their
                internal structure intact); only links leaving a unit are shuffled
If the deficit survives <base>|units, it is not produced by shuffling answers across events.
Also: which relations create the cross-links in real vs null graphs, and contributor / template provenance
of the prerequisite links. No edges are proposed and nothing is named.
"""
import argparse, gzip, json
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
import scipy.sparse as sp

from experiments.morphology import log
from experiments.sparse_core import load_graph, settings, real_regions, run_nulls


def units(g, mp, rname="HasPrerequisite"):
    h = g["rel"] == g["rels"].index(rname)
    E, P = mp[g["src"][h]], mp[g["dst"][h]]
    ue, ei = np.unique(E, return_inverse=True)
    U = sp.csr_matrix((np.ones(2 * len(E)), (np.r_[ei, ei], np.r_[E, P])), shape=(len(ue), g["n"]))
    U.data[:] = 1
    Ut = U.T.tocsr()
    intra = np.asarray(Ut[mp[g["src"]]].multiply(Ut[mp[g["dst"]]]).sum(1)).ravel() > 0
    return h, h | intra, U


def provenance(g, mp, reg, path, rname="HasPrerequisite"):
    """Contributors/templates of prerequisite links; linked share of HP x HP pairs by contributor overlap."""
    idx = {x: i for i, x in enumerate(g["ids"])}
    con = {}
    tmpl, act = Counter(), Counter()
    ncon = Counter()
    for line in gzip.open(path, "rt"):
        r, s, e, dset, c, a, t = line.rstrip("\n").split("\t")
        if r != rname or s not in idx or e not in idx:
            continue
        cs = set(c.split("|")) - {""}
        con.setdefault((mp[idx[s]], mp[idx[e]]), set()).update(cs)
        tmpl[t] += 1; ncon[len(cs)] += 1
        for x in a.split("|"):
            act[x] += 1
    # answer reuse across events
    ev_of = defaultdict(set)
    for (E, y) in con:
        ev_of[y].add(E)
    reuse = Counter(min(len(v), 5) for v in ev_of.values())
    # same contributor behind a reused answer?
    same, tot = 0, 0
    rng = np.random.default_rng(0)
    pool = list(con.values())
    base_same = np.mean([bool(pool[i] & pool[j]) for i, j in rng.integers(0, len(pool), (20000, 2))])
    for y, Es in ev_of.items():
        Es = sorted(Es)
        for i in range(len(Es)):
            for j in range(i + 1, len(Es)):
                tot += 1; same += bool(con[(Es[i], y)] & con[(Es[j], y)])
    # HP x HP candidate pairs: contributors per core
    r = reg["r"]; groups = reg["groups"]; codes = reg["space"].codes; n = g["n"]
    hp = g["rels"].index(rname)
    key = hp * 1000 + hp
    w = np.flatnonzero(r["rp"] == key)
    core_con = {}
    for gi in set(r["i"][w]) | set(r["j"][w]):
        M, F = groups[gi]
        Cs = set()
        for c in codes[F]:
            if c // n // 2 != hp:
                continue
            a_ = c % n
            for m in M:
                Cs |= con.get((a_, m), set()) | con.get((m, a_), set())
        core_con[gi] = Cs
    jac = np.array([len(core_con[i] & core_con[j]) / max(1, len(core_con[i] | core_con[j])) for i, j in zip(r["i"][w], r["j"][w])])
    lk = r["cross"][w] > 0
    share = lambda m: (float(lk[m].mean()) if m.any() else None, int(m.sum()))
    return dict(links=len(con), templates=tmpl.most_common(12), activities=act.most_common(8),
                contributors_per_link={str(k): v for k, v in sorted(ncon.items())},
                answer_reuse={str(k): v for k, v in sorted(reuse.items())},
                reused_answer_pairs=tot, reused_same_contributor=round(same / max(tot, 1), 3),
                random_link_pairs_same_contributor=round(float(base_same), 4),
                hp_pairs_linked_by_contributor_overlap=dict(none=share(jac == 0), some=share(jac > 0)),
                hp_pairs_with_contributor_overlap=round(float((jac > 0).mean()), 3))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("arrays"); ap.add_argument("real", help="typed-groups.json.gz (settings)"); ap.add_argument("out")
    ap.add_argument("--keep"); ap.add_argument("--sources", required=True); ap.add_argument("--merge")
    ap.add_argument("--provenance"); ap.add_argument("--nulls", type=int, default=1000)
    ap.add_argument("--n-rel", type=int, default=100); ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--modes", default="strict,profile,profile2,profile|hp,strict|units,profile|units,profile2|units")
    ap.add_argument("--extra-units", default="", help="relations whose collection units are available as mode|units:REL")
    a = ap.parse_args()
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    g = load_graph(a.arrays, a.keep, a.sources)
    mp = np.load(a.merge)["cls"] if a.merge else np.arange(g["n"])
    reg = real_regions(g, mp, settings(a.real))
    hp, un, U = units(g, mp)
    log(f"{len(reg['groups']):,} groups, {len(reg['r']['i']):,} pairs; units {U.shape[0]:,}; "
        f"HasPrerequisite links {hp.sum():,}, held fixed with units {un.sum():,} of {len(un):,}")
    from experiments.sparse_core import by_relation
    r = reg["r"]
    real_rel = by_relation(g, mp, g["src"], g["dst"], r["Co"], r["i"], r["j"], reg["W"])
    modes = a.modes.split(",")
    fixed = dict(hp=hp, units=un)
    for rn in filter(None, a.extra_units.split(",")):
        fixed[f"units:{rn}"] = units(g, mp, rn)[1]
        log(f"{rn} units: {fixed[f'units:{rn}'].sum():,} links held fixed")
    st = run_nulls(g, mp, reg, modes, a.nulls, fixed=fixed, workers=a.workers, n_rel=a.n_rel)
    res = dict(settings=vars(a), units=int(U.shape[0]), hp_links=int(hp.sum()), fixed_units=int(un.sum()), strata=[])
    for t, name in enumerate(reg["names"]):
        d = dict(relations=name, pairs=int(reg["W"][t].sum()), linked=round(float(reg["real"][t]), 3), nulls={},
                 real_by_relation={g["rels"][k]: round(float(real_rel[k, t]), 3) for k in range(g["R"]) if real_rel[k, t] > 0})
        for m in modes:
            s = st[m]
            d["nulls"][m] = dict(mean=round(float(s["mean"][t]), 3), sd=round(float(s["sd"][t]), 4), z=round(float(s["z"][t]), 2),
                                 p=round(float(s["p"][t]), 5), q=round(float(s["q"][t]), 5),
                                 by_relation=None if s["rel"] is None else
                                 {g["rels"][k]: round(float(s["rel"][k, t]), 3) for k in range(g["R"]) if s["rel"][k, t] > 0.005})
        res["strata"].append(d)
    res["strata"].sort(key=lambda d: -d["pairs"])
    if a.provenance:
        res["provenance"] = provenance(g, mp, reg, a.provenance)
    with gzip.open(out / "collection-null.json.gz", "wt") as f:
        json.dump(res, f)
    L = ["| dominant relations | pairs | real linked | " + " | ".join(m.replace("|", " fixing ") for m in modes) + " |", "|" + "---|" * (3 + len(modes))]
    for d in res["strata"]:
        L.append(f"| {d['relations']} | {d['pairs']} | {d['linked']:.2f} | " + " | ".join(
            f"{d['nulls'][m]['mean']:.2f} ({d['nulls'][m]['z']:+.1f}; q {d['nulls'][m]['q']:.3f})" for m in modes) + " |")
    (out / "collection-null.md").write_text("Null mean (z; BH q for real < null)\n\n" + "\n".join(L) + "\n")
    log("done")


if __name__ == "__main__":
    main()
