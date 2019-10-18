"""
This module contains all assumptions we as team
FleetMonitor make about the system.
"""

from math import exp

# --- Globals concering cars

# unit [km]
CAR_REACH_AT_FULL_CHARGE = 80

# unit [days]
CAR_REPAIR_TIME = 3

# unit [hours]
SMALL_ROUND_TRIP_MAX_DURATION = 3

# unit [kv]
POWER_CAR_FULLY_CHARGED = 100

# unit [kv]
AVERAGE_POWER_USED_PER_KILOMETER = POWER_CAR_FULLY_CHARGED / CAR_REACH_AT_FULL_CHARGE

# unit [km]
AVERAGE_SPEED = 35

BATTERY_CONSERVATIVE_FACTOR = 0.2
CHARGE_PER_TIME_SLOT = 2.5

# --- Globals concerning users
LONELY_WOLF_THRESHOLD = 0.3

# Bonus points if car is returned in time
RETURN_ON_TIME_REWARD = 50
BONUS_POINT_TO_FREE_RIDE_EQUIVALENT = 100
FEATURE_DISCOVERY_MAX = 10

# --- Globals related to price function
PRICE_SURPLUS_OF_NO_CARPOOLING_RIDES = 0.2

_DISTANCE_PRICE_FACTOR = 0.5
_TIME_SLOT_PRICE_FACTOR = 0.1
_BONUS_POINT_PRICE_FACTOR = 0.2


def _DISTANCE_COST(distance):
    return _DISTANCE_PRICE_FACTOR * distance


def _TIME_COST(amount_time_slots):
    return _TIME_SLOT_PRICE_FACTOR * exp(amount_time_slots)


def BASE_PRICE(distance, amount_time_slots):
    return _DISTANCE_COST(distance) + _TIME_COST(amount_time_slots)


def BONUS_POINT_PRICE_DISCOUNT(bonus_points):
    return _BONUS_POINT_PRICE_FACTOR * bonus_points / 1000


LATE_RETURN_FEE_MAX = 0.2
LATE_RETURN_FEE = {
    5: 0.05,
    15: 0.1,
    30: 0.15,
    60: LATE_RETURN_FEE_MAX,
}

# --- Other globals
# unit [minutes]
SMALLEST_TIME_UNIT = 15

# Tags
#
# tag name -> description
DEFAULT_TAGS = {
    "Lebensmittel": "Die Person kauft während ihrer Buchung Lebensmittel ein",
}

# unit [time slots]
LOOK_AHEAD_DAYS = 60
TIME_SLOTS_PER_DAY = 96
LOOK_AHEAD_TIME_SLOTS = LOOK_AHEAD_DAYS * TIME_SLOTS_PER_DAY
