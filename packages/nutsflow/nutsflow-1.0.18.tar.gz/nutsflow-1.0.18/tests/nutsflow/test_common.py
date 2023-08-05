"""
.. module:: test_common
   :synopsis: Unit tests for common module
"""

from __future__ import print_function

from time import sleep
from nutsflow.common import (sec_to_hms, timestr, Redirect, as_tuple, as_set,
                             as_list, console, StableRandom)


def test_as_tuple():
    assert as_tuple(1) == (1,)
    assert as_tuple((1, 2)) == (1, 2)
    assert as_tuple([1, 2]) == (1, 2)


def test_as_list():
    assert as_list(1) == [1]
    assert as_list((1, 2)) == [1, 2]
    assert as_list([1, 2]) == [1, 2]


def test_as_set():
    assert as_set(1) == (1,)
    assert as_set((1, 2)) == {1, 2}
    assert as_set([1, 2]) == {1, 2}


def test_sec_to_hms():
    assert sec_to_hms('80') == (0, 1, 20)
    assert sec_to_hms(3 * 60 * 60 + 2 * 60 + 1) == (3, 2, 1)


def test_timestr():
    assert timestr('') == ''
    assert timestr('80') == '0:01:20'


def test_output():
    with Redirect() as out:
        console('test')
    assert out.getvalue() == 'test\n'


def test_Redirect():
    with Redirect() as out:
        print('test')
    assert out.getvalue() == 'test\n'


def test_StableRandom():
    rnd = StableRandom()
    assert max(rnd._next_rand() for _ in range(1000)) < 1.0
    assert min(rnd._next_rand() for _ in range(1000)) >= 0.0

    rnd1, rnd2 = StableRandom(0), StableRandom(0)
    for _ in range(100):
        assert rnd1.gauss_next() == rnd2.gauss_next()

    rnd1, rnd2 = StableRandom(0), StableRandom(0)
    rnd2.jumpahead(10)
    for _ in range(100):
        assert rnd1.gauss_next() != rnd2.gauss_next()
    rnd2.setstate(rnd1.getstate())
    for _ in range(100):
        assert rnd1.gauss_next() == rnd2.gauss_next()

    rnd1, rnd2 = StableRandom(0), StableRandom(1)
    for _ in range(100):
        assert rnd1.gauss_next() != rnd2.gauss_next()

    rnd1 = StableRandom()
    sleep(0.5)  # seed is based on system time.
    rnd2 = StableRandom()
    for _ in range(100):
        assert rnd1.gauss_next() != rnd2.gauss_next()
