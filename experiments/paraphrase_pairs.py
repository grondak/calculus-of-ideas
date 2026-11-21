"""Score candidate paraphrase pairs with a natural-language-inference cross-encoder (both directions).

Candidates: ideas with >= --min-deg typed links in the graph variant; pairs among each idea's --k nearest name
embeddings with cosine >= --cos, plus ConceptNet Synonym / SimilarTo / FormOf links between such ideas.
Output per pair: entailment and contradiction probability in each direction, cosine, and ConceptNet alias kind.
Mutual entailment (both directions) is the paraphrase criterion used by anchor_classes.py; one-way entailment
(running_in_marathon -> running, heifer -> cow) is hyponymy and is not merged.
"""
import argparse
import numpy as np
from experiments.morphology import CATEGORY, log
from experiments.typed_groups import UNTYPED


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("arrays"); ap.add_argument("emb"); ap.add_argument("out"); ap.add_argument("--keep")
    ap.add_argument("--min-deg", type=int, default=2); ap.add_argument("--k", type=int, default=10)
    ap.add_argument("--cos", type=float, default=0.4)
    ap.add_argument("--model", default="cross-encoder/nli-deberta-v3-small")
    a = ap.parse_args()
    z = np.load(a.arrays)
    ids, rels = [str(x) for x in z["ids"]], [str(r) for r in z["rels"]]
    n = len(ids)
    keep = np.load(a.keep)["keep"] if a.keep else np.ones(len(z["src"]), bool)
    fr = np.array([r not in UNTYPED and r not in CATEGORY for r in rels])
    s, d, r = z["src"][keep], z["dst"][keep], z["rel"][keep]
    m = fr[r] & (s != d)
    tdeg = np.bincount(np.r_[s[m], d[m]], minlength=n)
    e = np.load(a.emb)
    nodes, E = e["nodes"], e["E"].astype(np.float32)
    sel = nodes[tdeg[nodes] >= a.min_deg]
    Es = E[np.searchsorted(nodes, sel)]
    P = set()
    for i0 in range(0, len(sel), 4096):
        S = Es[i0:i0 + 4096] @ Es.T
        S[np.arange(S.shape[0]), np.arange(i0, i0 + S.shape[0])] = -1
        top = np.argpartition(-S, a.k, 1)[:, :a.k]
        v = np.take_along_axis(S, top, 1)
        for x, y in zip(*np.nonzero(v >= a.cos)):
            p, q = int(sel[i0 + x]), int(sel[top[x, y]])
            P.add((min(p, q), max(p, q)))
    ri = {x: k for k, x in enumerate(rels)}
    alias = {}
    ins = np.zeros(n, bool); ins[sel] = True
    for kname in ("Synonym", "SimilarTo", "FormOf"):
        am = (z["rel"] == ri[kname]) & ins[z["src"]] & ins[z["dst"]] & (z["src"] != z["dst"])
        for p, q in zip(z["src"][am].tolist(), z["dst"][am].tolist()):
            k_ = (min(p, q), max(p, q)); P.add(k_); alias[k_] = kname
    P = np.array(sorted(P), np.int64)
    pos = np.searchsorted(nodes, P)
    cos = np.einsum("ij,ij->i", E[pos[:, 0]], E[pos[:, 1]])
    log(f"{len(sel):,} ideas; {len(P):,} candidate pairs ({len(alias):,} ConceptNet aliases)")
    import torch
    torch.set_num_threads(8)
    from sentence_transformers import CrossEncoder
    ce = CrossEncoder(a.model)
    lab = {v.lower(): k for k, v in ce.model.config.id2label.items()}
    txt = lambda i: ids[i].replace("_", " ")
    out = np.zeros((len(P), 4), np.float32)  # entail ab, entail ba, contra ab, contra ba
    B = 4096
    for i0 in range(0, len(P), B):
        chunk = P[i0:i0 + B]
        L = ce.predict([(txt(p), txt(q)) for p, q in chunk] + [(txt(q), txt(p)) for p, q in chunk], batch_size=128)
        L = np.exp(L - L.max(1, keepdims=True)); L /= L.sum(1, keepdims=True)
        h = len(chunk)
        out[i0:i0 + h] = np.c_[L[:h, lab["entailment"]], L[h:, lab["entailment"]], L[:h, lab["contradiction"]], L[h:, lab["contradiction"]]]
        log(f"  {i0 + h:,}/{len(P):,}")
    ak = np.array([alias.get((int(p), int(q)), "") for p, q in P])
    np.savez_compressed(a.out, pairs=P, scores=out, cos=cos, alias=ak, model=a.model, settings=str(vars(a)))
    log("done")


if __name__ == "__main__":
    main()
