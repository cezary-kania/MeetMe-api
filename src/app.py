from fastapi import FastAPI

from Routers.UsersRouter import router as users_router

app = FastAPI()

app.include_router(
    users_router, 
    prefix='/user', 
    tags=['User']
)