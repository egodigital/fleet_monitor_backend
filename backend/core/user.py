from backend.core.globals import BONUS_POINT_TO_FREE_RIDE_EQUIVALENT
from backend.core.globals import FEATURE_DISCOVERY_MAX


class Credentials:

    def __init__(self, user_id, password):
        self.user_id = user_id
        self.password = password


class SocialStatus:

    def __init__(self):
        self.friends = 0
        self.favorites = 0
        self.comments = 0


class BehaviouralStatus:

    def __init__(self):
        # ("Unknown", "ECONOMICAL", "ECOLOGICAL", "EFFICIENT")
        self.preferences = "Unknown"
        # ("Unknown", "SOCIAL", "LONELY WOLF")
        self.nature = "Unknown"


class User:
    """
    Class to store user data.s
    """

    def __init__(self, first_name: str, last_name: str,
                 user_id: str, password: str, occupation: str = "",
                 phone_number: str = "", share_social_status:
                 bool = False, share_behavioural_status: bool =
                 False, share_booking_data: bool = False) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.credentials = Credentials(user_id, password)
        self.occupation = occupation
        self.phone_number = phone_number
        self.bonus = 0
        self.feature_discovery = 0
        self.free_rides = 0
        self.share_social_status = share_social_status
        self.share_behavioural_status = share_behavioural_status
        self.share_booking_data = share_booking_data
        self.social_status = SocialStatus()
        self.behavioural_status = BehaviouralStatus()

    def set_first_name(self, first_name: str) -> None:
        self.first_name = first_name

    def set_last_name(self, last_name: str) -> None:
        self.last_name = last_name

    def set_userid(self, user_id: str) -> None:
        self.credentials.user_id = user_id

    def set_password(self, password: str) -> None:
        self.credentials.password = password

    def set_occupation(self, occupation: str) -> None:
        self.occupation = occupation

    def set_phone_number(self, phone_number: str) -> None:
        self.phone_number = phone_number

    def add_bonus_points(self, bonus: int) -> None:
        temp = self.bonus
        if (temp % BONUS_POINT_TO_FREE_RIDE_EQUIVALENT + bonus) > BONUS_POINT_TO_FREE_RIDE_EQUIVALENT:
            self.free_rides += 1
        self.bonus += bonus

    def increment_feature_discovery(self) -> None:
        self.feature_discovery += 1
        if self.feature_discovery == FEATURE_DISCOVERY_MAX:
            self.free_rides += 1

    def take_free_ride(self):
        self.free_rides -= 1

    def set_share_social_status(self, share=False):
        self.share_social_status = share

    def set_share_behavioural_status(self, share=False):
        self.share_behavioural_status = share

    def set_share_booking_data(self, share=False):
        self.share_booking_data = share

    def increment_friends(self):
        self.social_status.friends += 1

    def increment_favorites(self):
        self.social_status.favorites += 1

    def increment_comments(self):
        self.social_status.comments += 1
