import os
from datetime import datetime

from config import Config
from src.db_controllers import get_db_controller


class Service:
    def __init__(self, config: Config):
        self.config = config

    def initialize_database(self):
        if self.config.DB_NAME is None:
            db_name = f"birthday_{datetime.now().date().isoformat()}"
        else:
            db_name = self.config.DB_NAME
        db_controller = get_db_controller(self.config.CONTROLLER_NAME, db_name=db_name)
        db_controller.create_db()

