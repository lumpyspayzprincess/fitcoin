# Import libraries



#  Import files that I made
from app import db
from models.base import BaseModel

from models.workout import WorkoutModel




# create WorkoutExerciseModel that extends from Base and SQL class
class WorkoutExerciseModel(db.Model, BaseModel):
  __tablename__ = "workouts_exercises"

  # id comes from base model
  workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'), nullable=False)
  exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'), nullable=False)

  ## relationships with both workouts and exercises are added here
    #! parent1 = db.Relationship("Parent1Model", backpopulates="parent2 tablename")
    #! parent2 = db.Relationship("Parent2Model", backpopulates="parent1 tablename")
  workout = db.Relationship("WorkoutModel", back_populates="exercises")
  exercise = db.Relationship("ExerciseModel", back_populates="workouts")
