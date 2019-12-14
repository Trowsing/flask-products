import unittest
from products.services import Filters


filters = Filters()


class ServicesTest(unittest.TestCase):
    """Tests for all services"""

    def setUp(self):
        self.product_id = 1
        self.product_name = "Kingston"

    def test_filter_product_by_id(self):
        """Check products filtering by ID"""
        products = filters.get_product_by_id(self.product_id)
        self.assertIsInstance(products, list)
        for product in products:
            self.assertEqual(product["id"], self.product_id)

    def test_filter_product_by_name(self):
        """Check products filtering by name"""
        products = filters.get_product_by_name(self.product_name)
        self.assertIsInstance(products, list)
        for product in products:
            self.assertIn(self.product_name, product["nome"])

    def test_filter_all_products(self):
        """Test all products filter"""
        products = filters.get_all_products()
        self.assertIsInstance(products, list)
        self.assertTrue(len(products) == 3)

    def test_filter_product_by_min_price(self):
        """Check filter by minimum price"""
        min_price = 600
        products = filters.get_products_by_price(min_price=min_price)
        self.assertIsInstance(products, list)
        for product in products:
            self.assertTrue(product["preco"] >= min_price)

    def test_filter_product_by_max_price(self):
        """Check filter by maximum price"""
        max_price = 800
        products = filters.get_products_by_price(max_price=max_price)
        self.assertIsInstance(products, list)
        for product in products:
            self.assertTrue(product["preco"] <= max_price)

    def test_filter_product_by_min_and_max_price(self):
        """Check filter in a price range"""
        min_price = 150
        max_price = 200
        products = filters.get_products_by_price(
            min_price=min_price, max_price=max_price
        )
        self.assertIsInstance(products, list)
        for product in products:
            self.assertTrue(product["preco"] <= max_price)
            self.assertTrue(product["preco"] >= min_price)


if __name__ == "__main__":
    unittest.main()
