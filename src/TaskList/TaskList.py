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
    #TODO: modify with **kwargs
    def add_task(self, args) -> bool:
        is_added = False
        try:
            new_task = Task(args.assignee, 
                            args.taskname, 
                            args.duedate, 
                            args.priority, 
                            args.description, 
                            "PENDING"
                            )
            self.__tasks.append(new_task)
            print(f"Task '{args.taskname}' created")
            is_added = True
        except Exception as e:
            print(f"Error while trying to add the task: {e}")
        
        return is_added

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
    # update_tasklist
    # -----------------------------------------------------------------------------
    # TODO: Modify with **kwargs
    def update_tasklist(self, args) -> bool:
        is_updated = False
        try: 
            if args.owners:
                self.__owners = args.owners
                is_updated = True
                print(f"Task list '{args.name}' updated")
            if args.tags:
                self.__tags = args.tags
                is_updated = True
                print(f"Task list '{args.name}' updated")
            if is_updated == False:
                print("Nothing to be updated")
        except Exception as e:
            print(f"Error while trying to update the task list {args.name}: {e}")
        
        return is_updated

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
    # display_tasklist
    # -----------------------------------------------------------------------------
    def display_tasklist(self) -> None:
        """
        Creates a default display of the task list
        """

        print("\n" + "-" * 130)
        print("\n" + "-" * 130)
        print(f"Todo List: {self.__task_list_name}")
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
                  f"{task.task_name:<25}"
                  f"{task.progress_status:<25}"
                  f"{task.assignee:<25}"
                  f"{task.due_date:<25}"
                  f"{task.priority}")

        print("-" * 130)

    # -----------------------------------------------------------------------------
    # display_task_description
    # -----------------------------------------------------------------------------
    # TODO: Modify args with task_id
    def display_task_description(self, args) -> bool:
        is_displayed = False
        try:
            print(f"\n{args.task_id}. {self.__tasks[args.task_id-1].task_name} - " 
                  f"Description: {self.__tasks[args.task_id-1].description}"
                  )
            is_displayed = True
        except Exception as e:
            print("Error while trying to display the task"
                  f"{self.__tasks[args.task_id-1].task_name}: {e}"
                  )
        
        return is_displayed