import datetime
from abc import abstractmethod, ABC
from typing import List, Optional, Type

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from common import NotificationStatus
from config import Config
from .models import Birthday, Notification, PreReminder


class SQLBaseController(ABC):
    def __init__(self, db_name: str, config: Config, *args, init_db=False, **kwargs):
        self.db_name = db_name
        self.config = config
        if init_db:
            self._create_db()

        self.engine = create_engine(self.connection_url)
        # session_maker is a session factory
        self.session: Session = sessionmaker(bind=self.engine)()
        # Update SQLALCHEMY_DATABASE_URI variable for alembic migrations
        self.config.SQLALCHEMY_DATABASE_URI = self.connection_url

    @abstractmethod
    def _create_db(self) -> Optional[str]:
        """
        Creates a new database. May produce an exception.
        :return: str or None
        """
        pass

    @property
    @abstractmethod
    def connection_url(self):
        pass

    def get_birthdays(self) -> List[Type[Birthday]]:
        birthdays = self.session.query(Birthday).all()
        return birthdays

    def get_individual_birthday(self, record_id=None, name=None, surname=None) -> Birthday:
        pass

    def create_birthday(self, date: datetime.date, name: str, surname: str) -> Birthday:
        birthday = Birthday(date=date, name=name, surname=surname)
        self.session.add(birthday)
        self.session.commit()
        return birthday

    def create_notification(self, birthdays: List[Type[Birthday]], notif_type: str, title: str, text: str) -> Notification:
        notification = Notification(
            title=title,
            text=text,
            notification_type=notif_type,
            status=NotificationStatus.CREATED.value,
            created_on=datetime.datetime.today(),
        )
        notification.birthdays.extend(birthdays)
        self.session.add(notification)
        self.session.commit()
        return notification

    def get_pre_reminders(self) -> List[PreReminder]:
        pass
