# Import libraries



#  Import files that I made
from app import db
from models.base import BaseModel


# create WorkoutModel that extends from Base and SQL class
class RewardModel(db.Model, BaseModel):
  __tablename__ = "rewards"

  ## id comes from the BaseModel
  name = db.Column(db.Text, nullable = False)
  description = db.Column(db.Text)
  fitcoin_cost = db.Column(db.Integer, nullable=False)
