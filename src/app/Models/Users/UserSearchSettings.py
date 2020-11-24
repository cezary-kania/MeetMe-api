import enum
from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Float, func 
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_method, hybrid_property

from app.Data.UserDatabase import Base


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
    latitude_pos = Column(Float, default=-1, nullable = False)
    longitude_pos = Column(Float, default =-1, nullable = False)
    gender_preferences = Column(Enum(PrefGenderEnum), nullable = False)
    minAge = Column(Integer, nullable = False, default=18)
    maxAge = Column(Integer, nullable = False, default = 100)
    user_id = Column(Integer, ForeignKey('User.id'))
    user = relationship('User', back_populates = 'searchSettings')

    @hybrid_method
    def haversine(self, other):
        r = 6371
        lat1, lon1 = self.latitude_pos, self.longitude_pos
        lat2, lon2 = other.latitude_pos, other.longitude_pos
        import math
        dlat = math.radians(lat2-lat1)
        dlon = math.radians(lon2-lon1)
        a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
            * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        d = r * c
        return d
    
    @haversine.expression
    def haversine(cls, other):
        r = 6371
        lat1, lon1 = cls.latitude_pos, cls.longitude_pos
        lat2, lon2 = other.latitude_pos, other.longitude_pos
        import math
        dlat = func.radians(lat2-lat1)
        dlon = func.radians(lon2-lon1)
        a = func.sin(dlat/2) * func.sin(dlat/2) + func.cos(func.radians(lat1)) \
            * func.cos(math.radians(lat2)) * func.sin(dlon/2) * func.sin(dlon/2)
        c = 2 * func.atan2(func.sqrt(a), func.sqrt(1-a))
        d = r * c
        return d 
    
    