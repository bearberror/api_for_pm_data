from pydantic import BaseModel

class PMResponse(BaseModel):

    transaction_id: int
    station_id: str
    station_name: str
    station_type: str
    lat: float
    long: float
    date: str
    time: str
    pm25: float | None = None
    pm10: float | None = None
    o3: float | None = None
    no2: float | None = None
    so2: float | None = None
    province: str
    district: str | None = None
    subdistrict: str | None = None

    class Config:
        from_attributes = True

class OdpcResponse(BaseModel):
    odpc: int
    provinces_list: str