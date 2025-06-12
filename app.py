from flask import Flask
from flask_migrate import Migrate
from models import db

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
  # $export FLASK_APP = app.py 
  # $ export FLASK_RUN_PORT=8000
 


