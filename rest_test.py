# import swagger clients
from flask import Flask, jsonify, make_response
from backend.api.swagger_client.api_client import ApiClient
from swagger_client.api.vehicles_api import VehiclesApi
from swagger_client.api.environments_api import EnvironmentsApi
from swagger_client.api.defaults_api import DefaultsApi
from swagger_client.api.bookings_api import BookingsApi

# our Api key
API_KEY = "07fb13b8-176a-4c9d-bfe6-9831271e3fac"

# init api client
client = ApiClient()
environments = EnvironmentsApi(client)
vehicles = VehiclesApi(client)
default = DefaultsApi(client)
bookings = BookingsApi(client)

# start flask
app = Flask(__name__)

# return all environments
@app.route('/environments', methods=['GET'])
def get_tasks():
    return str(environments.api_v2_environments_get(API_KEY))

# return a list of all vehicles
@app.route('api/v2/vehicles', methods=['GET'])
def get_all_vehicles():
    return vehicles.api_v2_vehicles_get(API_KEY)

# return all vehicle bookings
@app.route('/api/v2/bookings', methods=['GET'])
def get_bookings():
    return bookings.api_v2_bookings_get(API_KEY)

# return json with error if not found
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True, port=80)
