from typing import Annotated

from fastapi import APIRouter, Query, Depends

from app.schemas.schedule import (
    SchedulePostRequest,
    ScheduleGet,
    SchedulePostResponse,
    NextTaking,
    UserIdParam,
    UserIdScheduleIdParams,
)
from app.services.schedule_service import ScheduleService

router = APIRouter(prefix="", tags=["Schedule"])


@router.get("/schedule", response_model=ScheduleGet)
async def get_single_schedule(
    query: Annotated[UserIdScheduleIdParams, Query()],
    schedule_service: Annotated[ScheduleService, Depends(ScheduleService)],
):
    return await schedule_service.get_schedule(
        **query.model_dump(),  # как говорил великий: "Распакоука, на*уй"
    )


@router.post("/schedule", response_model=SchedulePostResponse)
async def create_single_schedule(
    schedule: SchedulePostRequest,
    schedule_service: Annotated[ScheduleService, Depends(ScheduleService)],
) -> SchedulePostResponse:
    return SchedulePostResponse(
        schedule_id=await schedule_service.create_schedule(
            schedule=schedule.model_dump(),
        )
    )


@router.get("/schedules", response_model=list[ScheduleGet])
async def get_schedules_list(
    query: Annotated[UserIdParam, Query()],
    schedule_service: Annotated[ScheduleService, Depends(ScheduleService)],
):
    return await schedule_service.get_schedules_list(
        **query.model_dump(),
    )


@router.get("/next_takings", response_model=list[NextTaking])
async def get_next_takings(
    query: Annotated[UserIdParam, Query()],
    schedule_service: Annotated[ScheduleService, Depends(ScheduleService)],
):
    return await schedule_service.get_next_takings(
        **query.model_dump(),
    )
