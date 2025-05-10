from contextlib import asynccontextmanager

from fastapi import FastAPI


from app.db.session import get_engine
from app.db.base import Base
from app.transports.views.schedule.views import router as schedule_router
from app.core.middlewares import schedule_middleware


@asynccontextmanager
async def _lifespan(app: FastAPI):
    engine = get_engine()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        yield
    await engine.dispose()


app = FastAPI(lifespan=_lifespan)

app.include_router(schedule_router)

app.add_middleware(schedule_middleware.LoggingMiddleware)
