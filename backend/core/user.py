class Credentials:

    def __init__(self, user_id, password):
        self.user_id = user_id
        self.password = password


class User:
    """
    Class to store user data.s
    """

    FEATURE_DISCOVERY_MAX = 10

    def __init__(self, name, phone_number, user_id, password):
        self.name = name
        self.phone_number = phone_number
        self.credentials = Credentials(user_id, password)
        self.tags = []
        self.bonus = 0
        self.feature_discovery = 0
        self.free_rides = 0

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def set_userid(self, user_id):
        self.credentials.user_id = user_id

    def set_password(self, password):
        self.credentials.password = password

    def add_tag(self, tag):
        if not (tag in self.tags):
            self.tags.append(tag)
            return True
        return False

    def remove_tag(self, tag):
        if tag in self.tags:
            self.tags.remove(tag)
            return True
        return False

    def add_bonus_points(self, bonus):
        temp = self.bonus
        if (temp % 100 + bonus) > 100:
            self.free_rides += 1
        self.bonus += bonus

    def increment_feature_discovery(self):
        self.feature_discovery += 1
        if self.feature_discovery == self.FEATURE_DISCOVERY_MAX:
            self.free_rides += 1

    def take_free_ride(self):
        self.free_rides -= 1
