"""Paraphrase equivalence classes of ideas, for normalising the graph before group mining.

Evidence (paraphrase_pairs.py): two ideas are joined when an NLI cross-encoder finds that each name entails the
other (both entailment probabilities >= --entail), e.g. go_on_internet / surf_net, see_movie / watch_film; or when
ConceptNet records one as a FormOf (inflection) of the other. One-way entailment (heifer -> cow) is not merged.
Must stay apart: ConceptNet Antonym / DistinctFrom links, pairs the NLI model finds contradictory, names that differ
by a ConceptNet antonym word pair (turn_on_tv / turn_off_tv), names where only one side carries a negation, and
names that only add content words to the other (chess / play_chess, see extends()).
Classes are complete-linkage clusters inside connected components of the evidence graph (joined pairs at distance
0.2, other pairs 1 - name cosine, forbidden pairs 2, cut at 1 - --complete = 0.25), so every pair in a class is
either directly joined or has name cosine >= 0.75, and classes cannot chain into blobs. Below name cosine --low-cos
both NLI models must be confident (liniment / lint passes the models at cosine 0.51).
Output keeps every original id: cls[i] is the representative idea (highest typed degree) of idea i's class.
"""
import argparse, gzip, json, re
import numpy as np
import scipy.sparse as sp
from scipy.cluster.hierarchy import fcluster, linkage
from scipy.sparse.csgraph import connected_components

from experiments.morphology import CATEGORY, log
from experiments.typed_groups import UNTYPED

NEG = {"not", "no", "never", "without", "dont", "don't", "cannot", "cant", "can't", "nobody", "nothing", "non"}


LIGHT = {"a", "an", "the", "to", "of", "some", "more", "do", "doing", "does", "did", "get", "getting", "got", "have",
         "having", "has", "be", "being", "one's", "your", "yourself", "oneself", "someone", "something", "thing", "things"}


def toks(x):
    return set(t for t in re.split(r"[_\W]+", x) if t)


def stem(t):
    for suf in ("ing", "es", "ed", "s"):
        if len(t) > len(suf) + 2 and t.endswith(suf):
            return t[: -len(suf)]
    return t


