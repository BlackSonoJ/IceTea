from datetime import date, datetime, time

from google.protobuf.timestamp_pb2 import Timestamp


def date_to_timestapm(d: date):
    if d:
        ts = Timestamp()
        ts.FromDatetime(datetime.combine(d, time.min))
        return ts


def timestamp_to_date(ts: Timestamp):
    if ts:
        dt = ts.ToDatetime()
        return date(year=dt.year, month=dt.month, day=dt.day)
