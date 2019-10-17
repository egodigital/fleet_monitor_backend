# swagger_client.VehiclesApi

All URIs are relative to *https://ego-vehicle-api.azurewebsites.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_vehicles_get**](VehiclesApi.md#api_v2_vehicles_get) | **GET** /api/v2/vehicles | Returns a list of all vehicles.
[**api_v2_vehicles_post**](VehiclesApi.md#api_v2_vehicles_post) | **POST** /api/v2/vehicles | Creates a new vehicle.
[**api_v2_vehicles_vehicle_id_bookings_get**](VehiclesApi.md#api_v2_vehicles_vehicle_id_bookings_get) | **GET** /api/v2/vehicles/{vehicle_id}/bookings | Returns a list of bookings of a vehicle, with optional filters.
[**api_v2_vehicles_vehicle_id_bookings_post**](VehiclesApi.md#api_v2_vehicles_vehicle_id_bookings_post) | **POST** /api/v2/vehicles/{vehicle_id}/bookings | Creates a new booking for a vehicle.
[**api_v2_vehicles_vehicle_id_delete**](VehiclesApi.md#api_v2_vehicles_vehicle_id_delete) | **DELETE** /api/v2/vehicles/{vehicle_id} | Resets the complete vehicle.
[**api_v2_vehicles_vehicle_id_events_delete**](VehiclesApi.md#api_v2_vehicles_vehicle_id_events_delete) | **DELETE** /api/v2/vehicles/{vehicle_id}/events | Removes the complete queue of events.
[**api_v2_vehicles_vehicle_id_events_get**](VehiclesApi.md#api_v2_vehicles_vehicle_id_events_get) | **GET** /api/v2/vehicles/{vehicle_id}/events | Gets a list of unhandled events and marks them as handled.
[**api_v2_vehicles_vehicle_id_get**](VehiclesApi.md#api_v2_vehicles_vehicle_id_get) | **GET** /api/v2/vehicles/{vehicle_id} | Returns the information of the vehicle.
[**api_v2_vehicles_vehicle_id_infotainment_delete**](VehiclesApi.md#api_v2_vehicles_vehicle_id_infotainment_delete) | **DELETE** /api/v2/vehicles/{vehicle_id}/infotainment | Resets the infotainment screen.
[**api_v2_vehicles_vehicle_id_infotainment_get**](VehiclesApi.md#api_v2_vehicles_vehicle_id_infotainment_get) | **GET** /api/v2/vehicles/{vehicle_id}/infotainment | Gets the current infotainment screen.
[**api_v2_vehicles_vehicle_id_infotainment_post**](VehiclesApi.md#api_v2_vehicles_vehicle_id_infotainment_post) | **POST** /api/v2/vehicles/{vehicle_id}/infotainment | Sets the data of the screen as image or video.
[**api_v2_vehicles_vehicle_id_infotainment_put**](VehiclesApi.md#api_v2_vehicles_vehicle_id_infotainment_put) | **PUT** /api/v2/vehicles/{vehicle_id}/infotainment | Writes an image to the infotainment screen.
[**api_v2_vehicles_vehicle_id_infotainment_text_put**](VehiclesApi.md#api_v2_vehicles_vehicle_id_infotainment_text_put) | **PUT** /api/v2/vehicles/{vehicle_id}/infotainment/text | Writes text to the infotainment system.
[**api_v2_vehicles_vehicle_id_logs_signals_delete**](VehiclesApi.md#api_v2_vehicles_vehicle_id_logs_signals_delete) | **DELETE** /api/v2/vehicles/{vehicle_id}/logs/signals | Deletes all vehicle signal logs.
[**api_v2_vehicles_vehicle_id_logs_signals_get**](VehiclesApi.md#api_v2_vehicles_vehicle_id_logs_signals_get) | **GET** /api/v2/vehicles/{vehicle_id}/logs/signals | Gets vehicle signal logs.
[**api_v2_vehicles_vehicle_id_patch**](VehiclesApi.md#api_v2_vehicles_vehicle_id_patch) | **PATCH** /api/v2/vehicles/{vehicle_id} | Updates a vehicle.
[**api_v2_vehicles_vehicle_id_signals_delete**](VehiclesApi.md#api_v2_vehicles_vehicle_id_signals_delete) | **DELETE** /api/v2/vehicles/{vehicle_id}/signals | Resets all signals.
[**api_v2_vehicles_vehicle_id_signals_get**](VehiclesApi.md#api_v2_vehicles_vehicle_id_signals_get) | **GET** /api/v2/vehicles/{vehicle_id}/signals | Gets a list of all signals.
[**api_v2_vehicles_vehicle_id_signals_patch**](VehiclesApi.md#api_v2_vehicles_vehicle_id_signals_patch) | **PATCH** /api/v2/vehicles/{vehicle_id}/signals | Updates a list of one or more vehicle signals.
[**api_v2_vehicles_vehicle_id_state_delete**](VehiclesApi.md#api_v2_vehicles_vehicle_id_state_delete) | **DELETE** /api/v2/vehicles/{vehicle_id}/state | Unsets the state value for the vehicle.
[**api_v2_vehicles_vehicle_id_state_get**](VehiclesApi.md#api_v2_vehicles_vehicle_id_state_get) | **GET** /api/v2/vehicles/{vehicle_id}/state | Gets the state value of the vehicle.
[**api_v2_vehicles_vehicle_id_state_patch**](VehiclesApi.md#api_v2_vehicles_vehicle_id_state_patch) | **PATCH** /api/v2/vehicles/{vehicle_id}/state | Sets a state value for the vehicle.


# **api_v2_vehicles_get**
> VehicleListResponse api_v2_vehicles_get(x_api_key)

Returns a list of all vehicles.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VehiclesApi()
x_api_key = 'x_api_key_example' # str | The API key.

try:
    # Returns a list of all vehicles.
    api_response = api_instance.api_v2_vehicles_get(x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VehiclesApi->api_v2_vehicles_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| The API key. | 

### Return type

[**VehicleListResponse**](VehicleListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_vehicles_post**
> CreateVehicleResponse api_v2_vehicles_post(body, x_api_key)

Creates a new vehicle.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VehiclesApi()
body = swagger_client.CreateVehicleRequest() # CreateVehicleRequest | Options for a request.
x_api_key = 'x_api_key_example' # str | The API key.

try:
    # Creates a new vehicle.
    api_response = api_instance.api_v2_vehicles_post(body, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VehiclesApi->api_v2_vehicles_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateVehicleRequest**](CreateVehicleRequest.md)| Options for a request. | 
 **x_api_key** | **str**| The API key. | 

### Return type

[**CreateVehicleResponse**](CreateVehicleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_vehicles_vehicle_id_bookings_get**
> VehicleBookingListResponse api_v2_vehicles_vehicle_id_bookings_get(x_api_key, vehicle_id, _from=_from, status=status, until=until, vehicle=vehicle)

Returns a list of bookings of a vehicle, with optional filters.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VehiclesApi()
x_api_key = 'x_api_key_example' # str | The API key.
vehicle_id = 'vehicle_id_example' # str | The ID of the vehicle.
_from = '_from_example' # str | The filter for start date (UTC). (optional)
status = 'status_example' # str | The filter for the status. (optional)
until = 'until_example' # str | The filter for end date (UTC). (optional)
vehicle = 'vehicle_example' # str | The filter for the ID of the vehicle. (optional)

try:
    # Returns a list of bookings of a vehicle, with optional filters.
    api_response = api_instance.api_v2_vehicles_vehicle_id_bookings_get(x_api_key, vehicle_id, _from=_from, status=status, until=until, vehicle=vehicle)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VehiclesApi->api_v2_vehicles_vehicle_id_bookings_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| The API key. | 
 **vehicle_id** | **str**| The ID of the vehicle. | 
 **_from** | **str**| The filter for start date (UTC). | [optional] 
 **status** | **str**| The filter for the status. | [optional] 
 **until** | **str**| The filter for end date (UTC). | [optional] 
 **vehicle** | **str**| The filter for the ID of the vehicle. | [optional] 

### Return type

[**VehicleBookingListResponse**](VehicleBookingListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_vehicles_vehicle_id_bookings_post**
> CreateVehicleBookingResponse api_v2_vehicles_vehicle_id_bookings_post(body, x_api_key, vehicle_id)

Creates a new booking for a vehicle.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VehiclesApi()
body = swagger_client.CreateVehicleBookingRequest() # CreateVehicleBookingRequest | Options for a request.
x_api_key = 'x_api_key_example' # str | The API key.
vehicle_id = 'vehicle_id_example' # str | The ID of the vehicle.

try:
    # Creates a new booking for a vehicle.
    api_response = api_instance.api_v2_vehicles_vehicle_id_bookings_post(body, x_api_key, vehicle_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VehiclesApi->api_v2_vehicles_vehicle_id_bookings_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateVehicleBookingRequest**](CreateVehicleBookingRequest.md)| Options for a request. | 
 **x_api_key** | **str**| The API key. | 
 **vehicle_id** | **str**| The ID of the vehicle. | 

### Return type

[**CreateVehicleBookingResponse**](CreateVehicleBookingResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_vehicles_vehicle_id_delete**
> DeleteVehicleResponse api_v2_vehicles_vehicle_id_delete(x_api_key, vehicle_id)

Resets the complete vehicle.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VehiclesApi()
x_api_key = 'x_api_key_example' # str | The API key.
vehicle_id = 'vehicle_id_example' # str | The ID of the vehicle.

try:
    # Resets the complete vehicle.
    api_response = api_instance.api_v2_vehicles_vehicle_id_delete(x_api_key, vehicle_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VehiclesApi->api_v2_vehicles_vehicle_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| The API key. | 
 **vehicle_id** | **str**| The ID of the vehicle. | 

### Return type

[**DeleteVehicleResponse**](DeleteVehicleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_vehicles_vehicle_id_events_delete**
> api_v2_vehicles_vehicle_id_events_delete(x_api_key, vehicle_id)

Removes the complete queue of events.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VehiclesApi()
x_api_key = 'x_api_key_example' # str | The API key.
vehicle_id = 'vehicle_id_example' # str | The ID of the vehicle.

try:
    # Removes the complete queue of events.
    api_instance.api_v2_vehicles_vehicle_id_events_delete(x_api_key, vehicle_id)
except ApiException as e:
    print("Exception when calling VehiclesApi->api_v2_vehicles_vehicle_id_events_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| The API key. | 
 **vehicle_id** | **str**| The ID of the vehicle. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_vehicles_vehicle_id_events_get**
> VehicleEventListResponse api_v2_vehicles_vehicle_id_events_get(x_api_key, vehicle_id, filter=filter)

Gets a list of unhandled events and marks them as handled.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VehiclesApi()
x_api_key = 'x_api_key_example' # str | The API key.
vehicle_id = 'vehicle_id_example' # str | The ID of the vehicle.
filter = 'filter_example' # str | Regex filter for event name (case insensitive). (optional)

try:
    # Gets a list of unhandled events and marks them as handled.
    api_response = api_instance.api_v2_vehicles_vehicle_id_events_get(x_api_key, vehicle_id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VehiclesApi->api_v2_vehicles_vehicle_id_events_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| The API key. | 
 **vehicle_id** | **str**| The ID of the vehicle. | 
 **filter** | **str**| Regex filter for event name (case insensitive). | [optional] 

### Return type

[**VehicleEventListResponse**](VehicleEventListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_vehicles_vehicle_id_get**
> GetVehicleResponse api_v2_vehicles_vehicle_id_get(x_api_key, vehicle_id)

Returns the information of the vehicle.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VehiclesApi()
x_api_key = 'x_api_key_example' # str | The API key.
vehicle_id = 'vehicle_id_example' # str | The ID of the vehicle.

try:
    # Returns the information of the vehicle.
    api_response = api_instance.api_v2_vehicles_vehicle_id_get(x_api_key, vehicle_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VehiclesApi->api_v2_vehicles_vehicle_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| The API key. | 
 **vehicle_id** | **str**| The ID of the vehicle. | 

### Return type

[**GetVehicleResponse**](GetVehicleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_vehicles_vehicle_id_infotainment_delete**
> api_v2_vehicles_vehicle_id_infotainment_delete(x_api_key, vehicle_id)

Resets the infotainment screen.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VehiclesApi()
x_api_key = 'x_api_key_example' # str | The API key.
vehicle_id = 'vehicle_id_example' # str | The ID of the vehicle.

try:
    # Resets the infotainment screen.
    api_instance.api_v2_vehicles_vehicle_id_infotainment_delete(x_api_key, vehicle_id)
except ApiException as e:
    print("Exception when calling VehiclesApi->api_v2_vehicles_vehicle_id_infotainment_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| The API key. | 
 **vehicle_id** | **str**| The ID of the vehicle. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_vehicles_vehicle_id_infotainment_get**
> api_v2_vehicles_vehicle_id_infotainment_get(x_api_key, vehicle_id, cache=cache)

Gets the current infotainment screen.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VehiclesApi()
x_api_key = 'x_api_key_example' # str | The API key.
vehicle_id = 'vehicle_id_example' # str | The ID of the vehicle.
cache = 0 # float | Use cache or not. (optional) (default to 0)

try:
    # Gets the current infotainment screen.
    api_instance.api_v2_vehicles_vehicle_id_infotainment_get(x_api_key, vehicle_id, cache=cache)
except ApiException as e:
    print("Exception when calling VehiclesApi->api_v2_vehicles_vehicle_id_infotainment_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| The API key. | 
 **vehicle_id** | **str**| The ID of the vehicle. | 
 **cache** | **float**| Use cache or not. | [optional] [default to 0]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_vehicles_vehicle_id_infotainment_post**
> api_v2_vehicles_vehicle_id_infotainment_post(x_api_key, image, vehicle_id)

Sets the data of the screen as image or video.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VehiclesApi()
x_api_key = 'x_api_key_example' # str | The API key.
image = 'B' # str | The image to write / insert.
vehicle_id = 'vehicle_id_example' # str | The ID of the vehicle.

try:
    # Sets the data of the screen as image or video.
    api_instance.api_v2_vehicles_vehicle_id_infotainment_post(x_api_key, image, vehicle_id)
except ApiException as e:
    print("Exception when calling VehiclesApi->api_v2_vehicles_vehicle_id_infotainment_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| The API key. | 
 **image** | **str**| The image to write / insert. | 
 **vehicle_id** | **str**| The ID of the vehicle. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: image/bmp, image/gif, image/jpeg, image/png, image/tiff, text/plain, video/mp4, video/mpeg, video/ogg
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_vehicles_vehicle_id_infotainment_put**
> api_v2_vehicles_vehicle_id_infotainment_put(image, x_api_key, vehicle_id, x=x, y=y)

Writes an image to the infotainment screen.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VehiclesApi()
image = 'B' # str | The image to write / insert.
x_api_key = 'x_api_key_example' # str | The API key.
vehicle_id = 'vehicle_id_example' # str | The ID of the vehicle.
x = 0 # float | The x coorinate where to place the image. (optional) (default to 0)
y = 0 # float | The y coorinate where to place the image. (optional) (default to 0)

try:
    # Writes an image to the infotainment screen.
    api_instance.api_v2_vehicles_vehicle_id_infotainment_put(image, x_api_key, vehicle_id, x=x, y=y)
except ApiException as e:
    print("Exception when calling VehiclesApi->api_v2_vehicles_vehicle_id_infotainment_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image** | **str**| The image to write / insert. | 
 **x_api_key** | **str**| The API key. | 
 **vehicle_id** | **str**| The ID of the vehicle. | 
 **x** | **float**| The x coorinate where to place the image. | [optional] [default to 0]
 **y** | **float**| The y coorinate where to place the image. | [optional] [default to 0]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: image/png

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_vehicles_vehicle_id_infotainment_text_put**
> api_v2_vehicles_vehicle_id_infotainment_text_put(text, x_api_key, vehicle_id, black=black, size=size, x=x, y=y)

Writes text to the infotainment system.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VehiclesApi()
text = 'text_example' # str | The text to write / insert.
x_api_key = 'x_api_key_example' # str | The API key.
vehicle_id = 'vehicle_id_example' # str | The ID of the vehicle.
black = 0 # float | Indicates if to use black font color or not. (optional) (default to 0)
size = 32 # float | The font size. (optional) (default to 32)
x = 0 # float | The x coorinate where to place the text. (optional) (default to 0)
y = 0 # float | The y coorinate where to place the text. (optional) (default to 0)

try:
    # Writes text to the infotainment system.
    api_instance.api_v2_vehicles_vehicle_id_infotainment_text_put(text, x_api_key, vehicle_id, black=black, size=size, x=x, y=y)
except ApiException as e:
    print("Exception when calling VehiclesApi->api_v2_vehicles_vehicle_id_infotainment_text_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| The text to write / insert. | 
 **x_api_key** | **str**| The API key. | 
 **vehicle_id** | **str**| The ID of the vehicle. | 
 **black** | **float**| Indicates if to use black font color or not. | [optional] [default to 0]
 **size** | **float**| The font size. | [optional] [default to 32]
 **x** | **float**| The x coorinate where to place the text. | [optional] [default to 0]
 **y** | **float**| The y coorinate where to place the text. | [optional] [default to 0]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: image/png

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_vehicles_vehicle_id_logs_signals_delete**
> api_v2_vehicles_vehicle_id_logs_signals_delete(x_api_key, vehicle_id)

Deletes all vehicle signal logs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VehiclesApi()
x_api_key = 'x_api_key_example' # str | The API key.
vehicle_id = 'vehicle_id_example' # str | The ID of the vehicle.

try:
    # Deletes all vehicle signal logs.
    api_instance.api_v2_vehicles_vehicle_id_logs_signals_delete(x_api_key, vehicle_id)
except ApiException as e:
    print("Exception when calling VehiclesApi->api_v2_vehicles_vehicle_id_logs_signals_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| The API key. | 
 **vehicle_id** | **str**| The ID of the vehicle. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_vehicles_vehicle_id_logs_signals_get**
> VehicleSignalLogListResponse api_v2_vehicles_vehicle_id_logs_signals_get(x_api_key, vehicle_id, limit=limit, offset=offset, sort=sort, filter=filter)

Gets vehicle signal logs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VehiclesApi()
x_api_key = 'x_api_key_example' # str | The API key.
vehicle_id = 'vehicle_id_example' # str | The ID of the vehicle.
limit = 100 # float | The maximum number of results. (optional) (default to 100)
offset = 0 # float | The zero based offset. (optional) (default to 0)
sort = 'desc' # str | Sort order. (optional) (default to desc)
filter = 'filter_example' # str | Regex filter for signal name (case insensitive). (optional)

try:
    # Gets vehicle signal logs.
    api_response = api_instance.api_v2_vehicles_vehicle_id_logs_signals_get(x_api_key, vehicle_id, limit=limit, offset=offset, sort=sort, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VehiclesApi->api_v2_vehicles_vehicle_id_logs_signals_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| The API key. | 
 **vehicle_id** | **str**| The ID of the vehicle. | 
 **limit** | **float**| The maximum number of results. | [optional] [default to 100]
 **offset** | **float**| The zero based offset. | [optional] [default to 0]
 **sort** | **str**| Sort order. | [optional] [default to desc]
 **filter** | **str**| Regex filter for signal name (case insensitive). | [optional] 

### Return type

[**VehicleSignalLogListResponse**](VehicleSignalLogListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_vehicles_vehicle_id_patch**
> UpdateVehicleResponse api_v2_vehicles_vehicle_id_patch(update_vehicle_options, x_api_key, vehicle_id)

Updates a vehicle.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VehiclesApi()
update_vehicle_options = swagger_client.UpdateVehicleRequest() # UpdateVehicleRequest | The data to update.
x_api_key = 'x_api_key_example' # str | The API key.
vehicle_id = 'vehicle_id_example' # str | The ID of the vehicle.

try:
    # Updates a vehicle.
    api_response = api_instance.api_v2_vehicles_vehicle_id_patch(update_vehicle_options, x_api_key, vehicle_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VehiclesApi->api_v2_vehicles_vehicle_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_vehicle_options** | [**UpdateVehicleRequest**](UpdateVehicleRequest.md)| The data to update. | 
 **x_api_key** | **str**| The API key. | 
 **vehicle_id** | **str**| The ID of the vehicle. | 

### Return type

[**UpdateVehicleResponse**](UpdateVehicleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_vehicles_vehicle_id_signals_delete**
> VehicleSignalListResponse api_v2_vehicles_vehicle_id_signals_delete(x_api_key, vehicle_id)

Resets all signals.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VehiclesApi()
x_api_key = 'x_api_key_example' # str | The API key.
vehicle_id = 'vehicle_id_example' # str | The ID of the vehicle.

try:
    # Resets all signals.
    api_response = api_instance.api_v2_vehicles_vehicle_id_signals_delete(x_api_key, vehicle_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VehiclesApi->api_v2_vehicles_vehicle_id_signals_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| The API key. | 
 **vehicle_id** | **str**| The ID of the vehicle. | 

### Return type

[**VehicleSignalListResponse**](VehicleSignalListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_vehicles_vehicle_id_signals_get**
> VehicleSignalListResponse api_v2_vehicles_vehicle_id_signals_get(x_api_key, vehicle_id, cache=cache)

Gets a list of all signals.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VehiclesApi()
x_api_key = 'x_api_key_example' # str | The API key.
vehicle_id = 'vehicle_id_example' # str | The ID of the vehicle.
cache = 0 # float | Use cache or not. (optional) (default to 0)

try:
    # Gets a list of all signals.
    api_response = api_instance.api_v2_vehicles_vehicle_id_signals_get(x_api_key, vehicle_id, cache=cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VehiclesApi->api_v2_vehicles_vehicle_id_signals_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| The API key. | 
 **vehicle_id** | **str**| The ID of the vehicle. | 
 **cache** | **float**| Use cache or not. | [optional] [default to 0]

### Return type

[**VehicleSignalListResponse**](VehicleSignalListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_vehicles_vehicle_id_signals_patch**
> VehicleSignalListResponse api_v2_vehicles_vehicle_id_signals_patch(list_of_vehicle_signals_to_update, x_api_key, vehicle_id)

Updates a list of one or more vehicle signals.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VehiclesApi()
list_of_vehicle_signals_to_update = swagger_client.VehicleSignalListForPatchExample() # VehicleSignalListForPatchExample | A list of one or more value signals to update.
x_api_key = 'x_api_key_example' # str | The API key.
vehicle_id = 'vehicle_id_example' # str | The ID of the vehicle.

try:
    # Updates a list of one or more vehicle signals.
    api_response = api_instance.api_v2_vehicles_vehicle_id_signals_patch(list_of_vehicle_signals_to_update, x_api_key, vehicle_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VehiclesApi->api_v2_vehicles_vehicle_id_signals_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_of_vehicle_signals_to_update** | [**VehicleSignalListForPatchExample**](VehicleSignalListForPatchExample.md)| A list of one or more value signals to update. | 
 **x_api_key** | **str**| The API key. | 
 **vehicle_id** | **str**| The ID of the vehicle. | 

### Return type

[**VehicleSignalListResponse**](VehicleSignalListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_vehicles_vehicle_id_state_delete**
> api_v2_vehicles_vehicle_id_state_delete(x_api_key, vehicle_id)

Unsets the state value for the vehicle.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VehiclesApi()
x_api_key = 'x_api_key_example' # str | The API key.
vehicle_id = 'vehicle_id_example' # str | The ID of the vehicle.

try:
    # Unsets the state value for the vehicle.
    api_instance.api_v2_vehicles_vehicle_id_state_delete(x_api_key, vehicle_id)
except ApiException as e:
    print("Exception when calling VehiclesApi->api_v2_vehicles_vehicle_id_state_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| The API key. | 
 **vehicle_id** | **str**| The ID of the vehicle. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_vehicles_vehicle_id_state_get**
> api_v2_vehicles_vehicle_id_state_get(x_api_key, vehicle_id)

Gets the state value of the vehicle.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VehiclesApi()
x_api_key = 'x_api_key_example' # str | The API key.
vehicle_id = 'vehicle_id_example' # str | The ID of the vehicle.

try:
    # Gets the state value of the vehicle.
    api_instance.api_v2_vehicles_vehicle_id_state_get(x_api_key, vehicle_id)
except ApiException as e:
    print("Exception when calling VehiclesApi->api_v2_vehicles_vehicle_id_state_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| The API key. | 
 **vehicle_id** | **str**| The ID of the vehicle. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_vehicles_vehicle_id_state_patch**
> api_v2_vehicles_vehicle_id_state_patch(x_api_key, new_vehicle_state_value, vehicle_id)

Sets a state value for the vehicle.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VehiclesApi()
x_api_key = 'x_api_key_example' # str | The API key.
new_vehicle_state_value = 'new_vehicle_state_value_example' # str | The new value.
vehicle_id = 'vehicle_id_example' # str | The ID of the vehicle.

try:
    # Sets a state value for the vehicle.
    api_instance.api_v2_vehicles_vehicle_id_state_patch(x_api_key, new_vehicle_state_value, vehicle_id)
except ApiException as e:
    print("Exception when calling VehiclesApi->api_v2_vehicles_vehicle_id_state_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| The API key. | 
 **new_vehicle_state_value** | **str**| The new value. | 
 **vehicle_id** | **str**| The ID of the vehicle. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

