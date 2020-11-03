#!/usr/bin/env python3
"""Test for scrapescript.py"""

import os
from clean import Clean
from subprocess import getstatusoutput, getoutput

prg = './clean.py'


# -------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# -------------------------------------------------
def test_price():
    """£51.77 -> 51.77 type float"""

    c = Clean()

    res = c.value('<td>£51.77</td>')
    assert res == float('51.77')
