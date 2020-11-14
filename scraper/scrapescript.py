#!/usr/bin/env python3
"""
Author : Albert Ulysses <albertulysseschavez@gmail.com>
Purpose: Scrape data from books.toscrape.com
"""
import requests
from bs4 import BeautifulSoup
import clean as cl
import models


def main():
    """Main function"""
    page = requests.get('https://books.toscrape.com/catalogue/'
                        'a-light-in-the-attic_1000/index.html')
    soup = BeautifulSoup(page.content, 'html.parser')
    upc = soup.select('tr:nth-child(1) > td:nth-child(2)')[0].get_text()
    product_type = soup.select('tr:nth-child(2) > td:nth-child(2)')[0].get_text()
    price = soup.select('tr:nth-child(3) > td:nth-child(2)')[0].get_text()
    tax = soup.select('tr:nth-child(5) > td:nth-child(2)')[0].get_text()
    availability = soup.select('tr:nth-child(6) > td:nth-child(2)')[0].get_text()

    print(models.Product(upc=upc, product_type=product_type,
                         price=cl.monetary(price),
                         tax=cl.monetary(tax),
                         availability=cl.wholenumber(availability))._asdict())


if __name__ == '__main__':
    main()
