"""Sentence embeddings of idea names (underscores -> spaces) for every idea with a typed link in the chosen
graph variant. Used only to propose paraphrase equivalence classes (anchor_classes.py); independent of ConceptNet."""
import argparse
import numpy as np
from experiments.morphology import CATEGORY, log
from experiments.typed_groups import UNTYPED


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("arrays"); ap.add_argument("out"); ap.add_argument("--keep")
    ap.add_argument("--model", default="all-mpnet-base-v2")
    a = ap.parse_args()
    z = np.load(a.arrays)
    ids, rels = [str(x) for x in z["ids"]], [str(r) for r in z["rels"]]
    keep = np.load(a.keep)["keep"] if a.keep else np.ones(len(z["src"]), bool)
    fr = np.array([r not in UNTYPED and r not in CATEGORY for r in rels])
    s, d, r = z["src"][keep], z["dst"][keep], z["rel"][keep]
    m = fr[r] & (s != d)
    nodes = np.unique(np.r_[s[m], d[m]])
    log(f"embedding {len(nodes):,} ideas with {a.model}")
    from sentence_transformers import SentenceTransformer
    E = SentenceTransformer(a.model).encode([ids[i].replace("_", " ") for i in nodes], batch_size=256,
                                            normalize_embeddings=True, show_progress_bar=False)
    np.savez_compressed(a.out, nodes=nodes, E=E.astype(np.float16), model=a.model)
    log("done")


if __name__ == "__main__":
    main()
