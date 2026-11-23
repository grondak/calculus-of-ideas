"""Synthetic relational worlds with hidden rules (generator side only).

Every world has the same shape regardless of family: n entities, 2 unary base
predicates, 3 binary base relations and one binary target. Discovery code never
imports this module; the runner anonymises slots and entity order first.
"""
import numpy as np

N_UNARY, N_BINARY = 2, 3


def _blank(n):
    return np.zeros((N_UNARY, n), bool), np.zeros((N_BINARY, n, n), bool)


def _er(rng, n, deg):
    m = rng.random((n, n)) < deg / max(n - 1, 1)
    np.fill_diagonal(m, False)
    return m


def _closure(r):
    c = r.copy()
    while True:
        nxt = c | ((c.astype(np.int32) @ c.astype(np.int32)) > 0)
        if (nxt == c).all():
            return c
        c = nxt


def _forest(rng, n, tree_size, shallow):
    parent = np.zeros((n, n), bool)
    for start in range(0, n, tree_size):
        nodes = list(range(start, min(start + tree_size, n)))
        for k in range(1, len(nodes)):
            if shallow:
                cand = [nodes[0]] + [v for v in nodes[1:k] if parent[v, nodes[0]]]
                p = cand[rng.integers(len(cand))] if rng.random() < 0.5 else nodes[0]
            else:
                p = nodes[max(0, k - 1 - rng.integers(2))]
            parent[nodes[k], p] = True
    return parent


def closure(rng, size, shallow=False, shuffled=False):
    n, ts = (24, 8) if size == "small" else (48, 16)
    u, b = _blank(n)
    u[0], u[1] = rng.random(n) < 0.5, rng.random(n) < 0.5
    b[0] = _forest(rng, n, ts, shallow)
    b[1], b[2] = _er(rng, n, 1.5), _er(rng, n, 1.5)
    src = b[0]
    if shuffled:
        perm = rng.permutation(n)
        src = _forest(rng, n, ts, shallow)[np.ix_(perm, perm)]
    return u, b, _closure(src)


def _timeline(rng, size):
    a, t = (4, 14) if size == "small" else (6, 30)
    n = a + t
    u, b = _blank(n)
    u[0, :a] = True
    u[1] = rng.random(n) < 0.5
    for i in range(a, n - 1):
        b[0, i, i + 1] = True
    b[1, :a, a:] = rng.random((a, t)) < 0.3
    b[2] = _er(rng, n, 1.5)
    return a, t, u, b


def parity(rng, size):
    a, t, u, b = _timeline(rng, size)
    target = np.zeros_like(b[0])
    target[:a, a:] = (np.cumsum(b[1, :a, a:], axis=1) % 2) == 1
    return u, b, target


def temporal_local(rng, size):
    a, t, u, b = _timeline(rng, size)
    ev = b[1, :a, a:]
    target = np.zeros_like(b[0])
    target[:a, a + 1:] = ev[:, 1:] & ev[:, :-1]
    return u, b, target


def block(rng, size):
    n = 30 if size == "small" else 60
    u, b = _blank(n)
    u[0], u[1] = rng.random(n) < 0.5, rng.random(n) < 0.5
    h = rng.random(n) < 0.5
    same = h[:, None] == h[None, :]
    b[0] = rng.random((n, n)) < np.where(same, 0.3, 0.03)
    b[1] = rng.random((n, n)) < 0.2
    b[2] = _er(rng, n, 1.5)
    for m in b:
        np.fill_diagonal(m, False)
    return u, b, b[1] & same


def count(rng, size):
    n = 24 if size == "small" else 48
    u, b = _blank(n)
    u[0], u[1] = rng.random(n) < 0.5, rng.random(n) < 0.5
    deg = rng.integers(0, 7, n)
    for x in range(n):
        others = np.delete(np.arange(n), x)
        b[0, x, rng.choice(others, deg[x], replace=False)] = True
    b[1], b[2] = _er(rng, n, 1.5), _er(rng, n, 1.5)
    d = b[0].sum(1)
    return u, b, d[:, None] > d[None, :]


def compose(rng, size, depth):
    n = 24 if size == "small" else 48
    u, b = _blank(n)
    u[0], u[1] = rng.random(n) < 0.5, rng.random(n) < 0.5
    for k in range(N_BINARY):
        b[k] = _er(rng, n, 1.5)
    t = b[0]
    for k in range(1, depth):
        t = (t.astype(np.int32) @ b[k].astype(np.int32)) > 0
    return u, b, t


def noise(rng, size):
    n = 24 if size == "small" else 48
    u, b = _blank(n)
    u[0], u[1] = rng.random(n) < 0.5, rng.random(n) < 0.5
    for k in range(N_BINARY):
        b[k] = _er(rng, n, 1.5)
    return u, b, rng.random((n, n)) < 0.08


FAMILIES = {
    # hidden primitive inside the invention menu
    "closure": (lambda r, s: closure(r, s), "positive"),
    "parity": (parity, "positive"),
    "block": (block, "positive"),
    # hidden primitive outside the invention menu
    "count": (count, "out-of-menu"),
    # original ontology sufficient, or nothing to explain
    "closure_shallow": (lambda r, s: closure(r, s, shallow=True), "negative"),
    "closure_shuffled": (lambda r, s: closure(r, s, shuffled=True), "negative"),
    "temporal_local": (temporal_local, "negative"),
    "compose2": (lambda r, s: compose(r, s, 2), "negative"),
    "compose3": (lambda r, s: compose(r, s, 3), "negative"),
    "noise": (noise, "negative"),
}

# Generator-side ground truth, used only by the evaluator to label what was found.
TRUE_SOURCE = {"closure": ("TC", 0), "parity": ("FOLD", 0, 1), "block": ("BLOCK", 0)}


def make(family, rng, size):
    u, b, t = FAMILIES[family][0](rng, size)
    t = t.copy()
    np.fill_diagonal(t, False)
    return {"unary": u, "binary": b, "target": t}
