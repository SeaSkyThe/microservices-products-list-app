# FLASK APP

from dataclasses import dataclass
from flask import abort
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import UniqueConstraint
from flask_migrate import Migrate
import requests

from producer import publish

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@db/main"  # Connection to the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)                                                 # Defining database variable
migrate = Migrate(app, db)                                           # Define migrations


# Creating models
@dataclass
class Product(db.Model):
    id: int 
    title: str
    image: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=False) #Autoincrement is false, so we can maintain the same ID as the Django admin app
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))

@dataclass
class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    UniqueConstraint('user_id', 'product_id', name='user_product_unique')


CORS(app)

# Main route, to show the products created in the Django app
@app.route('/api/products')
def index():
    return jsonify(Product.query.all()) # We make a query in our own database, and show the result


# Like route
@app.route('/api/products/<int:id>/like', methods=['POST'])
def like(id):
    req = requests.get('http://host.docker.internal:8000/api/user')  # We make a get request to the Django app (ATTENTION TO THE LOCALHOST IP (172.17.0.1)
    json = req.json()                                                # Get the request result

    try:
        productUser = ProductUser(user_id=json['id'], product_id=id)
        db.session.add(productUser)
        db.session.commit()

        publish('product_liked', id)
    except:
        abort(400, 'You already liked this product')

    return jsonify({ 
        'message': 'success'
    })


if __name__ == '__main__':
    db.init_app(app)
    migrate.init_app(app, db)

    app.run(debug=True, host='0.0.0.0')

