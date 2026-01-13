from fastapi import FastAPI
from app.database import Base, engine
from app.routers import user

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI + PostgreSQL App")

app.include_router(user.router)

@app.get("/")
def root():
    return {"status": "API running"}
