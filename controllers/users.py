# Import libraries
from flask import Blueprint, request
# Blueprint is the router that works in Flask -> similar to the router that's in react-router-dom
# request is a global object that is imported, not like in JS where it's a parameter

from marshmallow.exceptions import ValidationError

from http import HTTPStatus


#  Import files that I made
# from controllers.target_areas import get_one_area_by_id


# models
from models.user import UserModel


# serialisers/schemas

from serialisers.user import UserSchema
user_schema = UserSchema()
from serialisers.workout import WorkoutSchema
workout_schema = WorkoutSchema()


# Router
router = Blueprint('users', __name__)

#  Requests

# get all users


@router.route('/users', methods=["GET"])
def get_all_users():
    users = UserModel.query.all()

    if not users:
        return {"message": "Users not found"}, HTTPStatus.NOT_FOUND

    try:
        print(users)
        return user_schema.jsonify(users, many=True), HTTPStatus.OK

    except ValidationError as e:
        return {"errors": e.messages, "message": "Something went wrong"}
    

## get user by id
@router.route('/user/<int:user_id>', methods=["GET"])
def get_one_user_by_id(user_id):
  user  = UserModel.query.get(user_id)
    # remember to add the type of the query(param) and its name in the <> when
    # defining a variable
    # and then then pass the id as an parameter in the function
  
  if not user:
    return { "message": "User not found" }, HTTPStatus.NOT_FOUND
  
  try:
    print(user)
    return user_schema.jsonify(user), HTTPStatus.OK

  except ValidationError as e:
    return { "errors" : e.messages, "message": "Something went wrong" }
  

#! ON SIGNUP - - - '/signup'
## post new user

@router.route('/users', methods=["POST"])
def admin_post_user():
  new_user_dict = request.json

  try:
    user = user_schema.load(new_user_dict)
    # print(new_exercise_dict)
    # print(exercise)
    user.save()
    
    # nb - no need to add `many=True` as argument below, unlike in get requests
    return user_schema.jsonify(user), HTTPStatus.OK

  except ValidationError as e:
    return { "errors" : e.messages, "message": "Something went wrong" }
  
#! ON CREATING A NEW WORKOUT WHILE THE USER IS LOGGED IN first time
# post new workout for specific user 
# @router.route('/user/<int:user_id>/', methods=["PUT", "PATCH"])
# def update_user_add_workout(user_id):
#     # remember to add the type of the query(param) and its name in the <> when
#     # defining a variable
#     # and then then pass the id as an parameter in the function
#   updates_dict = request.json
#   existing_user = UserModel.query.get(user_id)
#   user_workouts = existing_user.workouts
#   print (user_workouts)

#   if not existing_user:
#     return { "message": "User not found" }, HTTPStatus.NOT_FOUND
  
#   #! wanted to add if/else statement for if workout equals null, but that was tedious.
#   #! I think undefined if better here, but not comepletely sure of how to make sure that it's used properly 

#   try:
#     workout = workout_schema.load(
#       updates_dict,
#       instance=user_workouts,
#       partial=True
#     )
#     # print(new_exercise_dict)
#     # print(exercise)
#     # user.save()
    
#     # nb - no need to add `many=True` as argument below, unlike in get requests
#     return user_schema.jsonify(existing_user), HTTPStatus.OK

#   except ValidationError as e:
#     return { "errors" : e.messages, "message": "Something went wrong" }
  
  #! APPENDING WORKOUTS WHILE THE USER IS LOGGED IN first time
# post new workout for specific user 
@router.route('/user/<int:user_id>/', methods=["PUT", "PATCH"])
def update_user_add_workout(user_id):
    # remember to add the type of the query(param) and its name in the <> when
    # defining a variable
    # and then then pass the id as an parameter in the function
  updates_dict = request.json
  existing_user = UserModel.query.get(user_id)
  user_workouts = existing_user.workouts
  print (user_workouts)

  if not existing_user:
    return { "message": "User not found" }, HTTPStatus.NOT_FOUND
  
  #! wanted to add if/else statement for if workout equals null, but that was tedious.
  #! I think undefined if better here, but not comepletely sure of how to make sure that it's used properly 

  try:
    workout = workout_schema.load(
      updates_dict,
      instance=user_workouts,
      partial=True
    )
    # print(new_exercise_dict)
    # print(exercise)
    # user.save()
    
    # nb - no need to add `many=True` as argument below, unlike in get requests
    return user_schema.jsonify(existing_user), HTTPStatus.OK

  except ValidationError as e:
    return { "errors" : e.messages, "message": "Something went wrong" }


# #! Copy this code when creating a new route
# # @router.route('/', methods=[""])
# # def new_function():
#   # if not value:
#     # return { "message": "No food found" }, HTTPStatus.NOT_FOUND
#   # try:
#     # print(whatever)
#     # return whatever
#   # except ValidationError as e:
#   #   return { "errors" : e.messages, "message": "Something went wrong" }
