from .community import DEFAULT_TAGS


class Credentials:

    def __init__(self, user_id, password):
        self.user_id = user_id
        self.password = password


class User:
    """
    Class to store user data.s
    """

    FEATURE_DISCOVERY_MAX = 10

    def __init__(self, name: str, phone_number: str, user_id: str, password: str) -> None:
        self.name = name
        self.phone_number = phone_number
        self.credentials = Credentials(user_id, password)
        self.bonus = 0
        self.feature_discovery = 0
        self.free_rides = 0

    def set_name(self, name: str) -> None:
        self.name = name

    def set_phone_number(self, phone_number: str) -> None:
        self.phone_number = phone_number

    def set_userid(self, user_id: str) -> None:
        self.credentials.user_id = user_id

    def set_password(self, password: str) -> None:
        self.credentials.password = password

    def add_bonus_points(self, bonus: int) -> None:
        temp = self.bonus
        if (temp % 100 + bonus) > 100:
            self.free_rides += 1
        self.bonus += bonus

    def increment_feature_discovery(self) -> None:
        self.feature_discovery += 1
        if self.feature_discovery == self.FEATURE_DISCOVERY_MAX:
            self.free_rides += 1

    def take_free_ride(self):
        self.free_rides -= 1
