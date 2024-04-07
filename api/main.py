from fastapi import APIRouter
from api.routes import login, users
from core.database import Base, engine
from api.models.users import UserModel  # Não remova, dependencia de Base

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

api_router = APIRouter()
api_router.include_router(login.router)
api_router.include_router(users.router)
