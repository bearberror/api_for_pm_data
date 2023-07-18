from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from .database import Base

## Setup data models

class PMData(Base):
    __tablename__ = "pm"

    transaction_id = Column(Integer, primary_key= True)
    station_id = Column(String)
    station_name = Column(String)
    station_type = Column(String)
    lat = Column(Float)
    long = Column(Float)
    date = Column(String)
    time = Column(String)
    pm25 = Column(Float)
    pm10 = Column(Float)
    o3 = Column(Float)
    no2 = Column(Float)
    so2 = Column(Float)
    province = Column(String)
    district = Column(String)
    subdistrict = Column(String)

class Odpc(Base):
    __tablename__ = "odpc"

    odpc = Column(Integer, primary_key= True)
    provinces_list = Column(String)