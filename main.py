from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables
from router import router  # импортируем router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    print("DB is ready")
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(router)  # подключаем router

@app.get("/")
async def home():
    return {"data": "Hello World"}