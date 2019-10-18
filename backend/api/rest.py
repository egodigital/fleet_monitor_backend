# import json
from collections import defaultdict
import simplejson as json
import os
import sys


from backend.api.swagger_client.api.bookings_api import BookingsApi
from backend.api.swagger_client.api.defaults_api import DefaultsApi
from backend.api.swagger_client.api.environments_api import EnvironmentsApi
from backend.api.swagger_client.api.vehicles_api import VehiclesApi
from backend.api.swagger_client.api_client import ApiClient

from backend.utils import timeutil

from flask import Flask, jsonify
from flask import make_response
from flask import request
from flask import Response

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
    return jsonify(success)


@app.route("/get_users", methods=["GET"])
def api_get_users():
    users = _handler.handle_get_users()
    d = defaultdict(dict)
    for user in users:
        user_id = user.credentials.user_id
        d[user_id]["first_name"] = user.first_name
        d[user_id]["last_name"] = user.last_name
        d[user_id]["password"] = user.credentials.password
    return jsonify(d)


@app.route("/get_bookings", methods=["GET"])
def api_get_bookings():
    bookings = _handler.handle_get_bookings()
    return jsonify({"bookins:": bookings})


@app.route("/get_bookings_by_userid", methods=["GET"])
def api_get_bookings_by_userid():
    user_id = request.args.get("user_id")
    bookings = _handler.handle_get_bookings_by_userid(user_id)
    return jsonify(bookings)


@app.route("/book_vehicle", methods=["POST"])
def book_vehicle():
    data = request.json
    start_time = timeutil.timestamp_to_datetime(data["start_time"])
    end_time = timeutil.timestamp_to_datetime(data["end_time"])
    distance = data["distance"]
    user_id = data["user_id"]
    allow_car_pooling = data.get("allow_car_pooling", True)
    ret = _handler.handle_book_vehicle(
        start_time, end_time, distance, user_id, allow_car_pooling)
    return jsonify(ret)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not found"}), 404)


def run():
    app.run(host="0.0.0.0", port=5000, debug=True)
