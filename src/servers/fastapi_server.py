from contextlib import asynccontextmanager

from fastapi import FastAPI


from src.database import get_engine, Base
from src.api import schedule_routes


@asynccontextmanager
async def lifespan(app: FastAPI):
    engine = get_engine()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        yield
    await engine.dispose()


app = FastAPI(lifespan=lifespan)
app.include_router(schedule_routes.router)
