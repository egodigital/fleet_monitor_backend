import os
import sys

from flask import Flask, jsonify
from flask import make_response

from backend.api.swagger_client.api.bookings_api import BookingsApi
from backend.api.swagger_client.api.defaults_api import DefaultsApi
from swagger_client.api.environments_api import EnvironmentsApi
from swagger_client.api.vehicles_api import VehiclesApi
from swagger_client.api_client import ApiClient
myFolder = os.path.dirname(os.path.realpath(__file__))

# our Api key
API_KEY = "07fb13b8-176a-4c9d-bfe6-9831271e3fac"

# init api client
client = ApiClient()

# example
environment = EnvironmentsApi(client)
curr_environment = environment.api_v2_environments_get(API_KEY)

# print res
print(curr_environment)


def get_env():
    return curr_environment


app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


@app.route('/environment', methods=['GET'])
def get_tasks():
    return str(get_env())


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True, port=80)
