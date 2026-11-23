"""Statistical baselines on anonymous worlds: per-pair features, no rule language."""
import numpy as np
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from experiments.ontology.discover import base_dirs, flat


def pair_features(world, paths=False, extra=()):
    u, b = world["unary"], world["binary"]
    n = u.shape[1]
    cols = []
    d = [m.astype(float) for m in base_dirs(world)]
    for m in d:
        cols.append(m)
    for m in b.astype(float):
        for v in (m.sum(1), m.sum(0)):
            cols += [np.repeat(v[:, None], n, 1), np.repeat(v[None, :], n, 0)]
    for v in u.astype(float):
        cols += [np.repeat(v[:, None], n, 1), np.repeat(v[None, :], n, 0)]
    d2 = [a @ c for a in d for c in d]
    cols += d2
    if paths:
        cols += [a @ c for a in d2 for c in d]
    for m in extra:
        cols += [m.astype(float), m.T.astype(float)]
    return np.stack([flat(c) for c in cols], 1)


def design(worlds, **kw):
    return np.concatenate([pair_features(w, **kw) for w in worlds]), np.concatenate([flat(w["target"]) for w in worlds])


def fit_lr(worlds):
    X, y = design(worlds)
    if y.all() or not y.any():
        return None
    return make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000, C=1.0)).fit(X, y)


def fit_gbm(worlds, extra_fn=None):
    feats = [pair_features(w, paths=True, extra=extra_fn(w) if extra_fn else ()) for w in worlds]
    X, y = np.concatenate(feats), np.concatenate([flat(w["target"]) for w in worlds])
    if y.all() or not y.any():
        return None
    return HistGradientBoostingClassifier(max_iter=200, random_state=0).fit(X, y)


def predict(model, worlds, paths, extra_fn=None):
    out = []
    for w in worlds:
        n = w["target"].shape[0]
        if model is None:
            out.append(np.zeros((n, n), bool))
            continue
        X = pair_features(w, paths=paths, extra=extra_fn(w) if extra_fn else ())
        m = np.zeros((n, n), bool)
        m[~np.eye(n, dtype=bool)] = model.predict(X).astype(bool)
        out.append(m)
    return out
