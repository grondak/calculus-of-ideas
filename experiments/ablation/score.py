"""Score blind predictions against the sealed key (PROTOCOL.md). Writes OUT/results.json and prints Markdown tables."""
import argparse, glob, gzip, json, os, pickle
from collections import defaultdict
import numpy as np, scipy.sparse as sp
from scipy.stats import spearmanr
from experiments.ablation.common import undirected

ap = argparse.ArgumentParser()
ap.add_argument("out"); ap.add_argument("--preds", default=None)
ap.add_argument("--names", default=os.path.expanduser("~/data/abl/names-minilm.npz"))
ap.add_argument("--arrays", default=os.path.expanduser("~/data/abl/arrays.npz"))
a = ap.parse_args()
P = a.preds or a.out + "/preds"
key = json.load(gzip.open(a.out + "/key/key.json.gz")); tk = json.load(open(a.out + "/key/tasks_key.json"))
T = {t["task"]: t for t in json.load(open(a.out + "/blind/tasks.json"))["seeded"]}
rels = [str(r) for r in np.load(a.arrays)["rels"]]
preds = {os.path.basename(f)[:-7]: pickle.load(gzip.open(f)) for f in sorted(glob.glob(P + "/W*.pkl.gz"))}
W = key["worlds"]; C = key["concepts"]
byb = defaultdict(dict)
for wid, w in W.items():
    byb[w["batch"]][w["kind"]] = wid
INTACT, NULL = byb[0]["INTACT"], byb[0]["NULL"]
M = ("GEO", "RA", "PPR", "SPEC", "LANG")
R = {"recon": defaultdict(list), "ident": defaultdict(list), "rel": defaultdict(list), "per": defaultdict(dict)}
z = np.load(a.names); epos = np.full(max(int(z["nodes"].max()) + 1, 1), -1); epos[z["nodes"]] = np.arange(len(z["nodes"]))
E = z["E"].astype(np.float32)
wdeg = {}


def world_core(wid):
    if wid not in wdeg:
        zz = np.load(f"{a.out}/blind/worlds/{wid}.npz")
        A = undirected(int(zz["n"]), zz["src"], zz["dst"]); wdeg[wid] = (A, np.asarray(A.sum(1)).ravel())
    return wdeg[wid]


def rank_of_true(scores, labels, keep):
    s = np.asarray(scores); idx = [i for i, l in enumerate(labels) if l in keep]
    t = [i for i in idx if labels[i] == "true"][0]
    gt = sum(s[i] > s[t] for i in idx); eq = sum(s[i] == s[t] for i in idx) - 1
    return 1 + gt + eq / 2, len(idx)


def random_ap(T, N, K):
    """Expected AP@K (normalised by min(T, K)) of a uniformly random ranking of N ideas containing T targets."""
    if T == 0:
        return 0.0
    r = np.arange(1, min(K, N) + 1)
    return float((T / N) * ((1 + (r - 1) * (T - 1) / max(N - 1, 1)) / r).sum() / min(T, K))


