from fastapi import FastAPI
from app.controllers import parajes_router
from app.repositories.database import Base,engine

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(router=parajes_router, prefix=f"/api/v1")

