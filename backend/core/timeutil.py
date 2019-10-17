import datetime
import math

from .assumptions import BOOKING_TIME_SMALLEST_UNIT
from .assumptions import PARKING_TIME_SMALLEST_UNIT

HOURS_TO_MINUTES_FACTOR = 60
MINUTES_TO_HOURS_FACTOR = 1/60


def booking_time_slots_to_minutes(amount):
    return amount * BOOKING_TIME_SMALLEST_UNIT


def parking_time_slots_to_minutes(amount):
    return amount * PARKING_TIME_SMALLEST_UNIT


def minutes_to_hours(amount):
    return amount * MINUTES_TO_HOURS_FACTOR


def hours_to_minutes(amount):
    return amount * HOURS_TO_MINUTES_FACTOR
