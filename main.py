import argparse
from enum import Enum, auto


class ActionTypes(Enum):
    INIT = auto()
    DAILY_TASK = auto()
    UI = auto()
    UNINSTALL = auto()


def get_action() -> ActionTypes:
    """
    Parse cli arguments and return a chosen action. User must specify the action.
    :return: one of ActionTypes values
    """
    parser = argparse.ArgumentParser(description="Entry point of the BirthdayReminder application.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--init", action="store_const", const=ActionTypes.INIT,
                       help="The first project start")
    group.add_argument("--daily-task", action="store_const", const=ActionTypes.DAILY_TASK,
                       help="Run scanning database to find birthdays")
    group.add_argument("--ui", action="store_const", const=ActionTypes.UI,
                       help="Open UI for configuring the application (add birthday, remove, edit configs, etc.)")
    # TODO Carefully think over confirmation for uninstall operation
    group.add_argument('--uninstall', action="store_const", const=ActionTypes.UNINSTALL,
                       help="Remove tasks from the scheduler/cron and delete database")

    args = parser.parse_args()

    selected_action = next(value for option, value in vars(args).items() if value is not None)
    return selected_action


def main() -> None:
    """
    Entry point of the application, which runs the chosen action.
    :return: None
    """
    action = get_action()
    # TODO implement proper logging
    print(f"Selected action {action}")


if __name__ == "__main__":
    main()
