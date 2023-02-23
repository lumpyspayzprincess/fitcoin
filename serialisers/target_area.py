# Import installed libraries
  ## serialising involves marshmallow taking in complicated python objects
  ## and simplifying it to javascript opjects (json) that the web can read 
from app import ma


# imports from files/directories that I made
from models.target_area import TargetAreaModel

# create serialiser (called schema in docs): python -> SQLA -> JSON
  ## https://marshmallow-sqlalchemy.readthedocs.io/en/latest/ 
class TargetAreaSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = TargetAreaModel
      ## below means that the model is returned when we deserialised
    load_instance = True