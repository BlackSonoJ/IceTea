from datetime import datetime, timedelta

from app.models.schedule import Schedule
from app.utils.round_minutes import round_minutes


def get_schedule_next_takings(
    period: timedelta,
    period_start: datetime,
    notification_send_start: datetime,
    schedule: Schedule,
):
    period_end = period_start + period
    interval = timedelta(hours=14) / schedule.periodicity
    times = [
        round_minutes(notification_send_start + i * interval)
        for i in range(schedule.periodicity)
    ]
    result = []
    for calculated_time in times:
        if period_start <= calculated_time <= period_end:
            result.append(
                {
                    "medicine_name": schedule.medicine_name,
                    "calculated_time": calculated_time,
                }
            )
    return result
