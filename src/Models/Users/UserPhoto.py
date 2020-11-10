from Models import users_db as db

from sqlalchemy.orm import relationship
from passlib.hash import pbkdf2_sha256 as sha256


class UserPhoto(db.Model):
    
    __tablename__ = 'UserPhoto'

    id = db.Column(db.Integer, primary_key = True)
    user_personal_info_id = db.Column(db.Integer, db.ForeignKey('UserPersonalInfo.id'))
    user_personal_info = relationship('UserPersonalInfo', uselist=False, back_populates = 'photos')
