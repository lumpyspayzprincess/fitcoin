# Import libraries
from flask import Blueprint, request
## Blueprint is the router that works in Flask -> similar to the router that's in react-router-dom
## request is a global object that is imported, not like in JS where it's a parameter

from marshmallow.exceptions import ValidationError

from http import HTTPStatus


#  Import files that I made


## models
from models.target_area import TargetAreaModel
from models.exercise import ExerciseModel


## serialisers/schemas
from serialisers.target_area import TargetAreaSchema
target_area_schema = TargetAreaSchema()
from serialisers.exercise import ExerciseSchema
exercise_schema = ExerciseSchema()



# Router
router = Blueprint('target_areas', __name__)

#  Requests

## get all areas
@router.route('/areas', methods=["GET"])
def get_all_areas():
  areas = TargetAreaModel.query.all()

  if not areas:
    return { "message": "Areas not found" }, HTTPStatus.NOT_FOUND
  
  try:
    print(areas)
    return target_area_schema.jsonify(areas, many=True), HTTPStatus.OK

  except ValidationError as e:
    return { "errors" : e.messages, "message": "Something went wrong" }

## get area by id
@router.route('/area/<int:area_id>', methods=["GET"])
def get_one_area_by_id(area_id):
  area  = TargetAreaModel.query.get(area_id)
    # remember to add the type of the query(param) and its name in the <> when
    # defining a variable
    # and then then pass the id as an parameter in the function
  
  if not area:
    return { "message": "Area not found" }, HTTPStatus.NOT_FOUND
  
  try:
    print(area)
    return target_area_schema.jsonify(area), HTTPStatus.OK

  except ValidationError as e:
    return { "errors" : e.messages, "message": "Something went wrong" }

## ADMIN ONLY -- create area
@router.route('/areas', methods=["POST"])
def admin_post_areas():
  new_area_dict = request.json

  try:
    area = target_area_schema.load(new_area_dict)
    # print(new_exercise_dict)
    # print(exercise)
    area.save()
    
    # nb - no need to add `many=True` as argument below, unlike in get requests
    return target_area_schema.jsonify(area), HTTPStatus.OK

  except ValidationError as e:
    return { "errors" : e.messages, "message": "Something went wrong" }

## ADMIN ONLY -- update area
@router.route('/area/<int:area_id>', methods=["PUT", "PATCH"])
def admin_update_area(area_id):
    # remember to add the type of the query(param) and its name in the <> when
    # defining a variable
    # and then then pass the id as an parameter in the function
  updates_dict = request.json
  existing_area = TargetAreaModel.query.get(area_id)

  if not existing_area:
    return { "message": "Area not found" }, HTTPStatus.NOT_FOUND

  try:
    area = target_area_schema.load(
      updates_dict,
      instance=existing_area,
      partial=True
    )
    # print(new_exercise_dict)
    # print(exercise)
    area.save()
    
    # nb - no need to add `many=True` as argument below, unlike in get requests
    return target_area_schema.jsonify(existing_area), HTTPStatus.OK

  except ValidationError as e:
    return { "errors" : e.messages, "message": "Something went wrong" }

## ADMIN ONLY -- delete area
@router.route('/area/<int:area_id>', methods=["DELETE"])
def admin_delete_area(area_id):
  area_to_be_deleted = TargetAreaModel.query.get(area_id)
  
  if not area_to_be_deleted:
    return { "message": "No area found" }, HTTPStatus.NOT_FOUND

  # #? need to sort out issue with below code! why won't it delete?
  # #! no need to try catch here, unless it's done without the if statement
  area_to_be_deleted.delete_me()
  #   #! remember that we're using the methods on the BaseModel to interact with the database!
  #   #! remember to return something!!
  print(area_to_be_deleted)
  return '', HTTPStatus.NO_CONTENT


#  - - EXERCISES - -


#  Requests

## get all exercises by area id
@router.route('/area/<int:area_id>/exercises', methods=["GET"])
def get_all_exercises_by_area(area_id):
  exercises = ExerciseModel.query.filter_by(target_area_id = area_id)

  if not exercises:
    return { "message": "Exercises not found" }, HTTPStatus.NOT_FOUND
  
  try:
    print(exercises)
    return exercise_schema.jsonify(exercises, many=True), HTTPStatus.OK

  except ValidationError as e:
    return { "errors" : e.messages, "message": "Something went wrong" }



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

