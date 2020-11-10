from Services.UserService import UserService
from Models.Users import *
from users_db import Base, engine, SessionLocal

Base.metadata.create_all(bind = engine)

db_session = SessionLocal()

print(UserService.get_all_users(db_session))

