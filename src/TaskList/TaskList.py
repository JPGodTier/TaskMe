from src import logger
from typing import List

from src.TaskList.Task import Task


# -----------------------------------------------------------------------------
# TaskList
# -----------------------------------------------------------------------------
class TaskList:
    def __init__(self, task_list_name: str, owners: List[str], tags: List[str]) -> None:
        """ Initializes a new TaskList object which will contain a list of Task object

        Args:
            task_list_name:Name of the new TaskList
            owners:List of owner(s) of the new TaskList
            tags:Tag(s) to be added to the new tasklist

        Return:
             None
        """
        # Args init
        self.__name = task_list_name
        self.__owners = owners
        self.__tags = tags

        self.__tasks = []

    # -----------------------------------------------------------------------------
    # __add_task_from_object
    # -----------------------------------------------------------------------------
    def __add_task_from_object(self, task_obj) -> None:
        """ Adds a Task object to the internal TaskList

        Args:
            task_obj: Task Object

        Raises:
            ValueError: if the given task_obj is not of type Task
        """
        if not isinstance(task_obj, Task):
            logger.error("Expected a Task object.")
            raise ValueError("Expected a Task object.")
        self.__tasks.append(task_obj)

    # -----------------------------------------------------------------------------
    # add_task
    # -----------------------------------------------------------------------------
    def add_task(self, **kwargs) -> None:
        """Generic method to add a task to the task list.

        Args:
            **kwargs: Keyword arguments representing the properties of the task to add.
        """
        assignee = kwargs.get("assignee")
        name = kwargs.get("name")
        due_date = kwargs.get("due_date")
        priority = kwargs.get("priority")
        description = kwargs.get("description")

        new_task = Task(assignee, name, due_date, priority, description, "PENDING")

        self.__tasks.append(new_task)
        logger.debug(f"Task '{name}' created successfully.")

    # -----------------------------------------------------------------------------
    # remove_task
    # -----------------------------------------------------------------------------
    def remove_task(self, task_id: int) -> None:
        """ Removes task from the tasklist.

        Args:
            task_id (int): ID of the task to be removed.

        Raises:
            ValueError: if task_id is out of range
        """
        if 0 < task_id <= len(self.__tasks):
            self.__tasks.pop(task_id - 1)
            logger.debug(f"Task #{task_id} removed.")
        else:
            logger.error(f"Task ID #{task_id} is out of range.")
            raise ValueError(f"Task ID #{task_id} is out of range.")

    # -----------------------------------------------------------------------------
    # update_tasklist
    # -----------------------------------------------------------------------------
    def update_tasklist(self, **kwargs) -> None:
        """ Generic method to update a task list's properties

        Args:
            **kwargs: Keyword arguments representing the task list properties to update.

        Raises:
            ValueError: if attribute doesn't have a setter method
        """
        for key, value in kwargs.items():
            if hasattr(self, key) and value is not None:
                setattr(self, key, value)
            else:
                logger.error(f"TaskList does not have a setter for '{key}'.")
                raise ValueError(f"TaskList does not have a setter for '{key}'.")

    # -----------------------------------------------------------------------------
    # update_task
    # -----------------------------------------------------------------------------
    def update_task(self, task_id: int, **kwargs) -> None:
        """ Generic method to update a task's properties.

        Args:
            task_id (int): ID of the task to update.
            **kwargs: Keyword arguments representing the task properties to update.

        Raises:
            ValueError: if Task ID is out of range or if attribute doesn't have a setter method
        """
        if 0 < task_id <= len(self.__tasks):
            task = self.__tasks[task_id - 1]

            for key, value in kwargs.items():
                # Only update if the value is not None
                if value is not None:
                    if hasattr(task, key):
                        setattr(task, key, value)
                    else:
                        logger.error(f"Task does not have a setter for '{key}'.")
                        raise ValueError(f"Task does not have a setter for '{key}'.")
        else:
            logger.error(f"Task ID #{task_id} is out of range.")
            raise ValueError(f"Task ID #{task_id} is out of range.")

    # -----------------------------------------------------------------------------
    # display_tasklist
    # -----------------------------------------------------------------------------
    def display_tasklist(self) -> None:  # pragma: no cover
        """ Creates a default display of the task list.
        """
        print("\n" + "-" * 130)
        print("\n" + "-" * 130)
        print(f"Todo List: {self.__name}")
        print(f"Owner(s): {', '.join(self.__owners)}")
        print(f"Tag(s): {', '.join(self.__tags)}")
        print("-" * 130)

        # Print table headers
        headers = ['Task', 'Status', 'Assignee', 'Due date', 'Priority']
        print(f"{'ID':<5}" + "".join([f"{header:<25}" for header in headers]))
        print("-" * 130)

        # Print each task with its attributes
        for idx, task in enumerate(self.__tasks, 1):
            print(f"{idx:<5}"
                  f"{task.name:<25}"
                  f"{task.progress_status:<25}"
                  f"{task.assignee:<25}"
                  f"{task.due_date:<25}"
                  f"{task.priority}")

        print("-" * 130)

    # -----------------------------------------------------------------------------
    # display_task_description
    # -----------------------------------------------------------------------------
    def display_task_description(self, task_id: int) -> None:  # pragma: no cover
        """ Creates a default display of the task description.

        Args:
            task_id (int): ID of the task to update.

        Raises:
            ValueError: if Task ID is out of range
        """
        if 0 < task_id <= len(self.__tasks):
            task = self.__tasks[task_id - 1]
            print(f"\n{task_id}. {task.name} - "
                  f"Description: {task.description}"
                  )
        else:
            logger.error(f"Task ID #{task_id} is out of range.")
            raise ValueError(f"Task ID '{task_id}' is out of range.")

    # -----------------------------------------------------------------------------
    # name getter
    # -----------------------------------------------------------------------------
    @property
    def name(self) -> str:
        return self.__name

    # -----------------------------------------------------------------------------
    # owners getter & setter
    # -----------------------------------------------------------------------------
    @property
    def owners(self) -> List[str]:
        return self.__owners

    @owners.setter
    def owners(self, owners: List[str]):
        self.__owners = owners

    # -----------------------------------------------------------------------------
    # tags getter & estter
    # -----------------------------------------------------------------------------
    @property
    def tags(self) -> List[str]:
        return self.__tags

    @tags.setter
    def tags(self, tags: List[str]):
        self.__tags = tags

    # -----------------------------------------------------------------------------
    # tasks getter
    # -----------------------------------------------------------------------------
    @property
    def tasks(self) -> List:
        return self.__tasks

    # -----------------------------------------------------------------------------
    # to_dict
    # -----------------------------------------------------------------------------
    def to_dict(self):
        """ Dict representation of a TaskList object

        Returns:
            None
        """
        return {
            "taskListName": self.__name,
            "owners": self.__owners,
            "tags": self.__tags,
            "tasks": [task.to_dict() for task in self.__tasks]
        }

    # -----------------------------------------------------------------------------
    # from_dict
    # -----------------------------------------------------------------------------
    @classmethod
    def from_dict(cls, data: dict):
        """ Creates a TaskList Object from a given dictionary

        Args:
            data (dict): dictionary data

        Returns:
            TaskList object
        """
        task_list = cls(data["taskListName"], data["owners"], data["tags"])

        # If the task list possesses some tasks, load them into the task list
        if "tasks" in data:
            for task_data in data["tasks"]:
                task = Task.from_dict(task_data)
                task_list.__add_task_from_object(task)

        return task_list
