from tinydb import TinyDB


class Database:
    """
    TinyDB connection bootstrapper.

    Attributes:
        products (list): list of stored products.
    """

    def __init__(self):
        self.__db = TinyDB("products/database/products.json")
        self.products = self.__db.table("products")
