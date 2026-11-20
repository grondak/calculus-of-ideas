"""Learn link weights from text corpora (co-occurrence -> PPMI), kept apart from the graph.

Pipeline:
  1. `ConceptMatcher`: greedy longest-phrase match of text to idea ids. Uses the
     same normalisation as TextStimulus, but works on integer ids so it is fast.
  2. `count_cooccurrence`: concepts co-occur when they are within `window`
     matched concepts of each other in the same sentence. All pairs feed the
     marginals; joint counts are kept only for pairs that are graph links
     (fixed topology) and, optionally, for frequent non-link pairs (proposals).
  3. `ppmi_weights`: PPMI per link, mapped onto the original |weight|
     distribution by rank (quantile matching). The weight marginal is unchanged,
     so only *which* links are strong changes. Signs (inhibition) come from the
     original relation. "evidence" mode reweights only links the corpus
     observed; "replace" mode reranks every link (unseen = PPMI 0).

Learned weights are stored as an .npz aligned to `graph.links` order, with a
fingerprint of that order and JSON provenance. Use `apply_weights` to swap
them in temporarily.
"""
from __future__ import annotations

import hashlib
import json
import math
import re
from collections.abc import Callable, Iterable, Iterator
from multiprocessing import Pool

import numpy as np

from .graph import IdeaGraph
from .text import STOPWORDS

TOKEN = re.compile(r"[a-z0-9']+")
SENT = re.compile(r"(?<=[.!?])\s+")
SHIFT = 21  # idea ids < 2**21


