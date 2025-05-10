from fastapi import APIRouter, Query, HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.schemas import ScheduleAddSchema
from app.services.schedule_service import ScheduleService

router = APIRouter(prefix="", tags=["Schedule"])


@router.get("/schedule")
async def get_single_schedule(
    session: AsyncSession = Depends(get_session),
    user_id: int | None = Query(None),
    schedule_id: int | None = Query(None),
):
    service = ScheduleService(session=session)
    return await service.get_single_schedule(user_id=user_id, schedule_id=schedule_id)


@router.post("/schedule")
async def create_single_schedule(
    schedule: ScheduleAddSchema, session: AsyncSession = Depends(get_session)
):
    return await ScheduleService(session=session).create_single_schedule(
        schedule=schedule
    )


@router.get("/schedules")
async def get_schedules_list(
    session: AsyncSession = Depends(get_session),
    user_id: int = Query(None),
):
    return await ScheduleService(session=session).get_schedules_list(user_id=user_id)


@router.get("/next_takings")
async def get_next_takings(
    session: AsyncSession = Depends(get_session),
    user_id: int = Query(None),
):
    return await ScheduleService(session=session).get_next_takings(user_id=user_id)
