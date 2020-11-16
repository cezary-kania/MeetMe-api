from fastapi import FastAPI, APIRouter

from Routers.UsersRouter import router as users_router
from Routers.ConnectionsRouter import router as connections_router

app = FastAPI()

router = APIRouter()

 
router.include_router(
    users_router, 
    prefix='/user', 
    tags=['User']
)

router.include_router(
    connections_router, 
    prefix='/connections', 
    tags=['Connections']
)

app.include_router(
    router,
    prefix='/api'
)
