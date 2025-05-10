"""В моменте этот файл стал чистилищем, успею, приведу в порядок"""

from typing import Optional
from datetime import date, datetime

from pydantic import BaseModel, ConfigDict, Field


class ScheduleGet(BaseModel):
    # знаю, можно отнаследоваться от схемы SchedulePostRequest, но не буду
    id: int = Field(gt=0)
    medicine_name: str
    periodicity: int = Field(gt=0)
    receipt_duration_endless: bool = False
    receipt_duration_end: Optional[date] = None
    user_id: int = Field(gt=0)

    model_config = ConfigDict(from_attributes=True)


class SchedulePostResponse(BaseModel):
    schedule_id: int


class SchedulePostRequest(BaseModel):
    medicine_name: str
    periodicity: int = Field(gt=0)
    receipt_duration_endless: bool = False
    receipt_duration_end: Optional[date] = None
    user_id: int = Field(gt=0)


class NextTaking(BaseModel):
    medicine_name: str
    calculated_time: datetime


class UserIdParam(BaseModel):
    user_id: int = Field(gt=0)


class ScheduleIdParam(BaseModel):
    schedule_id: int = Field(gt=0)


class UserIdScheduleIdParams(UserIdParam, ScheduleIdParam): ...
