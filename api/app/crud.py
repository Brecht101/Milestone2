import datetime

from sqlalchemy.orm import Session

import models
import schemas


def get_user(db: Session):
    return db.query(models.User).first()