# swagger_client.AdminApi

All URIs are relative to *https://ego-vehicle-api.azurewebsites.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_teams_get**](AdminApi.md#admin_teams_get) | **GET** /admin/teams | Lists all teams.
[**admin_teams_post**](AdminApi.md#admin_teams_post) | **POST** /admin/teams | Creates a new team.


# **admin_teams_get**
> ListTeamsResponse admin_teams_get(token)

Lists all teams.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdminApi()
token = 'token_example' # str | The admin API key.

try:
    # Lists all teams.
    api_response = api_instance.admin_teams_get(token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_teams_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The admin API key. | 

### Return type

[**ListTeamsResponse**](ListTeamsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_teams_post**
> CreateTeamResponse admin_teams_post(body, token)

Creates a new team.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdminApi()
body = swagger_client.CreateTeamRequest() # CreateTeamRequest | Options for a request.
token = 'token_example' # str | The admin API key.

try:
    # Creates a new team.
    api_response = api_instance.admin_teams_post(body, token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_teams_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateTeamRequest**](CreateTeamRequest.md)| Options for a request. | 
 **token** | **str**| The admin API key. | 

### Return type

[**CreateTeamResponse**](CreateTeamResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

