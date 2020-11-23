from sqlalchemy.orm import Session

from Data.ConnectionsDatabase import connections_db
from Models.Connections.Connection import Connection, ConnectDecision


from Models.Users import (
    User, 
    UserPersonalInfo
)

from Services.UserService import UserService

class ConnectionService:

    @staticmethod
    def get_new_proposition(db_session : Session, user_id : int):
        user = UserService.get_user(db_session, user_id)
        if user is None: 
            raise Exception('User doesn\'t exists')
        user_search_settings = user.searchSettings
        if user_search_settings is None: 
            raise Exception('User search settings don\'t exists')
        new_propositions = db_session.query(User) \
            .join(UserPersonalInfo) \
            .filter(UserPersonalInfo.gender == user_search_settings.gender_preferences.value) \
            .filter(UserPersonalInfo.age.between(user_search_settings.minAge, user_search_settings.maxAge)) \
            .filter(User.id != user.id) \
            .all()
        return new_propositions
