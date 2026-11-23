"""Discovery system: MDL rule learning over a restricted vocabulary, plus
invention of new relational primitives from a fixed menu of generic operators.

Input worlds are anonymous: {"unary": (U, n) bool, "binary": (B, n, n) bool,
"target": (n, n) bool}. Nothing here knows which family a world came from.

Vocabulary L0: rules T(x,y) <- l1 & ... & lk (k <= max_len), where a literal is
a chain R1∘R2∘...∘Rd(x,y) (each Ri a base relation or its converse, d <= depth),
a negated single relation, or a unary predicate (or its negation) on x or y.
A theory is a disjunction of up to max_rules rules.
"""
from itertools import product
from math import lgamma, log, log2

import numpy as np

LN2 = log(2)
MAX_RULES, MAX_LEN = 8, 3
TABLES = list(product((0, 1), repeat=4))  # (d00, d01, d10, d11): next state for (state, input)


# ---------------------------------------------------------------- operators

def _mm(a, b):
    return (a.astype(np.int32) @ b.astype(np.int32)) > 0


def op_tc(r):
    c = r.copy()
    while True:
        nxt = c | _mm(c, c)
        if (nxt == c).all():
            return c
        c = nxt


def is_chain(o):
    if not o.any() or (o.sum(0) > 1).any() or (o.sum(1) > 1).any():
        return False
    return not (op_tc(o).diagonal()).any()


def op_fold(o, e, table):
    """2-state automaton run along each o-chain, reading e(a, t) for every entity a."""
    n = o.shape[0]
    nxt = np.full(n, -1)
    src, dst = np.nonzero(o)
    nxt[src] = dst
    heads = np.setdiff1d(np.arange(n), dst)
    out = np.zeros((n, n), bool)
    state = np.zeros(n, np.int8)
    d = np.array(table, np.int8).reshape(2, 2)
    for h in heads:
        state[:] = 0
        t = h
        while t >= 0:
            state = d[state, e[:, t].astype(np.int8)]
            out[:, t] = state == 1
            t = nxt[t]
    return out


def op_block(r):
    s = (r | r.T).astype(float)
    k = s.sum(1)
    m = k.sum()
    if m == 0:
        return np.zeros_like(r)
    mod = s - np.outer(k, k) / m
    w, v = np.linalg.eigh(mod)
    g = v[:, -1] >= 0
    out = g[:, None] == g[None, :]
    np.fill_diagonal(out, False)
    return out


def base_dirs(world):
    b = world["binary"]
    return [m for k in range(b.shape[0]) for m in (b[k], b[k].T)]


def invent(world, spec):
    d = base_dirs(world)
    op = spec[0]
    if op == "TC":
        return op_tc(d[spec[1]])
    if op == "FOLD":
        return op_fold(d[spec[1]], d[spec[2]], spec[3])
    if op == "BLOCK":
        return op_block(world["binary"][spec[1]])
    if op == "CONJ":
        return _mm(d[spec[1]], d[spec[2]])
    raise ValueError(op)


def spec_cost(spec, n_by_op):
    bits = log2(4) + log2(max(n_by_op[spec[0]], 1))
    return bits + (4 if spec[0] == "FOLD" else 0)


# ---------------------------------------------------------------- vocabulary

def atoms(world, inventions, cache):
    key = id(world)
    if key not in cache:
        cache[key] = {}
    c = cache[key]
    out = base_dirs(world)
    for spec in inventions:
        if spec not in c:
            c[spec] = invent(world, spec)
        out += [c[spec], c[spec].T]
    return out


def lit_matrix(lit, world, inv, cache):
    a = atoms(world, inv, cache)
    kind = lit[0]
    n = world["target"].shape[0]
    if kind == "chain":
        m = a[lit[1][0]]
        for i in lit[1][1:]:
            m = _mm(m, a[i])
        return m
    if kind == "neg":
        return ~a[lit[1]]
    if kind in ("ux", "uy"):
        v = world["unary"][lit[1]]
        if not lit[2]:
            v = ~v
        return np.repeat(v[:, None], n, 1) if kind == "ux" else np.repeat(v[None, :], n, 0)
    raise ValueError(kind)


def offdiag(n):
    return ~np.eye(n, dtype=bool)


def flat(m):
    return m[offdiag(m.shape[0])]


