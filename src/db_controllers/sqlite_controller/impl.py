import os.path
import sqlite3
from typing import Optional

from src.db_controllers.base_controllers import SQLController


class SQLiteController(SQLController):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._file_name = f"sqlite_{self.db_name}.db"
        self.db_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), self._file_name)

    def create_db(self) -> Optional[str]:
        if any((file.startswith("sqlite_") and file.endswith(".db") for file in os.listdir(os.path.abspath(os.path.dirname(__file__))))):
            print(f"Warning! There is at least one existing SQLite database.")
        if os.path.isfile(self.db_path):
            raise FileExistsError(f"File {self._file_name} already exists.")
        con = sqlite3.connect(self.db_path)
        con.close()
        return None
