import re
from tinydb import Query
from database.connection import Database


class Filters:
    """
    Implementation of all available filters.

    Attributes:
        products (list): all stored products
        product (Query instance): filter constructor
    """

    def __init__(self):
        self.products = Database().products
        self.product = Query()

    def get_product_by_id(self, product_id):
        """Return products matching the provided ID.
        
        Args:
            product_id (int): product ID

        Returns:
            filtered (list): list containing all matching products
        """
        filtered = self.products.search(self.product.id == product_id)
        return filtered

    def get_product_by_name(self, name):
        """Return products matching the provided name.
        
        Args:
            name (str): product name

        Returns:
            filtered (list): list containing all matching products
        """
        name_filter = self.product.nome.search(name, flags=re.IGNORECASE)
        filtered = self.products.search(name_filter)
        return filtered

    def get_products_by_price(self, min_price=None, max_price=None):
        """Return products matching the given price range or value.
        
        Args:
            min_price (int): minimum price to match
            max_price (int): maximum price to match

        Returns:
            filtered (list): list containing all matching products
        """
        price = self.product.preco
        if not max_price:
            filtered = self.products.search(price >= min_price)
        elif not min_price:
            filtered = self.products.search(price <= max_price)
        else:
            filtered = self.products.search((price <= max_price) & (price >= min_price))
        return filtered

    def get_all_products(self):
        """Return all stored products"""
        return self.products.all()

