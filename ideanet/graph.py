"""Idea graph: nodes are ideas, links carry signed activation weights."""
from __future__ import annotations

import json
import pickle
from dataclasses import asdict, dataclass, field
from pathlib import Path


@dataclass(slots=True)
class Idea:
    id: str
    labels: list[str] = field(default_factory=list)  # empty => no human word
    threshold: float = 1.0
    decay_tau: float = 4.0  # potential decays as exp(-dt / tau)
    refractory: float = 2.0
    reset: float = 0.0


@dataclass(slots=True)
class Link:
    source: str
    target: str
    weight: float  # >0 excitatory, <0 inhibitory
    delay: float = 1.0
    context: str | None = None  # active only when this context is set
    relation: str | None = None  # provenance, e.g. ConceptNet relation name


class IdeaGraph:
    def __init__(self) -> None:
        self.ideas: dict[str, Idea] = {}
        self.out_links: dict[str, list[Link]] = {}

    def add_idea(self, idea: Idea) -> Idea:
        self.ideas[idea.id] = idea
        self.out_links.setdefault(idea.id, [])
        return idea

    def add_link(self, link: Link) -> Link:
        for end in (link.source, link.target):
            if end not in self.ideas:
                raise KeyError(f"unknown idea {end!r}")
        self.out_links[link.source].append(link)
        return link

    def connect(self, a: str, b: str, weight: float, *, both: bool = False, **kw) -> None:
        self.add_link(Link(a, b, weight, **kw))
        if both:
            self.add_link(Link(b, a, weight, **kw))

    @property
    def links(self) -> list[Link]:
        return [l for ls in self.out_links.values() for l in ls]

    def out_degree(self) -> dict[str, int]:
        return {k: len(v) for k, v in self.out_links.items()}

    def in_degree(self) -> dict[str, int]:
        deg = {k: 0 for k in self.ideas}
        for l in self.links:
            deg[l.target] += 1
        return deg

    def copy(self) -> "IdeaGraph":
        return IdeaGraph.from_dict(self.to_dict())

    def to_dict(self) -> dict:
        return {
            "ideas": [asdict(i) for i in self.ideas.values()],
            "links": [asdict(l) for l in self.links],
        }

    @classmethod
    def from_dict(cls, data: dict) -> "IdeaGraph":
        g = cls()
        defaults = data.get("defaults", {})
        for raw in data["ideas"]:
            raw = {"id": raw} if isinstance(raw, str) else raw
            g.add_idea(Idea(**(defaults | raw)))
        for raw in data["links"]:
            if isinstance(raw, list):
                raw = dict(zip(("source", "target", "weight"), raw))
            g.add_link(Link(**raw))
        return g

    def save(self, path: str | Path) -> None:
        if str(path).endswith(".pkl"):
            with open(path, "wb") as fh:
                pickle.dump(self, fh, protocol=pickle.HIGHEST_PROTOCOL)
        else:
            Path(path).write_text(json.dumps(self.to_dict(), indent=1))

    @classmethod
    def load(cls, path: str | Path) -> "IdeaGraph":
        if str(path).endswith(".pkl"):
            with open(path, "rb") as fh:
                return pickle.load(fh)
        return cls.from_dict(json.loads(Path(path).read_text()))
