from .assumptions import CAR_REACH_AT_FULL_CHARGE
from .assumptions import CAR_REPAIR_TIME


class Car:

    def __init__(self, license_: str, model: str):
        self.license = license
        self.model = model
        self.car_id = license + "_" + model
        self.range = CAR_REACH_AT_FULL_CHARGE
        self.in_repair = False
        self.repair_time = 0

    def set_range(self, range: float):
        self.range = range

    def set_in_repair(self, in_repair):
        if in_repair:
            self.in_repair = True
            self.repair_time = CAR_REPAIR_TIME
