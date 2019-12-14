import unittest
import tinydb
from products.database import connection


class DatabaseTest(unittest.TestCase):
    """Tests for all database operations"""

    def setUp(self):
        self.database = connection.Database()

    def test_tinydb_table(self):
        """Check if products table exists"""
        products = self.database.products
        self.assertIsInstance(products, tinydb.database.Table)

    def test_db_attribute_is_private(self):
        """Check if self.__db attribute is private"""
        database = self.database
        with self.assertRaises(AttributeError):
            database.__db

    def test_products_listing(self):
        """Check all stored products"""
        products = self.database.products
        self.assertIsInstance(products.all(), list)
        self.assertEqual(len(products), 3)


if __name__ == "__main__":
    unittest.main()
