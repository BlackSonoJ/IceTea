from datetime import date, time, datetime, timedelta

from fastapi import APIRouter, Query
from sqlalchemy import select, or_


from models import Schedule
from .dependencies import SessionDepends
from config import period

router = APIRouter(prefix="/next_takings", tags=["Next taking"])


def round_minutes(dt: datetime, round_interval: int = 15) -> datetime:
    # высчитываем количество минут с 00:00 и округляем вверх (-1 нужно, чтобы не перескачить на интервал вперед)
    rounded_minutes = (
        (dt.hour * 60 + dt.minute + round_interval - 1) // round_interval
    ) * round_interval
    return dt.replace(hour=rounded_minutes // 60, minute=rounded_minutes % 60)


@router.get("/")
async def get_single_schedule(
    session: SessionDepends,
    user_id: int | None = Query(None),
):
    query = (
        select(Schedule)
        .where(Schedule.user_id == user_id)
        .where(
            or_(
                Schedule.receipt_duration_endless,
                Schedule.receipt_duration_end >= date.today(),
            )
        )
    )
    period_start = datetime.now()
    # period_start = datetime.now().replace(hour=9)
    period_end = period_start + period
    notification_send_start = datetime.combine(date.today(), time(hour=8))
    medicine_list = await session.execute(query)
    schedule_list = medicine_list.scalars().all()
    result = set()
    for schedule in schedule_list:
        interval = timedelta(hours=14) / schedule.periodicity
        times = [
            round_minutes(notification_send_start + i * interval)
            for i in range(schedule.periodicity)
        ]
        for calculated_time in times:
            if period_start <= calculated_time <= period_end:
                result.add(schedule.medicine_name)

    return list(result)
