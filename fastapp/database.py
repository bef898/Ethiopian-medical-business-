

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:1864@localhost/data_hub"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a session for interacting with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for the SQLAlchemy models
Base = declarative_base()

# Dependency: Get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
