from tinydb import TinyDB


class Database:
    def __init__(self):
        self.__db = TinyDB("products/database/products.json")
        self.products = self.__db.table("products")
