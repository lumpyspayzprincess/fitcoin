# Import installed libraries
  ## serialising involves marshmallow taking in complicated python objects
  ## and simplifying it to javascript opjects (json) that the web can read 
from app import ma

# imports from files/directories that I made
from models.exercise import ExerciseModel

# create serialiser (called schema in docs): python -> SQLA -> JSON
  ## https://marshmallow-sqlalchemy.readthedocs.io/en/latest/ 
class ExerciseSchema(ma.SQLAlchemyAutoSchema):

  class Meta:
    model = ExerciseModel
      ## below means that the model is returned when we deserialised
    load_instance = True