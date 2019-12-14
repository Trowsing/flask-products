import unittest
from products import handler


class ApiTest(unittest.TestCase):
    """Tests for all available endpoints"""

    def setUp(self):
        handler.app.config["TESTING"] = True
        self.client = handler.app.test_client()

    def test_product_endpoint(self):
        """Check individual product listing"""
        response = self.client.get("/products/1")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)
        self.assertEqual(len(response.json), 1)

    def test_products_list(self):
        """Check all products listing"""
        response = self.client.get("/products")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)
        self.assertEqual(len(response.json), 3)

    def test_product_filtering_by_name(self):
        """Filter products by name"""
        query_params = {"name": "SSD"}
        response = self.client.get("products/filter", data=query_params)
        self.assertEqual(response.status_code, 200)
        for product in response.json:
            self.assertIn(query_params["name"], product["nome"])

    def test_wrong_product_filtering_by_name(self):
        """Filter products by inexistent parameter"""
        query_params = {"random_key": "random_value"}
        response = self.client.get("products/filter", data=query_params)
        self.assertEqual(response.status_code, 400)

    def test_product_filtering_by_min_price(self):
        """Filter products starting on a price range"""
        query_params = {"min": 600}
        response = self.client.get("products/filter/price", data=query_params)
        self.assertEqual(response.status_code, 200)
        for product in response.json:
            self.assertTrue(query_params["min"] <= product["preco"])

    def test_product_filtering_by_max_price(self):
        """Filter products with a limit price"""
        query_params = {"max": 800}
        response = self.client.get("products/filter/price", data=query_params)
        self.assertEqual(response.status_code, 200)
        for product in response.json:
            self.assertTrue(query_params["max"] >= product["preco"])

    def test_product_filtering_by_min_and_max_price(self):
        """Filter products in a price range"""
        query_params = {"min": 150, "max": 200}
        response = self.client.get("products/filter/price", data=query_params)
        self.assertEqual(response.status_code, 200)
        for product in response.json:
            self.assertTrue(query_params["min"] <= product["preco"])
            self.assertTrue(query_params["max"] >= product["preco"])

    def test_wrong_product_filtering_by_min_and_max_price(self):
        """Filter products by inexistent price parameters"""
        query_params = {"not_min_value": 1, "not_max_value": 10}
        response = self.client.get("products/filter/price", data=query_params)
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
