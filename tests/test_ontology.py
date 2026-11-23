import numpy as np

from experiments.ontology import discover as D
from experiments.ontology import worlds as W


def test_tc_and_fold_operators():
    r = np.zeros((4, 4), bool)
    r[0, 1] = r[1, 2] = r[2, 3] = True
    assert D.op_tc(r).sum() == 6 and D.is_chain(r) and not D.is_chain(r | r.T)
    e = np.zeros((4, 4), bool)
    e[0, [0, 2]] = True
    assert D.op_fold(r, e, (0, 1, 1, 0))[0].tolist() == [True, True, False, False]


def test_discovery_finds_closure_and_rejects_noise():
    rng = np.random.default_rng(0)
    th, acc, _ = D.discover([W.make("closure", rng, "small") for _ in range(16)])
    assert acc and acc[0][0] == "TC"
    _, acc, _ = D.discover([W.make("noise", rng, "small") for _ in range(16)])
    assert acc == []
