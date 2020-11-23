from sqlalchemy import Column, Integer, String, Boolean 
from sqlalchemy.orm import relationship

from app.Data.UserDatabase import Base

class User(Base):
    
    __tablename__ = 'User'

    id = Column(Integer, primary_key = True)
    email = Column(String(100), unique = True, nullable = False)
    pass_hash = Column(String(256), nullable = False)
    is_active = Column(Boolean, default = True, nullable = False)
    personalInfo = relationship('UserPersonalInfo',uselist=False, back_populates = 'user')
    searchSettings = relationship('UserSearchSettings',uselist=False, back_populates = 'user')

    def __repr__(self):
        return f'User<id:{self.id},email:{self.email},status:{self.is_active}>'
