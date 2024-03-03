from abc import ABC, abstractmethod
from typing import Optional


class BaseController(ABC):
    def __init__(self, db_name):
        self.db_name = db_name

    @abstractmethod
    def create_db(self) -> Optional[str]:
        """
        Creates a new database. May produce an exception.
        :return: str or None
        """
        pass


class SQLController(BaseController):
    pass


class NoSQLController(BaseController):
    pass
