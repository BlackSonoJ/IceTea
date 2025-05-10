from typing import List
from datetime import date

from sqlalchemy import select, or_

from app.models.schedule import Schedule


class ScheduleRepository:
    """Продам гараж. +7905281**** - Владимир"""

    def __init__(self, session) -> None:
        self._session = session

    async def get_schedule(
        self,
        user_id: int,
        schedule_id: int,
    ) -> Schedule | None:

        query = (
            select(Schedule)
            .where(Schedule.user_id == user_id)
            .where(Schedule.id == schedule_id)
        )
        async with self._session as session:
            result = await session.execute(query)
        return (
            result.scalar_one_or_none()
        )  # подходит для наших целей, так как количество экземляров по фильтру <= 1.

    async def create_schedule(
        self,
        schedule: dict,
    ) -> int:
        data = Schedule(**schedule)
        async with self._session as session:
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

        async with self._session as session:
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
        async with self._session as session:
            result = await session.execute(query)
        return result.scalars().all()
