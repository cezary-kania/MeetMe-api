from Models import users_db as db

from sqlalchemy.orm import relationship
from passlib.hash import pbkdf2_sha256 as sha256


class User(db.Model):
    
    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(100), unique = True, nullable = False)
    pass_hash = db.Column(db.String(256), nullable = False)
    personalInfo = relationship('UserPersonalInfo', back_populates = 'personalInfo')

