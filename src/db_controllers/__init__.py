from .base_controllers import BaseController
from .sqlite_controller import SQLiteController

DEFAULT_CONTROLLER_CLASS = SQLiteController

REGISTERED_CONTROLLERS = {
    SQLiteController.__name__: SQLiteController
}


def get_db_controller(controller_name: str, *args, **kwargs) -> BaseController:
    """
    Get an initialized controller for interacting with the database.
    :param controller_name: controller class name
    :param args: necessary parameters for the controller initialization
    :param kwargs: necessary parameters for the controller initialization
    :return: an instance of the db controller
    """
    cls = REGISTERED_CONTROLLERS.get(controller_name, DEFAULT_CONTROLLER_CLASS)
    return cls(*args, **kwargs)
