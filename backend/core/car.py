class Car:

    def __init__(self, license_, model):
        self.license = license
        self.model = model
        self.car_id = license + "_" + model
        self.range = None

    def set_range(self, range):
        self.range = range
