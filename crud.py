from ast import literal_eval
from sqlalchemy.orm import Session
import models

## setup CRUD function
## Get all pollutions data
def get_pm(db: Session, skip= 0, limit= 100):
    return db.query(models.PMData).offset(skip).limit(limit).all()

## get provinces_list
def get_provinces_list(db: Session, odpc: int):
    return literal_eval(db.query(models.Odpc).filter(models.Odpc.odpc == odpc).first().provinces_list)