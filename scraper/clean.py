#!/usr/bin/env python3
"""
Author : Albert Ulysses <albertulysseschavez@gmail.com>
Purpose: Holds cleaning functions
"""
import re


def value(value_field):
    """Returns a float for items that are values"""
    amount = re.sub('[^0-9.]', '', value_field)
    amount = float(amount)
    return amount
