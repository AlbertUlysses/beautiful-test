"""Test for scrapescript.py."""
from clean.clean import monetary, wholenumber


# -------------------------------------------------
def test_price():
    """£51.77 -> 51.77 type float."""
    solution = 51.77
    assert monetary('£51.77') == solution


# -------------------------------------------------
def test_integer():
    """'in stock (22 available)' -> 22."""
    solution = 22
    assert wholenumber('in stock (22 available)') == solution
