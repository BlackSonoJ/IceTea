from fastapi import APIRouter

from routers.schedule import router as single_schedule_router
from routers.schedules import router as schedule_list_router
from routers.next_takings import router as next_takings_router

router = APIRouter()

router.include_router(single_schedule_router)
router.include_router(schedule_list_router)
router.include_router(next_takings_router)
