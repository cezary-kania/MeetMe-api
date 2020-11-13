from sqlalchemy.orm import Session

from Models.Users import User, UserPersonalInfo, UserSearchSettings, UserPhoto
from Schemas.UserSchemas import NewUser, UserPersonalInfoModel

class UserService:

    @staticmethod
    def get_all_users(db_session : Session):
        return db_session.query(User).all()
    @staticmethod
    def get_user(db_session : Session, user_id : int):
        return db_session.query(User).filter_by(id = user_id).first()
    def get_by_email(db_session : Session, email : str):
        return db_session.query(User).filter_by(email = email).first()
    @staticmethod
    def create_user(db_session : Session, user_data : NewUser):
        user = User(
            email = user_data.email,
            pass_hash = user_data.password,
        )
        db_session.add(user)
        db_session.commit()
        return user

    @staticmethod
    def set_new_personal_info(db_session : Session, user_id : int, user_data : UserPersonalInfoModel):
        user = UserService.get_user(db_session, user_id)
        if user is None:
            raise Exception('Invalid user id')
        user.personalInfo = UserPersonalInfo(
            firstname = user_data.firstname,
            lastname = user_data.lastname,
            age = user_data.age,
            description = user_data.description,
            photos = []
        )
        db_session.commit()
    
    @staticmethod
    def upload_photo(db_session: Session, user_id : int, photo_bytes : bytes):
        user = UserService.get_user(db_session, user_id)
        if user is None:
            raise Exception('Invalid user id')
        if user.personalInfo is None:
            raise Exception('User info not created')
        photo_item = UserPhoto(image = photo_bytes)
        user.personalInfo.photos.append(photo_item)
        db_session.commit()

    @staticmethod
    def get_photo(db_session: Session, user_id: int, photo_id: int):
        user = UserService.get_user(db_session, user_id)
        if user is None:
            raise Exception('Invalid user id')
        if user.personalInfo is None:
            raise Exception('User info not created')
        user_info_id = user.personalInfo.id
        photo = db_session.query(UserPhoto) \
            .filter_by(user_personal_info_id = user_id, id = photo_id) \
            .first()
        if photo is None:
            raise Exception('Invalid input')
        return photo.image
    
    @staticmethod
    def set_personal_info_prop(db_session: Session, user_id: int, **properties):
        user = UserService.get_user(db_session, user_data.user_id)
        if user is None:
            raise Exception('Invalid user id')
        user_info = db_session.query(UserPersonalInfo).filter_by(user_id = user.id).first()
        if user_info is None:
            raise Exception('Something gone wrong.')
        if 'firstname' in properties:
            user.personalInfo.firstname = properties.get('firstname')
        if 'lastname' in properties:
            user.personalInfo.firstname = properties.get('lastname')
        if 'age' in properties:
            user.personalInfo.firstname = properties.get('age')
        if 'description' in properties:
            user.personalInfo.firstname = properties.get('description')
        db_session.commit()
            
