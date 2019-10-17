class UserSettings:
    pass


class User:
    """
    Class to store user data.s
    """

    def __init__(self, name, phone_number, settings=None):
        self.name = name
        self.phone_number = phone_number
        self.settings = settings

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def update_settings(self, settings):
        self.settings = settings
