from src import logger
from datetime import datetime

from src.Common.utils import VALID_PRIORITIES, VALID_PROGRESS_STATUSES


# -----------------------------------------------------------------------------
# Task
# -----------------------------------------------------------------------------
class Task:
    """
    Initialize a Task object of the TaskMe application

    Attributes
    ----------
    __assignee : str
        The task assignee.
    __name : str
        The task name.
    __due_date : str
        A string indicating when the task is due, format is dd/mm/yyyy.
    __priority : str
        Priority of the task, available values are LOW, MEDIUM or HIGH.
    __description : str
        A brief description of the task.
    __progress_status : str
        The task progress, available values are PENDING, IN_PROGRESS, COMPLETED.


    Note
    ----
    When setting values for the 'priority' and 'progress_status' properties,
    they must be one of the predefined valid options in 'VALID_PRIORITIES' and 'VALID_PROGRESS_STATUSES', respectively.

    """
    def __init__(self,
                 assignee: str,
                 name: str,
                 due_date: str,
                 priority: str,
                 description: str,
                 progress_status: str) -> None:

        # Sanity checks for priority attribute
        if priority not in VALID_PRIORITIES:
            logger.error(f"Invalid priority value. Expected one of the following: {VALID_PRIORITIES}"
                         f" and got {priority}")
            raise ValueError(f"Invalid priority value. Expected one of the following: {VALID_PRIORITIES}"
                             f" and got {priority}")

        # Sanity checks for progress_status attribute
        if progress_status not in VALID_PROGRESS_STATUSES:
            logger.error(f"Invalid progress_status value. Expected one of the following: {VALID_PROGRESS_STATUSES}"
                         f" and got {progress_status}")
            raise ValueError(f"Invalid progress_status value. Expected one of the following: {VALID_PROGRESS_STATUSES}"
                             f" and got {progress_status}")

        # Attributes Init
        self.__assignee = assignee
        self.__name = name
        self.__due_date = due_date
        self.__priority = priority
        self.__description = description
        self.__progress_status = progress_status

    # -----------------------------------------------------------------------------
    # assignee getter & setter
    # -----------------------------------------------------------------------------
    @property
    def assignee(self) -> str:
        return self.__assignee

    @assignee.setter
    def assignee(self, new_assignee: str) -> None:
        self.__assignee = new_assignee

    # -----------------------------------------------------------------------------
    # name getter & setter
    # -----------------------------------------------------------------------------
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name: str) -> None:
        self.__name = new_name

    # -----------------------------------------------------------------------------
    # due_date getter & setter
    # -----------------------------------------------------------------------------
    @property
    def due_date(self) -> str:
        return self.__due_date

    @due_date.setter
    def due_date(self, new_due_date: str) -> None:
        """ Sets the due date attribute

        Args:
            new_due_date (str): new due_date to set

        Raises:
            ValueError: if new_due_date is not in the following format: dd/mm/YYYY

        """
        try:
            datetime.strptime(new_due_date, "%d/%m/%Y")
        except ValueError:
            logger.error("Invalid due_date format. Expected format is 'dd/mm/yyyy'.")
            raise ValueError("Invalid due_date format. Expected format is 'dd/mm/yyyy'.")
        self.__due_date = new_due_date

    # -----------------------------------------------------------------------------
    # priority getter & setter
    # -----------------------------------------------------------------------------
    @property
    def priority(self) -> str:
        return self.__priority

    @priority.setter
    def priority(self, new_priority: str) -> None:
        """ Sets the priority attribute

        Args:
            new_priority (str): new priority to set

        Raises:
            ValueError: if new_priority is not in the VALID_PRIORITIES expected values: i.e 'LOW', 'MEDIUM' or 'HIGH'
        """
        if new_priority not in VALID_PRIORITIES:
            logger.error(f"Invalid priority value. Expected one of the following: {VALID_PRIORITIES}"
                         f" and got {new_priority}")
            raise ValueError(f"Invalid priority value. Expected one of the following: {VALID_PRIORITIES}"
                             f" and got {new_priority}")
        self.__priority = new_priority

    # -----------------------------------------------------------------------------
    # description getter & setter
    # -----------------------------------------------------------------------------
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, new_description: str):
        self.__description = new_description

    # -----------------------------------------------------------------------------
    # progress_status getter & setter
    # -----------------------------------------------------------------------------
    @property
    def progress_status(self) -> str:
        return self.__progress_status

    @progress_status.setter
    def progress_status(self, new_status: str) -> None:
        """ Sets the status attribute

        Args:
            new_status (str): new status to set

        Raises:
            ValueError: if new_status is not in the VALID_PROGRESS_STATUSES expected values: i.e 'PENDING', 'IN_PROGRESS' or 'COMPLETED'
        """
        if new_status not in VALID_PROGRESS_STATUSES:
            logger.error(f"Invalid priority value. Expected one of the following: {VALID_PROGRESS_STATUSES}"
                         f" and got {new_status}")
            raise ValueError(f"Invalid priority value. Expected one of the following: {VALID_PROGRESS_STATUSES}"
                             f" and got {new_status}")
        self.__progress_status = new_status

    # -----------------------------------------------------------------------------
    # to_dicts
    # -----------------------------------------------------------------------------
    def to_dict(self):
        """ Dict representation of a Task object

        Returns:
            Dictionary representation of Task object
        """
        return {
            "assignee": self.__assignee,
            "name": self.__name,
            "due_date": self.__due_date,
            "priority": self.__priority,
            "description": self.__description,
            "progress_status": self.__progress_status
        }

    # -----------------------------------------------------------------------------
    # from_dicts
    # -----------------------------------------------------------------------------
    @classmethod
    def from_dict(cls, data_dict):
        """ Creates a Task Object from a given dictionary

        Args:
            data_dict: data dictionary

        Returns:
            TaskList object
        """
        return cls(
            assignee=data_dict["assignee"],
            name=data_dict["name"],
            due_date=data_dict["due_date"],
            priority=data_dict["priority"],
            description=data_dict["description"],
            progress_status=data_dict["progress_status"]
        )
