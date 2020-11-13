from fastapi import APIRouter, HTTPException, UploadFile, File
from typing import List
from starlette.responses import StreamingResponse

from Services.UserService import UserService
from Models.Users import *
from Schemas.UserSchemas import NewUser, UserPersonalInfoModel, UserPersonalInfoUpdate, UserModel
from Data.UserDatabase import Base, engine, SessionLocal

Base.metadata.create_all(bind = engine)

db_session = SessionLocal()

router = APIRouter()

@router.get('', response_model=List[UserModel])
def get_all_users():
    print(UserService.get_all_users(db_session))
    return UserService.get_all_users(db_session)

@router.get('/{userId}', response_model=UserModel)
def get_user(userId : int):
    return UserService.get_user(db_session, userId)

@router.post('', response_model = UserModel)
def create_user(user_data: NewUser):
    user = UserService.get_by_email(db_session, user_data.email)
    if user is not None:
        raise HTTPException(status_code=400, detail="Email already registered")
    return UserService.create_user(db_session, user_data)

@router.post('/{userId}/personalInfo',response_model=UserModel)
def set_new_personal_info(userId : int, user_data: UserPersonalInfoModel):
    user = UserService.get_user(db_session, userId)
    if user is None:
        raise HTTPException(status_code=404, detail="User doesnt exists.")
    UserService.set_new_personal_info(db_session,userId, user_data)
    return user

@router.put('/{userId}/personalInfo')
def set_personal_info(userId : int,user_data: UserPersonalInfoUpdate):
    user = UserService.get_user(db_session, userId)
    if user is None:
        raise HTTPException(status_code=404, detail="User doesnt exists.")
    #UserService.set_personal_info_prop(db_session,userId, user_data)

@router.post('/{userId}/uploadPhoto')
async def upload_photo(userId : int, photo : UploadFile = File(...)):   
    if photo.content_type == "image/jpeg":
        photo_bytes = await photo.read()
        try:
            UserService.upload_photo(db_session, userId, photo_bytes)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

@router.get('/{userId}/photos')
def upload_photo(userId : int, photoId: int):
    try:
        photo_bytes = UserService.get_photo(db_session, userId, photoId)
    except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
    import io
    return StreamingResponse(io.BytesIO(photo_bytes), media_type="image/png")