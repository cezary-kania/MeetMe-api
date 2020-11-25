from sqlalchemy.orm import Session

from app.Data.ConnectionsDatabase import connections_col, matches_col
from app.Models.Connections.Connection import Connection, ConnectDecision


from app.Models.Users import (
    User, 
    UserPersonalInfo,
    UserSearchSettings
)

from app.Services.UserService import UserService
from app.Models.Connections.Connection import ConnectDecision

class ConnectionService:

    @staticmethod
    def get_new_proposition(db_session : Session, user_id : int, proposition_amount: int, offset: int):
        user = UserService.get_user(db_session, user_id)
        if user is None: 
            raise Exception('User doesn\'t exists')
        user_search_settings = user.searchSettings
        if user_search_settings is None: 
            raise Exception('User search settings don\'t exists')
        new_propositions = db_session.query(User) \
            .join(UserPersonalInfo) \
            .join(UserSearchSettings) \
            .filter(UserPersonalInfo.gender == user_search_settings.gender_preferences.value) \
            .filter(UserPersonalInfo.age.between(user_search_settings.minAge, user_search_settings.maxAge)) \
            .filter(User.id != user.id) \
            .filter(UserSearchSettings.haversine(user_search_settings) <= user_search_settings.distance) \
            .order_by(User.id.asc()) \
            .limit(proposition_amount) \
            .offset(offset) \
            .all()
        for proposed_user in new_propositions:
            if ConnectionService.find_in_old_propositions(user.id, proposed_user.id).count() > 0:
                new_propositions.remove(proposed_user)
        return new_propositions
    

    @staticmethod
    def reg_propostion_result(user_id: int, proposed_user_id: int, decision: ConnectDecision):
        import datetime
        decision = {
            'user_id' : user_id,
            'proposed_user_id' : proposed_user_id,
            'decision' : decision.value,
            'date': datetime.datetime.utcnow()
        }
        connections_col.insert_one(decision)
        
    @staticmethod
    def check_if_match(user_id: int, proposed_user_id: int, decision: ConnectDecision):
        if decision.value == 'rejected': return False
        prev_accepted_connections = list(connections_col.find(
            {
                'user_id': proposed_user_id,
                'proposed_user_id' : user_id,
                'decision' : 'accepted'
            }
        ))
        lastOpositeSiteList = sorted(prev_accepted_connections, key=lambda dec: dec['date'], reverse=True)
        lastOpositeSiteDec = None
        if(len(lastOpositeSiteList) >= 1):
            lastOpositeSiteDec = lastOpositeSiteList[0]
        if lastOpositeSiteDec is None:
            return False
        else:
            import datetime
            matches_col.insert(
                {
                    'user1' : user_id,
                    'user2' : proposed_user_id,
                    'status' : 'active',
                    'date': datetime.datetime.utcnow()
                }
            )
            return True
    @staticmethod
    def find_in_old_propositions(user_id: int, proposed_user_id: int):
        return connections_col.find({'user_id' : user_id, 'proposed_user_id' : proposed_user_id})
        
