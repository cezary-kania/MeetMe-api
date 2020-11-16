import enum
from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Float 
from sqlalchemy.orm import relationship

from Data.UserDatabase import Base


class PrefGenderEnum(enum.Enum):
    male = 'male'
    female = 'female'
    not_specified = 'not_specified'
    
    @staticmethod
    def values():
        return list(PrefGenderEnum)

class UserSearchSettings(Base):
    
    __tablename__ = 'UserSearchSettings'

    id = Column(Integer, primary_key = True)
    distance = Column(Integer, nullable = False)
    latitude_pos = Column(Float, default=-1)
    longitude_pos = Column(Float, default =-1)
    gender_preferences = Column(Enum(PrefGenderEnum), nullable = False)
    minAge = Column(Integer, nullable = False, default=18)
    maxAge = Column(Integer, nullable = False, default = 100)
    user_id = Column(Integer, ForeignKey('User.id'))
    user = relationship('User', back_populates = 'searchSettings')   
