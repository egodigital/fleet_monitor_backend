import os
import sys


from backend.api.swagger_client.api.bookings_api import BookingsApi
from backend.api.swagger_client.api.defaults_api import DefaultsApi
from backend.api.swagger_client.api.environments_api import EnvironmentsApi
from backend.api.swagger_client.api.vehicles_api import VehiclesApi
from backend.api.swagger_client.api_client import ApiClient

from flask import Flask, jsonify
from flask import make_response
from flask import request

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
    return jsonify({"about": "This is the fleet monitor app"})


@app.route("/get_bookings", methods=["GET"])
def api_get_bookings():
    pass


@app.route("/get_bookings_by_userid", methods=["GET"])
def api_get_bookings_by_userid():
    pass


@app.route("/book_vehicle", methods=["POST"])
def book_vehicle(start_time, end_time, user_id):
    data = request.data
    return handler.handle_book_vehicle(data["start_time"], data["end_time"], data["user_id"])


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not found"}), 404)


def run():
    app.run(host="0.0.0.0", port=5000, debug=True)
