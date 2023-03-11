from flask import Flask, request
from flask_migrate import Migrate
from flask_cors import CORS
from controllers.products_controller import ProductsController
from controllers.categories_controller import CategoriesController
from db import db

app = Flask(__name__)
cors = CORS(app)

# app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///project.db"

# Si se quiere usar Mysql instalar: pip install mysqlclient
# app.config["SQLALCHEMY_DATABASE_URI"]= "mysql://username:password@localhost/db_name"

# Si se quiere usar Postgress instalar: pip install psycopg2-binary 
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost/db_name"

db.init_app(app)
migrate = Migrate(app, db)

@app.route("/")
def index():
    return "Hello world! 😁"

@app.route("/products/list")
def allProducts():
    controller = ProductsController()
    return controller.list()

@app.route("/products/create", methods=['POST'])
def createProducts():
    controller = ProductsController()
    return controller.create(request.json)

@app.route("/categories/list")
def allCategories():
    controller = CategoriesController()
    return controller.list()

@app.route("/categories/create", methods=['POST'])
def createCategories():
    controller = CategoriesController()
    return controller.create(request.json)

app.run(debug=True, port=5001)