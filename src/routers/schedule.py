"""
Обрабатываем запросы, содержащие информацию о модели Schedule
обрабатывается один объект за запрос (POST и GET)
"""

from fastapi import APIRouter, Query, HTTPException
from sqlalchemy import select

from schemas import ScheduleAddSchema
from models import Schedule
from .dependencies import SessionDepends


router = APIRouter(prefix="/schedule", tags=["Schedule"])


@router.get("/")
async def get_single_schedule(
    session: SessionDepends,
    user_id: int | None = Query(None),
    schedule_id: int | None = Query(None),
):
    query = (
        select(Schedule)
        .where(Schedule.user_id == user_id)
        .where(Schedule.id == schedule_id)
    )

    result = await session.execute(query)
    schedule = result.scalar()
    if not schedule:
        raise HTTPException(
            status_code=204,
            detail=f"For user with id {user_id} schedule with id {schedule_id} was not found",
        )
    return schedule


@router.post("/")
async def create_single_schedule(schedule: ScheduleAddSchema, session: SessionDepends):
    """
    Добавление в таблицу schedule бд
    возвращаем id
    """
    schedule = Schedule(
        medicine_name=schedule.medicine_name,
        periodicity=schedule.periodicity,
        receipt_duration_endless=schedule.receipt_duration_endless,
        receipt_duration_end=schedule.receipt_duration_end,
        user_id=schedule.user_id,
    )

    async with session.begin():
        session.add(schedule)
        await session.flush()
        schedule_id = schedule.id
        await session.commit()
    return {"schedule_id": schedule_id}
