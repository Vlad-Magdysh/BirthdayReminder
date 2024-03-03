import os
from dotenv import load_dotenv

ENV_FILE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "config.env"))
load_dotenv(dotenv_path=ENV_FILE_PATH)


class Config:
    """
    The main object, that stores configurations from the config.env file
    """
    DB_NAME = os.getenv("DB_NAME")
    CONTROLLER_NAME = os.getenv("DB_CONTROLLER", "")
