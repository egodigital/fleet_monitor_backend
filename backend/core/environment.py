from backend.definitions import get_prj_root

from .bookings import Booking
from .bookings import BookingInformation
from .bookings import BookingSystem
from .car import Car
from .user import User


class Environment:
    """
    The environment class keeps track of all
    users, cars and bookings in the system.
    """

    def __init__(self) -> None:
        self.cars = []
        self.users = []
        self.booking_system = BookingSystem()

    def _find_car(self, license_):
        for i in range(len(self.cars)):
            car = self.cars[i]
            if car.license == license_:
                return i
        return -1

    def add_car(self, license_: str, model: str) -> None:
        self.cars.append(Car(license_, model))

    def update_car_information(self, license_: str, range_: str = None, in_repair: bool = None) -> None:
        idx = self._find_car(license_)
        car = self.cars[idx]
        if range_ is not None:
            car.set_range(range_)
        if in_repair is not None:
            car.set_in_repair(in_repair)

    def remove_car(self, license_: str) -> bool:
        idx = self._find_car(license_)
        del self.cars[idx]

    def _find_user(self, user_id):
        for i in range(len(self.users)):
            user = self.users[i]
            if user.credentials.user_id == user_id:
                return i
        return -1

    def add_user(self, first_name: str, last_name:
                 str, user_id: str, password: str,
                 occupation: str = "",
                 phone_number: str = "", share_social_data:
                 bool = False, share_behavioural_data: bool = False, share_booking_data: bool = False) -> bool:
        idx = self._find_user(user_id)
        if idx == -1:
            self.users.append(
                User(first_name,
                     last_name,
                     user_id,
                     password,
                     occupation,
                     phone_number,
                     share_social_data,
                     share_behavioural_data,
                     share_booking_data,
                     )
            )
            # TODO: Save user credentials in file
            return True
        return False

    def update_user_information(self, user_id: str, last_name:
                                str = None, password: str = None, occupation: str =
                                None, phone_number: str = None, share_social_status:
                                bool = None, share_behavioural_status: str = None,
                                share_booking_data: str = None) -> None:
        idx = self._find_user(user_id)
        user: User = self.users[idx]
        if last_name is not None:
            user.set_last_name(last_name)
        if password is not None:
            # TODO: Update credentials file
            user.set_password(password)
        if occupation is not None:
            user.set_occupation(occupation)
        if phone_number is not None:
            user.set_phone_number(phone_number)
        if share_social_status is not None:
            user.set_share_social_status(share_social_status)
        if share_behavioural_status is not None:
            user.set_share_behavioural_status(share_behavioural_status)
        if share_booking_data is not None:
            user.set_share_booking_data(share_booking_data)

    def delete_user(self, user_id: str) -> bool:
        idx = self._find_user(user_id)
        del self.users[idx]

    def _find_booking(self, booking_id):
        return self.booking_system.get_booking_by_id(booking_id)

    def add_booking(self, start_time: str, end_time: str,
                    distance: float, user_id: str,
                    allow_car_pooling:
                    bool = True) -> None:
        booking_info = BookingInformation(
            start_time, end_time, distance, user_id, allow_car_pooling
        )
        id_ = self.booking_system.add_booking(
            Booking(booking_info)
        )
        return id_

    def delete_booking(self, booking_id) -> None:
        self.booking_system.delete_booking(booking_id)

    def add_tag_to_booking(self, booking_id, tag):
        booking: Booking = self.booking_system.get_booking_by_id(
            booking_id
        )
        booking.add_tag(tag)

    def remove_tag_from_booking(self, booking_id, tag):
        booking: Booking = self.booking_system.get_booking_by_id(
            booking_id
        )
        booking.remove_tag(tag)
