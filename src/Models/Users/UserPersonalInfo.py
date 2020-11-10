from Models import users_db as db

from sqlalchemy.orm import relationship
from passlib.hash import pbkdf2_sha256 as sha256


class UserPersonalInfo(db.Model):
    
    __tablename__ = 'UserPersonalInfo'

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('UserPersonalInfo.id'))    
    firstname = db.Column(db.String(100), nullable = False)
    lastname = db.Column(db.String(100), nullable = False)
    photos = relationship('UserPhoto', back_populates = 'user_personal_info')
    description = db.Column(db.String(1000))
    age = db.Column(db.Integer, nullable = False)
    
