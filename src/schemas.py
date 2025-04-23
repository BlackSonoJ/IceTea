from typing import Optional
from datetime import date

from pydantic import BaseModel, ConfigDict


class ScheduleAddSchema(BaseModel):
    medicine_name: str
    periodicity: int
    receipt_duration_endless: bool = False
    receipt_duration_end: Optional[date] = None
    user_id: int


class ScheduleGetSchema(ScheduleAddSchema):
    id: int

    model_config = ConfigDict(from_attributes=True)
