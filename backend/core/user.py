class User:
    """
    Class to store user data.s
    """

    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number
