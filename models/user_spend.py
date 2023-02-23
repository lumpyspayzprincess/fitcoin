# Import libraries



#  Import files that I made
from app import db
from models.base import BaseModel


# create WorkoutModel that extends from Base and SQL class
class SpendModel(db.Model, BaseModel):
  __tablename__ = "user_spend"

  ## id comes from the BaseModel
  #! user id will be added here, but it will be inherited as foreign key
  # user_id = db.Column(db.Integer, nullable=False)
 #! reward id will be added here, but it will be inherited as foreign key
  # reward_id = db.Column(db.Integer, nullable=False)
  reward_quantity = db.Column(db.Integer, nullable=False)
  fitcoin_cost = db.Column(db.Integer, nullable=False)
  ## date_created is inherited from yhe base model