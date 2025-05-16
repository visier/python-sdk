import os

import dotenv
from dotenv import load_dotenv

from visier_platform_sdk import Configuration, ApiClient


def create_api(api_class, env_file_path=None):
    config = Configuration.from_dict(
        dotenv.dotenv_values(env_file_path)) if env_file_path else Configuration.get_default()

    api_client = ApiClient(config)
    return api_class(api_client)


load_dotenv(dotenv_path='../.env')
TENANT_CODE = os.getenv('VISIER_TENANT_CODE')
