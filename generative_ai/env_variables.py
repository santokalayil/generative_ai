from .paths import ENV_FILEPATH, check_for_env_file
from dotenv import load_dotenv

check_for_env_file()
load_dotenv(str(ENV_FILEPATH))
