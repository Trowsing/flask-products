from tinydb import TinyDB


class Database:
    def __init__(self):
        self.db = TinyDB("products/database/products.json")
        self.products = self.db.table("products")
