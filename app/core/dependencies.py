from typing import Annotated, Any

from fastapi import Depends

from app.db.session import get_session
from app.integrations.schedule_repo import ScheduleRepository


def get_schedule_repo(
    session: Annotated[Any, Depends(get_session)],
) -> ScheduleRepository:
    return ScheduleRepository(session)