def enumerate_literals(worlds, inv, depth, cache, extra_chains=()):
    """Chains up to `depth` over all atoms, deduplicated by extension on `worlds`."""
    n_atoms = len(atoms(worlds[0], inv, cache))
    lits, cols, seen = [], [], set()

    def add(lit, col):
        h = col.tobytes()
        if h in seen or not col.any() or col.all():
            return False
        seen.add(h)
        lits.append(lit)
        cols.append(col)
        return True

    # Prefixes are deduplicated on full matrices (including the diagonal): a prefix that is empty or
    # redundant off-diagonal can still extend to a new chain.
    frontier, seen_full = [], set()

    def extend(chain, mats):
        add(("chain", chain), np.concatenate([flat(m) for m in mats]))
        h = b"".join(m.tobytes() for m in mats)
        if h in seen_full or not any(m.any() for m in mats):
            return
        seen_full.add(h)
        nxt.append((chain, mats))

    per_world = [atoms(w, inv, cache) for w in worlds]
    nxt = []
    for i in range(n_atoms):
        extend((i,), [pw[i] for pw in per_world])
    frontier = nxt
    for _ in range(depth - 1):
        nxt = []
        for chain, mats in frontier:
            for i in range(n_atoms):
                extend(chain + (i,), [_mm(m, pw[i]) for m, pw in zip(mats, per_world)])
        frontier = nxt
    for chain in extra_chains:
        lit = ("chain", chain)
        add(lit, np.concatenate([flat(lit_matrix(lit, w, inv, cache)) for w in worlds]))
    for i in range(n_atoms):
        lit = ("neg", i)
        add(lit, np.concatenate([flat(lit_matrix(lit, w, inv, cache)) for w in worlds]))
    for k in range(worlds[0]["unary"].shape[0]):
        for kind in ("ux", "uy"):
            for sign in (True, False):
                lit = (kind, k, sign)
                add(lit, np.concatenate([flat(lit_matrix(lit, w, inv, cache)) for w in worlds]))
    return lits, np.stack(cols, 1)


# ---------------------------------------------------------------- MDL

def log2comb(n, k):
    n = np.asarray(n, float)
    k = np.asarray(k, float)
    from scipy.special import gammaln
    return (gammaln(n + 1) - gammaln(k + 1) - gammaln(n - k + 1)) / LN2


def data_dl(p, fp, m, fn):
    return np.log2(np.asarray(p, float) + 1) + log2comb(p, fp) + np.log2(np.asarray(m, float) + 1) + log2comb(m, fn)


def theory_dl(rule_lens, n_lits):
    return log2(MAX_RULES + 1) + sum(log2(MAX_LEN) + k * log2(n_lits) for k in rule_lens)


def learn(F, y, max_rules=MAX_RULES, max_len=MAX_LEN):
    """Greedy sequential covering minimising L(H) + L(D|H). Returns list of column-index rules."""
    tot, ypos = len(y), int(y.sum())
    n_lits = F.shape[1]
    pred = np.zeros(tot, bool)
    rules = []
    cur = float(data_dl(0, 0, tot, ypos)) + theory_dl([], n_lits)
    for _ in range(max_rules):
        p0, tp0 = int(pred.sum()), int((pred & y).sum())
        cov = ~pred
        rule, best, best_dl = [], None, cur
        for _ in range(max_len):
            if not cov.any():
                break
            sub = F[cov]
            add_p = sub.sum(0)
            add_tp = sub[y[cov]].sum(0)
            p, tp = p0 + add_p, tp0 + add_tp
            dl = data_dl(p, p - tp, tot - p, ypos - tp) + theory_dl([len(r) for r in rules] + [len(rule) + 1], n_lits)
            dl[2 * add_tp < add_p] = np.inf  # a rule must assert positives (precision >= 1/2)
            if rule:
                dl[rule] = np.inf
            if np.isfinite(dl).any():
                j = int(np.argmin(dl))
            else:  # no admissible rule yet: specialise by FOIL gain
                prec0 = (y[cov].sum() + 1) / (cov.sum() + 2)
                gain = add_tp * (np.log2((add_tp + 1) / (add_p + 2)) - np.log2(prec0))
                gain[add_tp == 0] = -np.inf
                if rule:
                    gain[rule] = -np.inf
                j = int(np.argmax(gain))
                if not np.isfinite(gain[j]):
                    break
            if dl[j] < best_dl - 1e-9:
                best, best_dl = rule + [j], float(dl[j])
            rule = rule + [j]
            cov = cov & F[:, j]
        if best is None:
            break
        rules.append(best)
        pred |= F[:, best].all(1)
        cur = best_dl
    return rules, cur


class Theory:
    def __init__(self, rules, lits, inv, n_lits):
        self.rules = [[lits[j] for j in r] for r in rules]
        self.inv = list(inv)
        self.n_lits = n_lits

    def predict(self, world, cache):
        n = world["target"].shape[0]
        out = np.zeros((n, n), bool)
        for r in self.rules:
            m = np.ones((n, n), bool)
            for lit in r:
                m &= lit_matrix(lit, world, self.inv, cache)
            out |= m
        np.fill_diagonal(out, False)
        return out

    def hdl(self):
        return theory_dl([len(r) for r in self.rules], self.n_lits)

    def describe(self):
        return " | ".join(" & ".join(fmt_lit(l) for l in r) for r in self.rules) or "FALSE"


def fmt_lit(lit):
    if lit[0] == "chain":
        return "∘".join(f"a{i}" for i in lit[1])
    if lit[0] == "neg":
        return f"¬a{lit[1]}"
    return f"{'' if lit[2] else '¬'}u{lit[1]}({'x' if lit[0] == 'ux' else 'y'})"


