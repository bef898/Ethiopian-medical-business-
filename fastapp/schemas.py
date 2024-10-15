# schemas.py

from pydantic import BaseModel

# Pydantic schema for detection
class DetectionBase(BaseModel):
    image_name: str
    object_class: str
    confidence: float
    xmin_value:float
    ymin :float
    xmax_value: float
    ymax :float

# Schema used when returning data from the database (response)
class Detection(DetectionBase):
    id: int

    class Config:
        orm_mode = True
