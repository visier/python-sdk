import os

from dotenv import load_dotenv

from visier_api_core import Configuration, ApiClient

TENANT = 'd3m'
TENANT_CODE = 'WFF_d3m'


def create_api(api_class, env_file_path='.env'):
    if not os.path.isfile(env_file_path):
        raise FileNotFoundError(f"Environment file not found: {env_file_path}")

    load_dotenv(env_file_path)
    config = Configuration(
        host=os.getenv('VISIER_HOST'),
        api_key=os.getenv('VISIER_APIKEY'),
        username=os.getenv('VISIER_USERNAME'),
        password=os.getenv('VISIER_PASSWORD'),
        client_id=os.getenv('VISIER_CLIENT_ID'),
        client_secret=os.getenv('VISIER_CLIENT_SECRET'),
        redirect_uri=os.getenv('VISIER_REDIRECT_URI'),
        vanity=os.getenv('VISIER_VANITY')
    )
    api_client = ApiClient(config)
    return api_class(api_client)


def get_query_content(file_name):
    file_path = os.path.join('visier_api_data_out/queries', file_name)
    with open(file_path, 'r') as file:
        return file.read()
