# swagger_client.BookingsApi

All URIs are relative to *https://ego-vehicle-api.azurewebsites.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_bookings_booking_id_cancel_patch**](BookingsApi.md#api_v2_bookings_booking_id_cancel_patch) | **PATCH** /api/v2/bookings/{booking_id}/cancel | Cancels a booking.
[**api_v2_bookings_booking_id_delete**](BookingsApi.md#api_v2_bookings_booking_id_delete) | **DELETE** /api/v2/bookings/{booking_id} | Deletes a vehicle booking.
[**api_v2_bookings_booking_id_finish_patch**](BookingsApi.md#api_v2_bookings_booking_id_finish_patch) | **PATCH** /api/v2/bookings/{booking_id}/finish | Finishes a booking.
[**api_v2_bookings_booking_id_start_patch**](BookingsApi.md#api_v2_bookings_booking_id_start_patch) | **PATCH** /api/v2/bookings/{booking_id}/start | Starts a booking.
[**api_v2_bookings_get**](BookingsApi.md#api_v2_bookings_get) | **GET** /api/v2/bookings | Returns all vehicle bookings.


# **api_v2_bookings_booking_id_cancel_patch**
> CancelVehicleBookingResponse api_v2_bookings_booking_id_cancel_patch(x_api_key, booking_id)

Cancels a booking.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BookingsApi()
x_api_key = 'x_api_key_example' # str | The API key.
booking_id = 'booking_id_example' # str | The ID of the booking.

try:
    # Cancels a booking.
    api_response = api_instance.api_v2_bookings_booking_id_cancel_patch(x_api_key, booking_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BookingsApi->api_v2_bookings_booking_id_cancel_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| The API key. | 
 **booking_id** | **str**| The ID of the booking. | 

### Return type

[**CancelVehicleBookingResponse**](CancelVehicleBookingResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_bookings_booking_id_delete**
> DeleteVehicleBookingResponse api_v2_bookings_booking_id_delete(x_api_key, booking_id)

Deletes a vehicle booking.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BookingsApi()
x_api_key = 'x_api_key_example' # str | The API key.
booking_id = 'booking_id_example' # str | The ID of the booking.

try:
    # Deletes a vehicle booking.
    api_response = api_instance.api_v2_bookings_booking_id_delete(x_api_key, booking_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BookingsApi->api_v2_bookings_booking_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| The API key. | 
 **booking_id** | **str**| The ID of the booking. | 

### Return type

[**DeleteVehicleBookingResponse**](DeleteVehicleBookingResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_bookings_booking_id_finish_patch**
> FinishVehicleBookingResponse api_v2_bookings_booking_id_finish_patch(x_api_key, booking_id)

Finishes a booking.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BookingsApi()
x_api_key = 'x_api_key_example' # str | The API key.
booking_id = 'booking_id_example' # str | The ID of the booking.

try:
    # Finishes a booking.
    api_response = api_instance.api_v2_bookings_booking_id_finish_patch(x_api_key, booking_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BookingsApi->api_v2_bookings_booking_id_finish_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| The API key. | 
 **booking_id** | **str**| The ID of the booking. | 

### Return type

[**FinishVehicleBookingResponse**](FinishVehicleBookingResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_bookings_booking_id_start_patch**
> StartVehicleBookingResponse api_v2_bookings_booking_id_start_patch(x_api_key, booking_id)

Starts a booking.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BookingsApi()
x_api_key = 'x_api_key_example' # str | The API key.
booking_id = 'booking_id_example' # str | The ID of the booking.

try:
    # Starts a booking.
    api_response = api_instance.api_v2_bookings_booking_id_start_patch(x_api_key, booking_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BookingsApi->api_v2_bookings_booking_id_start_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| The API key. | 
 **booking_id** | **str**| The ID of the booking. | 

### Return type

[**StartVehicleBookingResponse**](StartVehicleBookingResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_bookings_get**
> VehicleBookingListResponse api_v2_bookings_get(x_api_key, _from=_from, until=until)

Returns all vehicle bookings.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BookingsApi()
x_api_key = 'x_api_key_example' # str | The API key.
_from = '_from_example' # str | The filter for start date (UTC). (optional)
until = 'until_example' # str | The filter for end date (UTC). (optional)

try:
    # Returns all vehicle bookings.
    api_response = api_instance.api_v2_bookings_get(x_api_key, _from=_from, until=until)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BookingsApi->api_v2_bookings_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| The API key. | 
 **_from** | **str**| The filter for start date (UTC). | [optional] 
 **until** | **str**| The filter for end date (UTC). | [optional] 

### Return type

[**VehicleBookingListResponse**](VehicleBookingListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

