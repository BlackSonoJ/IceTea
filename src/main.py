from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn


from models import Base
from database import get_engine
from routers import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    engine = get_engine()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        yield
    await engine.dispose().ispose()


app = FastAPI(lifespan=lifespan)
app.include_router(router)


if __name__ == "__main__":
    uvicorn.run("main:app")
