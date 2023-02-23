# Import libraries
from datetime import datetime


#  Import files that I made
from app import db


#  This is the SQLA model that relies on everything
  # id,created_at,updated_at are the statis fields/columns that each model has
class BaseModel:
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    ## add the item, then commit the item
    def save(self):
      db.session.add(self)
      db.session.commit()
    
    ## remove the item, then commit the item
    def remove(self):
      db.session.remove(self)
      db.session.commit()