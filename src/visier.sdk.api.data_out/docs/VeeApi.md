# visier.sdk.api.data_out.VeeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vee_feedback**](VeeApi.md#vee_feedback) | **POST** /v1alpha/rest/vee/feedback | Submit Vee feedback
[**vee_question_request**](VeeApi.md#vee_question_request) | **POST** /v1alpha/rest/vee/question | Ask Vee a question
[**vee_sample_questions**](VeeApi.md#vee_sample_questions) | **GET** /v1alpha/rest/vee/sample-questions | Retrieve a list of sample questions to ask Vee


# **vee_feedback**
> VeeStatusCodeDTO vee_feedback(response_conversation_state_question_state=response_conversation_state_question_state, response_status_code_status_code=response_status_code_status_code, response_status_code_status_msg=response_status_code_status_msg, response_narrative=response_narrative, response_chart_url=response_chart_url, response_schema_metrics=response_schema_metrics, response_data_data_json=response_data_data_json, response_data_context=response_data_context, response_visual_image=response_visual_image, response_visual_title=response_visual_title, response_visual_context=response_visual_context, response_reworded_question=response_reworded_question, is_approved=is_approved, description=description)

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
    response_conversation_state_question_state = ['response_conversation_state_question_state_example'] # List[str] | The unique identifier of the conversation with Vee. (optional)
    response_status_code_status_code = 'response_status_code_status_code_example' # str | A status code indicating whether or not Vee successfully answered the question. (optional)
    response_status_code_status_msg = 'response_status_code_status_msg_example' # str | Additional information about whether or not Vee successfully answered the question. (optional)
    response_narrative = 'response_narrative_example' # str | Vee's answer to the question. (optional)
    response_chart_url = 'response_chart_url_example' # str | A URL to view the visualization in Visier. (optional)
    response_schema_metrics = ['response_schema_metrics_example'] # List[str] | A list of the metrics that contribute to Vee's answer. (optional)
    response_data_data_json = 'response_data_data_json_example' # str | A JSON string of fields and numerical values representing the data contributing to Vee's answer. For example, the number of employees per gender in Vee's answer. (optional)
    response_data_context = 'response_data_context_example' # str | The filter applied to the visualization generated by Vee. For example, a time filter of April 2024. (optional)
    response_visual_image = 'response_visual_image_example' # str | A PNG visualization encoded in a base64 string. (optional)
    response_visual_title = 'response_visual_title_example' # str | The visualization title. (optional)
    response_visual_context = 'response_visual_context_example' # str | Any filters applied to the visualization. For example, a time filter of April 2024. (optional)
    response_reworded_question = 'response_reworded_question_example' # str | Vee's plain language interpretation of the original question. For example, if you asked \"what is the headcount by gender in each org?\", Vee might reword the question as \"What is the gender breakdown of our workforce by organization this month?\". (optional)
    is_approved = True # bool | If `true`, Vee answered the question correctly. If `false`, Vee's answer was incorrect or lacked details. (optional)
    description = 'description_example' # str | A description of how Vee should have answered the question or how Vee can improve the answer; for example, \"Expected Headcount metric, but Vee returned Average Headcount\". (optional)

    try:
        # Submit Vee feedback
        api_response = api_instance.vee_feedback(response_conversation_state_question_state=response_conversation_state_question_state, response_status_code_status_code=response_status_code_status_code, response_status_code_status_msg=response_status_code_status_msg, response_narrative=response_narrative, response_chart_url=response_chart_url, response_schema_metrics=response_schema_metrics, response_data_data_json=response_data_data_json, response_data_context=response_data_context, response_visual_image=response_visual_image, response_visual_title=response_visual_title, response_visual_context=response_visual_context, response_reworded_question=response_reworded_question, is_approved=is_approved, description=description)
        print("The response of VeeApi->vee_feedback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VeeApi->vee_feedback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **response_conversation_state_question_state** | [**List[str]**](str.md)| The unique identifier of the conversation with Vee. | [optional] 
 **response_status_code_status_code** | **str**| A status code indicating whether or not Vee successfully answered the question. | [optional] 
 **response_status_code_status_msg** | **str**| Additional information about whether or not Vee successfully answered the question. | [optional] 
 **response_narrative** | **str**| Vee&#39;s answer to the question. | [optional] 
 **response_chart_url** | **str**| A URL to view the visualization in Visier. | [optional] 
 **response_schema_metrics** | [**List[str]**](str.md)| A list of the metrics that contribute to Vee&#39;s answer. | [optional] 
 **response_data_data_json** | **str**| A JSON string of fields and numerical values representing the data contributing to Vee&#39;s answer. For example, the number of employees per gender in Vee&#39;s answer. | [optional] 
 **response_data_context** | **str**| The filter applied to the visualization generated by Vee. For example, a time filter of April 2024. | [optional] 
 **response_visual_image** | **str**| A PNG visualization encoded in a base64 string. | [optional] 
 **response_visual_title** | **str**| The visualization title. | [optional] 
 **response_visual_context** | **str**| Any filters applied to the visualization. For example, a time filter of April 2024. | [optional] 
 **response_reworded_question** | **str**| Vee&#39;s plain language interpretation of the original question. For example, if you asked \&quot;what is the headcount by gender in each org?\&quot;, Vee might reword the question as \&quot;What is the gender breakdown of our workforce by organization this month?\&quot;. | [optional] 
 **is_approved** | **bool**| If &#x60;true&#x60;, Vee answered the question correctly. If &#x60;false&#x60;, Vee&#39;s answer was incorrect or lacked details. | [optional] 
 **description** | **str**| A description of how Vee should have answered the question or how Vee can improve the answer; for example, \&quot;Expected Headcount metric, but Vee returned Average Headcount\&quot;. | [optional] 

### Return type

[**VeeStatusCodeDTO**](VeeStatusCodeDTO.md)

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

# **vee_question_request**
> VeeResponseDTO vee_question_request(question=question, conversation_state_question_state=conversation_state_question_state, options_include_visual=options_include_visual, options_visual_options_width=options_visual_options_width, options_visual_options_height=options_visual_options_height, options_include_data=options_include_data, options_data_format=options_data_format, options_include_reworded_question=options_include_reworded_question)

Ask Vee a question

Use plain language to ask Vee a people question. Use query parameters to specify how Vee should respond, such as returning a visualization, data, or rewording the question.    The response always returns a `conversationState` object containing a unique ID for the conversation. To ask a follow-up question or continue the conversation with Vee, include the `conversationState` from the response in your next `/question` call. To submit feedback about Vee's answer, copy the entire response into your `/feedback` call.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

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
    api_instance = visier.sdk.api.data_out.VeeApi(api_client)
    question = 'question_example' # str | The question to ask Vee. If asking a follow-up question or continuing a conversation with Vee, specify the `conversationState` object from the question's response. (optional)
    conversation_state_question_state = ['conversation_state_question_state_example'] # List[str] | The unique identifier of the conversation with Vee. (optional)
    options_include_visual = True # bool | If `true`, returns a base64 string-encoded PNG of a rendered visualization with Vee's answer. Default is `false`. (optional)
    options_visual_options_width = 56 # int | The pixel width of the rendered visualization. Default is 600. Valid values are between 160 and 1600. (optional)
    options_visual_options_height = 56 # int | The pixel height of the rendered visualization. Default is 338. Valid values are between 90 and 900. (optional)
    options_include_data = True # bool | If `true`, returns additional data relevant to the question, including `dataJson` (visualization data) and `context` (filters applied to the visualization). Default is `false`. (optional)
    options_data_format = 'options_data_format_example' # str | The format to return visualization data in. Valid values: `json`. (optional)
    options_include_reworded_question = True # bool | If `true`, returns Vee's plain language interpretation of the original question. For example, if you asked \"what is the headcount by gender in each org?\", Vee might reword the question as \"What is the gender breakdown of our workforce by organization this month?\". Default is `false`. (optional)

    try:
        # Ask Vee a question
        api_response = api_instance.vee_question_request(question=question, conversation_state_question_state=conversation_state_question_state, options_include_visual=options_include_visual, options_visual_options_width=options_visual_options_width, options_visual_options_height=options_visual_options_height, options_include_data=options_include_data, options_data_format=options_data_format, options_include_reworded_question=options_include_reworded_question)
        print("The response of VeeApi->vee_question_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VeeApi->vee_question_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question** | **str**| The question to ask Vee. If asking a follow-up question or continuing a conversation with Vee, specify the &#x60;conversationState&#x60; object from the question&#39;s response. | [optional] 
 **conversation_state_question_state** | [**List[str]**](str.md)| The unique identifier of the conversation with Vee. | [optional] 
 **options_include_visual** | **bool**| If &#x60;true&#x60;, returns a base64 string-encoded PNG of a rendered visualization with Vee&#39;s answer. Default is &#x60;false&#x60;. | [optional] 
 **options_visual_options_width** | **int**| The pixel width of the rendered visualization. Default is 600. Valid values are between 160 and 1600. | [optional] 
 **options_visual_options_height** | **int**| The pixel height of the rendered visualization. Default is 338. Valid values are between 90 and 900. | [optional] 
 **options_include_data** | **bool**| If &#x60;true&#x60;, returns additional data relevant to the question, including &#x60;dataJson&#x60; (visualization data) and &#x60;context&#x60; (filters applied to the visualization). Default is &#x60;false&#x60;. | [optional] 
 **options_data_format** | **str**| The format to return visualization data in. Valid values: &#x60;json&#x60;. | [optional] 
 **options_include_reworded_question** | **bool**| If &#x60;true&#x60;, returns Vee&#39;s plain language interpretation of the original question. For example, if you asked \&quot;what is the headcount by gender in each org?\&quot;, Vee might reword the question as \&quot;What is the gender breakdown of our workforce by organization this month?\&quot;. Default is &#x60;false&#x60;. | [optional] 

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

