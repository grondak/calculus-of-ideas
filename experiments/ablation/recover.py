"""Blind recovery (PROTOCOL.md). Reads only BLIND/{worlds.json, worlds/*.npz, tasks.json} and idea-name embeddings;
never the intact graph, families or answer key. Writes one prediction file per world to PREDS/.

Methods: GEO (analog geometry in a typed low-rank space), RA (resource allocation), PPR (personalised
PageRank), SPEC (untyped spectral embedding), LANG (name embeddings, no graph), DEG (degree-only detector),
MFR (most-frequent-relation baseline for relation types), LANG-NAME (candidate name vs seed names)."""
import argparse, gzip, json, os, pickle, time
from multiprocessing import Pool
import numpy as np, scipy.sparse as sp
from sklearn.utils.extmath import randomized_svd

ap = argparse.ArgumentParser()
ap.add_argument("blind"); ap.add_argument("preds")
ap.add_argument("--names", default=os.path.expanduser("~/data/abl/names-minilm.npz"))
ap.add_argument("--dim", type=int, default=128); ap.add_argument("--top", type=int, default=200)
ap.add_argument("--hyp", type=int, default=10); ap.add_argument("--workers", type=int, default=4)
a = ap.parse_args()
METHODS = ("GEO", "RA", "PPR", "SPEC", "LANG")


def norm_rows(M):
    return M / np.maximum(np.linalg.norm(M, axis=-1, keepdims=True), 1e-9)


