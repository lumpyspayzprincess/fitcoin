# import libraries
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


# imports from files/directories that I made
from config.environment import db_URI


# Instantiate flask
  ## we use double unders here so that flask takes the name of the file. (__name__)
  ## changes with each file that we use  
app = Flask(__name__)


# Tell SQLA where the database is
  # 2nd config line makes the linting cleaner
app.config['SQLALCHEMY_DATABASE_URI'] = db_URI
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False


# Instantiate SQLA -> for models to work, for columns to be added, for posting/deleting to work
  ## SQLA uses app above as a parameter
  ## https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/ is where I can find docs
db = SQLAlchemy(app)

# Instantiate Marshmallow
ma = Marshmallow(app)


# Import controllers
  ## nb - import entire file in the controller, not just the list that we're
  ## looking to use

from controllers import exercises

app.register_blueprint(exercises.router, url_prefix='/api')
# see https://flask.palletsprojects.com/en/2.2.x/blueprints/ -> "Registering Blueprints"