from collections.abc import Mapping
from wield.bunch import Bunch, DeepBunch, walk
from wield.bunch.hdf_deep_bunch import HDFDeepBunch
from wield.pytest import tpath_join, dprint
from wield.utilities.file_io import load, save


def test_bunch(dprint):
    b = Bunch()
    b.a = 1
    b.c = 2
    b.b = Bunch(z=1, x=Bunch(y=12, k=23), y=dict(a=1, b=80))
    dprint(b)
    for k, v in b.walk():
        dprint(k, v)


def test_deepbunch(dprint):
    b = DeepBunch()
    b.a = 1
    b.c = 2
    b.b.z = 1
    b.b.y = dict(a=1, b=80)
    b.b.x.y = 12
    b.b.x.k = 23
    dprint(b)
    for k, v in b.walk():
        dprint(k, v)


def test_hdfdeepbunch(tpath_join, dprint):
    b = DeepBunch()
    b.a = 1
    b.c = 2
    b.b.z = 1
    b.b.y = dict(a=1, b=80)
    b.b.x.y = 12
    b.b.x.k = 23
    dprint(b)
    for k, v in b.walk():
        dprint(k, v)
    save(tpath_join('data.h5'), b)
    b2 = load(tpath_join('data.h5'))
    dprint(b2)
    for k, v, in b2.walk():
        dprint(k, v)


def test_dict(dprint):
    b = dict(a=1, c=2)
    b['b'] = dict(z=1, x=dict(y=12, k=23), y=dict(a=1, b=80))
    dprint(b)
    for k, v in walk(b):
        dprint(k, v)