# ---- reconstruction, relation types, identification (method rankings restricted, like RANDOM and the targets, to
# ideas with surviving degree >= 2)
for tid, k in tk["seeded"].items():
    t = T[tid]; wid = t["world"]; c = k["concept"]
    if wid not in preds:
        continue
    pr = preds[wid]["seeded"][tid]
    tg = {int(x): v for x, v in C[c]["targets"][wid].items()}
    truth = set(tg) - set(t["seeds"])
    _, dg = world_core(wid); ncore = int((dg >= 2).sum()) - len(t["seeds"])
    g = (k["kind"], k["k"])
    R["recon"][g + ("RANDOM",)].append((random_ap(len(truth), ncore, len(pr["GEO"]["top"])), min(1.0, 50 / ncore)))
    for m in M:
        top = [v for v in pr[m]["top"] if dg[int(v)] >= 2]; hit = np.array([int(v) in truth for v in top], bool)
        ap_ = (np.cumsum(hit) / np.arange(1, len(hit) + 1))[hit].sum() / max(1, min(len(truth), len(top)))
        r50 = hit[:50].sum() / max(1, len(truth))
        R["recon"][g + (m,)].append((ap_, r50)); R["per"][(c, k["kind"], k["k"])][m + ":ap"] = ap_
        for lab, keep in (("rand", {"true", "rand"}), ("hard", {"true", "hard"})):
            rk, nn = rank_of_true(pr[m]["ident"], k["labels"], keep)
            R["ident"][g + (lab, m)].append((rk <= 1, 1 / rk)); R["per"][(c, k["kind"], k["k"])][f"{m}:{lab}"] = float(rk <= 1)
    for lab, keep in (("rand", {"true", "rand"}), ("hard", {"true", "hard"})):
        rk, nn = rank_of_true(pr["LANG-NAME"]["ident"], k["labels"], keep)
        R["ident"][g + (lab, "LANG-NAME")].append((rk <= 1, 1 / rk))
        R["per"][(c, k["kind"], k["k"])][f"LANG-NAME:{lab}"] = float(rk <= 1)
        R["ident"][g + (lab, "RANDOM")].append((1 / nn, np.mean(1 / np.arange(1, nn + 1))))
    top = pr["GEO"]["top"]
    for j, v in enumerate(top):  # relation types: GEO's own list (index j aligns with pr["GEO"]["rel"])
        if int(v) in truth:
            want = {rels.index(r) * 2 + (0 if out else 1) for r, out in tg[int(v)]}
            R["rel"][(k["kind"], "GEO")].append(pr["GEO"]["rel"][j] in want)
            R["rel"][(k["kind"], "MFR")].append(pr["MFR"]["rel"][j] in want)
            R["rel"][(k["kind"], "GEO-reltype")].append(pr["GEO"]["rel"][j] // 2 in {x // 2 for x in want})
            R["rel"][(k["kind"], "MFR-reltype")].append(pr["MFR"]["rel"][j] // 2 in {x // 2 for x in want})


def auc(x, y):
    x, y = np.asarray(x), np.asarray(y)
    if len(x) == 0 or len(y) == 0:
        return float("nan")
    return float(((x[:, None] > y[None]).mean() + 0.5 * (x[:, None] == y[None]).mean()))


# ---- detection and localization
DET = defaultdict(list); LOC = defaultdict(list)
DM = M + ("DEG",)
for b, kinds in byb.items():
    pk = tk["pools"][str(b)]; nodes, lab = pk["nodes"], pk["concept"]
    aff = [s for s, l in zip(nodes, lab) if l]; bg = [s for s, l in zip(nodes, lab) if not l]
    if INTACT not in preds:
        continue
    base = preds[INTACT]["pool"]
    for kind, wid in kinds.items():
        if wid not in preds or kind in ("INTACT", "NULL"):
            continue
        pool = preds[wid]["pool"]
        base = preds[NULL if kind == "NULL-ND" else INTACT]["pool"]
        for m in DM:
            pa = [s for s in aff if s in pool]; pb = [s for s in bg if s in pool]
            d_aff = [float(pool[s][m][0] > base[s][m][0]) + 0.5 * float(pool[s][m][0] == base[s][m][0]) for s in pa]
            d_bg = [float(pool[s][m][0] > base[s][m][0]) + 0.5 * float(pool[s][m][0] == base[s][m][0]) for s in pb]
            within = auc([pool[s][m][0] for s in pa], [pool[s][m][0] for s in pb])
            DET[(kind, m)].append((np.mean(d_aff), np.mean(d_bg), within, len(pa)))
        if kind in ("ND0", "ND", "NI1", "NI2", "NI3", "SHAM-ND"):
            for m in M:
                for wk, P_ in ((kind, pool), ("INTACT", preds[INTACT]["pool"])):
                    order = sorted((s for s in dict.fromkeys(nodes) if s in P_), key=lambda s: -P_[s][m][0])
                    isbg = set(bg) - set(aff); nbg = sum(s in isbg for s in order)
                    for c, kc in C.items():
                        if kc["batch"] != b:
                            continue
                        nb = {int(x) for x in kc["targets"][kinds["ND" if kind == "SHAM-ND" else kind]]}
                        above = 0; pct = 1.0
                        for s in order:
                            H = P_[s][m][3]
                            if np.mean([int(h) in nb for h in H]) >= 0.3:
                                pct = above / max(1, nbg); break
                            above += s in isbg
                        LOC[(kind, wk, m)].append(pct)
                        if wk == kind:
                            R["per"][(c, kind, "loc")][m] = pct

# ---- properties
props = {}
for c, kc in C.items():
    wid = byb[kc["batch"]]["ND"]; A, dg = world_core(wid)
    nb = np.array(sorted(int(x) for x in kc["targets"][wid]))
    sub = A[nb][:, nb]; k_ = len(nb)
    cn = (A[nb] @ A[nb].T).toarray(); np.fill_diagonal(cn, 0)
    ok = epos[nb[nb < len(epos)]]; ok = ok[ok >= 0]
    En = E[ok]; nc = float(((En @ En.T).sum() - len(ok)) / max(1, len(ok) * (len(ok) - 1)))
    rcount = defaultdict(int)
    for v in kc["targets"][wid].values():
        for r, o in v:
            rcount[(r, o)] += 1
    p = np.array(list(rcount.values()), float); p /= p.sum()
    props[c] = {"cat": kc["cat"], "deg": kc["deg"], "surv_deg": k_, "family_nd": kc["n_nd"], "family_ni1": kc["n_ni1"],
                "tri_density": float(sub.sum() / max(1, k_ * (k_ - 1))), "mean_common_nbrs": float(cn.sum() / max(1, k_ * (k_ - 1))),
                "nbr_mean_deg": float(dg[nb].mean()), "name_coherence": nc, "rel_entropy": float(-(p * np.log(p)).sum())}


def mean(v, i=None):
    v = [x[i] if i is not None else x for x in v]; return float(np.mean(v)) if v else float("nan")


out = {"recon": {"|".join(map(str, k)): (mean(v, 0), mean(v, 1), len(v)) for k, v in R["recon"].items()},
       "ident": {"|".join(map(str, k)): (mean(v, 0), mean(v, 1), len(v)) for k, v in R["ident"].items()},
       "rel": {"|".join(k): (mean(v), len(v)) for k, v in R["rel"].items()},
       "det": {"|".join(k): [float(np.nanmean([x[i] for x in v])) for i in range(3)] + [int(sum(x[3] for x in v))] for k, v in DET.items()},
       "loc": {"|".join(k): (float(np.median(v)), float(np.mean(np.array(v) < 0.05)), len(v)) for k, v in LOC.items()},
       "props": props, "per": {"|".join(map(str, k)): v for k, v in R["per"].items()}}
json.dump(out, open(a.out + "/results.json", "w"), indent=1, default=float)
print("results ->", a.out + "/results.json")
