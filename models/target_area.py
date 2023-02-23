# Import libraries



#  Import files that I made
from app import db
from models.base import BaseModel

# Import child Models needed for creating relationships
from models.exercise import ExerciseModel

# create ExerciseModel that extends from Base and SQL class

class TargetAreaModel(db.Model, BaseModel):
  __tablename__ = "target_areas"

  ## id comes from the BaseModel
    ## target area is the parent of exercises, since it needs to be created first 
  name = db.Column(db.Text, nullable=False)

  #! might have to use backref here since it's a one to many relationship
  ## if a target area is deleted, the related exercises will also be deleted 
  exercises = db.relationship('ExerciseModel', backref='exercises', cascade='all, delete')
  # users = db.relationship('UserModel', backref='users', cascade='all,delete')