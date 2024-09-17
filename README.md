# Visier API Python SDK (Beta)
This Python SDK provides a convenient way to interact with the Visier API. 
The SDK is in beta for now.

## Description:
Visier API is split in 5 main categories:
- Authentication: Manage user authentication and tokens.
- Administration: Manage your tenant or tenants in Visier.
- Analytic Model: Configure and manage the Analytic Model.
- Data In: Upload data to the Visier Platform.
- Data Out: Download data from the Visier Platform.

The Visier API Python SDK according to the above categories is split in 5 main packages:

- `visier-api-core` - It contains logic for authenticating, configuring, and contains classes to make requests. 
This package is required to be installed to use the SDK.
- `visier-api-administration` - for managing your tenant or tenants in Visier. 
- `visier-api-analytic-model` - to configure and manage the Analytic Model.
- `visier-api-data-in` - APIs to upload data to Visier Platform.
- `visier-api-data-out` - APIs to download data to Visier Platform.

Each package except `visier-api-core` contains API classes which are used to interact with different APIs in the Visier API.

## Installation:

To use the SDK you need to install the packages using pip. 
You can install the packages separately depending on the functionality you need.
The `visier-api-core` package will be installed automatically as it is a dependency for all other packages.

```bash
pip install visier-api-administration
pip install visier-api-analytic-model
pip install visier-api-data-in
pip install visier-api-data-out
```

## Usage:
To use the API you need configure ApiClient with Configuration object.
Configuration could be created in 3 ways:
- From environment variables.
- From dictionary which could be loaded from env file.
- Explicitly set the configuration parameters.

You can configure environment variables like described below depending on the type of authentication you want to use.
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

After you set this environment variables you can create Configuration object using from_env method:
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

# You can create APIs objects implicitly using default ApiClient object
data_intake_api = DataIntakeApi()
```

