import datetime
import uuid

from typing import List

from .user import User


class BookingSettings:
    """
    Class encapsulates further booking settings.
    """

    def __init__(self, start_time: str, end_time: str,
                 distance: int, parking_duration: int, user:
                 User, allow_car_pooling: bool = True) -> None:
        self.start_time = start_time
        self.end_time = end_time
        self.distance = distance
        self.parking_duration = parking_duration
        self.user = User
        self.allow_car_pooling = allow_car_pooling


class Booking:
    """
    Class abstracts a car booking.
    """

    def __init__(self, settings: BookingSettings) -> None:
        self.settings = settings

    def __str__(self):
        # TODO: Implement string representation of reservation
        pass


class BookingSystem:
    """
    Class which manages all reservations.
    """

    def __init__(self):
        self.__bookings = {}

    def add_booking(self, start_time: datetime, end_time:
                    datetime, user: User, settings: BookingSettings) -> bool:
        booking = Booking(settings)
        id_ = id_ = str(uuid.uuid1())
        self.__bookings[id_] = booking
        # Everything worked fine
        return True

    def delete_booking(self, id_: str) -> bool:
        del self.__bookings[id_]
        return True

    def get_bookings_of_user(self, user_id: str) -> None:
        user_bookings = []
        for _, v in self.__bookings.items():
            if v.user.credentials.uer_id == user_id:
                user_bookings.append(v)
        return user_bookings

    def get_all_bookings(self) -> List[Booking]:
        return self.__bookings.values()