def extends(x, y):
    """y is x plus content words (chess / play_chess, fire / light_fire, music / love_music): an entity or topic
    and an activity or attitude about it, which a symmetric NLI judgement often accepts but which are not paraphrases."""
    sx, sy = {stem(t) for t in toks(x) - LIGHT}, {stem(t) for t in toks(y) - LIGHT}
    return bool(sx) and sx < sy


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("arrays"); ap.add_argument("emb"); ap.add_argument("pairs"); ap.add_argument("out")
    ap.add_argument("--keep")
    ap.add_argument("--entail", type=float, default=0.5)
    ap.add_argument("--contra", type=float, default=0.5)
    ap.add_argument("--complete", type=float, default=0.75,
                    help="every pair in a class must be joined by evidence or have name cosine >= this")
    ap.add_argument("--low-cos", type=float, default=0.55,
                    help="below this name cosine, both NLI models must give >= 0.9 entailment in both directions")
    ap.add_argument("--max-class", type=int, default=40)
    ap.add_argument("--judge", help="paraphrase_rescore.py output: a second NLI model must also find mutual entailment")
    ap.add_argument("--judge-entail", type=float, default=0.8)
    a = ap.parse_args()
    z = np.load(a.arrays)
    ids, rels = [str(x) for x in z["ids"]], [str(r) for r in z["rels"]]
    n = len(ids)
    e = np.load(a.emb)
    nodes, E = e["nodes"], e["E"].astype(np.float32)
    keep = np.load(a.keep)["keep"] if a.keep else np.ones(len(z["src"]), bool)
    fr = np.array([r not in UNTYPED and r not in CATEGORY for r in rels])
    s, d, r = z["src"][keep], z["dst"][keep], z["rel"][keep]
    m = fr[r] & (s != d)
    tdeg = np.bincount(np.r_[s[m], d[m]], minlength=n)

    pp = np.load(a.pairs)
    P, Sc, cosv, ak = pp["pairs"], pp["scores"], pp["cos"], pp["alias"]
    ri = {x: k for k, x in enumerate(rels)}
    fs, fd, fl = z["src"], z["dst"], z["rel"]
    cm = np.isin(fl, [ri["Antonym"], ri["DistinctFrom"]]) & (fs != fd)
    cannot = set(zip(fs[cm].tolist(), fd[cm].tolist()))
    antw = {(ids[x], ids[y]) for x, y in cannot if "_" not in ids[x] and "_" not in ids[y]}
    contra = Sc[:, 2:].max(1) >= a.contra
    cannot |= set(map(tuple, P[contra].tolist()))
    cannot |= {(y, x) for x, y in cannot}

    mutual = Sc[:, :2].min(1) >= a.entail

    def forbidden(x, y):
        if (x, y) in cannot:
            return True
        tx, ty = toks(ids[x]), toks(ids[y])
        if bool(tx & NEG) != bool(ty & NEG):
            return True
        dx, dy = tx - ty, ty - tx
        if any((u, v) in antw for u in dx for v in dy):
            return True
        return extends(ids[x], ids[y]) or extends(ids[y], ids[x])

    if a.judge:
        jz = np.load(a.judge)
        jk = {(int(p), int(q)): k for k, (p, q) in enumerate(jz["pairs"])}
        js = np.zeros((len(P), 4), np.float32); js[:, 2:] = 1
        for k, (p, q) in enumerate(P.tolist()):
            if (p, q) in jk:
                js[k] = jz["scores"][jk[(p, q)]]
        jcon = js[:, 2:].max(1) >= a.contra
        cannot |= set(map(tuple, P[jcon & (js[:, :2].min(1) < a.judge_entail)].tolist()))
        cannot |= {(y, x) for x, y in cannot}
        contra |= jcon
        mutual &= js[:, :2].min(1) >= a.judge_entail
        log(f"second model {jz['model']}: mutual entailment kept {mutual.sum():,}")
    strong = Sc[:, :2].min(1) >= 0.9
    if a.judge:
        strong &= js[:, :2].min(1) >= 0.9
    mutual &= (cosv >= a.low_cos) | strong
    acc = (mutual | ((ak == "FormOf") & (cosv >= 0.5))) & ~contra
    acc &= np.array([not forbidden(int(p), int(q)) for p, q in P], bool)
    log(f"{len(P):,} scored pairs: mutual entailment {mutual.sum():,}, FormOf {(ak == 'FormOf').sum():,}, "
        f"contradiction {contra.sum():,}; accepted {acc.sum():,}")
    AP = P[acc]
    u_nodes, inv = np.unique(AP, return_inverse=True)
    inv = inv.reshape(-1, 2)
    G = sp.coo_matrix((np.ones(len(AP)), (inv[:, 0], inv[:, 1])), shape=(len(u_nodes),) * 2)
    ncomp, lab = connected_components(G, directed=False)
    sizes = np.bincount(lab)
    log(f"evidence components: {ncomp:,}, largest {sizes.max():,}")
    pos = -np.ones(n, np.int64); pos[nodes] = np.arange(len(nodes))
    cls = np.arange(n)
    order = np.argsort(lab, kind="stable"); bounds = np.searchsorted(lab[order], np.arange(ncomp + 1))
    split = 0
    cut = 1 - a.complete
    negf = np.array([bool(toks(x) & NEG) for x in ids])
    cn = np.array(sorted(cannot), np.int64).reshape(-1, 2)
    loc = -np.ones(n, np.int64)
    for c in range(ncomp):
        mem = u_nodes[order[bounds[c]:bounds[c + 1]]]
        if len(mem) == 2:
            parts = np.array([1, 1])
        else:
            loc[mem] = np.arange(len(mem))
            V = E[pos[mem]]
            D = 1 - V @ V.T
            jm = (loc[AP[:, 0]] >= 0) & (loc[AP[:, 1]] >= 0)
            jx, jy = loc[AP[jm, 0]], loc[AP[jm, 1]]
            D[jx, jy] = D[jy, jx] = 0.2
            D[negf[mem][:, None] != negf[mem][None, :]] = 2.0
            fm = (loc[cn[:, 0]] >= 0) & (loc[cn[:, 1]] >= 0)
            D[loc[cn[fm, 0]], loc[cn[fm, 1]]] = 2.0
            xs, ys = np.nonzero(np.triu(D < cut, 1))
            for x, y in zip(xs.tolist(), ys.tolist()):
                if forbidden(int(mem[x]), int(mem[y])):
                    D[x, y] = D[y, x] = 2.0
            np.fill_diagonal(D, 0)
            D = np.clip(np.maximum(D, D.T), 0, None)
            parts = fcluster(linkage(D[np.triu_indices(len(mem), 1)], "complete"), cut, "distance")
            split += len(np.unique(parts)) > 1
            loc[mem] = -1
            del D, V
        for p_ in np.unique(parts):
            sub = mem[parts == p_]
            if 1 < len(sub) <= a.max_class:
                cls[sub] = sub[np.argmax(tdeg[sub])]
            elif len(sub) > a.max_class:
                log(f"  class of {len(sub)} left unmerged: {[ids[x] for x in sub[:8]]}")
    u, cnt = np.unique(cls, return_counts=True)
    multi = u[cnt > 1]
    log(f"components split by complete linkage: {split}; classes with >= 2 ideas: {len(multi):,}; "
        f"ideas merged away: {int((cnt - 1).sum()):,}; largest {cnt.max()}")
    pk = {(int(p), int(q)): k for k, (p, q) in enumerate(P)}
    order = np.argsort(cls, kind="stable"); cs = cls[order]
    classes = []
    for c in multi:
        lo, hi = np.searchsorted(cs, [c, c + 1]); mem = sorted(order[lo:hi].tolist())
        ev = []
        for x in range(len(mem)):
            for y in range(x + 1, len(mem)):
                k = pk.get((mem[x], mem[y]))
                if k is not None and acc[k]:
                    ev.append([ids[mem[x]], ids[mem[y]], "FormOf" if ak[k] == "FormOf" and not mutual[k] else "mutual_entailment",
                               round(float(Sc[k, 0]), 3), round(float(Sc[k, 1]), 3), round(float(cosv[k]), 3)])
        classes.append(dict(rep=ids[c], members=[ids[x] for x in mem], typed_degree=[int(tdeg[x]) for x in mem], evidence=ev))
    classes.sort(key=lambda c_: -sum(c_["typed_degree"]))
    np.savez_compressed(a.out + ".npz", cls=cls, settings=json.dumps(vars(a)))
    with gzip.open(a.out + ".json.gz", "wt") as f:
        json.dump(dict(settings=vars(a), classes=classes), f)
    log("done")


if __name__ == "__main__":
    main()
