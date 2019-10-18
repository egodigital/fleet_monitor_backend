from datetime import datetime
import math

from backend.core.globals import SMALLEST_TIME_UNIT

MINUTE_TO_TIME_SLOT_FACTOR = 1 / SMALLEST_TIME_UNIT
TIME_SLOT_TO_MINUTE_FACTOR = SMALLEST_TIME_UNIT
DAY_TO_MINUTES_FACTOR = 1440
HOUR_TO_MINUTE_FACTOR = 60
SECOND_TO_MINUTE_FACTOR = 1/60
MINUTE_TO_HOUR_FACTOR = 1/60


def minutes_to_time_slots(amount: int) -> int:
    return amount * MINUTE_TO_TIME_SLOT_FACTOR


def time_slots_to_minutes(amount: int) -> int:
    return amount * TIME_SLOT_TO_MINUTE_FACTOR


def days_to_minutes(amount: int) -> int:
    return amount * DAY_TO_MINUTES_FACTOR


def hours_to_minutes(amount: float) -> int:
    return int(amount * HOUR_TO_MINUTE_FACTOR)


def seconds_to_minutes(amount: int) -> int:
    return int(amount * SECOND_TO_MINUTE_FACTOR)


def minutes_to_hours(amount: int) -> float:
    return amount * MINUTE_TO_HOUR_FACTOR


def datetimes_to_time_slots(t1: datetime, t2:
                            datetime) -> int:
    delta = t2 - t1
    seconds = delta.total_seconds()
    minutes = seconds_to_minutes(seconds)
    booking_slots = minutes_to_time_slots(minutes)
    return booking_slots
