"""Command line: run, null, perturb, generate."""
from __future__ import annotations

import argparse
import json
import sys

from .analysis import characterize, null_comparison, perturb_links
from .engine import Engine
from .graph import IdeaGraph
from .ontology import inject_unfamiliar, random_ontology


def _stimuli(specs: list[str]) -> list[tuple[str, float]]:
    out = []
    for s in specs:
        idea, _, strength = s.partition(":")
        out.append((idea, float(strength or 2.0)))
    return out


def _engine_kw(a: argparse.Namespace) -> dict:
    return {"fire_gain": a.gain, "noise_rate": a.noise, "contexts": a.context or [], "top_k": a.top_k, "global_inhibition": a.inhibition}


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="ideanet", description="Activation dynamics over an idea graph.")
    sub = p.add_subparsers(dest="cmd", required=True)

    def common(sp):
        sp.add_argument("ontology", help="JSON ontology file")
        sp.add_argument("-s", "--stimulus", action="append", default=[], help="idea[:strength], repeatable")
        sp.add_argument("-t", "--text", help="free text; words/phrases matched to idea labels become stimuli")
        sp.add_argument("--strength", type=float, default=2.0, help="stimulus strength for --text matches")
        sp.add_argument("--until", type=float, default=100.0)
        sp.add_argument("--seed", type=int, default=0)
        sp.add_argument("--gain", type=float, default=1.0, help="global multiplier on link weights")
        sp.add_argument("--noise", type=float, default=0.0, help="spontaneous noise events per time unit")
        sp.add_argument("--context", action="append", help="activate context-gated links, repeatable")
        sp.add_argument("--fanout-alpha", type=float, default=0.0, help="damp hub out-links (0=off, 1=full cap)")
        sp.add_argument("--fanout-budget", type=float, default=3.0)
        sp.add_argument("--top-k", type=int, help="firing idea propagates only along its k strongest links")
        sp.add_argument("--inhibition", type=float, default=0.0, help="global inhibitory pool strength (raises thresholds with recent activity)")
        sp.add_argument("--threshold", type=float, help="override every idea's threshold")

    r = sub.add_parser("run", help="run once, print jumble and dynamics")
    common(r)
    r.add_argument("--trace", help="write full activation trace (JSONL)")
    r.add_argument("--plot", help="write raster plot PNG")
    r.add_argument("--max-words", type=int, default=200, help="truncate printed jumble")

    n = sub.add_parser("null", help="compare against degree-preserving rewired graphs")
    common(n)
    n.add_argument("--samples", type=int, default=50)

    q = sub.add_parser("perturb", help="knock out each link, rank by effect on dynamics")
    common(q)
    q.add_argument("--top", type=int, default=10)

    imp = sub.add_parser("import-conceptnet", help="build an ontology from a ConceptNet assertions .csv.gz")
    imp.add_argument("csv_gz")
    imp.add_argument("out", help=".pkl recommended for large graphs")
    imp.add_argument("--lang", default="en")

    gen = sub.add_parser("generate", help="write a synthetic community-structured ontology")
    gen.add_argument("out")
    gen.add_argument("--nodes", type=int, default=1000)
    gen.add_argument("--k", type=int, default=4)
    gen.add_argument("--seed", type=int, default=0)
    gen.add_argument("--unfamiliar", type=int, default=0, help="inject N 'bee-axle' links")

    a = p.parse_args(argv)

    if a.cmd == "generate":
        g = random_ontology(a.nodes, a.k, seed=a.seed)
        if a.unfamiliar:
            inject_unfamiliar(g, a.unfamiliar, seed=a.seed)
        g.save(a.out)
        print(f"wrote {a.out}: {len(g.ideas)} ideas, {len(g.links)} links")
        return 0

    if a.cmd == "import-conceptnet":
        from .conceptnet import import_conceptnet
        g = import_conceptnet(a.csv_gz, lang=a.lang)
        g.save(a.out)
        print(f"wrote {a.out}: {len(g.ideas):,} ideas, {sum(len(v) for v in g.out_links.values()):,} links")
        return 0

    g = IdeaGraph.load(a.ontology)
    if a.fanout_alpha:
        from .ontology import normalize_fanout
        normalize_fanout(g, a.fanout_budget, a.fanout_alpha)
    if a.threshold is not None:
        for idea in g.ideas.values():
            idea.threshold = a.threshold
    stim = _stimuli(a.stimulus)
    if a.text:
        from .text import TextStimulus
        matched, unmatched = TextStimulus(g).match(a.text)
        print(f"text matched: {matched or '-'}  unmatched: {unmatched or '-'}")
        stim += [(m, a.strength) for m in matched]
    if not stim:
        p.error("no stimulus: give -s and/or a --text that matches some idea")

    if a.cmd == "run":
        eng = Engine(g, seed=a.seed, **_engine_kw(a))
        for idea, s in stim:
            eng.stimulate(idea, s)
        eng.run(a.until)
        words = eng.emissions
        shown = ". ".join(w.capitalize() for w in words[: a.max_words])
        more = f" ... (+{len(words) - a.max_words} more)" if len(words) > a.max_words else ""
        print((shown + "." + more) if words else "(silence)")
        print()
        print(characterize(eng, a.until).summary())
        from collections import Counter
        top = Counter(f.word or f"<{f.idea}>" for f in eng.fires).most_common(15)
        print(f"distinct ideas fired={len({f.idea for f in eng.fires})} events={len(eng.trace)} most frequent={top}")
        if a.trace:
            eng.write_trace(a.trace)
            print(f"trace: {a.trace} ({len(eng.trace)} events)")
        if a.plot:
            from .plot import raster
            raster(eng, a.plot, title=f"{a.ontology.split('/')[-1]} stimulus={a.stimulus or a.text!r}")
            print(f"plot: {a.plot}")
    elif a.cmd == "null":
        res = null_comparison(g, stim, a.until, samples=a.samples, seed=a.seed, **_engine_kw(a))
        print(f"{'metric':<20}{'observed':>10}{'null mean':>11}{'null sd':>9}{'z':>7}{'p':>7}")
        for k, v in res.items():
            print(f"{k:<20}{v['observed']:>10.1f}{v['null_mean']:>11.1f}{v['null_sd']:>9.1f}{v['z']:>7.2f}{v['p']:>7.3f}")
    elif a.cmd == "perturb":
        for row in perturb_links(g, stim, a.until, seed=a.seed, top=a.top, **_engine_kw(a)):
            print(json.dumps(row))
    return 0


if __name__ == "__main__":
    sys.exit(main())