class World:
    def __init__(self, path, names):
        z = np.load(path); self.n = n = int(z["n"])
        s, d, r = z["src"].astype(np.int64), z["dst"].astype(np.int64), z["rel"].astype(np.int64)
        A = sp.coo_matrix((np.ones(len(s), np.float32), (s, d)), shape=(n, n)).tocsr(); A = (A + A.T).tocsr(); A.data[:] = 1
        self.A, self.deg = A, np.asarray(A.sum(1)).ravel()
        self.present = self.deg > 0
        rows = np.concatenate([s, d]); rd = np.concatenate([r * 2, r * 2 + 1]); part = np.concatenate([d, s])
        self.nrd = nrd = int(rd.max()) + 1
        uk, inv = np.unique(part * 1000 + rd, return_inverse=True)  # columns sorted by partner
        self.uk, self.col_part, self.col_rd = uk, uk // 1000, uk % 1000
        self.colw = (1 / np.sqrt(np.bincount(inv))).astype(np.float32)
        X = sp.csr_matrix((self.colw[inv], (rows, inv)), shape=(n, len(uk)))
        self.Xb = sp.csr_matrix((np.ones(len(inv), np.float32), (rows, inv)), shape=(n, len(uk)))
        U, S, Vt = randomized_svd(X, a.dim, n_iter=4, random_state=0)
        self.Vt = np.ascontiguousarray(Vt.astype(np.float32)); self.geo = norm_rows((U * S).astype(np.float32))
        self.has = np.zeros(n, bool); self.has[self.col_part] = True
        self.lo = np.searchsorted(self.col_part, np.arange(n)); self.hi = np.searchsorted(self.col_part, np.arange(n), "right")
        self.prior = np.bincount(rd, minlength=nrd).astype(np.float32); self.prior /= self.prior.sum()
        cnt = sp.csr_matrix((np.ones(len(rows), np.float32), (rows, rd)), shape=(n, nrd))
        self.mfr = np.asarray(cnt.argmax(1)).ravel() ^ 1  # flipped to the hypothetical idea's side
        dinv = 1 / np.sqrt(np.maximum(self.deg, 1))
        U2, S2, _ = randomized_svd(sp.diags(dinv) @ A @ sp.diags(dinv), a.dim, n_iter=4, random_state=0)
        self.spec = norm_rows((U2 * S2).astype(np.float32))
        self.PT = (sp.diags(1 / np.maximum(self.deg, 1)) @ A).T.tocsr()
        self.lang = np.zeros((n, names["E"].shape[1]), np.float32); self.lang[names["nodes"]] = names["E"]
        self.lang_ok = np.zeros(n, bool); self.lang_ok[names["nodes"]] = True; self.lang_ok &= self.present

    def cols(self, part, rd):
        k = np.asarray(part, np.int64) * 1000 + np.asarray(rd, np.int64)
        j = np.minimum(np.searchsorted(self.uk, k), len(self.uk) - 1)
        ok = self.uk[j] == k
        return j[ok], ok

    def best_col(self, xrow, t):
        lo, hi = self.lo[t], self.hi[t]
        return lo + int(np.argmax(xrow[lo:hi])) if hi > lo else -1

    def geo_query(self, seeds_list, k=50):
        """Analog geometry: fold a hypothetical idea linked to each seed set (relation-type prior) into the typed
        low-rank space, take the k ideas whose typed-link shape is nearest, and predict the hypothetical idea's
        typed links as their similarity-weighted typed links."""
        m = len(seeds_list)
        score = np.full((m, self.n), -np.inf, np.float32); xc = np.zeros((m, len(self.uk)), np.float32)
        starts = self.lo[self.has]
        for i, S in enumerate(seeds_list):
            ps = np.repeat(S, self.nrd); rds = np.tile(np.arange(self.nrd), len(S))
            j, ok = self.cols(ps, rds)
            q = self.Vt[:, j] @ (self.prior[rds[ok]] * self.colw[j]); q /= max(np.linalg.norm(q), 1e-9)
            sim = self.geo @ q; sim[S] = -1
            nn = np.argpartition(-sim, k)[:k]
            xc[i] = self.Xb[nn].T @ np.maximum(sim[nn], 0)
            score[i, self.has] = np.add.reduceat(xc[i], starts) + 1e-6 * self.deg[self.has] / self.deg.max()
            score[i, S] = -np.inf
        return score, xc

    def scores(self, method, seeds_list):
        if method == "GEO":
            return self.geo_query(seeds_list)
        m = len(seeds_list)
        Sm = sp.csr_matrix((np.concatenate([np.full(len(S), 1 / len(S)) for S in seeds_list]),
                            (np.repeat(np.arange(m), [len(S) for S in seeds_list]), np.concatenate(seeds_list))),
                           shape=(m, self.n), dtype=np.float32)
        if method == "RA":
            Sd = Sm.multiply(1 / np.maximum(self.deg, 1)[None]).multiply(np.asarray([[len(S)] for S in seeds_list]))
            out = np.asarray((Sd @ self.A).todense()) + 1e-6 * self.deg / self.deg.max()
        elif method == "PPR":
            e = Sm.T.toarray(); x = e.copy()
            for _ in range(10):
                x = 0.3 * e + 0.7 * (self.PT @ x)
            out = x.T
        elif method == "SPEC":
            out = (Sm @ self.spec) @ self.spec.T
        else:
            c = norm_rows(np.asarray(Sm @ self.lang)); out = c @ self.lang.T; out[:, ~self.lang_ok] = -np.inf
        out = np.ascontiguousarray(out, dtype=np.float32); out[:, ~self.present] = -np.inf
        for i, S in enumerate(seeds_list):
            out[i, S] = -np.inf
        return out, None

    def coherence(self, method, H):
        k = len(H)
        if method in ("GEO", "SPEC", "LANG"):
            M = norm_rows({"GEO": self.geo, "SPEC": self.spec, "LANG": self.lang}[method][H]); C = M @ M.T
        else:
            R = self.A[H]; nr = np.sqrt(np.asarray(R.sum(1)).ravel())
            C = (R @ R.T).toarray() / np.maximum(np.outer(nr, nr), 1e-9)
        return float((C.sum() - np.trace(C)) / (k * (k - 1)))

    def coverage(self, H):
        return float(np.asarray(self.A[H].sum(0)).ravel().max() / len(H))


