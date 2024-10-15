

import os
import sys
sys.path.append(os.path.abspath('../scripts'))
sys.path.append(os.path.abspath('../fastapp'))
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .models import Detection  # Relative import
from .schemas import DetectionBase, Detection  # Relative import
from .crud import get_detections, get_detection, create_detection  # Relative import
from .database import get_db  # Relative import



# Create the database tables if they don't exist
#models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Route to retrieve all detections
@app.get("/detections/", response_model=list[schemas.Detection])
def read_detections(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    detections = crud.get_detections(db=db, skip=skip, limit=limit)
    return detections

# Route to retrieve a specific detection by ID
@app.get("/detections/{detection_id}", response_model=schemas.Detection)
def read_detection(detection_id: int, db: Session = Depends(get_db)):
    detection = crud.get_detection(db=db, detection_id=detection_id)
    if detection is None:
        raise HTTPException(status_code=404, detail="Detection not found")
    return detection

# Route to create a new detection
@app.post("/detections/", response_model=schemas.Detection)
def create_detection(detection: schemas.DetectionBase, db: Session = Depends(get_db)):
    return crud.create_detection(db=db, detection=detection)
