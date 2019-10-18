from datetime import datetime
import math

from .assumptions import SMALLEST_TIME_UNIT

DAY_TO_MINUTES_FACTOR = 1440
HOUR_TO_MINUTE_FACTOR = 60
SECOND_TO_MINUTE_FACTOR = 1/60
MINUTE_TO_HOUR_FACTOR = 1/60


def booking_time_slots_to_minutes(amount: int) -> int:
    return amount * SMALLEST_TIME_UNIT


def minutes_to_hours(amount: int) -> float:
    return amount * MINUTE_TO_HOUR_FACTOR


def hours_to_minutes(amount: float) -> int:
    return int(amount * HOUR_TO_MINUTE_FACTOR)


def datetimes_to_time_slots(start_time: datetime, end_time:
                            datetime) -> int:
    delta = end_time - start_time
    seconds = delta.total_seconds()
    minutes = int(seconds * SECOND_TO_MINUTE_FACTOR)
    booking_slots = minutes / BOOKING_TIME_SMALLEST_UNIT
    return booking_slots
