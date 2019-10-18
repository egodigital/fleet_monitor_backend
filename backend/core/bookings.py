from datetime import datetime
import uuid

from typing import List

from backend.core.globals_ import SMALL_ROUND_TRIP_MAX_DURATION
from backend.core.user import User


class Booking:
    """
    Class abstracts a car booking.
    """

    def __init__(self, start_time: str, end_time: str,
                 distance: float, user_id: str, license_: str = None,
                 allow_car_pooling:
                 bool = True) -> None:
        self.start_time = datetime(start_time)
        self.end_time = datetime(end_time)
        self.distance = distance
        # TODO: Implement carpooling such that more than
        # one user can be assigned to a booking
        self.user_id = user_id
        self.license = license_
        self.allow_car_pooling = allow_car_pooling
        self.minutes_late = 0
        self.price = 0
        # Tags attached to booking
        self.tags = []
        self.closed = False

    def set_start_time(self, start_time: str) -> None:
        self.start_time = datetime(start_time)

    def set_end_time(self, end_time: str) -> None:
        self.end_time = datetime(end_time)

    def set_distance(self, distance: float) -> None:
        self.distance = distance

    def set_license(self, license_: str) -> None:
        self.license = license_

    def set_car_pooling_option(self, allow_car_pooling: bool) -> None:
        self.allow_car_pooling = allow_car_pooling

    def set_minutes_late(self, minutes_late: int) -> None:
        self.minutes_late = minutes_late

    def set_price(self, price: float) -> None:
        self.price = price

    def add_cost(self, cost: float) -> None:
        self.price += cost

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
        self.__bookings[id_] = bookin.__bookings[id_] = booking
        return id_

    def close_booking(self, booking_id):
        booking = self.__bookings[booking_id]
        booking.closed = True

    def delete_booking(self, id_: str) -> None:
        del self.__bookings[id_]

    def delete_bookings_by_license(self, license_):
        ids = []
        for id_, b in self.__bookings.items():
            if b.license == license_:
                ids.append(id_)

        for id_ in ids:
            del self.__bookings[id_]

    def delete_bookings_by_userid(self, user_id):
        ids = []
        for id_, b in self.__bookings.items():
            if b.user_id == user_id:
                ids.append(id_)

        for id_ in ids:
            del self.__bookings[id_]

    def get_booking(self, booking_id):
        return self.__bookings[booking_id]

    def get_bookings_by_license(self, license_: str) -> None:
        bookings = []
        for _, b in self.__bookings.items():
            if b.license == license_:
                bookings.append(b)
        return bookings

    def get_bookings_by_user_id(self, user_id: str) -> None:
        bookings = []
        for _, b in self.__bookings.items():
            if b.user.credentials.uer_id == user_id:
                bookings.append(b)
        return bookings

    def get_all_bookings(self) -> List[Booking]:
        return self.__bookings.values()
