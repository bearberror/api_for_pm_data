from sqlalchemy.orm import Session
import models

## setup CRUD function
## Get all pollutions data
def get_pm(db: Session, skip= 0, limit= 100):
    return db.query(models.PMData).offset(skip).limit(limit).all()