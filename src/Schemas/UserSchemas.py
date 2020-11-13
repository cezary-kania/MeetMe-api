from pydantic import BaseModel
from typing import Optional, List

class NewUser(BaseModel):
    email: str
    password: str

class Photo(BaseModel):
    id : int
    class Config:
        orm_mode = True
class UserPersonalInfoModel(BaseModel):
    firstname : str
    lastname : str
    age : int
    photos : List[Photo] = []
    description : str
    class Config:
        orm_mode = True

class UserPersonalInfoUpdate(BaseModel):
    firstname : Optional[str] = None
    lastname : Optional[str] = None
    age : Optional[int] = None
    description : Optional[str] = None

class UserModel(BaseModel):
    id : int
    email: str
    is_active : bool
    personalInfo : UserPersonalInfoModel = None
    class Config:
        orm_mode = True