"""
Purpose: Data Models.

Author : Albert Ulysses <albertulysseschavez@gmail.com>
"""
from collections import namedtuple

Product = namedtuple(
    'Product', [
        'upc',
        'product_type',
        'price',
        'tax',
        'availability',
    ],
)
