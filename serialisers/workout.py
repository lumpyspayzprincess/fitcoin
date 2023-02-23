# Import installed libraries
from app import ma


# imports from files/directories that I made
from models.workout import WorkoutModel

# create serialiser (called schema in docs): python -> SQLA -> JSON
class WorkoutSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = WorkoutModel
    load_instance = True