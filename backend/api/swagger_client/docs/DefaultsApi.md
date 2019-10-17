# swagger_client.DefaultsApi

All URIs are relative to *https://ego-vehicle-api.azurewebsites.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_delete**](DefaultsApi.md#api_v2_delete) | **DELETE** /api/v2 | Resets the data of the current team.
[**api_v2_get**](DefaultsApi.md#api_v2_get) | **GET** /api/v2 | Returns general information.


# **api_v2_delete**
> api_v2_delete(x_api_key)

Resets the data of the current team.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultsApi()
x_api_key = 'x_api_key_example' # str | The API key.

try:
    # Resets the data of the current team.
    api_instance.api_v2_delete(x_api_key)
except ApiException as e:
    print("Exception when calling DefaultsApi->api_v2_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| The API key. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_get**
> GeneralInfoResponse api_v2_get(x_api_key)

Returns general information.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultsApi()
x_api_key = 'x_api_key_example' # str | The API key.

try:
    # Returns general information.
    api_response = api_instance.api_v2_get(x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultsApi->api_v2_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| The API key. | 

### Return type

[**GeneralInfoResponse**](GeneralInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

