import enum
from sqlalchemy import Column, Integer, String, ForeignKey, Enum 
from sqlalchemy.orm import relationship

from users_db import Base

class GenderEnum(enum.Enum):
    male = 1
    female = 2
    not_specified = 3

class UserSearchSettings(Base):
    
    __tablename__ = 'UserSearchSettings'

    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('User.id'))
    distance = Column(Integer, nullable = False)
    gender = Column(Enum(GenderEnum), nullable = False)   