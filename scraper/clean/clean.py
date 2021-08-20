"""
Purpose: Cleans dirty digits.

Author : Albert Ulysses <albertulysseschavez@gmail.com>
"""
import re


def monetary(value_field):
    """
    Returns a float for items that are values.

    :param value_field: A monetary value.

    """
    return float(re.sub('[^0-9.]', '', value_field))


def wholenumber(value_field):
    """
    Returns an intger datetype from a string.

    :param value_field: A string we want to convert to int.
    """
    return int(re.sub('[^0-9]', '', value_field))
