from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine

## Main API code
models.Base.metadata.create_all(bind= engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

    ## GET all Pollutions data
@app.get("/pmdata/", response_model= list[schemas.PMResponse])
def read_pm(skip= 0, limit= 100, db: Session = Depends(get_db)):
    pmdata = crud.get_pm(db, skip= skip, limit= limit)
    return pmdata

@app.get("/pmdata/provinces/")
def read_provinces(odpc:int, db: Session = Depends(get_db)):
    return crud.get_provinces_list(odpc= odpc, db= db)