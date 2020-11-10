from sqlalchemy.orm import Session

from Models.Users import *
from Schemas.UserSchemas import *

class UserService:

    @staticmethod
    def get_all_users(db_session : Session):
        return db_session.query(User).all()
    @staticmethod
    def get_user(db_session : Session, user_id : int):
        return db_session.query(User).filter_by(id = user_id).first()

    @staticmethod
    def create_user(db_session : Session, user_data : UserNew):
        user = User(
            email = user_data.email,
            pash_hash = user_data.password,
            personalInfo = None
        )
        db_session.add(user)
        db_session.commit()
