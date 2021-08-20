"""
Purpose: Scrape data from books.toscrape.com.

Author : Albert Ulysses <albertulysseschavez@gmail.com>
"""
import requests
from bs4 import BeautifulSoup
from clean.clean import monetary, wholenumber
from clean.models import Product

ADDRESS = """
          https://books.toscrape.com/catalogue/
          a-light-in-the-attic_1000/index.html
          """


def main():
    """Main function."""
    page = requests.get(ADDRESS)
    soup = BeautifulSoup(page.content, 'html.parser')
    upc = soup.select('tr:nth-child(1) > td:nth-child(2)')[0].get_text()
    product_type = soup.select(
        'tr:nth-child(2) > td:nth-child(2)',
    )[0].get_text()
    price = soup.select('tr:nth-child(3) > td:nth-child(2)')[0].get_text()
    tax = soup.select(
        'tr:nth-child(5) > td:nth-child(2)',
    )[0].get_text()
    availability = soup.select(
        'tr:nth-child(6) > td:nth-child(2)',
    )[0].get_text()

    return Product(
        upc=upc,
        product_type=product_type,
        price=monetary(price),
        tax=monetary(tax),
        availability=wholenumber(availability),
    )._asdict()


if __name__ == '__main__':
    main()
