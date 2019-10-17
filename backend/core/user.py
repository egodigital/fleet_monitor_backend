class Credentials:

    def __init__(self, username, password):
        self.username = username
        self.password = password


class User:
    """
    Class to store user data.s
    """

    def __init__(self, name, phone_number, group, username, password):
        self.name = name
        self.phone_number = phone_number
        self.group = group
        self.credentials = Credentials(username, password)

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def set_group(self, group):
        self.group = group

    def set_username(self, username):
        self.credentials.username = username

    def set_password(self, password):
        self.credentials.password = password
