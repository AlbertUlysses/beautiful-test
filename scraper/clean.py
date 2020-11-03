#!/usr/bin/env python3
"""
Author: Albert Ulysses <albertulysseschavez@gmail.com>
Purpose: Holds cleaning functions
"""
import re


class Clean():

    def value(self, amount):
        """Returns a float for items that are values"""
        amount = re.sub('[^0-9.]', '', amount)
        amount = float(amount)
        return amount
