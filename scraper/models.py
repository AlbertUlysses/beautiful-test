#!/usr/bin/env python3
"""
Author : Albert Ulysses <albertulysseschavez@gmail.com>
Purpose: Data Models
"""
from collections import namedtuple

Product = namedtuple('Product', [
    'upc',
    'product_type',
    'price',
    'tax',
    'availability'
    ])
