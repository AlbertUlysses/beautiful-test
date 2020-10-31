#!/usr/bin/env python3
"""Test for scrapescript.py"""

import os
from subprocess import getstatusoutput, getoutput

prg = './scrapescript.py'


# -------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# -------------------------------------------------
