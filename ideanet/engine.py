"""Deterministic discrete-event activation engine.

Each delivered event is integrated into the target idea's decaying potential.
Crossing threshold (outside the refractory window) fires the idea: it emits a
human word (if it has any), resets, and schedules events along its out-links.
Every event is kept in the trace, not just the emitted words.
"""
from __future__ import annotations

import heapq
import json
import math
import random
from collections import defaultdict
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Callable, Iterable

from .graph import IdeaGraph


@dataclass(order=True)
class Event:
    time: float
    seq: int
    target: str = field(compare=False)
    source: str | None = field(compare=False)  # None => external stimulus
    strength: float = field(compare=False)
    kind: str = field(default="link", compare=False)  # link | stimulus | noise


@dataclass
class TraceRecord:
    time: float
    target: str
    source: str | None
    kind: str
    strength: float
    potential_before: float
    potential_after: float
    fired: bool


@dataclass
class Fire:
    time: float
    idea: str
    word: str | None
    inputs: tuple[str, ...]  # distinct sources integrated since last reset


@dataclass
class _State:
    potential: float = 0.0
    last_t: float = 0.0
    refractory_until: float = -math.inf
    inputs: list[str] = field(default_factory=list)


# An interpreter sees recent fires and may return new stimuli (idea, strength).
Interpreter = Callable[[float, list[Fire]], Iterable[tuple[str, float]]]


class Engine:
    def __init__(
        self,
        graph: IdeaGraph,
        *,
        seed: int = 0,
        fire_gain: float = 1.0,
        noise_rate: float = 0.0,
        noise_strength: float = 0.3,
        contexts: Iterable[str] = (),
        interpreter: Interpreter | None = None,
        interpret_every: int = 8,
        max_events: int = 200_000,
        top_k: int | None = None,
        global_inhibition: float = 0.0,
        inhibition_tau: float = 3.0,
        weight_of: Callable | None = None,
    ) -> None:
        self.graph = graph
        self.rng = random.Random(seed)
        self.fire_gain = fire_gain
        self.noise_rate = noise_rate
        self.noise_strength = noise_strength
        self.contexts = set(contexts)
        self.interpreter = interpreter
        self.interpret_every = interpret_every
        self.max_events = max_events
        self.weight_of = weight_of or (lambda link: link.weight)  # override weights without mutating the graph
        self.top_k = top_k  # a firing idea propagates only along its k strongest links
        self._top_cache: dict[str, list] = {}
        # Shared inhibitory pool: every fire adds 1 to a decaying global activity A;
        # effective thresholds are threshold * (1 + global_inhibition * A).
        self.global_inhibition = global_inhibition
        self.inhibition_tau = inhibition_tau
        self._activity = 0.0
        self._activity_t = 0.0

        self.now = 0.0
        self._seq = 0
        self._queue: list[Event] = []
        self.state: defaultdict[str, _State] = defaultdict(_State)
        self.trace: list[TraceRecord] = []
        self.fires: list[Fire] = []
        self.hit_event_limit = False
        self._since_interpret = 0

    def schedule(self, target: str, strength: float, at: float, source: str | None = None, kind: str = "link") -> None:
        self._seq += 1
        heapq.heappush(self._queue, Event(at, self._seq, target, source, strength, kind))

    def stimulate(self, idea: str, strength: float = 2.0, at: float | None = None) -> None:
        if idea not in self.graph.ideas:
            raise KeyError(f"unknown idea {idea!r}")
        self.schedule(idea, strength, self.now if at is None else at, kind="stimulus")

    def _decayed(self, idea_id: str, t: float) -> float:
        st, idea = self.state[idea_id], self.graph.ideas[idea_id]
        dt = t - st.last_t
        return st.potential * math.exp(-dt / idea.decay_tau) if dt > 0 else st.potential

    def _schedule_noise(self, until: float) -> None:
        if self.noise_rate <= 0:
            return
        ids = sorted(self.graph.ideas)
        t = self.rng.expovariate(self.noise_rate)
        while t < until:
            self.schedule(self.rng.choice(ids), self.noise_strength, t, kind="noise")
            t += self.rng.expovariate(self.noise_rate)

    def run(self, until: float = 100.0) -> "Engine":
        self._schedule_noise(until)
        while self._queue and self._queue[0].time <= until:
            if len(self.trace) >= self.max_events:
                self.hit_event_limit = True
                break
            self._deliver(heapq.heappop(self._queue))
        self.now = max(self.now, until) if not self.hit_event_limit else self.now
        return self

    def _deliver(self, ev: Event) -> None:
        self.now = ev.time
        idea = self.graph.ideas[ev.target]
        st = self.state[ev.target]
        before = self._decayed(ev.target, ev.time)
        after = before + ev.strength
        st.last_t = ev.time
        if ev.strength > 0 and ev.source is not None and ev.source not in st.inputs:
            st.inputs.append(ev.source)
        fired = after >= self._threshold(idea.threshold, ev.time) and ev.time >= st.refractory_until
        st.potential = idea.reset if fired else after
        self.trace.append(TraceRecord(ev.time, ev.target, ev.source, ev.kind, ev.strength, before, st.potential, fired))
        if fired:
            self._fire(ev.target, ev.time)

    def _global_activity(self, t: float) -> float:
        if t > self._activity_t:
            self._activity *= math.exp(-(t - self._activity_t) / self.inhibition_tau)
            self._activity_t = t
        return self._activity

    def _threshold(self, base: float, t: float) -> float:
        if not self.global_inhibition:
            return base
        return base * (1.0 + self.global_inhibition * self._global_activity(t))

    def _fire(self, idea_id: str, t: float) -> None:
        idea, st = self.graph.ideas[idea_id], self.state[idea_id]
        if self.global_inhibition:
            self._activity = self._global_activity(t) + 1.0
        word = self.rng.choice(idea.labels) if idea.labels else None
        self.fires.append(Fire(t, idea_id, word, tuple(st.inputs)))
        st.inputs = []
        st.refractory_until = t + idea.refractory
        for link in self._outgoing(idea_id):
            if link.context is None or link.context in self.contexts:
                self.schedule(link.target, self.weight_of(link) * self.fire_gain, t + link.delay, source=idea_id)
        self._since_interpret += 1
        if self.interpreter and self._since_interpret >= self.interpret_every:
            self._since_interpret = 0
            for target, strength in self.interpreter(t, self.fires[-self.interpret_every:]):
                self.schedule(target, strength, t, kind="stimulus")

    def _outgoing(self, idea_id: str) -> list:
        links = self.graph.out_links[idea_id]
        if self.top_k is None or len(links) <= self.top_k:
            return links
        if idea_id not in self._top_cache:
            self._top_cache[idea_id] = sorted(links, key=lambda l: -abs(self.weight_of(l)))[: self.top_k]
        return self._top_cache[idea_id]

    @property
    def emissions(self) -> list[str]:
        return [f.word for f in self.fires if f.word is not None]

    def jumble(self) -> str:
        return ". ".join(w.capitalize() for w in self.emissions) + ("." if self.emissions else "")

    def write_trace(self, path: str | Path) -> None:
        with open(path, "w") as fh:
            for rec in self.trace:
                fh.write(json.dumps(asdict(rec)) + "\n")
