# Import installed libraries
from app import ma
from marshmallow import fields


# imports from files/directories that I made
from models.user import UserModel

# create serialiser (called schema in docs): python -> SQLA -> JSON
  ## nested field uses marshmallow and child serialiser to create a field within the parent.
  ## with this, I can see workouts linked to users within the user
class UserSchema(ma.SQLAlchemyAutoSchema):

  workouts = fields.Nested('WorkoutSchema', many=True)

  class Meta:
    model = UserModel
    load_instance = True