"""
Обрабатываем запросы, содержащие информацию о модели Schedule
обрабатывается список объектов (GET)
"""

from fastapi import APIRouter, Query, HTTPException
from sqlalchemy import select

from models import Schedule
from .dependencies import SessionDepends


router = APIRouter(prefix="/schedules", tags=["Schedule"])


@router.get("/")
async def get_schedules_list(
    session: SessionDepends,
    user_id: int = Query(None),
):
    """
    Обрабатываем запросы вида
    GET /schedules - возвращаем всю таблицу
    GET /schedules?user_id= - фильруем по пользователю
    возвращаем список данных
    """
    query = select(Schedule)

    if user_id is not None:
        # TODO: убрать проверку на is not None когда будет реализованна проверка на положительные id пользователей
        query = query.where(Schedule.user_id == user_id)

    result = await session.execute(query)
    schedules = result.scalars().all()
    if not schedules:
        raise HTTPException(status_code=204, detail="No data to return")
    return schedules
