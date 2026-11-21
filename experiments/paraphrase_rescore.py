"""Second NLI judgement for paraphrase candidates that pass the first model (paraphrase_pairs.py).

The small cross-encoder accepts many related-but-different short phrases as mutual entailment (liniment / linoleum,
salivate / gargle, tooth_paste / toothbrush). Pairs with first-model mutual entailment >= --entail, or a ConceptNet
FormOf link, are rescored in both directions with a larger NLI model; anchor_classes.py --judge requires both models.
"""
import argparse
import numpy as np
from experiments.morphology import log


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("arrays"); ap.add_argument("pairs"); ap.add_argument("out")
    ap.add_argument("--entail", type=float, default=0.6)
    ap.add_argument("--model", default="cross-encoder/nli-deberta-v3-base")
    a = ap.parse_args()
    ids = [str(x) for x in np.load(a.arrays)["ids"]]
    pp = np.load(a.pairs)
    sel = (pp["scores"][:, :2].min(1) >= a.entail) | (pp["alias"] == "FormOf")
    P = pp["pairs"][sel]
    log(f"rescoring {len(P):,} of {len(sel):,} pairs with {a.model}")
    import torch
    torch.set_num_threads(8)
    from sentence_transformers import CrossEncoder
    ce = CrossEncoder(a.model)
    lab = {v.lower(): k for k, v in ce.model.config.id2label.items()}
    txt = lambda i: ids[i].replace("_", " ")
    out = np.zeros((len(P), 4), np.float32)
    B = 4096
    for i0 in range(0, len(P), B):
        chunk = P[i0:i0 + B]
        L = ce.predict([(txt(p), txt(q)) for p, q in chunk] + [(txt(q), txt(p)) for p, q in chunk], batch_size=64)
        L = np.exp(L - L.max(1, keepdims=True)); L /= L.sum(1, keepdims=True)
        h = len(chunk)
        out[i0:i0 + h] = np.c_[L[:h, lab["entailment"]], L[h:, lab["entailment"]], L[:h, lab["contradiction"]], L[h:, lab["contradiction"]]]
        log(f"  {i0 + h:,}/{len(P):,}")
    np.savez_compressed(a.out, pairs=P, scores=out, model=a.model, settings=str(vars(a)))
    log("done")


if __name__ == "__main__":
    main()
