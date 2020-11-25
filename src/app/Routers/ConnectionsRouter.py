from fastapi import APIRouter, HTTPException, Response
from typing import List
from starlette.responses import StreamingResponse

from app.Services.ConnectionService import ConnectionService
from app.Services.UserService import UserService
from app.Data.UserDatabase import SessionLocal

from app.Schemas.UserSchemas import (
    UserModel
)
from app.Schemas.ConnectionsSchemas import (
    DecisionModel
)

db_session = SessionLocal()

router = APIRouter()

@router.get('/{user_id}/new-propositions',response_model=List[UserModel])
def get_new_propositions(user_id : int,proposition_amount: int = 10, offset: int = 0):
    try:
        proposed_users = ConnectionService.get_new_proposition(
            db_session, 
            user_id,
            proposition_amount,
            offset
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return proposed_users

@router.post('/{user_id}/decide')
def decide_about_proposition(user_id: int, decision: DecisionModel):
    user = UserService.get_user(db_session, user_id)
    if user is None:
        raise HTTPException(status_code=400, detail="User doesnt exists.")
    try:
        ConnectionService.reg_propostion_result(
            decision.user_id,
            decision.proposed_user_id,
            decision.decision 
        )
        result = ConnectionService.check_if_match(
            decision.user_id,
            decision.proposed_user_id,
            decision.decision 
        )
        return Response(status_code=200, content=result)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))