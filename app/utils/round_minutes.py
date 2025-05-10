from datetime import datetime


def round_minutes(dt: datetime, round_interval: int = 15) -> datetime:
    # высчитываем количество минут с 00:00 и округляем вверх (-1 нужно, чтобы не перескачить на интервал вперед)
    rounded_minutes = (
        (dt.hour * 60 + dt.minute + round_interval - 1) // round_interval
    ) * round_interval
    return dt.replace(hour=rounded_minutes // 60, minute=rounded_minutes % 60)
