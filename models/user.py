# Import libraries



#  Import files that I made
from app import db
from models.base import BaseModel


# create UserModel that extends from Base and SQL class

class UserModel(db.Model, BaseModel):
  __tablename__ = "users"

  ## userid comes from the BaseModel
  username = db.Column(db.Text, nullable=False)
  email = db.Column(db.Text, nullable=False)
  password = db.Column(db.Text, nullable=False)
  fitcoin = db.Column(db.Integer, nullable=False)
  target_areas = db.Column(db.Integer, nullable=False)
  #! target_areas is an integer for now, but in my extended project,
  #! I will look at making the data type a list or tuple
  image_url = db.Column(db.Text)
  #! image_url will come from cloudindary api -> need to look at Nick's notes
  #? extended work - thinking to add these values at a later date
  # completed_workouts = db.Column(db.Integer)
  # favourite_workouts = db.Column(db.List)
  #! can I use a list/tuple in my column? I think I mat need to have this as an FK




# Completed_workouts Int
# Favourite_workouts null Int