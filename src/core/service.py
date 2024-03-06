import os
from datetime import datetime

from config import Config, update_configs_on_disk
from src.db_controllers import get_db_controller


class Service:
    def __init__(self, config: Config):
        self.config = config

    def initialize_database(self):
        """
        Create a database, if it does not exist. Prepare database for usage (create tables, add schemas, etc.)
        :return: None
        """
        if self.config.DB_NAME is None:
            self.config.DB_NAME = f"birthday_{datetime.now().date().isoformat()}"

        db_controller = get_db_controller(self.config.CONTROLLER_NAME, config=self.config, db_name=self.config.DB_NAME, init_db=True)
        update_configs_on_disk(self.config)
