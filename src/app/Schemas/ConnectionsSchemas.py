from pydantic import BaseModel

from app.Models.Connections.Connection import ConnectDecision

class DecisionModel(BaseModel):
    user_id : int
    proposed_user_id: int
    decision: ConnectDecision
