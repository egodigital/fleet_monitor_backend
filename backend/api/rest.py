import json
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

from backend.api.handler import RequestHandler

# API key
API_KEY = "07fb13b8-176a-4c9d-bfe6-9831271e3fac"

# init api client
client = ApiClient()
environment = EnvironmentsApi(client)
vehicles = VehiclesApi(client)
app = Flask(__name__)

# Request handler
_handler = RequestHandler()


@app.route("/")
def print_app_info():
    return jsonify({"about": "This is the fleet monitor app"})


@app.route("/create_user", methods=["POST"])
def api_create_user():
    data = request.json
    first_name = data["first_name"]
    last_name = data["last_name"]
    user_id = data["user_id"]
    password = data["password"]
    success = _handler.handle_create_user(
        first_name, last_name, user_id, password)
    print(json.dumps(success))
    return json.dumps(success)


@app.route("/get_users", methods=["GET"])
def api_get_users():
    return json.dumps(_handler.handle_get_users())


@app.route("/get_bookings", methods=["GET"])
def api_get_bookings():
    return json.dumps(_handler.handle_get_bookings())


@app.route("/get_bookings_by_userid", methods=["GET"])
def api_get_bookings_by_userid(user_id):
    data = request.json
    user_id = data["user_id"]
    bookings = _handler.handle_get_bookings_by_userid(user_id)
    print(type(bookings))
    print(bookings)
    return json.loads(bookings)


@app.route("/book_vehicle", methods=["POST"])
def book_vehicle(start_time, end_time, user_id):
    data = request.data
    # return _handler.handle_book_vehicle(data["start_time"], data["end_time"], data["user_id"])


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not found"}), 404)


def run():
    app.run(host="0.0.0.0", port=5000, debug=True)
