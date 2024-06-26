from fastapi import FastAPI

from contextlib import asynccontextmanager

from database import create_tables, delete_tables
from router import router as users_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    #выполняется при старте проекта
    await delete_tables()
    print("База очищена")
    await create_tables()
    print("База готова")
    yield
    #выполняется по завершению
    print("Выключение")


app = FastAPI(lifespan=lifespan)
app.include_router(users_router)

