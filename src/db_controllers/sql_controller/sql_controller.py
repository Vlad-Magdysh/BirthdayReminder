from abc import abstractmethod
from functools import wraps

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ..base_controllers import BaseController


class SQLController(BaseController):
    def __init__(self, *args, init_db=False, **kwargs):
        super().__init__(*args, **kwargs)
        if init_db:
            self._create_db()

        self.engine = create_engine(self.connection_url)
        # session_maker is a session factory
        self.session_maker = sessionmaker(bind=self.engine)
        # Update SQLALCHEMY_DATABASE_URI variable for alembic migrations
        self.config.SQLALCHEMY_DATABASE_URI = self.connection_url

    @property
    @abstractmethod
    def connection_url(self):
        pass

    # Decorator
    def use_database(self, func):
        """
        Wrap the given function, establish a connection with the database and manage session object.
        Pass "session" parameter into the wrapped function.
        :param func:
        :return:
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            session_obj = self.session_maker()
            with session_obj.begin() as session:
                results = func(*args, session=session, **kwargs)
            return results
        return wrapper



