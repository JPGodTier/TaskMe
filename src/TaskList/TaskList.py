from typing import List

from src.TaskList.Task import Task


# -----------------------------------------------------------------------------
# TaskList
# -----------------------------------------------------------------------------
class TaskList:
    def __init__(self, task_list_name: str, owners: List[str], tags: List[str]) -> None:
        """ Initializes a new TaskList object which will contain a list of Task object

        Args
        ----
        name (str):
            Name of the new TaskList
        owners (List[str]):
            List of owner(s) of the new TaskList
        tags (List[str]):
            Tag(s) to be added to the new tasklist
        """
        # Args init
        self.__name = task_list_name
        self.__owners = owners
        self.__tags = tags

        self.__tasks = []

    # -----------------------------------------------------------------------------
    # add_task
    # -----------------------------------------------------------------------------
    """Generic method to add a task to the task list.

        Args
        ----
            **kwargs: Keyword arguments representing the properties of the task to add.

        Return
        -------
            None
        """
    def add_task(self, **kwargs) -> None:

        assignee = kwargs.get("assignee")
        name = kwargs.get("name")
        due_date = kwargs.get("due_date")
        priority = kwargs.get("priority")
        description = kwargs.get("description")

        new_task = Task(assignee, name, due_date, priority, description, "PENDING")

        self.__tasks.append(new_task)
        print(f"Task '{name}' created")
    
    # -----------------------------------------------------------------------------
    # remove_task
    # -----------------------------------------------------------------------------
    def remove_task(self, task_id: int) -> None:
        """Remove task from the tasklist.

        Args
        ----
            task_id (int): ID of the task to be removed.

        Returns
        -------
            None
        """
        if 0 < task_id <= len(self.__tasks):
            self.__tasks.pop(task_id - 1)
            print(f"\nTask #{task_id} has been removed.")
        else:
            raise ValueError(f"Task ID '{task_id}' is out of range.")

    # -----------------------------------------------------------------------------
    # update_tasklist
    # -----------------------------------------------------------------------------
    def update_tasklist(self, **kwargs) -> None:
        """Generic method to update a task list's properties.

        Args
        ----
            **kwargs: Keyword arguments representing the task list properties to update.

        Return
        -------
            None
        """
        is_updated = False

        if kwargs.get("owners"):
            self.__owners = kwargs.get("owners")
            is_updated = True
            print(f"Task list '{self.__name}' updated")
        if kwargs.get("tags"):
            self.__tags = kwargs.get("tags")
            is_updated = True
            print(f"Task list '{self.__name}' updated")
        if is_updated == False:
            print("Nothing to be updated")

    # -----------------------------------------------------------------------------
    # update_task
    # -----------------------------------------------------------------------------
    def update_task(self, task_id: int, **kwargs) -> None:
        """Generic method to update a task's properties.

        Args
        ----
            task_id (int): ID of the task to update.
            **kwargs: Keyword arguments representing the task properties to update.

        Return
        -------
            None
        """
        if 0 < task_id <= len(self.__tasks):
            task = self.__tasks[task_id - 1]

            is_updated = False

            if kwargs.get("assignee"):
                task.assignee = kwargs.get("assignee")
                is_updated = True
                print(f"Task '{task.name}' updated")
            if kwargs.get("name"):
                task.name = kwargs.get("name")
                is_updated = True
                print(f"Task '{task.name}' updated")
            if kwargs.get("due_date"):
                task.due_date = kwargs.get("due_date")
                is_updated = True
                print(f"Task '{task.name}' updated")
            if kwargs.get("priority"):
                task.priority = kwargs.get("priority")
                is_updated = True
                print(f"Task '{task.name}' updated")
            if kwargs.get("description"):
                task.description = kwargs.get("description")
                is_updated = True
                print(f"Task '{task.name}' updated")
            if kwargs.get("progress_status"):
                task.progress_status = kwargs.get("progress_status")
                is_updated = True
                print(f"Task '{task.name}' updated")
            if is_updated == False:
                print("Nothing to be updated")
        else:
            raise ValueError(f"Task ID '{task_id}' is out of range.")
        
    # -----------------------------------------------------------------------------
    # display_tasklist
    # -----------------------------------------------------------------------------
    def display_tasklist(self) -> None:
        """
        Creates a default display of the task list.
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
    """Creates a default display of the task description.

        Args
        ----
            task_id (int): ID of the task to update.

        Return
        -------
            None
        """
    def display_task_description(self, task_id) -> None:
        if 0 < task_id <= len(self.__tasks):
            task = self.__tasks[task_id - 1]
            print(f"\n{task_id}. {task.name} - " 
                    f"Description: {task.description}"
                    )
        else:
            raise ValueError(f"Task ID '{task_id}' is out of range.")