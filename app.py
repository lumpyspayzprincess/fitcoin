# import libraries
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS


# imports from files/directories that I made
from config.environment import db_URI


# Instantiate flask
  ## we use double unders here so that flask takes the name of the file. (__name__)
  ## changes with each file that we use  
app = Flask(__name__)
CORS(app)


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
from controllers import target_areas
from controllers import users


# Register routers for each table made in the controllers above 
  ## see https://flask.palletsprojects.com/en/2.2.x/blueprints/ -> "Registering Blueprints"

app.register_blueprint(exercises.router, url_prefix='/api')
app.register_blueprint(target_areas.router, url_prefix='/api')
app.register_blueprint(users.router, url_prefix='/api')
#? is it possible to add multiple arguements to each blueprint?