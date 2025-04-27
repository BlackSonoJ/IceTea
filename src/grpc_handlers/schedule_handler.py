from datetime import datetime, time

from google.protobuf.timestamp_pb2 import Timestamp

from generated.protos.schedule import schedule_pb2_grpc, schedule_pb2
from src.services.schedule_service import ScheduleService

from src.utils import date_converter


class ScheduleServer(schedule_pb2_grpc.ScheduleServerServicer):

    def __init__(
        self, session
    ):  # смотришь на это и думаешь, почему в книге было про grpc около страницы
        self.service = ScheduleService(session=session)

    async def GetSingleSchedule(self, request, context):

        schedule = await self.service.get_single_schedule(
            user_id=request.user_id,
            schedule_id=request.schedule_id,
        )

        if schedule is None:
            return schedule_pb2.GetSingleScheduleResponse()

        result = schedule_pb2.Schedule(
            id=schedule.id,
            medicine_name=schedule.medicine_name,
            periodicity=schedule.periodicity,
            receipt_duration_endless=schedule.receipt_duration_endless,
            user_id=schedule.user_id,
        )

        if schedule.receipt_duration_end:
            result.receipt_duration_end.CopyFrom(
                date_converter.date_to_timestapm(schedule.receipt_duration_end)
            )

        return schedule_pb2.GetSingleScheduleResponse(schedule=result)

    async def CreateSingleSchedule(self, request, context):
        temp = request.schedule
        schedule = {
            "medicine_name": temp.medicine_name,
            "periodiicity": temp.periodicity,
            "receipt_duration_endless": temp.receipt_duration_endless,
            "receipt_duration_end": (
                temp.receipt_duration_end.toDatetime()
                if temp.HasField("receipt_duration_end")
                else None
            ),
            "user_id": temp.user_id,
        }
        result = await self.service.create_single_schedule(
            schedule=schedule
        )  # передаем dict, так что схему редактивать не пришлось
        return schedule_pb2.CreateSingleScheduleResponse(id=result["schedule_id"])

    async def GetSchedulesList(self, request, context):
        schedules_list = await self.service.get_schedules_list(user_id=request.user_id)
        result = []

        for schedule in schedules_list:
            proto_schedule = schedule_pb2.Schedule()
            proto_schedule.id = schedule.id
            proto_schedule.medicine_name = schedule.medicine_name
            proto_schedule.periodicity = schedule.periodicity
            proto_schedule.receipt_duration_endless = schedule.receipt_duration_endless
            proto_schedule.user_id = schedule.user_id

            if schedule.receipt_duration_end:
                proto_schedule.receipt_duration_end.CopyFrom(
                    date_converter.date_to_timestapm(schedule.receipt_duration_end)
                )

            result.append(proto_schedule)

        return schedule_pb2.GetSchedulesListResponse(schedules=result)

    async def GetNextTakings(self, request, context):
        return schedule_pb2.GetNextTakingsResponse(
            medicine_name=await self.service.get_next_takings(user_id=request.user_id)
        )
