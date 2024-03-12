from datetime import datetime
from typing import List, Type, Optional, Union, Any

from common import NotificationType
from config import Config, update_configs_on_disk
from src.db_controllers import get_db_controller
import src.db_controllers.sql_base_controller.models as models
from src.db_controllers.sql_base_controller.models import Birthday, Notification
from src.notifiers import get_notifier


class Service:
    def __init__(self, config: Config):
        self.config = config
        self.db_controller = get_db_controller(
            self.config.CONTROLLER_NAME, config=self.config, db_name=self.config.DB_NAME, init_db=False
        )
        self.notifier = get_notifier()

    @staticmethod
    def initialize_database(config):
        """
        Create a database, if it does not exist. Prepare database for usage (create tables, add schemas, etc.)
        :return: None
        """
        if config.DB_NAME is None:
            config.DB_NAME = f"birthday_{datetime.now().date().isoformat()}"

        db_controller = get_db_controller(
            config.CONTROLLER_NAME, config=config, db_name=config.DB_NAME, init_db=True
        )
        update_configs_on_disk(config)

    def run_daily_task(self):
        """
        1. Collect "today" birthdays because they are first priority
        2. Check pre-reminder rules
        3. Produce notification according the
        :return:
        """
        notifications = []

        birthdays = self.db_controller.get_birthdays()
        notifications.extend(
            self._check_birthdays(birthdays)
        )
        # TODO implement pre-reminders

        for item in notifications:
            self.notifier.display_notification(item)

        return None

    def _check_birthdays(self, birthdays: List[Type[models.Birthday]]) -> Union[list[Any], list[Notification]]:
        """
        Check birthdays and generate notifications.

        If it finds birthdays to remind - returns a list with one notification. Otherwise, returns am empty list.

        :param birthdays: list of birthdays from db
        :return: list with a notification
        """

        today = datetime.today().date()
        people_to_congratulate = [birthday for birthday in birthdays if birthday.date == today]
        if not people_to_congratulate:
            return []

        title = f"🎉 Birthday Reminder! 🎈"
        text = [
            "Hello there!",
            f"Just a friendly reminder that today, {today}, is a special day for some of your dear connections! 🎂",
            "Let's take a moment to celebrate and send warm wishes to:"
        ]
        text.extend(
            [f"\t{birthday.name} {birthday.surname}" for birthday in people_to_congratulate]
        )
        text.extend([
            "Now's the perfect time to make their days even brighter with your heartfelt congratulations! 🌟✉️",
            "Warm regards,",
            "© 2024 BirthdayReminder, Inc."
        ])
        # Compile text together
        text = "\n".join(text)

        notification = self.db_controller.create_notification(
            birthdays=people_to_congratulate,
            notif_type=NotificationType.BIRTHDAY.value,
            title=title,
            text=text,
        )
        print(f"Notification was created {notification}")
        return [notification]

    def _check_pre_reminders(self, pre_reminders: list) -> List[Type[models.Notification]]:
        # TODO implement pre-reminders
        pass
