import os.path
import sqlite3
from typing import Optional

from src.db_controllers.sql_controller import SQLController


class SQLiteController(SQLController):
    def __init__(self, db_name: str, *args, **kwargs):
        self._file_name = f"sqlite_{db_name}.db"
        self.db_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), self._file_name)
        super().__init__(db_name, *args, **kwargs)

    def _create_db(self) -> Optional[str]:
        if any((file.startswith("sqlite_") and file.endswith(".db") for file in os.listdir(os.path.abspath(os.path.dirname(__file__))))):
            print(f"Warning! There is at least one existing SQLite database.")
        if os.path.isfile(self.db_path):
            print(f"File {self._file_name} already exists.")
            return None
        con = sqlite3.connect(self.db_path)
        con.close()
        return None

    @property
    def connection_url(self):
        return f"sqlite:///{self.db_path}"
