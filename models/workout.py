# Import libraries



#  Import files that I made
from app import db
from models.base import BaseModel


# create WorkoutModel that extends from Base and SQL class
class WorkoutModel(db.Model, BaseModel):
  __tablename__ = "workouts"

  ## id comes from the BaseModel
  #! user id will be added here, but it will be inherited as foreign key
  user_id = db.Column(db.Integer,db.ForeignKey('users.id'), nullable=False)
  #! warmup will be inherited from exercises, but for now will be created manually
  warmup = db.Column(db.Integer)
  #* DONE exercises will be inheited from exercise table but created manually for now
  # exercise1 = db.Column(db.Integer, db.ForeignKey('exercises.id'), nullable=False)
  # exercise2 = db.Column(db.Integer, db.ForeignKey('exercises.id'), nullable=False)
  # exercise3 = db.Column(db.Integer, db.ForeignKey('exercises.id'), nullable=False)
  exercise4 = db.Column(db.Integer)
  exercise5 = db.Column(db.Integer)
 #! cooldown will be inherited from exercises, but for now will be created manually
  cooldown = db.Column(db.Integer)
  rest = db.Column(db.Integer)
  #! rounds is a stretch goal
  # rounds = db.Column(db.Integer) 
  #! date created is inherited from the base model
  #! date updated is also inherited fom the base model, but should be hidden/omitted as it's never used
  #! is_completed is a stretch goal
  # is_completed = db.Column(db.Boolean, nullable=False)
  #! is_favourite is a stretch goal
  # is_favourite = db.Column(db.Boolean, nullable=False)
#! Length will be inherited from exercises and calculated, input manually for now
  length_of_workout = db.Column(db.Integer)