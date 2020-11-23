from fastapi import APIRouter, HTTPException, UploadFile, File
from typing import List
from starlette.responses import StreamingResponse

from app.Services.ConnetionService import ConnectionService
from app.Data.UserDatabase import SessionLocal

from app.Schemas.UserSchemas import (
    UserModel
)

db_session = SessionLocal()

router = APIRouter()

@router.get('/new-propositions',response_model=List[UserModel])
def get_new_propositions(user_id : int):
    try:
        proposed_users = ConnectionService.get_new_proposition(db_session, user_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return proposed_users