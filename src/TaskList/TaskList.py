from typing import List

from src.TaskList.Task import Task


# -----------------------------------------------------------------------------
# TaskList
# -----------------------------------------------------------------------------
class TaskList:
    def __init__(self, task_list_name: str, owners: List[str], tags: List[str]) -> None:
        """ Initializes a new TaskList object which will contain a list of Task object

        Attributes
        ----------
        name (str):
            Name of the new TaskList
        owners (List[str]): str
            List of owner(s) of the new TaskList
        tags (List[str]): str
            Tag(s) to be added to the new tasklist
        """
        # Attributes init
        self.__name = task_list_name
        self.__owners = owners
        self.__tags = tags

        self.__tasks = []

    # -----------------------------------------------------------------------------
    # update_name
    # -----------------------------------------------------------------------------
    def update_name(self, new_name: str) -> None:
        """ Updates the name of the Task List

        Args:
            new_name: new name of the task list

        Returns: None

        """
        self.__name = new_name

    # -----------------------------------------------------------------------------
    # add_owner
    # -----------------------------------------------------------------------------
    def add_owner(self, owner_name: str) -> None:
        """ Adds an owner to the tasklist

        Args:
            owner_name (str): Owner name to be added

        Returns:
            None

        Raises:
            ValueError: if the owner already exists
        """
        if owner_name in self.__owners:
            # TODO: raising an exception might be too harsh
            raise ValueError(f"Owner '{owner_name}' already exists.")
        self.__owners.append(owner_name)

    # -----------------------------------------------------------------------------
    # remove_owner
    # -----------------------------------------------------------------------------
    def remove_owner(self, owner_name: str) -> None:
        """ Removes an owner from the task list

        Args:
            owner_name (str): Owner name to be removed

        Returns:
            None

        Raises:
             ValueError: If owner doesn't exist.
        """
        if owner_name not in self.__owners:
            # TODO: raising an exception might be too harsh
            raise ValueError(f"Owner '{owner_name}' doesn't exists.")
        self.__owners.remove(owner_name)

    # -----------------------------------------------------------------------------
    # add_tag
    # -----------------------------------------------------------------------------
    def add_tag(self, tag_name: str) -> None:
        """ Adds a tag to the task list

        Args:
            tag_name (str): Tag Name to be added

        Returns:
            None

        Raises:
            ValueError: If tag already exists
        """
        if tag_name in self.__tags:
            # TODO: raising an exception might be too harsh
            raise ValueError(f"Tag '{tag_name}' already exists.")
        self.__tags.append(tag_name)

    # -----------------------------------------------------------------------------
    # remove_tag
    # -----------------------------------------------------------------------------
    def remove_tag(self, tag_name: str) -> None:
        """ Removes a tag to the task list

        Args:
            tag_name (str): Tag Name to be added

        Returns:
            None

        Raises:
            ValueError: If tag doesn't exist.
        """
        if tag_name not in self.__tags:
            # TODO: raising an exception might be too harsh
            raise ValueError(f"Tag '{tag_name}' doesn't exists.")
        self.__tags.remove(tag_name)

    # -----------------------------------------------------------------------------
    # add_task
    # -----------------------------------------------------------------------------
    def add_task(self, assignee: str, task_name: str, due_date: str, priority: str, description: str) -> None:
        """
        Add a task to the tasklist

        Args:
            assignee (str): Assignee name of the new task
            task_name (str): Name of the new task
            due_date (str): Date and time of creation of the new task
            priority (str): Priority of the new task (LOW, MEDIUM, HIGH)
            description (str): Description of the new task
        """
        if priority not in ['LOW', 'MEDIUM', 'HIGH']:
            raise ValueError(f"Invalid priority '{priority}'. Valid values are 'LOW', 'MEDIUM', 'HIGH'.")
        new_task = Task(assignee, task_name, due_date, priority, description, "PENDING")
        self.__tasks.append(new_task)

    # -----------------------------------------------------------------------------
    # remove_task
    # -----------------------------------------------------------------------------
    def remove_task(self, task_id: int) -> None:
        """
        Remove task from the tasklist

        Args:
            task_id (int): ID of the task to be removed

        Returns:
            None
        """
        if 0 < task_id <= len(self.__tasks):
            self.__tasks.pop(task_id - 1)
        else:
            raise ValueError(f"Task ID '{task_id}' is out of range.")

    # -----------------------------------------------------------------------------
    # update_task
    # -----------------------------------------------------------------------------
    def update_task(self, task_id: int, **kwargs) -> None:
        """Generic method to update a task's properties.

        Args:
            task_id (int): ID of the task to update.
            **kwargs: Keyword arguments representing the task properties to update.

        Return:
            None
        """
        if 0 < task_id <= len(self.__tasks):
            task = self.__tasks[task_id - 1]

            for key, value in kwargs.items():
                if hasattr(task, key):
                    setattr(task, key, value)
                else:
                    raise ValueError(f"Task does not have a setter for '{key}'.")
        else:
            raise ValueError(f"Task ID '{task_id}' is out of range.")

    # -----------------------------------------------------------------------------
    # get_tasks
    # -----------------------------------------------------------------------------
    def get_tasks(self) -> List[Task]:
        """ Returns the list of tasks

        Returns:
            List[Task]: List of tasks in the task list.
        """
        return self.__tasks

    # -----------------------------------------------------------------------------
    # get_name
    # -----------------------------------------------------------------------------
    def get_name(self) -> str:
        """ Returns the name of the task list

        Returns:
            str: Name of the tasklist
        """
        return self.__name

    # -----------------------------------------------------------------------------
    # get_owners
    # -----------------------------------------------------------------------------
    def get_owners(self) -> List[str]:
        """ Returns the list of owners of the task list

        Returns:
            List[str]: List of owners.
        """
        return self.__owners

    # -----------------------------------------------------------------------------
    # get_tags
    # -----------------------------------------------------------------------------
    def get_tags(self) -> List[str]:
        """ Returns the list of tags associated with the task list.

        Returns:
            List[str]: List of tags.
        """
        return self.__tags

    # -----------------------------------------------------------------------------
    # display
    # -----------------------------------------------------------------------------
    def display(self) -> None:
        """ Creates a default display of the tasklist

        Returns:
            None
        """

        print("\n" + "-" * 134)
        print(f"Todo List: {self.__name}")
        print(f"Owner(s): {', '.join(self.__owners)}")
        print(f"Tag(s): {', '.join(self.__tags)}")
        print("-" * 134)

        # Print table headers
        headers = ['No.', 'Task', 'Status', 'Assignee', 'Due date', 'Priority']
        print("".join([f"{header:<25}" for header in headers]))

        # Print each task with its attributes
        for idx, task in enumerate(self.__tasks, 1):
            print(f"{idx:<25}"
                  f"{task.name:<25}"
                  f"{task.progress_status:<25}"
                  f"{task.assignee:<25}"
                  f"{task.due_date:<25}"
                  f"{task.priority}")

        print("-" * 134)

    # -----------------------------------------------------------------------------
    # display_task_description
    # -----------------------------------------------------------------------------
    def display_task_description(self, task_id: int) -> None:
        try:
            print(f"\n{task_id}. {self.__tasks[task_id-1].name()} -"
                  f" Description: {self.__tasks[task_id-1].description()}")
        except Exception as e:
            raise Exception(f"Error while displaying task description: {e}")
