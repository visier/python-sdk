# visier.sdk.api.data_out.VeeQueryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vee_query_feedback**](VeeQueryApi.md#vee_query_feedback) | **POST** /v1alpha/rest/vee/query-feedback | Submit Vee feedback
[**vee_query_request**](VeeQueryApi.md#vee_query_request) | **POST** /v1alpha/rest/vee/query | Ask Vee a question
[**vee_sample_questions**](VeeQueryApi.md#vee_sample_questions) | **GET** /v1alpha/rest/vee/sample-questions | Get a list of sample questions


# **vee_query_feedback**
> VeeFeedbackDTO vee_query_feedback(question=question, thread_state_question_state=thread_state_question_state, options_include_visual=options_include_visual, options_chart_options_width=options_chart_options_width, options_chart_options_height=options_chart_options_height, options_include_data=options_include_data, options_data_format=options_data_format, options_include_reworded_question=options_include_reworded_question)

Submit Vee feedback

Give Vee feedback on a previous response. POST the JSON response returned from `query` endpoint above,  along with a positive or negative rating (`isApproved`) and any further information you'd like to provide (`description`).   Example: `POST /v1alpha/rest/vee/query-feedback` returns a success or failure:  ```json  {      \"response\": { (valueof_json_response_from_query_endpoint) },      \"isApproved\": \"false\",      \"description\": \"I wanted to see more orgs in the answer!\"  }  ```  <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.sdk.api.data_out
from visier.sdk.api.data_out.models.vee_feedback_dto import VeeFeedbackDTO
from visier.sdk.api.data_out.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.sdk.api.data_out.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: CookieAuth
configuration.api_key['CookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['CookieAuth'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization: BearerAuth
configuration = visier.sdk.api.data_out.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.sdk.api.data_out.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.sdk.api.data_out.VeeQueryApi(api_client)
    question = 'question_example' # str |  (optional)
    thread_state_question_state = ['thread_state_question_state_example'] # List[str] |  (optional)
    options_include_visual = True # bool |  (optional)
    options_chart_options_width = 56 # int |  (optional)
    options_chart_options_height = 56 # int |  (optional)
    options_include_data = True # bool |  (optional)
    options_data_format = 'options_data_format_example' # str |  (optional)
    options_include_reworded_question = True # bool |  (optional)

    try:
        # Submit Vee feedback
        api_response = api_instance.vee_query_feedback(question=question, thread_state_question_state=thread_state_question_state, options_include_visual=options_include_visual, options_chart_options_width=options_chart_options_width, options_chart_options_height=options_chart_options_height, options_include_data=options_include_data, options_data_format=options_data_format, options_include_reworded_question=options_include_reworded_question)
        print("The response of VeeQueryApi->vee_query_feedback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VeeQueryApi->vee_query_feedback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question** | **str**|  | [optional] 
 **thread_state_question_state** | [**List[str]**](str.md)|  | [optional] 
 **options_include_visual** | **bool**|  | [optional] 
 **options_chart_options_width** | **int**|  | [optional] 
 **options_chart_options_height** | **int**|  | [optional] 
 **options_include_data** | **bool**|  | [optional] 
 **options_data_format** | **str**|  | [optional] 
 **options_include_reworded_question** | **bool**|  | [optional] 

### Return type

[**VeeFeedbackDTO**](VeeFeedbackDTO.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [OAuth2Auth](../README.md#OAuth2Auth), [OAuth2Auth](../README.md#OAuth2Auth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vee_query_request**
> VeeResponseDTO vee_query_request(question=question, thread_state_question_state=thread_state_question_state, options_include_visual=options_include_visual, options_chart_options_width=options_chart_options_width, options_chart_options_height=options_chart_options_height, options_include_data=options_include_data, options_data_format=options_data_format, options_include_reworded_question=options_include_reworded_question)

Ask Vee a question

Use this API to ask Vee a People Analytic question and receive a response.  Options `includeData` and `includeVisual` can be set in the request data to receive additional data corresponding to the answer.   [ Example 1 ] initiating a conversation with Vee: `POST v1alpha/rest/vee/query` with body data  ```json  {      \"question\": \"what is the headcount by gender in each org?\",      \"options\": {          \"includeVisual\": \"true\",          \"includeData\": \"true\",          \"rewordedQuestion\": \"true\"      }  }  ```  returns  ```json  {     \"threadState\": {         \"questionState\": [             \"(encrypted threadState string)\"         ]     },     \"statusCode\": {         \"statusCode\": \"VEE_API_SUCCESS\",         \"statusMsg\": \"Successful Vee response for question=what is the headcount by gender in each org?\"     },     \"narrative\": \"In Apr 2024, the Headcount: for Man & Operations was the largest at 165 (16.1% of total) and for Woman & BlueSphere was the smallest at 1 (0.1% of total).\",     \"chartUrl\": \"http://(vanity).visier.com/hr/prod/appcontainer#/analytics/queryFnChart?fn=(chartPath)\",     \"schema\": {         \"metrics\": [             \"Headcount\"         ],         \"dimensions\": [             {                 \"name\": \"Organization\"             },             {                 \"name\": \"Gender\"             },             {                 \"name\": \"Gender\",                 \"paths\": [                     \"Employee\"                 ]             },             {                 \"name\": \"Organization\",                 \"paths\": [                     \"Employee\"                 ]             }         ]     },     \"data\": {         \"dataJson\": \"(hidden for length)\",         \"context\": \"{\\\"filters\\\":[],\\\"timeFilter\\\":[\\\"Apr 2024\\\"]}\"   ,     \"visual\": {         \"image\": \"(base64 encoded PNG of rasterized chart)\"         \"title\": \"Trend of Average Hourly Rate by Gender\",         \"context\": \"{\\\"filters\\\":[],\\\"timeFilter\\\":[\\\"Apr 2024\\\"]}\"     },     \"rewordedQuestion\": \"What is the gender breakdown of our workforce by organization this month?\"  }  ```   [ Example 2 ] Asking Vee a followup question: `POST v1alpha/rest/vee/query` with body data:  ```json  {     \"question\": \"what about by tenure?\",     \"threadState\": {         \"questionState\": [             \"(valueof_questionState_from_Example_1_above)\"         ]     },     \"options\": {         \"includeVisual\": \"false\",         \"includeData\": \"true\",         \"rewordedQuestion\": \"false\"     }  }  ````  returns  ```json  {     \"threadState\": {         \"questionState\": [             \"(valueof_questionState_from_Example_1_above)\",             \"(new encrypted threadState string)\"         ]     },     \"statusCode\": {         \"statusCode\": \"VEE_API_SUCCESS\",         \"statusMsg\": \"Successful Vee response for question=what about by tenure?\"     },     \"narrative\": \"In Apr 2024, the Headcount by Tenure Range were: 0 to 1 yr was 205 (20% of total), 1 to 2 yrs was 121 (11.8% of total) and 2 to 3 yrs was 91 (8.86% of total)and 4 more.\",     \"chartUrl\": \"http://(vanity).visier.com/hr/prod/appcontainer#/analytics/queryFnChart?fn=(chartPath)\",     \"schema\": {         \"metrics\": [             \"Headcount\"         ],         \"dimensions\": [             {                 \"name\": \"Tenure Range\"             },             {                 \"name\": \"Tenure Range\",                 \"paths\": [                     \"Employee\"                 ]             }         ]     },     \"data\": {         \"dataJson\": \"(hidden)\",         \"context\": \"{\\\"filters\\\":[],\\\"timeFilter\\\":[\\\"Apr 2024\\\"]}\"     }  }  ```  <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.sdk.api.data_out
from visier.sdk.api.data_out.models.vee_response_dto import VeeResponseDTO
from visier.sdk.api.data_out.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.sdk.api.data_out.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: CookieAuth
configuration.api_key['CookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['CookieAuth'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization: BearerAuth
configuration = visier.sdk.api.data_out.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.sdk.api.data_out.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.sdk.api.data_out.VeeQueryApi(api_client)
    question = 'question_example' # str |  (optional)
    thread_state_question_state = ['thread_state_question_state_example'] # List[str] |  (optional)
    options_include_visual = True # bool |  (optional)
    options_chart_options_width = 56 # int |  (optional)
    options_chart_options_height = 56 # int |  (optional)
    options_include_data = True # bool |  (optional)
    options_data_format = 'options_data_format_example' # str |  (optional)
    options_include_reworded_question = True # bool |  (optional)

    try:
        # Ask Vee a question
        api_response = api_instance.vee_query_request(question=question, thread_state_question_state=thread_state_question_state, options_include_visual=options_include_visual, options_chart_options_width=options_chart_options_width, options_chart_options_height=options_chart_options_height, options_include_data=options_include_data, options_data_format=options_data_format, options_include_reworded_question=options_include_reworded_question)
        print("The response of VeeQueryApi->vee_query_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VeeQueryApi->vee_query_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question** | **str**|  | [optional] 
 **thread_state_question_state** | [**List[str]**](str.md)|  | [optional] 
 **options_include_visual** | **bool**|  | [optional] 
 **options_chart_options_width** | **int**|  | [optional] 
 **options_chart_options_height** | **int**|  | [optional] 
 **options_include_data** | **bool**|  | [optional] 
 **options_data_format** | **str**|  | [optional] 
 **options_include_reworded_question** | **bool**|  | [optional] 

### Return type

[**VeeResponseDTO**](VeeResponseDTO.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [OAuth2Auth](../README.md#OAuth2Auth), [OAuth2Auth](../README.md#OAuth2Auth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vee_sample_questions**
> VeeSampleQuestionLibraryDTO vee_sample_questions(question=question, thread_state_question_state=thread_state_question_state, options_include_visual=options_include_visual, options_chart_options_width=options_chart_options_width, options_chart_options_height=options_chart_options_height, options_include_data=options_include_data, options_data_format=options_data_format, options_include_reworded_question=options_include_reworded_question)

Get a list of sample questions

To get started with Vee, use this API to get a list of sample questions.  Example: `GET /v1alpha/rest/vee/sample-questions` returns a string list of questions.  ```json     questions {         \"questions\": \"What is the turnover rate?\"         \"metadata\": {             \"categories\": \"metricQuestion\"\"         }     }  ```   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.sdk.api.data_out
from visier.sdk.api.data_out.models.vee_sample_question_library_dto import VeeSampleQuestionLibraryDTO
from visier.sdk.api.data_out.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.sdk.api.data_out.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: CookieAuth
configuration.api_key['CookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['CookieAuth'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization: BearerAuth
configuration = visier.sdk.api.data_out.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.sdk.api.data_out.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.sdk.api.data_out.VeeQueryApi(api_client)
    question = 'question_example' # str |  (optional)
    thread_state_question_state = ['thread_state_question_state_example'] # List[str] |  (optional)
    options_include_visual = True # bool |  (optional)
    options_chart_options_width = 56 # int |  (optional)
    options_chart_options_height = 56 # int |  (optional)
    options_include_data = True # bool |  (optional)
    options_data_format = 'options_data_format_example' # str |  (optional)
    options_include_reworded_question = True # bool |  (optional)

    try:
        # Get a list of sample questions
        api_response = api_instance.vee_sample_questions(question=question, thread_state_question_state=thread_state_question_state, options_include_visual=options_include_visual, options_chart_options_width=options_chart_options_width, options_chart_options_height=options_chart_options_height, options_include_data=options_include_data, options_data_format=options_data_format, options_include_reworded_question=options_include_reworded_question)
        print("The response of VeeQueryApi->vee_sample_questions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VeeQueryApi->vee_sample_questions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question** | **str**|  | [optional] 
 **thread_state_question_state** | [**List[str]**](str.md)|  | [optional] 
 **options_include_visual** | **bool**|  | [optional] 
 **options_chart_options_width** | **int**|  | [optional] 
 **options_chart_options_height** | **int**|  | [optional] 
 **options_include_data** | **bool**|  | [optional] 
 **options_data_format** | **str**|  | [optional] 
 **options_include_reworded_question** | **bool**|  | [optional] 

### Return type

[**VeeSampleQuestionLibraryDTO**](VeeSampleQuestionLibraryDTO.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [OAuth2Auth](../README.md#OAuth2Auth), [OAuth2Auth](../README.md#OAuth2Auth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

