from fastapi import FastAPI
from .Routers import router as api_router

app = FastAPI()

app.include_router(
    api_router,
    prefix='/api'
)
