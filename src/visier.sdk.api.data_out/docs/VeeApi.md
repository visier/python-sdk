# visier.sdk.api.data_out.VeeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vee_feedback**](VeeApi.md#vee_feedback) | **POST** /v1alpha/rest/vee/feedback | Submit Vee feedback
[**vee_question_request**](VeeApi.md#vee_question_request) | **POST** /v1alpha/rest/vee/question | Ask Vee a question
[**vee_sample_questions**](VeeApi.md#vee_sample_questions) | **GET** /v1alpha/rest/vee/sample-questions | Retrieve a list of sample questions to ask Vee


# **vee_feedback**
> VeeStatusCodeDTO vee_feedback(vee_feedback_dto)

Submit Vee feedback

Give Vee feedback for a previous answer. To submit feedback, include:  * The response object from the `/question` response.  * A rating of Vee's answer. If `isApproved` is `true`, Vee answered the question correctly. If `isApproved` is `false`, Vee's answer was incorrect or lacked details.  * A description of how Vee should have answered the question or how Vee can improve the answer, such as \"Expected Headcount metric, but Vee returned Average Headcount\".   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.sdk.api.data_out
from visier.sdk.api.data_out.models.vee_feedback_dto import VeeFeedbackDTO
from visier.sdk.api.data_out.models.vee_status_code_dto import VeeStatusCodeDTO
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
    api_instance = visier.sdk.api.data_out.VeeApi(api_client)
    vee_feedback_dto = visier.sdk.api.data_out.VeeFeedbackDTO() # VeeFeedbackDTO | 

    try:
        # Submit Vee feedback
        api_response = api_instance.vee_feedback(vee_feedback_dto)
        print("The response of VeeApi->vee_feedback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VeeApi->vee_feedback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vee_feedback_dto** | [**VeeFeedbackDTO**](VeeFeedbackDTO.md)|  | 

### Return type

[**VeeStatusCodeDTO**](VeeStatusCodeDTO.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [OAuth2Auth](../README.md#OAuth2Auth), [OAuth2Auth](../README.md#OAuth2Auth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vee_question_request**
> VeeResponseDTO vee_question_request(vee_question_dto)

Ask Vee a question

Use plain language to ask Vee a people question. Use body parameters to specify how Vee should respond, such as returning a visualization, data, or rewording the question.    The response always returns a `conversationState` object containing a unique ID for the conversation. To ask a follow-up question or continue the conversation with Vee, include the `conversationState` from the response in your next `/question` call. To submit feedback about Vee's answer, copy the entire response into your `/feedback` call.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.sdk.api.data_out
from visier.sdk.api.data_out.models.vee_question_dto import VeeQuestionDTO
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
    api_instance = visier.sdk.api.data_out.VeeApi(api_client)
    vee_question_dto = visier.sdk.api.data_out.VeeQuestionDTO() # VeeQuestionDTO | 

    try:
        # Ask Vee a question
        api_response = api_instance.vee_question_request(vee_question_dto)
        print("The response of VeeApi->vee_question_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VeeApi->vee_question_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vee_question_dto** | [**VeeQuestionDTO**](VeeQuestionDTO.md)|  | 

### Return type

[**VeeResponseDTO**](VeeResponseDTO.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [OAuth2Auth](../README.md#OAuth2Auth), [OAuth2Auth](../README.md#OAuth2Auth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vee_sample_questions**
> VeeSampleQuestionLibraryDTO vee_sample_questions()

Retrieve a list of sample questions to ask Vee

Get a list of sample questions to help your users start using Vee. The response returns a list of questions, such as \"What is the turnover rate?\".    <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

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
    api_instance = visier.sdk.api.data_out.VeeApi(api_client)

    try:
        # Retrieve a list of sample questions to ask Vee
        api_response = api_instance.vee_sample_questions()
        print("The response of VeeApi->vee_sample_questions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VeeApi->vee_sample_questions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

