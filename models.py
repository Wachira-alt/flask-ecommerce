from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from datetime import datetime
from sqlalchemy_serializer import SerializerMixin

# create the metadata instance
# metadata holds the information about our table definations, foreign-keys, columns, etc
metadata = MetaData()

#create the flask-sqlalchemy db instance
db = SQLAlchemy(metadata = metadata)

class Customer(db.Model, SerializerMixin):
    __tablename__ = 'customers'

    # table columns
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)
    age = db.Column(db.String, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    

#products
#orders
#order-item


