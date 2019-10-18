from typing import List

from backend.definitions import get_prj_root
from backend.utils import timeutil

from .bookings import Booking
from .bookings import BookingSystem
from .car import Car
from datetime import datetime
from .globals import BOOKING_BASE_PRICE
from .globals import COST_PER_KILOMETER
from .globals import LATE_RETURN_MAX_PENALTY
from .globals import LONELY_WOLF_THRESHOLD
from .globals import PENALTY_LATE_CAR_RETURN
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

    def get_cars(self) -> List[Car]:
        return self.cars

    def _find_user(self, user_id: str) -> int:
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

    def remove_user(self, user_id: str) -> bool:
        idx = self._find_user(user_id)
        del self.users[idx]

    def get_users(self) -> List[User]:
        return self.users

    def _find_booking(self, booking_id: str) -> Booking:
        return self.booking_system.get_booking_by_id(booking_id)

    def _retrieve_car_for_booking(self, new_booking: Booking, all_bookings: List[Booking]) -> Car:
        # TODO: Implement
        #
        # Availability depends on the fact
        return car

    def _get_price(self, new_booking: Booking, all_bookings: List[Booking]) -> float:
        return 1

    def _update_preferences_and_nature(self, user_id: str) -> bool:
        status_changed: bool = False
        preference = "Unknown"
        nature = "Unknown"
        bookings: List[Booking] = self.booking_system.get_bookings_of_user(
            user_id)

        n = len(bookings)
        n_car_pooled = sum(int(b.allow_car_pooling) for b in bookings)

        if n_car_pooled/n < LONELY_WOLF_THRESHOLD:
            idx = self._find_user(user_id)
            user = self.users[idx]
            user.behavioural_status.nature = "Lonely Wolf"
            status_changed = True

        # TODO: Figure out if user is economical, ecological
        # or efficient
        return status_changed

    def add_booking(self, start_time: str, end_time: str,
                    distance: float, user_id: str, license_: str = None,
                    allow_car_pooling: bool = True) -> None:
        new_booking = Booking(start_time, end_time, distance,
                              user_id, license_, allow_car_pooling)
        all_bookings = self.booking_system.get_all_bookings()
        car = self._retrieve_car_for_booking(new_booking, all_bookings)
        if car is not None:
            id_ = self.booking_system.add_booking(
                Booking(start_time, end_time, distance,
                        user_id, allow_car_pooling)
            )
            price = self._get_price(new_booking, all_bookings)
            self._update_preferences_and_nature(
                user_id)
            return id_, price, car
        return None, -1, None

    def close_booking(self, booking_id: str, handover_time: str):
        self.booking_system.close_booking(booking_id)
        booking: Booking = self.booking_system.get_booking_by_id(booking_id)
        handover_time = datetime(handover_time)
        end_time = booking.end_time
        minutes_late = timeutil.time_slots_to_minutes(
            timeutil.datetimes_to_time_slots(
                handover_time, end_time
            ))
        if minutes_late > 0:
            booking.set_minutes_late(minutes_late)
            keys = PENALTY_LATE_CAR_RETURN.keys()
            for i in range(keys) - 1:
                if minutes_late > keys[i] and minutes_late < keys[i+1]:
                    price = booking.price
                    booking.add_cost(price * PENALTY_LATE_CAR_RETURN[keys[i]])
                    break
        self.booking_system.close_booking(booking_id)

    def delete_booking(self, booking_id: str) -> None:
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

    def get_all_bookings(self) -> List[Booking]:
        return self.booking_system.get_all_bookings()

    def get_bookings_by_user(self, user_id) -> List[Booking]:
        return self.booking_system.get_bookings_of_user(user_id)
