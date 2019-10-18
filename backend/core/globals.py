"""
This module contains all assumptions we as team
FleetMonitor make about the system.
"""

# unit [km]
CAR_REACH_AT_FULL_CHARGE = 80

# unit [days]
CAR_REPAIR_TIME = 3

# unit [hours]
SMALL_ROUND_TRIP_MAX_DURATION = 3

# unit [minutes]
SMALLEST_TIME_UNIT = 15

# unit [kv]
POWER_CAR_FULLY_CHARGED = 100

# unit [kv]
AVERAGE_POWER_USED_PER_KILOMETER = POWER_CAR_FULLY_CHARGED / CAR_REACH_AT_FULL_CHARGE

# unit [km]
AVERAGE_SPEED = 35


# Tags
#
# tag name -> description
DEFAULT_TAGS = {
    "Lebensmittel": "Die Person kauft während ihrer Buchung Lebensmittel ein",
}

LATE_RETURN_MAX_PENALTY = 0.2
PENALTY_LATE_CAR_RETURN = {
    5: 0.05,
    15: 0.1,
    30: 0.15,
    60: LATE_RETURN_MAX_PENALTY,
}

LONELY_WOLF_THRESHOLD = 0.3

BOOKING_BASE_PRICE = 1
COST_PER_KILOMETER = 0.03
COST_PER_HOUR = 0.03

# unit [time slots]
LOOK_AHEAD_DAYS = 60
TIME_SLOTS_PER_DAY = 96
LOOK_AHEAD_TIME_SLOTS = LOOK_AHEAD_DAYS * TIME_SLOTS_PER_DAY
