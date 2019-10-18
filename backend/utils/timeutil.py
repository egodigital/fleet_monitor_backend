from datetime import datetime
import math

from backend.core.globals_ import SMALLEST_TIME_UNIT

MINUTE_TO_TIME_SLOT_FACTOR = 1 / SMALLEST_TIME_UNIT
TIME_SLOT_TO_MINUTE_FACTOR = SMALLEST_TIME_UNIT
DAY_TO_MINUTES_FACTOR = 1440
HOUR_TO_MINUTE_FACTOR = 60
MINUTE_TO_SECOND_FACTOR = 60
SECOND_TO_MINUTE_FACTOR = 1/60
MINUTE_TO_HOUR_FACTOR = 1/60


def days_to_time_slots(amount: int) -> int:
    return minutes_to_time_slots(
        amount * DAY_TO_MINUTES_FACTOR
    )


def minutes_to_time_slots(amount: int) -> int:
    return amount * MINUTE_TO_TIME_SLOT_FACTOR


def time_slots_to_minutes(amount: int) -> int:
    return amount * TIME_SLOT_TO_MINUTE_FACTOR


def days_to_minutes(amount: int) -> int:
    return amount * DAY_TO_MINUTES_FACTOR


def hours_to_minutes(amount: float) -> int:
    return int(amount * HOUR_TO_MINUTE_FACTOR)


def seconds_to_minutes(amount: int) -> int:
    return amount * SECOND_TO_MINUTE_FACTOR


def minutes_to_hours(amount: int) -> float:
    return amount * MINUTE_TO_HOUR_FACTOR


def datetimes_to_time_slots(t1: datetime, t2:
                            datetime) -> int:
    delta = t2 - t1
    seconds = delta.total_seconds()
    minutes = seconds_to_minutes(seconds)
    booking_slots = int(minutes_to_time_slots(minutes))
    return booking_slots


def _round_up_to_next_15_minutes(d: datetime) -> datetime:
    minutes = round(d.minute)
    if minutes == 0:
        d = d.replace(second=0)
    elif minutes < 15:
        d = d.replace(minute=15, second=0)
    elif minutes < 30:
        d = d.replace(minute=30, second=0)
    elif minutes < 45:
        d = d.replace(minute=45, second=0)
    else:
        d = d.replace(hour=d.hour+1, minute=0, second=0)
    return d


def get_current_time() -> datetime:
    return datetime.now()


def get_start_time() -> datetime:
    d = get_current_time()
    d = _round_up_to_next_15_minutes(datetime.now())
    date_str = d.strftime("%Y-%m-%d %H:%M:%S")
    return datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")


def timestamp_to_datetime(timestamp: int) -> datetime:
    return datetime.fromtimestamp(timestamp)
