from datetime import datetime, date, timedelta, time

from sqlalchemy.ext.asyncio import AsyncSession

from src.schemas import ScheduleGetSchema
from src.config import period  # начинал как временный
from src.repositories.schedule_repositoty import ScheduleRepository
from src.utils.round_minutes import round_minutes


class ScheduleService:
    """Место для вашей рекламы"""

    def __init__(self, session: AsyncSession):
        self.repository = ScheduleRepository(session=session)

    async def get_single_schedule(self, user_id: int, schedule_id: int):
        schedule = await self.repository.get_single_schedule(
            user_id=user_id,
            schedule_id=schedule_id,
        )
        return ScheduleGetSchema.model_validate(schedule) if schedule else None

    async def create_single_schedule(self, schedule: dict):
        return {
            "schedule_id": await self.repository.create_single_schedule(
                schedule=schedule
            )
        }

    async def get_schedules_list(self, user_id: int):
        schedules_list = await self.repository.get_schedules_list(user_id=user_id)
        return [
            ScheduleGetSchema.model_validate(schedule) for schedule in schedules_list
        ]

    async def get_next_takings(self, user_id: int):
        schedules_list = await self.repository.get_schedules_list_for_today(
            user_id=user_id
        )
        result = set()
        period_start = datetime.now()
        period_end = period_start + period
        notification_send_start = datetime.combine(date.today(), time(hour=8))
        for schedule in schedules_list:
            interval = timedelta(hours=14) / schedule.periodicity
            times = [
                round_minutes(notification_send_start + i * interval)
                for i in range(schedule.periodicity)
            ]
            for calculated_time in times:
                if period_start <= calculated_time <= period_end:
                    result.add(schedule.medicine_name)
        return list(result)
