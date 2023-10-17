from datetime import datetime


class Progress:
    PENDING = 0
    IN_PROGRESS = 1
    COMPLETED = 2

# -----------------------------------------------------------------------------
# Task
# -----------------------------------------------------------------------------
class Task:
    """
    Task class, initializing it with assignee, task name, due date, priority, description and progress status.
    Then creating necessary setters and getters.
    """
    def __init__(self, assignee: str, task_name: str, due_date: str, priority: str, description: str, progress_status: str) -> None:
        self.__assignee = assignee
        self.__task_name = task_name
        self.__due_date = due_date
        self.__priority = priority
        self.__description = description
        self.__progress_status = progress_status

    # -----------------------------------------------------------------------------
    # set_assignee
    # -----------------------------------------------------------------------------
    def set_assignee(self, new_assignee: str) -> None:
        """
        Set new assignee to the task

        Args:
            new_assignee (str): Name of new assignee
        """
        self.__assignee = new_assignee

    # -----------------------------------------------------------------------------
    # set_task_name
    # -----------------------------------------------------------------------------
    def set_task_name(self, new_name: str) -> None:
        """
        Set new name to the task

        Args:
            new_name (str): New name of task
        """
        self.__task_name = new_name

    # -----------------------------------------------------------------------------
    # set_due_date
    # -----------------------------------------------------------------------------
    def set_due_date(self, new_due_date: str) -> None:
        """
        Set new due date to the task

        Args:
            new_due_date (str): New due date of task
        """
        self.__due_date = new_due_date

    # -----------------------------------------------------------------------------
    # set_priority
    # -----------------------------------------------------------------------------
    def set_priority(self, new_priority: str) -> None:
        """
        Set new priority to the task

        Args:
            new_priority (str): New priority of task
        """
        if new_priority in ['LOW', 'MEDIUM', 'HIGH']:
            self.__priority = new_priority
        else:
            print("\nNew task priority not spelled correctly")

    # -----------------------------------------------------------------------------
    # set_description
    # -----------------------------------------------------------------------------
    def set_description(self, new_description: str) -> bool:
        """
        Set new description to the task

        Args:
            new_description (str): New description of task
        """
        self.__description = new_description

    # -----------------------------------------------------------------------------
    # set_progress_status
    # -----------------------------------------------------------------------------
    def set_progress_status(self, new_progress: str) -> None:
        """
        Set new progress status to the task

        Args:
            new_due_date (str): New due date of task
        """
        self.__progress_status = new_progress

        if new_progress in ['PENDING', 'IN_PROGRESS', 'COMPLETED']:
            self.__progress_status = new_progress
        else:
            print(f"\nNew progress status not spelled correctly")

    # -----------------------------------------------------------------------------
    # get_assignee
    # -----------------------------------------------------------------------------
    def get_assignee(self) -> str:
        """
        Get assignee of task

        Returns:
            str: Assignee of task
        """
        return self.__assignee
    
    # -----------------------------------------------------------------------------
    # get_name
    # -----------------------------------------------------------------------------
    def get_name(self) -> str:
        """
        Get name of task

        Returns:
            str: Name of task
        """
        return self.__task_name
    
    # -----------------------------------------------------------------------------
    # get_due_date
    # -----------------------------------------------------------------------------
    def get_due_date(self) -> str:
        """
        Get due date of task

        Returns:
            str: Due date of task
        """
        return self.__due_date
    
    # -----------------------------------------------------------------------------
    # get_priority
    # -----------------------------------------------------------------------------    
    def get_priority(self) -> str:
        """
        Get priority of task

        Returns:
            str: Priority of task
        """
        return self.__priority
    
    # -----------------------------------------------------------------------------
    # get_description
    # -----------------------------------------------------------------------------
    def get_description(self) -> str:
        """
        Get description of task

        Returns:
            str: Description of task
        """        
        return self.__description
    
    # -----------------------------------------------------------------------------
    # get_status
    # -----------------------------------------------------------------------------
    def get_status(self) -> str:
        """
        Get status of task

        Returns:
            str: Status of task
        """        
        return self.__progress_status
