#!flask/bin/python
from swagger_client.api.bookings_api import BookingsApi
from swagger_client.api.defaults_api import DefaultsApi
from swagger_client.api.environments_api import EnvironmentsApi
from swagger_client.api.vehicles_api import VehiclesApi
from swagger_client.api_client import ApiClient
from flask import Flask, jsonify
from flask import make_response

# set sys path to import swagger client
import os
import sys
myFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, "./../api/")

# import all Apis

# our Api key
API_KEY = "07fb13b8-176a-4c9d-bfe6-9831271e3fac"

# init api client
client = ApiClient()
environment = EnvironmentsApi(client)
vehicles = VehiclesApi(client)

app = Flask(__name__)


@app.route('/environment', methods=['GET'])
def get_tasks():
    return str(environment.api_v2_environments_get(API_KEY))


@app.route('api/v2/vehicles', methods=['GET'])
def get_all_vehicles():
    return vehicles.api_v2_vehicles_get


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True, port=80)
