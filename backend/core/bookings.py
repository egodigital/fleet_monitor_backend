import datetime
import uuid

from typing import List

from .globals import SMALL_ROUND_TRIP_MAX_DURATION
from .user import User


class BookingInformation:
    """
    Class encapsulates all booking information.
    """

    def __init__(self, start_time: str, end_time: str,
                 distance: int, user_id: str,
                 allow_car_pooling:
                 bool = True) -> None:
        self.start_time = start_time
        self.end_time = end_time
        self.distance = distance
        self.user_id = user_id
        self.allow_car_pooling = allow_car_pooling
        # Tags attached to booking
        self.tags = []


class Booking:
    """
    Class abstracts a car booking.
    """

    def __init__(self, booking_info: BookingInformation) -> None:
        self.booking_info = booking_info

    def set_start_time(self, start_time):
        self.booking_info.start_time = start_time

    def set_end_time(self, end_time):
        self.booking_info.end_time = end_time

    def set_distance(self, distance):
        self.booking_info.distance = distance

    def set_car_pooling_option(self, allow_car_pooling):
        self.booking_info.allow_car_pooling = allow_car_pooling

    def add_tag(self, tag: str) -> None:
        self.booking_info.tags.append(tag)

    def remove_tag(self, tag: str) -> None:
        self.booking_info.tags.remove(tag)


class BookingSystem:
    """
    Class which manages all reservations.
    """

    def __init__(self):
        self.__bookings = {}

    def add_booking(self, booking: Booking) -> None:
        id_ = id_ = str(uuid.uuid1())
        self.__bookings[id_] = booking

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
