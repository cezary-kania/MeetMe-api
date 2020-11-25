from pydantic import BaseModel
import datetime
from app.Models.Connections.Connection import ConnectDecision

class DecisionModel(BaseModel):
    user_id : int
    proposed_user_id: int
    decision: ConnectDecision

class MatchModel(BaseModel):
    user1 : int
    user2 : int
    status_for_user_1 : str
    status_for_user_2 : str
    status : str
    date : datetime.datetime
    id : str

def parseMatchDict(matchDict : dict):
    matchDict['id'] = str(matchDict['_id'])
    return MatchModel.parse_obj(matchDict)    