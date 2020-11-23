from sqlalchemy import Column, Integer, String, ForeignKey, LargeBinary 
from sqlalchemy.orm import relationship

from Data.UserDatabase import Base

class UserPhoto(Base):
    
    __tablename__ = 'UserPhoto'

    id = Column(Integer, primary_key = True)
    image = Column(LargeBinary, nullable = True) # nullable == True - for development purposes
    user_personal_info_id = Column(Integer, ForeignKey('UserPersonalInfo.id'))
    user_personal_info = relationship('UserPersonalInfo', uselist=False, back_populates = 'photos')