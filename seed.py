# Import libraries


#  Import files that I made
from app import app, db

# Import *schema
from models.exercise import ExerciseModel
from models.target_area import TargetAreaModel
from models.user import UserModel
from models.workout import WorkoutModel
from models.user_spend import SpendModel
from models.reward import RewardModel


# SQLA was installed as a flask plugin, so the following code is need to avoid errors
  ## app_context() manually manages the application-level data during a request, CLI command, or other activity
  ## the current_app proxy is used and this proxy that allows SQLA to run
  ## https://flask.palletsprojects.com/en/2.2.x/api/#flask.current_app

with app.app_context():
    try:
      print('Creating...')
      db.drop_all()
      db.create_all()

      print('Seeding...')

      # seeded in order of succession. Everything relies on the user, so user is seeded first
      
      target_area=TargetAreaModel(name="core")
      target_area.save()

      target_area1=TargetAreaModel(name="shoulders")
      target_area1.save()

      #! note to use args, kwargs in seeding for target_areas so there's a full table
      # exercise = ExerciseModel(name="plank")
      exercise = ExerciseModel(name="plank",target_area_id=target_area.id)
      exercise.save()

      # # exercise2 = ExerciseModel(name="shoulder rotations",target_area_id=target_area1.id)
      # exercise2 = ExerciseModel(name="shoulder rotations")
      # exercise2.save()

      # # exercise3 = ExerciseModel(name="crunches",target_area_id=target_area.id)
      # exercise3 = ExerciseModel(name="crunches")
      # exercise3.save()

      #* target_area -> exercises has been mapped successfully and we can see this in tableplus

      user = UserModel(username="jane",email="jane@jane.co", password="highcupsintegerwow",
      fitcoin=0, target_areas=1, image_url="https://img.icons8.com/color/480/lumpy-space-princess.png")
      user.save()

      #! note to use args, kwargs in seeding for exercises so there's a full table

      print(exercise.id)
      
      # workout = WorkoutModel(warmup=1,exercise1=exercise.id, exercise2=exercise2.id, exercise3=exercise3.id, cooldown=1, rest=1,length_of_workout=10)
      workout = WorkoutModel(user_id=user.id, warmup=1, cooldown=1, rest=1,length_of_workout=10)
      workout.save()

      reward = RewardModel(name="£10 Sephora voucher", description="£10 to use at Sephora, online and in stores.",fitcoin_cost=900)
      reward.save()
      
      spend = SpendModel(reward_quantity=1,fitcoin_cost=100)
      spend.save()

      


      #! note to use args, kwargs in seeding for rewards so there's a full table


      print('Completed!')

    except Exception as e:
      print(e)