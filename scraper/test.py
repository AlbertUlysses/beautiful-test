#!/usr/bin/env python3
"""Test for scrapescript.py"""

import os
import clean as cl

prg = './clean.py'


# -------------------------------------------------
def test_exists():
    """checks if the file exist"""

    assert os.path.isfile(prg)


# -------------------------------------------------
def test_price():
    """£51.77 -> 51.77 type float"""

    res = cl.monetary('£51.77')
    assert res == float(51.77)


# -------------------------------------------------
def test_integer():
    """'in stock (22 available)' -> 22"""

    res = cl.wholenumber('in stock (22 available)')
    assert res == int(22)
