# swagger_client.EnvironmentsApi

All URIs are relative to *https://ego-vehicle-api.azurewebsites.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_environments_environment_id_vehicles_get**](EnvironmentsApi.md#api_v2_environments_environment_id_vehicles_get) | **GET** /api/v2/environments/{environment_id}/vehicles | Returns a list of all vehicles of an environment.
[**api_v2_environments_get**](EnvironmentsApi.md#api_v2_environments_get) | **GET** /api/v2/environments | Returns a list of all environments.


# **api_v2_environments_environment_id_vehicles_get**
> VehicleListResponse api_v2_environments_environment_id_vehicles_get(x_api_key, environment_id)

Returns a list of all vehicles of an environment.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EnvironmentsApi()
x_api_key = 'x_api_key_example' # str | The API key.
environment_id = 'environment_id_example' # str | The ID of the environment.

try:
    # Returns a list of all vehicles of an environment.
    api_response = api_instance.api_v2_environments_environment_id_vehicles_get(x_api_key, environment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->api_v2_environments_environment_id_vehicles_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| The API key. | 
 **environment_id** | **str**| The ID of the environment. | 

### Return type

[**VehicleListResponse**](VehicleListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_environments_get**
> EnvironmentListResponse api_v2_environments_get(x_api_key)

Returns a list of all environments.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EnvironmentsApi()
x_api_key = 'x_api_key_example' # str | The API key.

try:
    # Returns a list of all environments.
    api_response = api_instance.api_v2_environments_get(x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->api_v2_environments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| The API key. | 

### Return type

[**EnvironmentListResponse**](EnvironmentListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

