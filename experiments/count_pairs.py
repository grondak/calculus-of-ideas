"""Count co-occurrence for every concept pair (linked or not) in a corpus, for gap analysis.

Same matcher, sentence unit and window as learn_weights.py; non-link pairs are kept with count >= --min.
"""
import argparse, json, time
import numpy as np
from ideanet.graph import IdeaGraph
from ideanet.corpus import count_cooccurrence, save_counts, read_wikitext, read_gutenberg, sample

ap = argparse.ArgumentParser()
ap.add_argument("graph"); ap.add_argument("corpus", choices=["wikitext103", "gutenberg"])
ap.add_argument("out"); ap.add_argument("files", nargs="+")
ap.add_argument("--min", type=int, default=1); ap.add_argument("--window", type=int, default=10)
ap.add_argument("--sample-mod", type=int, default=1); ap.add_argument("--sample-rem", type=int, default=0)
a = ap.parse_args()
g = IdeaGraph.load(a.graph)
reader = {"wikitext103": read_wikitext, "gutenberg": read_gutenberg}[a.corpus]
t = time.time()
c = count_cooccurrence(g, sample(reader(a.files), a.sample_mod, a.sample_rem), window=a.window, proposals_min=a.min)
prov = dict(corpus=a.corpus, files=a.files, window=a.window, min=a.min, sample_mod=a.sample_mod,
            sample_rem=a.sample_rem, graph=a.graph, seconds=round(time.time() - t))
save_counts(a.out, c, prov)
print(json.dumps(c["stats"]), len(c.get("prop_keys", [])), "non-link pairs")
