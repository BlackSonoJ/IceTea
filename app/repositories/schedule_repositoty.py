from typing import Dict, List
from datetime import date

from sqlalchemy import select, or_
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Schedule
from app.schemas import ScheduleAddSchema


class ScheduleRepository:
    """Продам гараж. +7905281**** - Владимир"""

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_single_schedule(
        self,
        user_id: int,
        schedule_id: int,
    ) -> Schedule | None:

        query = (
            select(Schedule)
            .where(Schedule.user_id == user_id)
            .where(Schedule.id == schedule_id)
        )
        async with self.session as session:
            result = await session.execute(query)
        return (
            result.scalar_one_or_none()
        )  # если нет совпадений, вернет None, иначе первый в списке (а у на с список всегда из 1)

    async def create_single_schedule(self, schedule: ScheduleAddSchema) -> Dict:

        data = Schedule(  # мысль распаковать пришла сильно позже...
            medicine_name=schedule.medicine_name,
            periodicity=schedule.periodicity,
            receipt_duration_endless=schedule.receipt_duration_endless,
            receipt_duration_end=schedule.receipt_duration_end,
            user_id=schedule.user_id,
        )
        async with self.session as session:
            session.add(data)
            await session.flush()
            schedule_id = data.id
            await session.commit()
        return schedule_id

    async def get_schedules_list(
        self,
        user_id: int,
    ) -> List[Schedule]:

        query = select(Schedule)
        if user_id is not None:
            query = query.where(Schedule.user_id == user_id)

        async with self.session as session:
            result = await session.execute(query)
        return result.scalars().all()

    async def get_schedules_list_for_today(
        self,
        user_id: int,
    ) -> List[Schedule]:

        query = select(Schedule)
        if user_id is not None:
            query = query.where(Schedule.user_id == user_id).where(
                or_(
                    Schedule.receipt_duration_endless,
                    Schedule.receipt_duration_end >= date.today(),
                ),
            )
        async with self.session as session:
            result = await session.execute(query)
        return result.scalars().all()
