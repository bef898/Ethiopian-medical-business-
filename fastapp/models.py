from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Detection(Base):
    __tablename__ = "yolo_detections"

    id = Column(Integer, primary_key=True, index=True)
    image_name = Column(String, index=True)
    object_class = Column(String, index=True)
    confidence = Column(Float)
    xmin_value = Column(Float)
    ymin = Column(Float)
    xmax_value = Column(Float)
    ymax = Column(Float)
