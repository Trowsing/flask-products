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
    filtered = products.search(product.name.matches(name, flags=re.IGNORECASE))
    return filtered


def get_all_products():
    products = Database().products
    return products.all()
