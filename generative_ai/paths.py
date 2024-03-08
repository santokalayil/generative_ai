from pathlib import Path
from .exceptions import EnvFileNotFound

PACKAGE_DIR = Path(__file__).parent
MAIN_DIR = PACKAGE_DIR.parent


ENV_FILEPATH = MAIN_DIR / ".env"


def check_for_env_file():
    if not ENV_FILEPATH.is_file():
        raise EnvFileNotFound(
            ".env file not found main project dir. \
            Make sure you have keys set with proper key name"
        )
