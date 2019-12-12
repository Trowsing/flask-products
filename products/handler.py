from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from services import filters

app = Flask(__name__)
api = Api(app)


parser = reqparse.RequestParser()
parser.add_argument("name")


class Product(Resource):
    def get(self, product_id):
        product = filters.get_product_by_id(product_id)
        return product


class ProductsList(Resource):
    def get(self):
        products = filters.get_all_products()
        return products


class ProductFilter(Resource):
    def get(self):
        name = parser.parse_args().get("name")
        products = filters.get_product_by_name(name)
        return products


api.add_resource(ProductFilter, "/products/filter")
api.add_resource(ProductsList, "/products")
api.add_resource(Product, "/products/<int:product_id>")


if __name__ == "__main__":
    app.run(debug=True)
