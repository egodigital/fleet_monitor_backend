from datetime import datetime
from typing import List
from collections import defaultdict

from backend.definitions import get_prj_root
from backend.utils import timeutil

from backend.core.bookings import Booking
from backend.core.bookings import BookingSystem
from backend.core.car import Car

from backend.core.globals_ import BASE_PRICE
from backend.core.globals_ import BATTERY_CONSERVATIVE_FACTOR
from backend.core.globals_ import BONUS_POINT_PRICE_DISCOUNT
from backend.core.globals_ import LATE_RETURN_FEE
from backend.core.globals_ import LATE_RETURN_FEE_MAX
from backend.core.globals_ import LOOK_AHEAD_TIME_SLOTS
from backend.core.globals_ import LONELY_WOLF_THRESHOLD
from backend.core.globals_ import RETURN_ON_TIME_REWARD
from backend.core.globals_ import PRICE_SURPLUS_OF_NO_CARPOOLING_RIDES
from backend.core.user import User


class Environment:
    """
    The environment class keeps track of all
    users, cars and bookings in the system.
    """

    def __init__(self) -> None:
        self.cars = []
        self.cars_to_timeslots = defaultdict(list)
        self.start_time = timeutil.get_start_time()
        self.last_car_booked = None
        self.users = []
        self.booking_system = BookingSystem()

    def _get_user_by_id(self, user_id):
        for user in self.users:
            if user.credentials.user_id == user_id:
                return user

    def _get_car_by_license(self, license_):
        for car in self.cars:
            if car.license == license_:
                return car

    def _time_slot_offset(self, t: datetime) -> int:
        offset = timeutil.datetimes_to_time_slots(t, self.start_time)
        return offset

    def _get_indices(self, t1: datetime, t2: datetime) -> List[int]:
        offset = self._time_slot_offset(t1)
        print(t1)
        print(t2)
        print(offset)
        amount_of_time_slots = timeutil.datetimes_to_time_slots(t1, t2)
        indices = [x for x in list(range(amount_of_time_slots))]
        return [x + offset for x in indices]

    def _book_time_slots(self, license_: str, t1: datetime, t2: datetime) -> None:
        indices = self._get_indices(t1, t2)
        time_slots = self.cars_to_timeslots[license_]
        for i in indices:
            time_slots[i] = 1

    def _free_time_slots(self, license_: str, t1: datetime, t2: datetime) -> None:
        indices = self._get_indices(t1, t2)
        time_slots = self.cars_to_timeslots[license_]
        for i in indices:
            time_slots[i] = 0

    def _time_slot_free(self, license_: str, t1: datetime, t2: datetime) -> None:
        indices = self._get_indices(t1, t2)
        print(indices)
        time_slots = self.cars_to_timeslots[license_]
        # Safety padding
        #   ->  keep at least one 15 minute slot free
        #       before and after the booking
        if len(time_slots) == 1:
            pass
        if time_slots[indices[0] - 1] == 1:
            return False
        if time_slots[indices[len(indices) - 1] + 1] == 1:
            return False

        for i in indices:
            if time_slots[i] == 1:
                return False
        return True

    def _enough_charge(self, license_: str, t1: datetime, distance: float) -> bool:
        prior_bookings: List[Booking] = self._get_prior_bookings_of_car(
            license_, t1)
        car = self._get_car_by_license(license_)
        sum_distance = sum(b.distance for b in prior_bookings)
        estimate_left_range = car.range - sum_distance
        if estimate_left_range * (1 + BATTERY_CONSERVATIVE_FACTOR) < distance:
            return False
        return True

    def _time_slot_available(self, license_: str, t1: datetime, t2: datetime, distance: float) -> None:
        # A time slot is available if it is free
        # and if the car has enough charge by a
        # conservative estimate
        available = self._time_slot_free(
            license_, t1, t2) and self._enough_charge(license_, t1, distance)
        return available

    def _get_prior_bookings_of_car(self, license_: str, t1: datetime) -> List[Booking]:
        bookings = self.booking_system.get_bookings_by_license(license_)
        prior_bookings = []
        for b in bookings:
            if b.start_time < t1:
                prior_bookings.append(b)
        return prior_bookings

    def _find_booking(self, booking_id: str) -> Booking:
        return self.booking_system.get_booking(booking_id)

    def _retrieve_car_for_booking(self, new_booking: Booking, bookings: List[Booking]) -> Car:
        # Assign cars by round-robin principle
        # Also make sure the car is sufficiently
        # charged.
        n_cars = len(self.cars)
        idx = self._find_car(self.last_car_booked)
        indices = [(idx + i) % n_cars for i in range(n_cars)]
        start_time = new_booking.start_time
        end_time = new_booking.end_time
        distance = new_booking.distance
        for i in indices:
            car = self.cars[i]
            license_ = self.cars[i].license
            if self._time_slot_available(license_, start_time, end_time, distance):
                return car
        return None

    def _get_estimated_price(self, new_booking: Booking, bookings: List[Booking]) -> float:
        """
        Optimization goals:
            1.) Maximize utilization
            2.) Minimize late returns
            3.) Improve charging behaviour
            4.) Reduce CO^2 emissions
            5.) High availability

        How each individual goal is achieved:
            1.) * Because long rides are charged very high, they are discouraged
                  such that the service may be utilised by more people and parking
                  time is minimized.

                  We understand utilization as a booked car that is actually driving
                  and not just parking somewhere.

            2.) * Bonus points which have positive influence on price function
                * Charge late return fee by a progressive model

            3.) * Make sure the car has at least 20% more battery charge then
                  is expected to be needed for the ride.
                    -> NOTE: This reduces availability a little bit of course

            4.) * Incentivize car pooling by charging a surplus if car pooling is
                  not used.

            5.) * Incentivize shorter booking spans by fast growing time cost function.
        """
        start_time = new_booking.start_time
        end_time = new_booking.end_time
        distance = new_booking.distance
        user_id = new_booking.user_id
        user = self._get_user_by_id(user_id)
        amount_time_slots = timeutil.datetimes_to_time_slots(
            start_time, end_time)

        base_price = BASE_PRICE(distance, amount_time_slots)
        discount = BONUS_POINT_PRICE_DISCOUNT(user.bonus_points)
        estimated_price = base_price - discount
        surplus = estimated_price * (1 + PRICE_SURPLUS_OF_NO_CARPOOLING_RIDES)
        estimated_price = estimated_price + surplus
        return estimated_price

    def _update_preferences_and_nature(self, user_id: str) -> bool:
        status_changed: bool = False
        bookings: List[Booking] = self.booking_system.get_bookings_by_user_id(
            user_id)

        n = len(bookings)
        n_car_pooled = sum(int(b.allow_car_pooling) for b in bookings)

        if n_car_pooled/n < LONELY_WOLF_THRESHOLD:
            user = self._get_user_by_id(user_id)
            user.behavioural_status.nature = "Lonely Wolf"
            status_changed = True

        # TODO: Figure out if user is economical, ecological
        # or efficient
        return status_changed

    def _find_car(self, license_: str) -> int:
        for i in range(len(self.cars)):
            car = self.cars[i]
            if car.license == license_:
                return i
        return -1

    def _find_user(self, user_id: str) -> int:
        for i in range(len(self.users)):
            user = self.users[i]
            if user.credentials.user_id == user_id:
                return i
        return -1

    def add_car(self, license_: str, model: str) -> None:
        car = Car(license_, model)
        self.cars.append(car)
        self.cars_to_timeslots[license_] = list(range(LOOK_AHEAD_TIME_SLOTS))
        return True

    def update_car_information(self, license_: str, range_: str = None, in_repair: bool = None) -> None:
        car = self._get_car_by_license(license_)
        if range_ is not None:
            car.set_range(range_)
        if in_repair is not None:
            car.set_in_repair(in_repair)
            # TODO: Create a booking for the repair
            # time and cancel all booking in that time
            #
            # Automatically assing new car to user and
            # send notification

    def remove_car(self, license_: str) -> bool:
        idx = self._find_car(license_)
        if license_ == self.last_car_booked:
            self.last_car_booked = self.cars[idx-1].license
        del self.cars[idx]
        del self.cars_to_timeslots[idx]
        self.booking_system.delete_bookings_by_license(license_)

    def get_cars(self) -> List[Car]:
        return self.cars

    def add_user(self, first_name: str, last_name:
                 str, user_id: str, password: str = "",
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
                                str = None, password: str = None, occupation: str = None, phone_number: str = None, share_social_status:
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
        bookings = self.booking_system.get_bookings_by_user_id(user_id)
        for b in bookings:
            license_ = b.license
            start_time = b.start_time
            end_time = b.end_time
            self._free_time_slots(license_, start_time, end_time)
        self.booking_system.delete_bookings_by_userid(user_id)

    def get_users(self) -> List[User]:
        return self.users

    def add_booking(self, start_time: datetime, end_time:
                    datetime, distance: float, user_id: str,
                    license_: str = None, allow_car_pooling: bool = True) -> None:
        new_booking = Booking(start_time, end_time, distance,
                              user_id, license_, allow_car_pooling)
        bookings = self.booking_system.get_all_bookings()
        car = self._retrieve_car_for_booking(new_booking, bookings)
        if car is not None:
            new_booking.set_license(car.license)
            user = self._get_user_by_id(user_id)
            self.last_car_booked = car.license
            id_ = self.booking_system.add_booking(new_booking)
            # User has free ride available
            if user.free_rides > 0:
                price = 0
                user.free_rides -= 1
            # Price determined by fine-tuned price function
            else:
                price = self._get_estimated_price(new_booking, bookings)
            # Update user stats
            self._update_preferences_and_nature(user_id)
            return {
                "booking_id": id_,
                "price": price,
                "car": car,
            }
        return {
            "booking_id": None,
            "price": -1,
            "car": None,
        }

    def close_booking(self, booking_id: str, handover_time: str):
        booking: Booking = self.booking_system.get_booking(booking_id)
        # Update the cars range
        license_ = booking.license
        distance = booking.distance
        idx = self._find_car(license_)
        self.cars[idx].range -= distance

        # Check if the car is returned in time
        handover_time = datetime(handover_time)
        end_time = booking.end_time
        minutes_late = timeutil.time_slots_to_minutes(
            timeutil.datetimes_to_time_slots(
                handover_time, end_time
            ))
        if minutes_late > 0:
            booking.set_minutes_late(minutes_late)
            keys = LATE_RETURN_FEE.keys()
            for i in range(keys) - 1:
                if minutes_late > keys[i] and minutes_late < keys[i+1]:
                    price = booking.price
                    booking.add_cost(price * LATE_RETURN_FEE[keys[i]])
                    break
        else:
            user_id = booking.user_id
            for user in self.users:
                if user.credentials.user_id == user_id:
                    user.add_bonus_points(RETURN_ON_TIME_REWARD)
                    break

        self.booking_system.close_booking(booking_id)

    def delete_booking(self, booking_id: str) -> None:
        booking = self.booking_system.get_booking(booking_id)
        license_ = booking.license
        start_time = booking.start_time
        end_time = booking.end_time
        self._free_time_slots(license_, start_time, end_time)
        self.booking_system.delete_booking(booking_id)

    def add_tag_to_booking(self, booking_id, tag):
        booking: Booking = self.booking_system.get_booking(
            booking_id
        )
        booking.add_tag(tag)

    def remove_tag_from_booking(self, booking_id, tag):
        booking: Booking = self.booking_system.get_booking(
            booking_id
        )
        booking.remove_tag(tag)

    def get_all_bookings(self) -> List[Booking]:
        return self.booking_system.get_all_bookings()

    def get_bookings_by_user(self, user_id) -> List[Booking]:
        return self.booking_system.get_bookings_by_user_id(user_id)


class TestData:

    def __init__(self):
        self.users = [
            User("Patrice", "Dummy1", "patrice", "asdasd"),
            User("Patrice", "Dummy2", "patrice2", "asdasd"),
            User("Patrice", "Dummy3", "patrice3", "asdasd"),
        ]

        self.cars = [
            Car("License1", "Model1"),
            Car("License2", "Model2"),
            Car("License3", "Model3"),
        ]

        # current date and time
        now = timeutil.get_start_time()
        timestamp = timeutil.datetime_to_timestamp(now)
        self.bookings = [
            Booking(timestamp, timestamp + 900, 1000, "patrice")
        ]


if __name__ == "__main__":
    env = Environment()
    data = TestData()
    users = data.users
    cars = data.cars
    bookings = data.bookings

    print("######### CREATING USERS #############")
    for user in users:
        ret = env.add_user(user.first_name, user.set_last_name,
                           user.credentials.user_id, user.credentials.password)
        print(ret)

    print("######### CREATING CARS #############")
    for car in cars:
        ret = env.add_car(car.license, car.model)
        print(ret)

    print("######### CREATING BOOKINGS #############")
    for b in bookings:
        ret = env.add_booking(
            timeutil.timestamp_to_datetime(b.start_time),
            timeutil.timestamp_to_datetime(b.end_time),
            b.distance,
            b.user_id
        )
        print(ret)
