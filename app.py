from flask import Flask, make_response
from flask_migrate import Migrate
from models import db, Customer

# create a flask application instance/ heart of the application

app = Flask(__name__)

# configure a database connection
# app.config

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///store.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


#initialize flask migrate

migrate = Migrate (app = app, db = db)

# initialize the app to use sqlalchemy database
db.init_app(app=app)

#flask cli
#inform cli about flask app and port to use
  # $ export FLASK_APP=app.py
  # $ export FLASK_RUN_PORT=5555

  #to run $ flask run --debug

  # $ flask db migrate -m "Initial migration."
  # $ flask db upgrade head
 
#CRUD OPERATIONS
# create, retreive info, update, delete


@app.get("/customers")
def get_all_customers():
    customers = Customer.query.all()

    customer_list = []
    for customer in customers:
        customer_data = {
            "id": customer.id,
            "first_name": customer.first_name,
            "last_name": customer.last_name,
            "email": customer.email,
            "phone": customer.phone,
            "gender": customer.gender,
            "age": customer.age,
            "created_at": customer.created_at.isoformat() if customer.created_at else None
        }
        customer_list.append(customer_data)

    return make_response(customer_list, 200)

@app.get("/customers/<int:id>")
def get_one_customer(id):
    customer = Customer.query.get(id)
    if customer:
        customer_data = {
            "id": customer.id,
            "first_name": customer.first_name,
            "last_name": customer.last_name,
            "email": customer.email,
            "phone": customer.phone,
            "gender": customer.gender,
            "age": customer.age,
            "created_at": customer.created_at.isoformat() if customer.created_at else None
        }
        return make_response(customer_data, 200)
    else:
        return make_response({"status" : 404, "message": "No customer found"}, 404)
        