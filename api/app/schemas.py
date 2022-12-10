from datetime import datetime

from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    
class User(UserBase):

    class Config:
        orm_mode = True