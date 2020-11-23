from pydantic import BaseModel, Field
from typing import Optional, List

from Models.Users.UserSearchSettings import PrefGenderEnum
from Models.Users.UserPersonalInfo import GenderEnum
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
    gender : GenderEnum
    age : int
    photos : List[Photo] = []
    description : str
    class Config:
        orm_mode = True

class UserPersonalInfoUpdate(BaseModel):
    firstname : Optional[str] = Field(
        None, title='user firstname', max_length= 100
    )
    lastname : Optional[str] = Field(
        None, title='user lastname', max_length= 100
    )
    gender : Optional[GenderEnum] = None
    age : Optional[int] = Field(
        None, 
        title='user firstname', 
        gt=17,
        description='User must be at least 18 years old'
    )
    description : Optional[str] = Field(
        None, 
        title='user description', 
        max_length= 1000,
        description='Description max length = 1000'
    )

class UserBaseSearchSettingsModel(BaseModel):
    distance : int = Field(
        ...,
        lt=3000
    )
    gender_preferences : PrefGenderEnum
    maxAge : int = Field(
        ..., 
        lt=100, 
        gt=17, 
        description='Max age must be lower than 100 and greater than 17' )
    minAge : int = Field(
        ..., 
        lt=100, 
        gt=17, 
        description='Min age must be lower than 100 and greater than 17' )
    class Config:
        orm_mode = True

class UserChangeSearchSettingsModel(BaseModel):
    distance :  Optional[int] = Field(
        None,
        lt=3000
    )
    gender_preferences : PrefGenderEnum
    maxAge :  Optional[int] = Field(
        None, 
        lt=100, 
        gt=17, 
        description='Max age must be lower than 100 and greater than 17' )
    minAge : Optional[int] = Field(
        None, 
        lt=100, 
        gt=17, 
        description='Min age must be lower than 100 and greater than 17' )

class UserPositionModel(BaseModel):
    latitude_pos : float
    longitude_pos : float

class UserSearchSettingsModel(UserBaseSearchSettingsModel, UserPositionModel):
    pass

class UserModel(BaseModel):
    id : int
    email: str
    is_active : bool
    personalInfo : UserPersonalInfoModel = None
    searchSettings : UserSearchSettingsModel = None
    class Config:
        orm_mode = True

