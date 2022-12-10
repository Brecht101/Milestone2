import datetime

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/user", response_model=schemas.User)
def read_user(db: Session = Depends(get_db)):
    user = crud.get_user(db)
    return user

@app.get("/test")
def test():
    return 'test'