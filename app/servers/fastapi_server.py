from contextlib import asynccontextmanager

from fastapi import FastAPI


from app.database import get_engine, Base
from app.api import schedule_routes
from app.middleware import LoggingMiddleware
from app.logger import logger_setup

logger_setup.configure_logging()


@asynccontextmanager
async def lifespan(app: FastAPI):
    engine = get_engine()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        yield
    await engine.dispose()


app = FastAPI(lifespan=lifespan)

app.add_middleware(LoggingMiddleware)

app.include_router(schedule_routes.router)
