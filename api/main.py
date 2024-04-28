from fastapi import APIRouter

from api.models.users import UserModel  # Não remova, dependencia de Base
from api.models.posts import PostModel  # Não remova, dependencia de Base
from api.models.reactions import ReactionModel  # Não remova, dependencia de Base
from api.routes import auth, reactions, users, posts
from core.database import Base, engine
from core.init_data import init_db

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

api_router = APIRouter()
api_router.include_router(auth.router)
api_router.include_router(users.router)
api_router.include_router(posts.router)
api_router.include_router(reactions.router)


@api_router.on_event('startup')
async def startup():
    await init_db()
