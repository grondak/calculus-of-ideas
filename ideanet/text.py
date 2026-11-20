"""Text -> stimulus: match words and phrases to idea labels."""
from __future__ import annotations

import re

from .graph import IdeaGraph

STOPWORDS = set("a an the of and or to in on at for with by is are was were be been it this that as from into".split())


class TextStimulus:
    def __init__(self, graph: IdeaGraph, max_ngram: int = 4) -> None:
        self.graph = graph
        self.max_ngram = max_ngram
        self.index: dict[str, str] = {}
        for idea in graph.ideas.values():
            for label in [idea.id.replace("_", " "), *idea.labels]:
                self.index.setdefault(self._norm(label), idea.id)

    @staticmethod
    def _norm(s: str) -> str:
        return " ".join(re.findall(r"[a-z0-9']+", s.lower()))

    def _lookup(self, phrase: str) -> str | None:
        if phrase in self.index:
            return self.index[phrase]
        for suffix, repl in (("ies", "y"), ("es", ""), ("s", "")):
            if phrase.endswith(suffix) and phrase[: -len(suffix)] + repl in self.index:
                return self.index[phrase[: -len(suffix)] + repl]
        return None

    def match(self, text: str) -> tuple[list[str], list[str]]:
        """Greedy longest-phrase match. Returns (matched idea ids, unmatched words)."""
        words = self._norm(text).split()
        matched, unmatched, i = [], [], 0
        while i < len(words):
            for n in range(min(self.max_ngram, len(words) - i), 0, -1):
                phrase = " ".join(words[i:i + n])
                if n == 1 and phrase in STOPWORDS:
                    idea = None
                    break
                idea = self._lookup(phrase)
                if idea:
                    break
            if idea:
                matched.append(idea)
                i += n
            else:
                if words[i] not in STOPWORDS:
                    unmatched.append(words[i])
                i += 1
        return matched, unmatched

    def stimuli(self, text: str, strength: float = 2.0) -> list[tuple[str, float]]:
        matched, _ = self.match(text)
        return [(idea, strength) for idea in matched]
