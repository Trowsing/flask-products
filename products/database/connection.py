import os
from tinydb import TinyDB


class Database:
    """
    TinyDB connection bootstrapper.

    Attributes:
        products (list): list of stored products.
    """

    def __init__(self):
        self.__db_dir = os.path.dirname(os.path.abspath(__file__))
        self.__db = TinyDB(f"{self.__db_dir}/products.json")
        self.products = self.__db.table("products")
