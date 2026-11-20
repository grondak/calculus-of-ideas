"""Raster plot of fires over time (one row per idea)."""
from __future__ import annotations

from .engine import Engine


def raster(engine: Engine, path: str, title: str = "") -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    ideas = sorted({f.idea for f in engine.fires}, key=lambda i: min(f.time for f in engine.fires if f.idea == i))
    if not ideas:
        return
    row = {k: n for n, k in enumerate(ideas)}
    fig, ax = plt.subplots(figsize=(12, max(3, 0.2 * len(ideas))))
    named = [f for f in engine.fires if f.word is not None]
    unnamed = [f for f in engine.fires if f.word is None]
    ax.scatter([f.time for f in named], [row[f.idea] for f in named], marker="|", s=120, c="tab:blue", label="emitted word")
    ax.scatter([f.time for f in unnamed], [row[f.idea] for f in unnamed], marker="|", s=120, c="tab:red", label="no human word")
    ax.set_yticks(range(len(ideas)), ideas if len(ideas) <= 150 else [""] * len(ideas), fontsize=8 if len(ideas) <= 60 else 6)
    ax.invert_yaxis()
    ax.set_xlabel("time")
    ax.set_title(title or "idea activation raster")
    ax.legend(loc="upper right", fontsize=8)
    fig.tight_layout()
    fig.savefig(path, dpi=120)
    plt.close(fig)
