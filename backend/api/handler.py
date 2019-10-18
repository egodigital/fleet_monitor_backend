from backend.core.environment import Environment


class RequestHandler:

    def __init__(self):
        self.__env = Environment()

    def create_user(self, first_name, last_name, user_id):
        pass

    def handle_get_bookings(self, start_time, end_time, user_id):
        return self.__env.get_all_bookings()

    def get_bookings_by_userid(self, user_id):
        bookings = self.__env.get_bookings_by_user(user_id)
        return bookings
