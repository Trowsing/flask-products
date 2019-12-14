from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from services import Filters


app = Flask(__name__)
api = Api(app)
filters = Filters()


parser = reqparse.RequestParser()
parser.add_argument("name", type=str)
parser.add_argument("min", type=int)
parser.add_argument("max", type=int)


class Product(Resource):
    def get(self, product_id):
        """Get a product by its ID.
        
        Args:
            product_id (int): product ID

        Returns:
            product (list): product matching query
        """
        product = filters.get_product_by_id(product_id)
        return product


class ProductsList(Resource):
    def get(self):
        """Get a list of all products.
        
        Returns:
            products (list): all stored products
        """
        products = filters.get_all_products()
        return products


class ProductNameFilter(Resource):
    def get(self):
        """Get all products matching a name.
        
        Args:
            name (str): product name or part of it

        Returns:
            products (list): all products matching the name
        """
        name = parser.parse_args().get("name")
        if not name:
            return "Invalid filter value", 400
        products = filters.get_product_by_name(name)
        return products


class ProductPriceFilter(Resource):
    def get(self):
        """Get all products on a price range. At least one value is required.
        
        Args:
            min (int): minimum desired price
            max (int): maximum desired price

        Returns:
            products (list): all products mathing the price range or value
        """
        args = parser.parse_args()
        min_price = args.get("min")
        max_price = args.get("max")
        if not min_price and not max_price:
            return "Must provide at least one value", 400
        products = filters.get_products_by_price(min_price, max_price)
        return products


api.add_resource(ProductPriceFilter, "/products/filter/price")
api.add_resource(ProductNameFilter, "/products/filter")
api.add_resource(ProductsList, "/products")
api.add_resource(Product, "/products/<int:product_id>")


if __name__ == "__main__":
    app.run(debug=True)
