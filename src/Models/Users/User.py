from sqlalchemy import Column, Integer, String, Boolean 
from sqlalchemy.orm import relationship

from users_db import Base

class User(Base):
    
    __tablename__ = 'User'

    id = Column(Integer, primary_key = True)
    email = Column(String(100), unique = True, nullable = False)
    pass_hash = Column(String(256), nullable = False)
    is_active = Column(Boolean, default = True, nullable = False)
    personalInfo = relationship('UserPersonalInfo', back_populates = 'user')
