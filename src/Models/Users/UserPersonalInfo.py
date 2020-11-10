from sqlalchemy import Column, Integer, String, ForeignKey 
from sqlalchemy.orm import relationship

from users_db import Base

class UserPersonalInfo(Base):
    
    __tablename__ = 'UserPersonalInfo'

    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('User.id'))
    user = relationship('User', back_populates = 'personalInfo')    
    firstname = Column(String(100), nullable = False)
    lastname = Column(String(100), nullable = False)
    photos = relationship('UserPhoto', back_populates = 'user_personal_info')
    description = Column(String(1000))
    age = Column(Integer, nullable = False)
    
