#set sys path to import swagger client
import os, sys
myFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, "./../api/")

#import all Apis
from swagger_client.api_client import ApiClient
from swagger_client.api.vehicles_api import VehiclesApi
from swagger_client.api.environments_api import EnvironmentsApi
from swagger_client.api.defaults_api import DefaultsApi
from swagger_client.api.bookings_api import BookingsApi

#our Api key
API_KEY = "07fb13b8-176a-4c9d-bfe6-9831271e3fac"

#init api client
client = ApiClient()

#example
environment = EnvironmentsApi(client)
curr_environment = environment.api_v2_environments_get(API_KEY)

#print res
print(curr_environment)

def get_env():
    return curr_environment
