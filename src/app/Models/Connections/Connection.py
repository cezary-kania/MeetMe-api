from pydantic import BaseModel
from enum import Enum

class ConnectDecision(Enum):
    accepted = 'accepted'
    rejected = 'rejected'

class Connection(BaseModel):
    user_id : int
    proposed_user_id : int
    decision : ConnectDecision