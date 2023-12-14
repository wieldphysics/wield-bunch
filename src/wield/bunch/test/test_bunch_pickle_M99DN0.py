"""
Test of capturing a bunch into a pickle
"""
import numpy as np

from wield.bunch import Bunch

import pickle as pkl

import pytest  # noqa
from wield.pytest.fixtures import (  # noqa
    tjoin,
    fjoin,
    dprint
)


def test_bunch_pickle():
    b = Bunch(
        A=1,
        B=2,
    )
    sb = pkl.dumps(b)
    b2 = pkl.loads(sb)

    assert (b == b2)
