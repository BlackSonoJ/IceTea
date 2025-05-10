from datetime import datetime, date, timedelta, time
from typing import Annotated

from fastapi.params import Depends

from app.schemas.schedule import ScheduleGet, NextTaking
from app.core.config import period
from app.integrations.schedule_repo import ScheduleRepository
from app.utils.count_next_takings import get_schedule_next_takings
from app.core.dependencies import get_schedule_repo


class ScheduleService:
    """Место для вашей рекламы"""

    def __init__(
        self,
        repository: Annotated[ScheduleRepository, Depends(get_schedule_repo)],
    ):
        self._repository = repository

    async def get_schedule(self, user_id: int, schedule_id: int) -> ScheduleGet | None:
        schedule = await self._repository.get_schedule(
            user_id=user_id,
            schedule_id=schedule_id,
        )
        return ScheduleGet.model_validate(schedule) if schedule else None

    async def create_schedule(self, schedule: dict) -> int:
        return await self._repository.create_schedule(schedule=schedule)

    async def get_schedules_list(self, user_id: int) -> list[ScheduleGet]:
        schedules_list = await self._repository.get_schedules_list(user_id=user_id)
        return [ScheduleGet.model_validate(schedule) for schedule in schedules_list]

    async def get_next_takings(
        self,
        user_id: int,
        period_start: datetime = None,
        notification_send_start=None,
    ) -> list[dict]:
        schedules_list = await self._repository.get_schedules_list_for_today(
            user_id=user_id
        )
        result = []
        for schedule in schedules_list:
            result.extend(
                get_schedule_next_takings(
                    period=period,
                    period_start=period_start if period_start else datetime.now(),
                    notification_send_start=(
                        notification_send_start
                        if notification_send_start
                        else datetime.combine(
                            date=date.today(),
                            time=time(hour=8),
                        )
                    ),
                    schedule=schedule,
                ),
            )
        return result
