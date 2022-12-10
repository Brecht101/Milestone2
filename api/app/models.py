from sqlalchemy import String, Column

from database import Base


class User(Base):
    __tablename__ = "user"

    name = Column(String(100), primary_key=True, index=True)