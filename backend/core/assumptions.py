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
