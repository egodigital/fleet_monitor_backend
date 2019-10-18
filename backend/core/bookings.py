from datetime import datetime
import uuid

from typing import List

from .globals import SMALL_ROUND_TRIP_MAX_DURATION
from .user import User


class Booking:
    """
    Class abstracts a car booking.
    """

    def __init__(self, start_time: str, end_time: str,
                 distance: float, user_id: str, license_,
                 allow_car_pooling:
                 bool = True) -> None:
        self.start_time = datetime(start_time)
        self.end_time = datetime(end_time)
        self.distance = distance
        self.user_id = user_id
        self.license = license_
        self.allow_car_pooling = allow_car_pooling
        # Tags attached to booking
        self.tags = []
        self.minutes_late = 0

    def set_start_time(self, start_time: str) -> None:
        self.start_time = datetime(start_time)

    def set_end_time(self, end_time: str) -> None:
        self.end_time = datetime(end_time)

    def set_distance(self, distance: float) -> None:
        self.distance = distance

    def set_car_pooling_option(self, allow_car_pooling: bool) -> None:
        self.allow_car_pooling = allow_car_pooling

    def add_tag(self, tag: str) -> None:
        self.tags.append(tag)

    def remove_tag(self, tag: str) -> None:
        self.tags.remove(tag)


class BookingSystem:
    """
    Class which manages all reservations.
    """

    def __init__(self):
        self.__bookings = {}

    def add_booking(self, booking: Booking) -> str:
        id_ = id_ = str(uuid.uuid1())
        self.__bookings[id_] = booking
        return id_

    def close_booking(self, booking_id: str, handover_time: str):
        booking = self.__bookings[booking_id]
        end_time = booking.end_time
        handover_time = datetime(handover_time)

    def delete_booking(self, id_: str) -> None:
        del self.__bookings[id_]

    def get_booking_by_id(self, booking_id):
        return self.__bookings[booking_id]

    def get_bookings_of_user(self, user_id: str) -> None:
        user_bookings = []
        for _, v in self.__bookings.items():
            if v.user.credentials.uer_id == user_id:
                user_bookings.append(v)
        return user_bookings

    def get_all_bookings(self) -> List[Booking]:
        return self.__bookings.values()
