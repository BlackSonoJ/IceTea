from datetime import datetime, timedelta

from app.models.schedule import Schedule
from app.utils.count_next_takings import get_schedule_next_takings


def test_base():
    notification_send_start = datetime(year=2025, month=1, day=1, hour=8)
    period = timedelta(hours=1)
    schedule = Schedule(
        id=1,
        medicine_name="string",
        periodicity=1,
        receipt_duration_endless=True,
        receipt_duration_end=None,
        user_id=1,
    )
    result = get_schedule_next_takings(
        period=period,
        period_start=notification_send_start,
        notification_send_start=notification_send_start,
        schedule=schedule,
    )
    assert result == [
        {
            "medicine_name": "string",
            "calculated_time": notification_send_start,
        },
    ]


def test_outside_period():
    notification_send_start = datetime(year=2025, month=1, day=1, hour=8)
    period = timedelta(hours=1)
    schedule = Schedule(
        id=1,
        medicine_name="string",
        periodicity=1,
        receipt_duration_endless=True,
        receipt_duration_end=None,
        user_id=1,
    )
    result = get_schedule_next_takings(
        period=period,
        period_start=datetime(year=2025, month=1, day=1, hour=9),
        notification_send_start=notification_send_start,
        schedule=schedule,
    )

    assert len(result) == 0


def test_several_timestamps():
    notification_send_start = datetime(year=2025, month=1, day=1, hour=8)
    period = timedelta(hours=1)
    schedule = Schedule(
        id=1,
        medicine_name="string",
        periodicity=15,
        receipt_duration_endless=True,
        receipt_duration_end=None,
        user_id=1,
    )
    result = get_schedule_next_takings(
        period=period,
        period_start=datetime(year=2025, month=1, day=1, hour=9),
        notification_send_start=notification_send_start,
        schedule=schedule,
    )

    assert len(result) == 2
