# Visier API Python SDK (Beta)
Welcome to the Visier API Python SDK! This SDK provides a convenient way to interact with Visier's public APIs.

**Note:** 
- This SDK is currently in beta. You may encounter issues while using it.
- This SDK supports Python 3.8 and above.

## Overview
For detailed information about Visier APIs, see [Visier APIs](https://docs.visier.com/developer/Default.htm#cshid=1007).

Visier APIs are divided into collections.
- [Authentication](https://docs.visier.com/developer/Default.htm#cshid=1039): Authenticate yourself as a Visier user who is allowed to use Visier APIs.
- [Administration](https://docs.visier.com/developer/Default.htm#cshid=1040): Manage your tenant or tenants in Visier.
- [Analytic Model](https://docs.visier.com/developer/Default.htm#cshid=1041): Retrieve and configure your analytic model in Visier.
- [Data In](https://docs.visier.com/developer/Default.htm#cshid=1042): Send data to Visier.
- [Data Out](https://docs.visier.com/developer/Default.htm#cshid=1043): Get data out of Visier.

The Visier API Python SDK contains five packages that correspond to the Visier API collections.

- `visier-api-core`: Contains logic for authenticating and configuring, and contains classes to make requests. Required to use the other packages.
- `visier-api-administration`: APIs to manage your tenant or tenants in Visier.
- `visier-api-analytic-model`: APIs to retrieve and configure the analytic model in Visier.
- `visier-api-data-in`: APIs to send data to Visier.
- `visier-api-data-out`: APIs get data out of Visier.

The packages, excluding `visier-api-core`, contain API classes to interact with different Visier APIs.

## Installation

Install the packages according to their required functionality. `visier-api-core` is installed automatically because it's a dependency for the other packages.

```bash
pip install visier-api-administration
pip install visier-api-analytic-model
pip install visier-api-data-in
pip install visier-api-data-out
```

## Usage
To use the API, provide the `ApiClient` with a `Configuration` object. You can create the configuration:
- From environment variables.
- From a dictionary loaded from the `.env` file.
- By explicitly setting the configuration parameters.

Configure the environment variables according to your authentication method:
```env
# Required for all authentication methods.
VISIER_HOST=https://customer-specific.api.visier.io
VISIER_APIKEY='visier-provided-api-key'
VISIER_VANITY='visier-tenant-vanity-name'

# Required for OAuth 2.0 authentication.
VISIER_CLIENT_ID='client-id-from-registration'  # Retrieve the client ID from your client registration in Visier.
VISIER_CLIENT_SECRET='client-secret-from-registration'  # Retrieve the client secret from your client registration in Visier.

# For 3-legged OAuth 2.0 authentication, provide a redirect URI in addition to the VISIER_CLIENT_ID and VISIER_CLIENT_SECRET. The redirect URI must be registered in Visier. The client starts a local server to handle the callback. The default is http://localhost:5000/oauth2/callback.
VISIER_REDIRECT_URI='http://localhost:5000/oauth2/callback'

# For basic authentication, provide only the VISIER_USERNAME and VISIER_PASSWORD. Leave VISIER_CLIENT_ID and VISIER_CLIENT_SECERT blank.
# For 2-legged OAuth 2.0 authentication, provide the VISIER_USERNAME, VISIER_PASSWORD, VISIER_CLIENT_ID, and VISIER_CLIENT_SECRET.
VISIER_USERNAME='visier-username'
VISIER_PASSWORD='visier-password'
```

For more information about registering a client ID, client secret, and redirect URIs in Visier, see [Register a Client Application](https://docs.visier.com/developer/Default.htm#cshid=1044).

After setting the environment variables, you can create a `Configuration` object using the `from_env` method:
```python
from visier_api_core import Configuration

config = Configuration.from_env()
```

Alternatively, store the environment variables in a `.env` file and load them using dotenv library.
```python
from dotenv import dotenv_values
from visier_api_core import Configuration

config_dict = dotenv_values(".env")
config = Configuration.from_dict(config_dict)
```

Or, explicitly set the configuration parameters. The following example shows explicitly setting the configuration parameters for 3-legged OAuth 2.0 authentication.

```python
from visier_api_core import Configuration

def get_secret(secret_name):
    """Your secret retrieval logic"""
    pass

config = Configuration(
    host="https://api.visier.com",
    api_key=get_secret("api_key"),
    client_id=get_secret("client_id"),
    client_secret=get_secret("client_id"),
    vanity="your_vanity"
)
```
> **Warning:** Don't store sensitive information in code or in a repository. 
> Use environment variables or a secure storage solution.

After you have the `Configuration` object, create the API client and start using the API.

```python
from visier_api_core import ApiClient, Configuration
from visier_api_data_out import DataQueryApi

config = Configuration.from_env()
client = ApiClient(config)
data_query_api = DataQueryApi(client)
```

You can create the API client using the default `Configuration` object.
```python
from visier_api_data_out import DataQueryApi
data_query_api = DataQueryApi()
```
The `Configuration` object is created using the environment variable values. You can change the default configuration object using the `Configuration.set_default` method.

The `ApiClient` object is created using the default configuration object. The default `ApiClient` object is used to create API objects implicitly. You can change the default `ApiClient` object using the `ApiClient.set_default` method.

```python
from dotenv import dotenv_values
from visier_api_core import Configuration, ApiClient
from visier_api_data_in import DataUploadApi, DataIntakeApi

config_dict = dotenv_values(".env")
config = Configuration.from_dict(config_dict)
Configuration.set_default(config)

# The `ApiClient` object is created using the default `Configuration` object.
api_client = ApiClient()
data_upload_api = DataUploadApi(api_client)

# You can set the default `ApiClient` using the `ApiClient.set_default` method.
ApiClient.set_default(ApiClient(config))

# The default `ApiClient` object is used to create API objects implicitly.
data_intake_api = DataIntakeApi()
```

The API response is returned in DTO format, ApiResponse, or RESTResponseType respectively.

```python
from visier_api_analytic_model import DataModelApi, PropertiesDTO

analytic_object_id = 'Employee'
data_model_api = DataModelApi()

# DTO format
properties = data_model_api.properties(analytic_object_id)

# ApiResponse 
api_response = data_model_api.properties_with_http_info(analytic_object_id)
if api_response.status_code == 200:
    properties = api_response.data

# RESTResponseType
# Use this method to work with raw data.
rest_response = data_model_api.properties_without_preload_content(analytic_object_id)
if rest_response.status == 200:
    properties = PropertiesDTO.from_json(rest_response.data.decode())    
```

For full API DTO documentation, see the API references. For example, [Visier Data In APIs](https://docs.visier.com/developer/Default.htm#cshid=1042).
All DTOs have a `from_json` method to create a DTO object from a JSON string. In some cases, you may need to switch from DTO format to CSV format. To switch, set the `Accept` header to `text/csv` when creating the `ApiClient` or making a request.

```python
from visier_api_core import ApiClient
from visier_api_data_out import DataQueryApi, AggregationQueryExecutionDTO

with open('query_examples/aggregate/applicants-source.json') as f:
    headcount_json = f.read()
aggr_query_dto = AggregationQueryExecutionDTO.from_json(headcount_json)

# Set the `Accept` header to `text/csv` in the constructor ApiClient(header_name='Accept', header_value='text/csv') or by using the `set_default_header` method.
# The `set_default_header` method allows you to add additional headers as needed.
api_client = ApiClient()
api_client.set_default_header('Accept', 'text/csv')

query_api = DataQueryApi(api_client)
response = query_api.aggregate_without_preload_content(aggr_query_dto)

# Passing `Accept` header to request.
query_api = DataQueryApi()
response = query_api.aggregate_without_preload_content(aggr_query_dto, _headers={'Accept': 'text/csv'})

with open('data.csv', mode='w') as f:
    f.write(response.data.decode())
```
For more query body examples, see the [query_examples](query_examples) directory.

## Error Handling

This SDK handles exceptions using custom exception classes derived from `OpenApiException`. The following list describes the main exception classes and their usages.

- `OpenApiException`: The base exception class for all API exceptions.
- `ApiValueError`: Raised when a function receives an argument with an inappropriate value, such as when an authentication token is not set, or when both `body` and `post_params` are provided.
- `ApiException`: Raised for general HTTP API exceptions. This class is subclassed into:
  - `BadRequestException`: Raised for HTTP 400 errors.
  - `UnauthorizedException`: Raised for HTTP 401 errors.
  - `ForbiddenException`: Raised for HTTP 403 errors.
  - `NotFoundException`: Raised for HTTP 404 errors.
  - `ServiceException`: Raised for HTTP 500-599 errors.

### Fields in ApiException

- `status`: The HTTP status code of the response.
- `reason`: The reason phrase returned by the server.
- `body`: The body of the HTTP response.
- `data`: The data parsed from the HTTP response.
- `headers`: The headers of the HTTP response.

The following example shows how to handle exceptions.

```python
from visier_api_core.exceptions import ApiException, BadRequestException, UnauthorizedException
from visier_api_analytic_model import DataModelApi

analytic_object_id = 'Employee'
data_model_api = DataModelApi()

try:
    # Requesting properties of an analytic object.
    properties = data_model_api.properties(analytic_object_id)
except BadRequestException as e:
    print(f"Bad request: {e}")
except UnauthorizedException as e:
    print(f"Unauthorized: {e}")
except ApiException as e:
    print(f"An error occurred: {e}")
```

### More Examples
For more examples, see [github.com/visier/api-samples](https://github.com/visier/api-samples).
