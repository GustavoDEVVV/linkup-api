from fastapi import FastAPI
from database.connection import engine, Base

from src.routers.post_routers import post_router
from src.routers.user_routers import user_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post_router)
app.include_router(user_router)
