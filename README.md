# Visier API Python SDK (Beta)
Welcome to the Visier API Python SDK! This SDK provides a convenient way to interact with the Visier API. 

**Note: This SDK is currently in beta.**

## Description
For detailed documentation of the Visier API, please visit the [Visier API Documentation](https://docs.visier.com/developer/apis/apis.htm).
The Visier API is divided into five main categories:

- [Authentication](https://docs.visier.com/developer/apis/authentication/swagger/current/index.html): Manage user
  authentication and tokens.
- [Administration](https://docs.visier.com/developer/apis/administration/swagger/current/index.html): Manage your tenant
  or tenants in Visier.
- [Analytic Model](https://docs.visier.com/developer/apis/analytic-model/swagger/current/index.html): Configure and
  manage the Analytic Model.
- [Data In](https://docs.visier.com/developer/apis/data-in/swagger/current/index.html): Upload data to the Visier
  Platform.
- [Data Out](https://docs.visier.com/developer/apis/data-out/swagger/current/index.html): Download data from the Visier
  Platform.

The Visier API Python SDK is organized into five main packages corresponding to the API categories:

- `visier-api-core` - It contains logic for authenticating, configuring, and contains classes to make requests. 
This package is required to be installed to use any other package of the SDK.
- `visier-api-administration` - for managing your tenant or tenants in Visier. 
- `visier-api-analytic-model` - to configure and manage the Analytic Model.
- `visier-api-data-in` - APIs to upload data to Visier Platform.
- `visier-api-data-out` - APIs to download data to Visier Platform.

Each package except `visier-api-core` contains API classes which are used to interact with different APIs in the Visier API.

## Installation

You can install the packages separately depending on the functionality you need.
The `visier-api-core` package will be installed automatically as it is a dependency for all other packages.

```bash
pip install visier-api-administration
pip install visier-api-analytic-model
pip install visier-api-data-in
pip install visier-api-data-out
```

## Usage
To use the API, you need to configure the `ApiClient` with a `Configuration` object. 
The configuration can be created in three ways:
- From environment variables.
- From dictionary which could be loaded from env file.
- Explicitly set the configuration parameters.

Configure the environment variables as described below, depending on the type of authentication you want to use:
```env
# Necessary for all types of auth
VISIER_HOST=https://customer-specific.api.visier.io
VISIER_APIKEY='visier-provided-api-key'
VISIER_VANITY='visier-tenant-vanity-name'

# For OAuth 2.0 authentication
VISIER_CLIENT_ID='client-id-from-registration'  # OAuth client ID (obtain from Visier app registration)
VISIER_CLIENT_SECRET='client-secret-from-registration'  # OAuth client secret (obtain from Visier app registration)

# For 3-legged OAuth 2.0, include the redirect URI along with VISIER_CLIENT_ID and VISIER_CLIENT_SECRET.
# The client will start a local server to handle the callback.
# Register this redirect URI on the Visier platform. The default is http://localhost:5000/oauth2/callback.
VISIER_REDIRECT_URI='http://localhost:5000/oauth2/callback'

# For Basic authentication, provide ONLY the following and leave VISIER_CLIENT_ID and VISIER_CLIENT_SECRET blank:
# For 2-legged OAuth 2.0, provide the following IN ADDITION TO VISIER_CLIENT_ID and VISIER_CLIENT_SECRET
VISIER_USERNAME='visier-username'
VISIER_PASSWORD='visier-password'
```

After setting the environment variables, you can create a `Configuration` object using the `from_env` method:
```python
from visier_api_core import Configuration

config = Configuration.from_env()
```

Another way is to store environment variables in a .env file and load them using dotenv library.
```python
from dotenv import dotenv_values
from visier_api_core import Configuration

config_dict = dotenv_values(".env")
config = Configuration.from_dict(config_dict)
```

Also, you can explicitly set the configuration parameters. E.g. for 2-legged OAuth 2.0 authentication:

```python
from visier_api_core import Configuration

config = Configuration(
    host="https://api.visier.com",
    api_key="api_key",
    username="your_username",
    password="your_password",
    client_id="your_client_id",
    client_secret="your_client_secret",
    vanity="your_vanity",
    access_token="your_access_token",
    refresh_token="your_refresh_token"
)
```

After you have the configuration object you can create the API client and start using the API.

```python
from visier_api_core import ApiClient, Configuration
from visier_api_data_out import DataQueryApi

config = Configuration.from_env()
client = ApiClient(config)
data_query_api = DataQueryApi(client)
```

You can create the API client using default configuration object.
```python
from visier_api_data_out import DataQueryApi
data_query_api = DataQueryApi()
```
Under the hood, it will create the configuration object using the environment variables.
You can change the default configuration object using `Configuration.set_default` method.
By default, this default configuration object is used to create default ApiClient object.
`ApiClient` object also has a method `ApiClient.set_default`.

```python
from dotenv import dotenv_values
from visier_api_core import Configuration, ApiClient
from visier_api_data_in import DataUploadApi, DataIntakeApi

config_dict = dotenv_values(".env")
config = Configuration.from_dict(config_dict)
Configuration.set_default(config)

# ApiClient will be created using default configuration object
api_client = ApiClient()
data_upload_api = DataUploadApi(api_client)

# ApiClient also has a method to set default ApiClient
ApiClient.set_default(ApiClient(config))

# You can create APIs objects implicitly using default ApiClient object
data_intake_api = DataIntakeApi()
```

Every API method has 3 different ways to be called:

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
# If you're having some problems with DTO format you can use this method to get raw response
rest_response = data_model_api.properties_without_preload_content(analytic_object_id)
if rest_response.status == 200:
    properties = PropertiesDTO.from_json(rest_response.data.decode())    
```

All API DTOs are described in documentation for each API, e.g. [Data Out API DTOs](https://docs.visier.com/developer/apis/data-in/swagger/current/index.html#:~:text=files/%7Bfilename%7D-,Schemas,-Data%20types%20and).
Each DTOs has a method `from_json` to create DTO object from json string.
In some cases you need to switch from DTO format to csv format.
You can do this by setting the `Accept` header to `text/csv` when creating the ApiClient or when making a request.

```python
from visier_api_core import ApiClient
from visier_api_data_out import DataQueryApi, AggregationQueryExecutionDTO

with open('query_examples/aggregate/applicants-source.json') as f:
    headcount_json = f.read()
aggr_query_dto = AggregationQueryExecutionDTO.from_json(headcount_json)

# Passing 'Accept' header to ApiClient
api_client = ApiClient(header_name='Accept', header_value='text/csv')
query_api = DataQueryApi(api_client)
response = query_api.aggregate_without_preload_content(aggr_query_dto)

# Passing 'Accept' header to request
query_api = DataQueryApi()
response = query_api.aggregate_without_preload_content(aggr_query_dto, _headers={'Accept': 'text/csv'})

with open('data.csv', mode='w') as f:
    f.write(response.data.decode())
```

## Error Handling

This Python SDK handles exceptions using custom exception classes derived from `OpenApiException`. Below are the main exception classes and their usage:

- `OpenApiException`: The base exception class for all API exceptions.
- `ApiTypeError`: Raised for type errors.
- `ApiValueError`: Raised for value errors.
- `ApiAttributeError`: Raised for attribute errors.
- `ApiKeyError`: Raised for key errors.
- `ApiException`: Raised for general Http API exceptions. This class subclassed into:
  - `BadRequestException`: Raised for HTTP 400 errors.
  - `UnauthorizedException`: Raised for HTTP 401 errors.
  - `ForbiddenException`: Raised for HTTP 403 errors.
  - `NotFoundException`: Raised for HTTP 404 errors.
  - `ServiceException`: Raised for HTTP 500-599 errors.

### Fields in `ApiException`

- `status`: The HTTP status code of the response.
- `reason`: The reason phrase returned by the server.
- `body`: The body of the HTTP response.
- `data`: The data parsed from the HTTP response.
- `headers`: The headers of the HTTP response.

Below is an example of how to handle these exceptions:

```python
from visier_api_core.exceptions import ApiException, BadRequestException, UnauthorizedException
from visier_api_analytic_model import DataModelApi

analytic_object_id = 'Employee'
data_model_api = DataModelApi()

try:
    # Requesting properties of an analytic object
    properties = data_model_api.properties(analytic_object_id)
except BadRequestException as e:
    print(f"Bad request: {e}")
except UnauthorizedException as e:
    print(f"Unauthorized: {e}")
except ApiException as e:
    print(f"An error occurred: {e}")
```

