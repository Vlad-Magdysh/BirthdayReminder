from abc import ABC, abstractmethod
from typing import Optional


class BaseController(ABC):
    def __init__(self, db_name, config=None):
        self.db_name = db_name
        self.config = config

    @abstractmethod
    def _create_db(self) -> Optional[str]:
        """
        Creates a new database. May produce an exception.
        :return: str or None
        """
        pass
