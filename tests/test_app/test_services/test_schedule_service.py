from datetime import datetime
from unittest.mock import AsyncMock

import pytest

from app.services.schedule_service import ScheduleService
from app.models.schedule import Schedule
from app.schemas.schedule import ScheduleGet


@pytest.mark.asyncio
async def test_get_schedule():
    mock_repo = AsyncMock()
    mock_repo_return_value = Schedule(
        id=1,
        medicine_name="string",
        periodicity=1,
        receipt_duration_endless=True,
        receipt_duration_end=None,
        user_id=1,
    )
    mock_repo.get_schedule.return_value = mock_repo_return_value
    service = ScheduleService(repository=mock_repo)

    result = await service.get_schedule(user_id=1, schedule_id=1)

    assert result == ScheduleGet(
        id=1,
        medicine_name="string",
        periodicity=1,
        receipt_duration_endless=True,
        receipt_duration_end=None,
        user_id=1,
    )
    mock_repo.get_schedule.assert_awaited_once_with(user_id=1, schedule_id=1)


# где-то здесь должен был быть тест для create_schedule,
# но так как в нем после моков не остается никакой логики, его не будет


@pytest.mark.asyncio
async def test_get_schedules_list():
    mock_repo = AsyncMock()
    mock_repo_return_value = [
        Schedule(
            id=1,
            medicine_name="string",
            periodicity=1,
            receipt_duration_endless=True,
            receipt_duration_end=None,
            user_id=1,
        ),
    ]
    mock_repo.get_schedules_list.return_value = mock_repo_return_value

    service = ScheduleService(repository=mock_repo)
    result = await service.get_schedules_list(user_id=1)
    assert result == [
        ScheduleGet(
            id=1,
            medicine_name="string",
            periodicity=1,
            receipt_duration_endless=True,
            receipt_duration_end=None,
            user_id=1,
        ),
    ]
    mock_repo.get_schedules_list.assert_awaited_once_with(user_id=1)


@pytest.mark.xfail
@pytest.mark.asyncio
async def test_get_next_takings():
    mock_repo = AsyncMock()
    mock_repo_return_value = [
        Schedule(
            id=1,
            medicine_name="string",
            periodicity=1,
            receipt_duration_endless=True,
            receipt_duration_end=None,
            user_id=1,
        ),
    ]
    mock_repo.get_schedule_list_for_today.return_value = mock_repo_return_value

    service = ScheduleService(repository=mock_repo)
    result = await service.get_next_takings(
        user_id=1,
        period_start=datetime(year=2025, month=1, day=1, hour=8),
        notification_send_start=datetime(year=2025, month=1, day=1, hour=8),
    )

    assert len(result) == 1

    mock_repo.get_next_takings.assert_awaited_once_with(
        user_id=1,
        period_start=datetime(year=2025, month=1, day=1, hour=8),
        notification_send_start=datetime(year=2025, month=1, day=1, hour=8),
    )
