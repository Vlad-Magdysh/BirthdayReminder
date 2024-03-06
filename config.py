import os
from dotenv import load_dotenv, dotenv_values, set_key

ENV_FILE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "config.env"))
load_dotenv(dotenv_path=ENV_FILE_PATH)


class Config:
    """
    The main object, that stores configurations from the config.env file
    """
    DB_NAME = os.getenv("DB_NAME")
    CONTROLLER_NAME = os.getenv("DB_CONTROLLER", "")


def update_configs_on_disk(config: Config):
    """
    Saves current configurations into the file ENV_FILE_PATH (config.env)
    :return: None
    """
    for name, value in vars(config).items():
        if not name.startswith('__') and not callable(value):
            set_key(dotenv_path=ENV_FILE_PATH, key_to_set=name, value_to_set=value)
