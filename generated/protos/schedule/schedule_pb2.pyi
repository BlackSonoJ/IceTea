from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Schedule(_message.Message):
    __slots__ = ("id", "medicine_name", "periodicity", "receipt_duration_endless", "receipt_duration_end", "user_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    MEDICINE_NAME_FIELD_NUMBER: _ClassVar[int]
    PERIODICITY_FIELD_NUMBER: _ClassVar[int]
    RECEIPT_DURATION_ENDLESS_FIELD_NUMBER: _ClassVar[int]
    RECEIPT_DURATION_END_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    medicine_name: str
    periodicity: int
    receipt_duration_endless: bool
    receipt_duration_end: _timestamp_pb2.Timestamp
    user_id: int
    def __init__(self, id: _Optional[int] = ..., medicine_name: _Optional[str] = ..., periodicity: _Optional[int] = ..., receipt_duration_endless: bool = ..., receipt_duration_end: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[int] = ...) -> None: ...

class ScheduleAddSchema(_message.Message):
    __slots__ = ("medicine_name", "periodicity", "receipt_duration_endless", "receipt_duration_end", "user_id")
    MEDICINE_NAME_FIELD_NUMBER: _ClassVar[int]
    PERIODICITY_FIELD_NUMBER: _ClassVar[int]
    RECEIPT_DURATION_ENDLESS_FIELD_NUMBER: _ClassVar[int]
    RECEIPT_DURATION_END_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    medicine_name: str
    periodicity: int
    receipt_duration_endless: bool
    receipt_duration_end: _timestamp_pb2.Timestamp
    user_id: int
    def __init__(self, medicine_name: _Optional[str] = ..., periodicity: _Optional[int] = ..., receipt_duration_endless: bool = ..., receipt_duration_end: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[int] = ...) -> None: ...

class GetSingleScheduleRequest(_message.Message):
    __slots__ = ("user_id", "schedule_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    schedule_id: int
    def __init__(self, user_id: _Optional[int] = ..., schedule_id: _Optional[int] = ...) -> None: ...

class GetSingleScheduleResponse(_message.Message):
    __slots__ = ("schedule",)
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    schedule: Schedule
    def __init__(self, schedule: _Optional[_Union[Schedule, _Mapping]] = ...) -> None: ...

class CreateSingleScheduleRequest(_message.Message):
    __slots__ = ("schedule",)
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    schedule: ScheduleAddSchema
    def __init__(self, schedule: _Optional[_Union[ScheduleAddSchema, _Mapping]] = ...) -> None: ...

class CreateSingleScheduleResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class UserIdRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    def __init__(self, user_id: _Optional[int] = ...) -> None: ...

class GetSchedulesListResponse(_message.Message):
    __slots__ = ("schedules",)
    SCHEDULES_FIELD_NUMBER: _ClassVar[int]
    schedules: _containers.RepeatedCompositeFieldContainer[Schedule]
    def __init__(self, schedules: _Optional[_Iterable[_Union[Schedule, _Mapping]]] = ...) -> None: ...

class GetNextTakingsResponse(_message.Message):
    __slots__ = ("medicine_name",)
    MEDICINE_NAME_FIELD_NUMBER: _ClassVar[int]
    medicine_name: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, medicine_name: _Optional[_Iterable[str]] = ...) -> None: ...
