# Import libraries
from flask import Blueprint, request
## Blueprint is the router that works in Flask -> similar to the router that's in react-router-dom
## request is a global object that is imported, not like in JS where it's a parameter

from marshmallow.exceptions import ValidationError

from http import HTTPStatus


#  Import files that I made


## models
from models.exercise_data import exercises_db
from models.exercise import ExerciseModel


## serialisers/schemas
from serialisers.exercise import ExerciseSchema
exercise_schema = ExerciseSchema()



# Router
router = Blueprint('exercises', __name__)

#  Requests

## get all exercises
@router.route('/exercises', methods=["GET"])
def get_all_exercises():
  exercises = ExerciseModel.query.all()

  if not exercises:
    return { "message": "Exercises not found" }, HTTPStatus.NOT_FOUND
  
  try:
    print(exercises)
    return exercise_schema.jsonify(exercises, many=True), HTTPStatus.OK

  except ValidationError as e:
    return { "errors" : e.messages, "message": "Something went wrong" }

## get exercise by id
@router.route('/exercise/<int:exercise_id>', methods=["GET"])
def get_one_exercise_by_id(exercise_id):
  exercise  = ExerciseModel.query.get(exercise_id)
    # remember to add the type of the query(param) and its name in the <> when
    # defining a variable
    # and then then pass the id as an parameter in the function
  
  if not exercise:
    return { "message": "Exercise not found" }, HTTPStatus.NOT_FOUND
  
  try:
    print(exercise)
    return exercise_schema.jsonify(exercise), HTTPStatus.OK

  except ValidationError as e:
    return { "errors" : e.messages, "message": "Something went wrong" }

## ADMIN ONLY -- create exercise
@router.route('/exercises', methods=["POST"])
def admin_post_exercise():
  new_exercise_dict = request.json

  try:
    exercise = exercise_schema.load(new_exercise_dict)
    # print(new_exercise_dict)
    # print(exercise)
    exercise.save()
    
    # nb - no need to add `many=True` as argument below, unlike in get requests
    return exercise_schema.jsonify(exercise), HTTPStatus.OK

  except ValidationError as e:
    return { "errors" : e.messages, "message": "Something went wrong" }

## ADMIN ONLY -- update exercise
@router.route('/exercise/<int:exercise_id>', methods=["PUT", "PATCH"])
def admin_update_exercise(exercise_id):
    # remember to add the type of the query(param) and its name in the <> when
    # defining a variable
    # and then then pass the id as an parameter in the function
  updates_dict = request.json
  existing_exercise = ExerciseModel.query.get(exercise_id)

  if not existing_exercise:
    return { "message": "Exercise not found" }, HTTPStatus.NOT_FOUND

  try:
    exercise = exercise_schema.load(
      updates_dict,
      instance=existing_exercise,
      partial=True
    )
    # print(new_exercise_dict)
    # print(exercise)
    exercise.save()
    
    # nb - no need to add `many=True` as argument below, unlike in get requests
    return exercise_schema.jsonify(existing_exercise), HTTPStatus.OK

  except ValidationError as e:
    return { "errors" : e.messages, "message": "Something went wrong" }

## ADMIN ONLY -- delete exercise
@router.route('/exercise/<int:exercise_id>', methods=["DELETE"])
def admin_delete_exercise(exercise_id):
  exercise_to_be_deleted = ExerciseModel.query.get(exercise_id)
  
  if not exercise_to_be_deleted:
    return { "message": "No exercise found" }, HTTPStatus.NOT_FOUND

  # #? need to sort out issue with below code! why won't it delete?
  # #! no need to try catch here, unless it's done without the if statement
  exercise_to_be_deleted.delete_me()
  #   #! remember that we're using the methods on the BaseModel to interact with the database!
  #   #! remember to return something!!
  print(exercise_to_be_deleted)
  return '', HTTPStatus.NO_CONTENT





#! Copy this code when creating a new route
# @router.route('/', methods=[""])
# def new_function():
  # if not value:
    # return { "message": "No food found" }, HTTPStatus.NOT_FOUND
  # try:
    # print(whatever)
    # return whatever 
  # except ValidationError as e:
  #   return { "errors" : e.messages, "message": "Something went wrong" }

