from sqlalchemy.orm import Session
from . import models, schemas

# Function to get all detection records
def get_detections(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Detection).offset(skip).limit(limit).all()

# Function to get detection by ID
def get_detection(db: Session, detection_id: int):
    return db.query(models.Detection).filter(models.Detection.id == detection_id).first()

# Function to create a new detection record
def create_detection(db: Session, detection: schemas.DetectionBase):
    db_detection = models.Detection(**detection.dict())
    db.add(db_detection)
    db.commit()
    db.refresh(db_detection)
    return db_detection
