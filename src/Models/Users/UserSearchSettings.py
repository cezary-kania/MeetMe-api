import enum
from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Float 
from sqlalchemy.orm import relationship

from users_db import Base

class GenderEnum(enum.Enum):
    male = 1
    female = 2
    not_specified = 3

class UserSearchSettings(Base):
    
    __tablename__ = 'UserSearchSettings'

    id = Column(Integer, primary_key = True)
    distance = Column(Integer, nullable = False)
    last_latitude_pos = Column(Float)
    last_longitude_pos = Column(Float)
    gender = Column(Enum(GenderEnum), nullable = False)
    user_id = Column(Integer, ForeignKey('User.id'))
    user = relationship('User', back_populates = 'searchSettings')   
