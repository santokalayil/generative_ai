import os
from .paths import ENV_FILEPATH, check_for_env_file
from .exceptions import EnvVariableNotFound
from dotenv import load_dotenv

check_for_env_file()
load_dotenv(str(ENV_FILEPATH))


def get_variable(key: str) -> bool:
    if key in os.environ.keys():
        return os.environ[key]
    raise EnvVariableNotFound(f"The environment variable '{key}' not found")
