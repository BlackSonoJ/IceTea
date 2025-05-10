from datetime import datetime, timedelta


def round_minutes(dt: datetime, round_interval: int = 15) -> datetime:
    minutes_to_be_added = (
        round_interval - dt.minute % round_interval
        if dt.minute % round_interval > 0
        else 0
    )
    return (
        dt + timedelta(minutes=minutes_to_be_added) if minutes_to_be_added > 0 else dt
    )
