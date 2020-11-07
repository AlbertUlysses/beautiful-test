#!/usr/bin/env python3
"""
Author : Albert Ulysses <albertulysseschavez@gmail.com>
Purpose: Holds cleaning functions
"""
import re


def monetary(value_field):
    """Returns a float for items that are values"""
    amount = re.sub('[^0-9.]', '', value_field)
    return float(amount)


def wholenumber(value_field):
    """Returns an intger datetype from a string"""
    value = re.sub('[^0-9]', '', value_field)
    return int(value)