def topk(x, k):
    k = min(k, int(np.isfinite(x).sum()))
    j = np.argpartition(-x, k)[:k]; return j[np.argsort(-x[j])]


def run(job):
    wid, tasks, pool, cname = job
    out = f"{a.preds}/{wid}.pkl.gz"
    if os.path.exists(out):
        return wid, 0
    t0 = time.time()
    names = dict(np.load(a.names)); names["E"] = names["E"].astype(np.float32)
    w = World(f"{a.blind}/worlds/{wid}.npz", names)
    res = {"seeded": {}, "pool": {}}
    for mth in METHODS:
        for c0 in range(0, len(tasks), 64):
            ch = tasks[c0:c0 + 64]
            sc, xh = w.scores(mth, [t["seeds"] for t in ch])
            for i, t in enumerate(ch):
                top = topk(sc[i], a.top)
                p = np.zeros(w.n, np.float32); p[top] = sc[i][top] - sc[i][top].min() + 1e-6
                ident = []
                for prof in t["candidates"]:  # only (inferred profile, candidate profile) similarity is used
                    q = np.asarray([x for x in prof if w.present[x]], np.int64)
                    ident.append(float(p[q].sum() / (np.linalg.norm(p) * np.sqrt(max(len(q), 1)))))
                r = res["seeded"].setdefault(t["task"], {})
                r[mth] = {"top": top.astype(np.int32), "score": sc[i][top], "ident": ident}
                if mth == "GEO":
                    r[mth]["rel"] = [int(w.col_rd[w.best_col(xh[i], v)]) for v in top]
                    r["MFR"] = {"rel": [int(w.mfr[v]) for v in top]}
                if mth == "LANG":
                    cen = norm_rows(w.lang[t["seeds"]].mean(0))
                    r["LANG-NAME"] = {"ident": [float(cname[nm] @ cen) for nm in t["candidate_names"]]}
        if pool:
            P = np.asarray(pool)
            for c0 in range(0, len(P), 64):
                ch = P[c0:c0 + 64]
                sc, _ = w.scores(mth, [[int(s)] for s in ch])
                for i, s in enumerate(ch):
                    H = np.concatenate([[s], topk(sc[i], a.hyp)]).astype(np.int64)
                    coh, cov = w.coherence(mth, H), w.coverage(H)
                    res["pool"].setdefault(int(s), {})[mth] = (coh * (1 - cov), coh, cov, H.astype(np.int32))
    for s in pool or ():
        res["pool"][int(s)]["DEG"] = (1 / (1 + w.deg[s]), 0.0, 0.0, None)
    with gzip.open(out, "wb") as fh:
        pickle.dump(res, fh)
    return wid, time.time() - t0


if __name__ == "__main__":
    os.makedirs(a.preds, exist_ok=True)
    wl = json.load(open(f"{a.blind}/worlds.json"))["worlds"]
    T = json.load(open(f"{a.blind}/tasks.json"))
    allnames = sorted({nm for t in T["seeded"] for nm in t["candidate_names"]})
    from sentence_transformers import SentenceTransformer
    emb = SentenceTransformer("all-MiniLM-L6-v2").encode(allnames, batch_size=512, normalize_embeddings=True)
    cname = dict(zip(allnames, emb.astype(np.float32)))
    by = {wd: [] for wd in wl}
    for t in T["seeded"]:
        by[t["world"]].append(t)
    jobs = [(wd, by[wd], T["pools"].get(wd), {nm: cname[nm] for t in by[wd] for nm in t["candidate_names"]}) for wd in wl]
    jobs.sort(key=lambda j: -len(j[2] or []))
    with Pool(a.workers) as p:
        for wid, dt in p.imap_unordered(run, jobs):
            print(wid, f"{dt:.0f}s", flush=True)
