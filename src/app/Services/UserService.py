from sqlalchemy.orm import Session

from app.Models.Users import (
    User, 
    UserPersonalInfo, 
    UserSearchSettings, 
    UserPhoto, 
    GenderEnum, 
    PrefGenderEnum
)
    
from app.Schemas.UserSchemas import (
    NewUser, 
    UserPersonalInfoModel, 
    UserPositionModel, 
    UserBaseSearchSettingsModel,
    UserPersonalInfoUpdate,
    UserChangeSearchSettingsModel
)
    
class UserService:

    @staticmethod
    def get_all_users(db_session : Session):
        return db_session.query(User).all()
    
    @staticmethod
    def get_user(db_session : Session, user_id : int):
        return db_session.query(User).filter_by(id = user_id).first()
    
    @staticmethod
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
            gender = user_data.gender,
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
    def delete_photo(db_session: Session, user_id: int, photo_id: int):
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
        db_session.delete(photo)
        db_session.commit()

    @staticmethod
    def change_personal_info(db_session: Session, user_id: int, user_data : UserPersonalInfoUpdate):
        user = UserService.get_user(db_session, user_id)
        if user is None:
            raise Exception('Invalid user id')
        if user.personalInfo is None:
            raise Exception('Something gone wrong.')
        if user_data.firstname:
            user.personalInfo.firstname = user_data.firstname
        if user_data.lastname:
            user.personalInfo.lastname = user_data.lastname
        if user_data.gender:
            user.searchSettings.gender = user_data.gender
        if user_data.age:
            user.personalInfo.age = user_data.age
        if user_data.description:
            user.personalInfo.description = user_data.description
        db_session.commit()
    
    @staticmethod
    def set_new_search_settings(db_session: Session, user_id : int, user_data : UserBaseSearchSettingsModel):
        user = UserService.get_user(db_session, user_id)
        if user is None:
            raise Exception('Invalid user id')
        if user_data.minAge > user_data.maxAge:
            raise Exception('Invalid age preferences settings')
        user.searchSettings = UserSearchSettings(
            distance = user_data.distance,
            gender_preferences = user_data.gender_preferences,
            minAge = user_data.minAge,
            maxAge = user_data.maxAge,
        )
        db_session.commit()
    
    @staticmethod
    def change_search_info(db_session: Session, user_id: int, user_data : UserChangeSearchSettingsModel):
        user = UserService.get_user(db_session, user_id)
        if user is None:
            raise Exception('Invalid user id')
        if user.searchSettings is None:
            raise Exception('Something gone wrong.')
        if user_data.distance:
            user.searchSettings.distance = user_data.distance
        if user_data.gender_preferences:
            user.searchSettings.gender_preferences = user_data.gender_preferences
        if user_data.minAge:
            user.searchSettings.minAge = user_data.minAge
        if user_data.maxAge:
            user.searchSettings.maxAge = user_data.maxAge
        db_session.commit()

    @staticmethod
    def set_user_postion(db_session: Session, user_id : int, user_position : UserPositionModel):
        user = UserService.get_user(db_session, user_id)
        if user is None:
            raise Exception('Invalid user id')
        if user.searchSettings is None:
            raise Exception('User search settings not created')
        user.searchSettings.latitude_pos = user_position.latitude_pos
        user.searchSettings.longitude_pos = user_position.longitude_pos
        db_session.commit()
