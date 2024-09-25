import os

import dotenv
from dotenv import load_dotenv

from visier_api_core import Configuration, ApiClient


def create_api(api_class, env_file_path=None):
    config = Configuration.from_dict(
        dotenv.dotenv_values(env_file_path)) if env_file_path else Configuration.get_default()

    api_client = ApiClient(config)
    return api_class(api_client)


def get_query_content(file_name):
    file_path = os.path.join('visier_api_data_out/queries', file_name)
    with open(file_path, 'r') as file:
        return file.read()


load_dotenv(dotenv_path='.env')
TENANT_CODE = f"WFF_{os.getenv('VISIER_VANITY')}"
