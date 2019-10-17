import datetime
import uuid

from typing import List

from .user import User


class ReservationSettings:
    """
    Class encapsulates further reservation settings.
    """

    def __init__(self, allow_car_pooling: bool = True) -> None:
        self.allow_car_pooling = allow_car_pooling


class Reservation:
    """
    Class abstracts a car reservation.
    """

    def __init__(self, start_time: datetime, end_time: datetime,
                 user: User, settings: ReservationSettings) -> None:
        self.start_time = start_time
        self.end_time = end_time
        self.user = user
        self.settings = settings

    def __str__(self):
        # TODO: Implement string representation of reservation
        pass


class ReservationSystem:
    """
    Class which manages all reservations.
    """

    def __init__(self):
        self.__reservations = {}

    def add_reservation(self, start_time: datetime, end_time:
                        datetime, user: User, settings: ReservationSettings) -> bool:
        reservation = Reservation(start_time, end_time, user, settings)
        id_ = id_ = str(uuid.uuid1())
        self.__reservations[id_] = reservation
        # Everything worked fine
        return True

    def delete_reservation(self, id_: str) -> bool:
        del self.__reservations[id_]
        return True

    def get_reservation_by_user(self, username):
        user_reservations = []
        for _, v in self.__reservations.items():
            if v.user.name == username:
                user_reservations.append(v)
        return user_reservations

    def get_all_reservations(self) -> List[Reservation]:
        return self.__reservations.values()