def eval_dl(theory, worlds, cache):
    tot = p = tp = ypos = 0
    for w in worlds:
        pr, y = flat(theory.predict(w, cache)), flat(w["target"])
        tot += len(y); p += pr.sum(); tp += (pr & y).sum(); ypos += y.sum()
    return float(data_dl(p, p - tp, tot - p, ypos - tp))


def fit(worlds, inv, depth, cache, extra=()):
    lits, F = enumerate_literals(worlds, inv, depth, cache, extra)
    y = np.concatenate([flat(w["target"]) for w in worlds])
    rules, dl = learn(F, y)
    return Theory(rules, lits, inv, len(lits)), dl


def inv_extra_chains(inv, n_base):
    """Depth-2 compositions of each invented atom with every atom (generic, not task-specific)."""
    n_atoms = n_base + 2 * len(inv)
    out = []
    for k in range(len(inv)):
        for a in (n_base + 2 * k, n_base + 2 * k + 1):
            for b in range(n_atoms):
                out += [(a, b), (b, a)]
    return out


# ---------------------------------------------------------------- invention search

def candidates(worlds, ops=("TC", "FOLD", "BLOCK", "CONJ")):
    n_dirs = 2 * worlds[0]["binary"].shape[0]
    n_rel = worlds[0]["binary"].shape[0]
    specs = [("TC", d) for d in range(n_dirs)]
    chains = [d for d in range(n_dirs) if all(is_chain(base_dirs(w)[d]) for w in worlds)]
    specs += [("FOLD", o, e, t) for o in chains for e in range(n_dirs) for t in TABLES]
    specs += [("BLOCK", k) for k in range(n_rel)]
    specs += [("CONJ", a, b) for a in range(n_dirs) for b in range(n_dirs)]
    specs = [sp for sp in specs if sp[0] in ops]
    n_by_op = {"TC": n_dirs, "FOLD": max(len(chains), 1) * n_dirs * len(TABLES), "BLOCK": n_rel, "CONJ": n_dirs ** 2}
    return specs, n_by_op


def discover(train, depth=3, max_inv=2, top=6, ops=("TC", "FOLD", "BLOCK", "CONJ")):
    """Select inventions by validation description length on a split of the training worlds."""
    cache = {}
    half = len(train) // 2
    fitw, valw = train[:half], train[half:]
    n_base = 2 * train[0]["binary"].shape[0]
    specs, n_by_op = candidates(fitw, ops)
    accepted, trace = [], []
    th, _ = fit(fitw, accepted, depth, cache)
    best_val = eval_dl(th, valw, cache) + th.hdl()
    trace.append({"step": 0, "val_dl": best_val, "theory": th.describe()})
    for _ in range(max_inv):
        lits, F = enumerate_literals(fitw, accepted, depth, cache, inv_extra_chains(accepted, n_base))
        y = np.concatenate([flat(w["target"]) for w in fitw])
        known = {F[:, j].tobytes() for j in range(F.shape[1])}
        pred = np.zeros(len(y), bool)
        for r in th.rules:
            pred |= np.all([np.concatenate([flat(lit_matrix(l, w, accepted, cache)) for w in fitw]) for l in r], 0)
        scored, seen = [], set()
        tot, ypos = len(y), int(y.sum())
        for spec in specs:
            if spec in accepted:
                continue
            cols = [np.concatenate([flat(m) for m in mats]) for mats in
                    zip(*[(invent(w, spec), invent(w, spec).T) for w in fitw])]
            h = cols[0].tobytes()
            if h in seen or not cols[0].any() or cols[0].all() or h in known:
                continue
            seen.add(h)
            best = np.inf
            for c, base in product(cols, (pred, np.zeros_like(pred))):
                cov = c & ~base
                sub = F[cov]
                p = base.sum() + np.concatenate([[cov.sum()], sub.sum(0)])
                tp = (base & y).sum() + np.concatenate([[(cov & y).sum()], sub[y[cov]].sum(0)])
                dl = data_dl(p, p - tp, tot - p, ypos - tp)
                dl[2 * (tp - (base & y).sum()) < p - base.sum()] = np.inf
                best = min(best, float(np.min(dl)))
            scored.append((best, spec))
        scored.sort(key=lambda s: s[0])
        round_best = None
        for _, spec in scored[:top]:
            inv = accepted + [spec]
            cand_th, _ = fit(fitw, inv, depth, cache, inv_extra_chains(inv, n_base))
            v = eval_dl(cand_th, valw, cache) + cand_th.hdl() + sum(spec_cost(s, n_by_op) for s in inv)
            trace.append({"candidate": spec, "val_dl": v, "theory": cand_th.describe()})
            if round_best is None or v < round_best[0]:
                round_best = (v, spec, cand_th)
        base_cost = best_val + sum(spec_cost(s, n_by_op) for s in accepted)
        if round_best is None or round_best[0] >= base_cost:
            break
        accepted.append(round_best[1])
        th = round_best[2]
        best_val = round_best[0] - sum(spec_cost(s, n_by_op) for s in accepted)
    final, _ = fit(train, accepted, depth, cache, inv_extra_chains(accepted, n_base))
    return final, accepted, trace
