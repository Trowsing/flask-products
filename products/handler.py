from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from db import Database
from tinydb import Query

app = Flask(__name__)
api = Api(app)


parser = reqparse.RequestParser()
parser.add_argument("product")


class Product(Resource):
    def get(self, product_id):
        products = Database().products
        product = products.search(Query().id == product_id)
        return product


class ProductsList(Resource):
    def get(self):
        products = Database().products
        return products.all()


api.add_resource(ProductsList, "/products")
api.add_resource(Product, "/products/<product_id>")


if __name__ == "__main__":
    app.run(debug=True)
