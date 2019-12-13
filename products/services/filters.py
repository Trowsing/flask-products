import re
from tinydb import Query
from database.connection import Database


def get_product_by_id(product_id):
    products = Database().products
    product = Query()
    filtered = products.search(product.id == product_id)
    return filtered


def get_product_by_name(name):
    products = Database().products
    product = Query()
    filtered = products.search(product.nome.search(name, flags=re.IGNORECASE))
    return filtered


def get_products_by_price(min_price=None, max_price=None):
    products = Database().products
    product = Query()
    if not max_price:
        filtered = products.search(product.preco >= min_price)
    elif not min_price:
        filtered = products.search(product.preco <= max_price)
    else:
        filtered = products.search(
            (product.preco <= max_price) & (product.preco >= min_price)
        )
    return filtered


def get_all_products():
    products = Database().products
    return products.all()
