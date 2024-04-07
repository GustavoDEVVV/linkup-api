from fastapi import FastAPI
from api.main import api_router
from core.database import Base, engine

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(api_router)
