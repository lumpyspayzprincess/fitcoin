# Import libraries



#  Import files that I made
from app import db
from models.base import BaseModel
#! may need to remove the import below 

from models.workout_exercise import WorkoutExerciseModel

# create ExerciseModel that extends from Base and SQL class

class ExerciseModel(db.Model, BaseModel):
  __tablename__ = "exercises"

  ## id comes from the BaseModel
  #! id is a foreign key in the workouts table 
  name = db.Column(db.Text, nullable=False)
  #! target_area is relational so need to replace later
  target_area_id = db.Column(db.Integer, db.ForeignKey('target_areas.id'), nullable=False)
  ## here's where I establish the relationship that workkouts have with exercises
  ## `tablename = db.relationship('TableItemModel', backpopulates='table name', cascade=all, delete*)`
  ## cascade decides what happens if my workout if the parent (exercise) is affected)
  ## ref https://docs.sqlalchemy.org/en/20/orm/cascades.html 
  #! struggled to get workout to link to exercises
    #! `When initializing mapper Mapper[ExerciseModel(exercises)], expression 'WorkoutModel' 
    #! failed to locate a name ('WorkoutModel'). If this is a class name, consider adding
    #! this relationship() to the <class 'models.exercise.ExerciseModel'> class after both
    #! dependent classes have been defined.` 
    #* sorted by importing workoutmodel here
  
  #! might need to add another table connecting workouts to exercises, but will leave to the end
  ## workouts = db.relationship('WorkoutModel', backref='workouts', cascade='all, delete')

  # relationship to exercises
  workouts = db.Relationship("WorkoutExerciseModel", back_populates="exercise")