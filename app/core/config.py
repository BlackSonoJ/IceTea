from datetime import timedelta
from functools import lru_cache
from pydantic_settings import BaseSettings

period = timedelta(hours=1)


# class AppSettings(BaseSettings):
#     app_name: str = "Aibolit API"
#     next_takings_count_period: timedelta = timedelta(hours=1)


# class EnvSettings(BaseSettings): ...


# def get_app_settings() -> AppSettings:
#     return AppSettings()
