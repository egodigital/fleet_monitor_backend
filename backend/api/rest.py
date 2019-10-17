import os
import sys


from backend.api.swagger_client.api.bookings_api import BookingsApi
from backend.api.swagger_client.api.defaults_api import DefaultsApi
from backend.api.swagger_client.api.environments_api import EnvironmentsApi
from backend.api.swagger_client.api.vehicles_api import VehiclesApi
from backend.api.swagger_client.api_client import ApiClient
from flask import Flask, jsonify
from flask import make_response

from backend.api import handler

# API key
API_KEY = "07fb13b8-176a-4c9d-bfe6-9831271e3fac"

# init api client
client = ApiClient()
environment = EnvironmentsApi(client)
vehicles = VehiclesApi(client)

app = Flask(__name__)


@app.route("/")
def print_app_info():
    return "This is the fleet monitor app"


@app.route("/booking_price", methods=["GET"])
def booking_price(start_time, end_time, user_id):
    return handler.handle_booking_price(start_time, end_time, user_id)


@app.route("/book_vehicle", methods=["POST"])
def book_vehicle(start_time, end_time, user_id):
    return handler.handle_book_vehicle(start_time, end_time, user_id)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
