from fastapi import FastAPI, APIRouter

from .UsersRouter import router as users_router
from .ConnectionsRouter import router as connections_router

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