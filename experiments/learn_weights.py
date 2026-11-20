"""Learn PPMI link weights from a corpus; store counts and weights separately from the graph.

usage: python experiments/learn_weights.py GRAPH.pkl CORPUS_NAME OUT_PREFIX FILES... [--window 10] [--max-tokens N]
Writes OUT_PREFIX.counts.npz and OUT_PREFIX.weights.npz (aligned to graph.links, with provenance).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import time

import numpy as np

from ideanet import IdeaGraph
from ideanet.corpus import count_cooccurrence, load_counts, ppmi_weights, read_dailydialog, read_gutenberg, read_wikitext, sample, save_counts, save_weights

READERS = {"wikitext103": read_wikitext, "gutenberg": read_gutenberg, "dailydialog": read_dailydialog}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("graph")
    ap.add_argument("corpus", choices=sorted(READERS))
    ap.add_argument("out")
    ap.add_argument("files", nargs="+")
    ap.add_argument("--window", type=int, default=10)
    ap.add_argument("--min-count", type=int, default=3)
    ap.add_argument("--max-tokens", type=int)
    ap.add_argument("--sample-mod", type=int, default=1, help="keep paragraph i when i %% mod == rem")
    ap.add_argument("--sample-rem", type=int, default=0)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--reuse-counts", action="store_true")
    a = ap.parse_args()
    t0 = time.time()
    log = lambda *m, **k: print(f"[{time.time() - t0:6.1f}s]", *m, flush=True)
    g = IdeaGraph.load(a.graph)
    log(f"loaded graph: {len(g.ideas):,} ideas")
    if a.reuse_counts:
        counts = load_counts(a.out + ".counts.npz")
    else:
        counts = count_cooccurrence(g, sample(READERS[a.corpus](a.files), a.sample_mod, a.sample_rem), window=a.window, workers=a.workers,
                                    max_tokens=a.max_tokens, log=log)
    prov = counts["provenance"] if a.reuse_counts else {"corpus": a.corpus, "files": [{"path": f, "bytes": os.path.getsize(f),
                                           "sha1": hashlib.sha1(open(f, "rb").read()).hexdigest()} for f in a.files],
            "window": a.window, "unit": "sentence; pairs within window matched concepts",
            "max_tokens": a.max_tokens, "max_tokens_unit": "ideanet.corpus.TOKEN matches",
            "sample": {"mod": a.sample_mod, "rem": a.sample_rem, "unit": "paragraph index"}, "graph": a.graph, "stats": counts["stats"]}
    if not a.reuse_counts:
        save_counts(a.out + ".counts.npz", counts, prov)
    log("counts", counts["stats"], f"links observed: {(counts['link_cnt'] > 0).sum():,}/{len(counts['link_cnt']):,}")
    for mode in ("evidence", "replace"):
        w, info = ppmi_weights(g, counts, min_count=a.min_count, mode=mode)
        p = prov | {"weighting": "PPMI, rank-matched to original |weight| distribution; sign from relation",
                    **{k: v for k, v in info.items() if not isinstance(v, np.ndarray)}}
        save_weights(f"{a.out}.{mode}.weights.npz", g, w, info, p)
        log("weights", {k: v for k, v in info.items() if not isinstance(v, np.ndarray)})
        json.dump(p, open(f"{a.out}.{mode}.provenance.json", "w"), indent=1)


if __name__ == "__main__":
    main()