def pair_key(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    lo, hi = np.minimum(a, b).astype(np.int64), np.maximum(a, b).astype(np.int64)
    return (lo << SHIFT) | hi


def links_fingerprint(graph: IdeaGraph) -> str:
    h = hashlib.sha1()
    for l in graph.links:
        h.update(f"{l.source}\t{l.target}\t{l.relation}\n".encode())
    return h.hexdigest()


class ConceptMatcher:
    def __init__(self, graph: IdeaGraph, max_ngram: int = 4) -> None:
        self.ids = list(graph.ideas)
        num = {k: i for i, k in enumerate(self.ids)}
        self.index: dict[str, int] = {}
        for idea in graph.ideas.values():
            for label in [idea.id.replace("_", " "), *idea.labels]:
                phrase = " ".join(TOKEN.findall(label.lower()))
                if phrase:
                    self.index.setdefault(phrase, num[idea.id])
        self.max_ngram = max_ngram
        self.first_len: dict[str, int] = {}
        for phrase in self.index:
            w = phrase.split(" ")
            if len(w) <= max_ngram:
                self.first_len[w[0]] = max(self.first_len.get(w[0], 1), len(w))

    def _lookup(self, phrase: str) -> int | None:
        i = self.index.get(phrase)
        if i is not None:
            return i
        for suffix, repl in (("ies", "y"), ("es", ""), ("s", "")):
            if phrase.endswith(suffix):
                i = self.index.get(phrase[: -len(suffix)] + repl)
                if i is not None:
                    return i
        return None

    def match_tokens(self, words: list[str]) -> list[int]:
        out, i, n_words = [], 0, len(words)
        while i < n_words:
            w = words[i]
            if w in STOPWORDS:
                i += 1
                continue
            hit, step = None, 1
            for n in range(min(self.first_len.get(w, 1), n_words - i), 1, -1):
                hit = self.index.get(" ".join(words[i:i + n]))
                if hit is not None:
                    step = n
                    break
            if hit is None:
                hit = self._lookup(w)
            if hit is not None:
                out.append(hit)
            i += step
        return out

    def sentences(self, text: str) -> Iterator[list[int]]:
        for s in SENT.split(text.lower()):
            ids = self.match_tokens(TOKEN.findall(s))
            if ids:
                yield ids


# ---- corpus readers: each yields paragraphs (str) -------------------------

def read_wikitext(paths: Iterable[str]) -> Iterator[str]:
    import pyarrow.parquet as pq
    for p in paths:
        for batch in pq.ParquetFile(p).iter_batches(batch_size=20_000, columns=["text"]):
            for t in batch.column(0).to_pylist():
                t = t.strip()
                if t and not t.startswith("="):
                    yield t.replace(" @-@ ", "-").replace(" @,@ ", ",").replace(" @.@ ", ".")


# ---- counting --------------------------------------------------------------

_W: dict = {}


def _init(matcher, link_keys, prop_min, window):
    _W.update(matcher=matcher, link_keys=link_keys, prop_min=prop_min, window=window)


def _count_chunk(paras: list[str]):
    m, window = _W["matcher"], _W["window"]
    flat, sent_id, sents, tokens = [], [], 0, 0
    for p in paras:
        tokens += len(p.split())
        for ids in m.sentences(p):
            flat.extend(ids)
            sent_id.extend([sents] * len(ids))
            sents += 1
    ids = np.asarray(flat, dtype=np.int64)
    sid = np.asarray(sent_id, dtype=np.int64)
    n_ideas = len(m.ids)
    unigram = np.bincount(ids, minlength=n_ideas)
    marg = np.zeros(n_ideas, dtype=np.int64)
    keys = []
    for k in range(1, window + 1):
        if len(ids) <= k:
            break
        a, b = ids[:-k], ids[k:]
        ok = (sid[:-k] == sid[k:]) & (a != b)
        a, b = a[ok], b[ok]
        marg += np.bincount(a, minlength=n_ideas) + np.bincount(b, minlength=n_ideas)
        keys.append(pair_key(a, b))
    keys = np.concatenate(keys) if keys else np.zeros(0, np.int64)
    lk = _W["link_keys"]
    pos = np.searchsorted(lk, keys)
    pos[pos == len(lk)] = 0
    is_link = lk[pos] == keys
    li, lc = np.unique(pos[is_link], return_counts=True)
    other = None
    if _W["prop_min"]:
        ok, oc = np.unique(keys[~is_link], return_counts=True)
        other = (ok, oc)
    return dict(tokens=tokens, sentences=sents, matched=len(ids), pairs=len(keys),
                unigram=unigram, marg=marg, link_idx=li, link_cnt=lc, other=other)


def _chunks(paras: Iterable[str], size: int) -> Iterator[list[str]]:
    buf = []
    for p in paras:
        buf.append(p)
        if len(buf) >= size:
            yield buf
            buf = []
    if buf:
        yield buf


def count_cooccurrence(graph: IdeaGraph, paragraphs: Iterable[str], *, window: int = 10,
                       workers: int = 8, chunk: int = 2000, max_tokens: int | None = None,
                       proposals_min: int = 0, matcher: ConceptMatcher | None = None,
                       log: Callable[..., None] = print) -> dict:
    """Count concept co-occurrence. Returns arrays keyed to `link_keys` (sorted unique undirected link pairs)."""
    matcher = matcher or ConceptMatcher(graph)
    num = {k: i for i, k in enumerate(matcher.ids)}
    link_keys = np.unique(pair_key(np.array([num[l.source] for l in graph.links]),
                                   np.array([num[l.target] for l in graph.links])))
    n = len(matcher.ids)
    tot = dict(tokens=0, sentences=0, matched=0, pairs=0)
    unigram, marg = np.zeros(n, np.int64), np.zeros(n, np.int64)
    link_cnt = np.zeros(len(link_keys), np.int64)
    other_parts: list[tuple[np.ndarray, np.ndarray]] = []

    def capped():
        seen = 0
        for p in paragraphs:
            if max_tokens is not None and seen >= max_tokens:
                return
            seen += len(p.split())
            yield p

    with Pool(workers, initializer=_init, initargs=(matcher, link_keys, proposals_min, window)) as pool:
        for i, r in enumerate(pool.imap(_count_chunk, _chunks(capped(), chunk))):
            for k in tot:
                tot[k] += r[k]
            unigram += r["unigram"]
            marg += r["marg"]
            np.add.at(link_cnt, r["link_idx"], r["link_cnt"])
            if r["other"] is not None:
                other_parts.append(r["other"])
                if len(other_parts) >= 50:
                    other_parts = [_merge(other_parts)]
            if i % 50 == 0:
                log(f"  chunk {i}: {tot['tokens']:,} tokens, {tot['matched']:,} concepts", flush=True)
    out = dict(stats=tot, window=window, ids=matcher.ids, unigram=unigram, marg=marg,
               link_keys=link_keys, link_cnt=link_cnt)
    if proposals_min and other_parts:
        ok, oc = _merge(other_parts)
        keep = oc >= proposals_min
        out["prop_keys"], out["prop_cnt"] = ok[keep], oc[keep]
    return out


def _merge(parts):
    k = np.concatenate([p[0] for p in parts])
    c = np.concatenate([p[1] for p in parts])
    u, inv = np.unique(k, return_inverse=True)
    return u, np.bincount(inv, weights=c).astype(np.int64)


def save_counts(path: str, counts: dict, provenance: dict) -> None:
    arrays = {k: v for k, v in counts.items() if isinstance(v, np.ndarray)}
    meta = {"stats": counts["stats"], "window": counts["window"], "provenance": provenance}
    np.savez_compressed(path, ids=np.array(counts["ids"], dtype=object), meta=json.dumps(meta), **arrays)


def load_counts(path: str) -> dict:
    z = np.load(path, allow_pickle=True)
    d = {k: z[k] for k in z.files if k not in ("meta", "ids")}
    meta = json.loads(str(z["meta"]))
    d.update(ids=list(z["ids"]), stats=meta["stats"], window=meta["window"], provenance=meta["provenance"])
    return d


# ---- weights ---------------------------------------------------------------

def ppmi(counts: dict, keys: np.ndarray, joint: np.ndarray, min_count: int = 3) -> np.ndarray:
    marg = counts["marg"].astype(np.float64)
    total = marg.sum() / 2  # each pair adds 1 to both endpoints
    a, b = keys >> SHIFT, keys & ((1 << SHIFT) - 1)
    with np.errstate(divide="ignore", invalid="ignore"):
        pmi = np.log(joint * total / (marg[a] * marg[b]))
    pmi[(joint < min_count) | ~np.isfinite(pmi)] = 0.0
    return np.maximum(pmi, 0.0)


def _quantile_map(score: np.ndarray, mags: np.ndarray) -> np.ndarray:
    """Give the k-th lowest score the k-th lowest magnitude. Ties in score (e.g. the many unseen
    links at PPMI 0) are broken by the original magnitude, so the multiset of magnitudes is
    preserved exactly and tied links keep their original relative order."""
    order = np.lexsort((mags, score))
    out = np.empty(len(score))
    out[order] = np.sort(mags)
    return out


def ppmi_weights(graph: IdeaGraph, counts: dict, *, min_count: int = 3,
                 mode: str = "evidence") -> tuple[np.ndarray, dict]:
    """Learned weight per link (graph.links order), quantile-matched to original |weights|.

    mode="replace":  every link is ranked by PPMI (unseen links tie at 0) and mapped onto
                     the full original |weight| distribution.
    mode="evidence": only links whose pair co-occurs >= min_count times are re-ranked, mapped
                     onto those same links' original |weights|; all other links keep their
                     original weight. The corpus changes only what it has evidence about.
    """
    links = graph.links
    num = {k: i for i, k in enumerate(counts["ids"])}
    keys = pair_key(np.array([num[l.source] for l in links]), np.array([num[l.target] for l in links]))
    pos = np.searchsorted(counts["link_keys"], keys)
    joint = counts["link_cnt"][pos]
    score = ppmi(counts, keys, joint, min_count)
    orig = np.array([l.weight for l in links])
    if mode == "replace":
        learned = _quantile_map(score, np.abs(orig)) * np.sign(orig)
    elif mode == "evidence":
        ev = joint >= min_count
        learned = orig.copy()
        learned[ev] = _quantile_map(score[ev], np.abs(orig[ev])) * np.sign(orig[ev])
    else:
        raise ValueError(mode)
    info = {"mode": mode, "links": len(links), "observed": int((joint > 0).sum()),
            "evidence_links": int((joint >= min_count).sum()),
            "ppmi_positive": int((score > 0).sum()), "min_count": min_count,
            "changed_links": int((np.abs(learned - orig) > 1e-6).sum()),
            "ppmi_mean_pos": float(score[score > 0].mean()) if (score > 0).any() else 0.0}
    return learned.astype(np.float32), {"ppmi": score.astype(np.float32), "joint": joint, **info}


def save_weights(path: str, graph: IdeaGraph, weights: np.ndarray, extra: dict, provenance: dict) -> None:
    np.savez_compressed(path, weights=weights, fingerprint=links_fingerprint(graph),
                        provenance=json.dumps(provenance),
                        **{k: v for k, v in extra.items() if isinstance(v, np.ndarray)})


def load_weights(path: str, graph: IdeaGraph | None = None) -> dict:
    z = np.load(path, allow_pickle=True)
    if graph is not None and str(z["fingerprint"]) != links_fingerprint(graph):
        raise ValueError("learned weights were built for a different link order")
    d = {k: z[k] for k in z.files}
    d["provenance"] = json.loads(str(z["provenance"]))
    return d


def apply_weights(graph: IdeaGraph, weights: Iterable[float]) -> Callable[[], None]:
    """Set link weights in place (graph.links order); returns a restore callback."""
    links = graph.links
    old = [l.weight for l in links]
    w = list(map(float, weights))
    if len(w) != len(links):
        raise ValueError("weight count does not match link count")
    for l, x in zip(links, w):
        l.weight = x

    def restore():
        for l, x in zip(links, old):
            l.weight = x
    return restore


class WeightTable:
    """Look up per-link weights from arrays aligned to graph.links, without mutating the graph.

    `weight_fn(w, jitter_seed, sigma)` returns an Engine `weight_of` callable. Jitter is paired:
    the same seed gives the same multiplicative factor per link under every weight array.
    """

    def __init__(self, graph: IdeaGraph) -> None:
        self.links = graph.links
        self.index = {id(l): i for i, l in enumerate(self.links)}
        self.original = np.array([l.weight for l in self.links], dtype=np.float64)

    @staticmethod
    def jitter(n: int, seed: int, sigma: float) -> np.ndarray:
        return np.exp(np.random.default_rng(10_000 + seed).normal(0.0, sigma, n))

    def weight_fn(self, w: np.ndarray, jitter_seed: int | None = None, sigma: float = 0.05):
        arr = np.asarray(w, dtype=np.float64)
        if jitter_seed:
            arr = arr * self.jitter(len(arr), jitter_seed, sigma)
        vals, index = arr.tolist(), self.index
        return lambda link: vals[index[id(link)]]
