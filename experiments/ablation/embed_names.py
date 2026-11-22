"""Sentence embeddings (all-MiniLM-L6-v2) of every idea name with a conceptual link: the language baseline's only
resource. Names only; no graph information."""
import sys, numpy as np, time
from experiments.ablation.common import load
from sentence_transformers import SentenceTransformer
g = load(sys.argv[1])
nodes = np.flatnonzero(g.deg0 > 0)
t = time.time()
E = SentenceTransformer("all-MiniLM-L6-v2").encode([g.ids[i].replace("_", " ") for i in nodes], batch_size=512,
                                                   normalize_embeddings=True, show_progress_bar=False)
np.savez_compressed(sys.argv[2], nodes=nodes, E=E.astype(np.float16))
print(len(nodes), time.time() - t)
