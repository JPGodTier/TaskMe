from src.TaskList.Task import Task

# -----------------------------------------------------------------------------
# TaskList
# -----------------------------------------------------------------------------
class TaskList:
    def __init__(self, task_list_name: str, owners: [], tags: [], description: str) -> None:
        """
        Intialize a new tasklist

        Args:
            owners (list): List of strings listing the owner(s) of the new tasklist
            task_list_name (str): Name of the new tasklist
            tags (list): Tag(s) to be added to the new tasklist
            description (str): Description of tasklist
        """
        self.__task_list_name = task_list_name
        self.__task_list_owners = owners
        self.__task_list_tags = tags
        self.__task_list_description = description
        self.__task_list = []

    # -----------------------------------------------------------------------------
    # update_task_list_name
    # -----------------------------------------------------------------------------
    def update_task_list_name(self, new_name: str) -> None:
        """
        Update name of tasklist

        Args:
            new_name (str): New name of tasklist
        """
        self.__task_list_name = new_name

    # -----------------------------------------------------------------------------
    # manage_owners
    # -----------------------------------------------------------------------------
    def manage_owners(self, owner_name: str, status: str) -> None:
        """
        Add or remove an owner to or from the tasklist

        Args:
            owner_name (str): Owner name to be added or removed
            status (str): "Add" when willing to add new owner. "Remove" when willing to remove existing owner.

        Raises:
            Exception: When trying to add an already existing owner. When trying to remove a non existing owner.
        """
        if status == "Add":
            if owner_name not in self.__task_list_owners:
                self.__task_list_owners.append(owner_name)
            else:
                print(f"{owner_name} is already an owner")
        elif status == "Remove":
            if owner_name in self.__task_list_owners:
                self.__task_list_owners.remove(owner_name)
            else:
                print(f"{owner_name} not found")
        else:
            raise Exception(f"Status {status} not recognized")

    # -----------------------------------------------------------------------------
    # manage_tags
    # -----------------------------------------------------------------------------
    def manage_tags(self, tag_name: str, status: str) -> None:
        """
        Add or remove a tag to or from the tasklist

        Args:
            tag_name (str): Name of the tag to be added or removed
            status (str): "Add" when willing to add new tag. "Remove" when willing to remove existing tag.

        Raises:
            Exception: When trying to add an already existing tag. When trying to remove a non existing tag.
        """
        if status == "Add":
            if tag_name not in self.__task_list_tags:
                self.__task_list_tags.append(tag_name)
            else:
                print(f"{tag_name} already existing")
        elif status == "Remove":
            if tag_name in self.__task_list_tags:
                self.__task_list_tags.remove(tag_name)
            else:
                print(f"{tag_name} not found")
        else:
            raise Exception(f"Status {status} not recognized")

    # -----------------------------------------------------------------------------
    # update_task_list_description
    # -----------------------------------------------------------------------------
    def update_task_list_description(self, new_description: str) -> None:
        """
        Update description of tasklist

        Args:
            new_name (str): New name of tasklist
        """
        self.__task_list_description = new_description

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
        if priority in ['LOW', 'MEDIUM', 'HIGH']:
            new_task = Task(assignee, task_name, due_date, priority, description, "PENDING")
            self.__task_list.append(new_task)
        else:
            print("\nNew task priority not spelled correctly")
    
    # -----------------------------------------------------------------------------
    # remove_task
    # -----------------------------------------------------------------------------
    def remove_task(self, task_id: int) -> bool:
        """
        Remove task from the tasklist

        Args:
            task_id (int): ID of the task to be removed

        Returns:
            bool: True if task was successfully removed from tasklist. False if not.
        """
        is_removed = False

        try:
            self.__task_list.pop(task_id-1)
            is_updated = True
        except Exception as e:
            print(f"Error while trying to remove task {e}")

        return is_removed

    # -----------------------------------------------------------------------------
    # update_task_assignee
    # -----------------------------------------------------------------------------
    def update_task_assignee(self, task_id: int, new_task_assignee: str) -> None:
        """
        Update the assignee of the task

        Args:
            task_id (int): ID of the task where assignee to be updated
            new__task_assignee (str): New assignee 
        """
        self.__task_list[task_id-1].set_assignee(new_task_assignee)
    
    # -----------------------------------------------------------------------------
    # update_task_name
    # -----------------------------------------------------------------------------
    def update_task_name(self, task_id: int, new_task_name: str) -> None:
        """
        Update the name of the task

        Args:
            task_id (int): ID of the task where task name to be updated
            new_task_name (str): New task name 
        """
        self.__task_list[task_id-1].set_task_name(new_task_name)
    
    # -----------------------------------------------------------------------------
    # update_task_due_date
    # -----------------------------------------------------------------------------
    def update_task_due_date(self, task_id: int, new_task_due_date: str) -> bool:
        """
        Update the due date of the task

        Args:
            task_id (int): ID of the task where due date to be updated
            new_task_due_date (str): New due date of the task

        Returns:
            bool: True if due date was successfully updated. False if not.
        """
        is_updated = False

        try:
            self.__task_list[task_id-1].set_due_date(new_task_due_date)
            is_updated = True
        except Exception as e:
            print(f"Error while trying to update task due date {e}")

        return is_updated
    
    # -----------------------------------------------------------------------------
    # update_task_priority
    # -----------------------------------------------------------------------------
    def update_task_priority(self, task_id: int, new_task_priority: str) -> bool:
        """
        Update the priority of the task

        Args:
            task_id (int): ID of the task where priority to be updated
            new_task_priority (str): New priority of the task ("LOW", "MEDIUM", "HIGH")

        Returns:
            bool: True if task priority was successfully updated. False if not.
        """
        is_updated = False

        try:
            self.__task_list[task_id-1].set_priority(new_task_priority)
            is_updated = True
        except Exception as e:
            print(f"Error while trying to update task priority {e}")

        return is_updated
    
    # -----------------------------------------------------------------------------
    # update_task_description
    # -----------------------------------------------------------------------------
    def update_task_description(self, task_id: int, new_task_description: str) -> None:
        """
        Update the description of the task

        Args:
            task_id (int): ID of the task where description to be updated
            new_task_description (str): New description of the task 
        """
        self.__task_list[task_id-1].set_description(new_task_description)

    # -----------------------------------------------------------------------------
    # update_task_status
    # -----------------------------------------------------------------------------
    def update_task_status(self, task_id: int, new_task_status: str) -> bool:
        """
        Update the status of the task

        Args:
            task_id (int): ID of the task where status to be updated
            new_task_status (str): New progress status ("PENDING", "IN_PROGRESS", "COMPLETED")

        Returns:
            bool: True if status was successfully updated. False if not.
        """
        is_updated = False

        try:
            self.__task_list[task_id-1].set_progress_status(new_task_status)
            is_updated = True
        except Exception as e:
            print(f"Error while trying to update task status {e}")

        return is_updated

    # -----------------------------------------------------------------------------
    # display
    # -----------------------------------------------------------------------------
    def display(self) -> None:
        """
        Creating display of tasklist with:
        - Column 1 : IDs of tasks in the tasklist
        - Column 2 : Names of tasks in the tasklist
        - Column 3 : Status of tasks in the tasklist
        """

        print(" ")
        print(" ")
        print("-" * 100)
        print("-" * 100)

        print(f"Todo List: {self.__task_list_name}")
        print(f"Owner(s): {', '.join(self.__task_list_owners)}")
        print(f"Tag(s): {', '.join(self.__task_list_tags)}")
        print(f"Description: {self.__task_list_description}")


        print("-" * 100)

        # Print table headers
        print(f"{'No.':<5}{'Task':<25}{'Status':<20}{'Assignee':<20}{'Due date':<20}{'Priority'}")
        print("-" * 100)

        # Print each task with its status
        for idx, task in enumerate(self.__task_list, 1):
            print(f"{idx:<5}{task.get_name():<25}{task.get_status():<20}{task.get_assignee():<20}{task.get_due_date():<20}{task.get_priority()}")

        print("-" * 100)

    # -----------------------------------------------------------------------------
    # display_task_description
    # -----------------------------------------------------------------------------
    def display_task_description(self, task_id: int) -> bool:
        is_displayed = False
        try:
            print(f"\n{task_id}. {self.__task_list[task_id-1].get_name()} - Description: {self.__task_list[task_id-1].get_description()}")
            is_displayed = True
        except Exception as e:
            print(f"Error : {e}")
        
        return is_displayed

    # -----------------------------------------------------------------------------
    # get_tasks
    # -----------------------------------------------------------------------------
    def get_tasks(self) -> list:
        """
        Get list of tasks in the tasklist

        Returns:
            list: List of tasks in the tasklist
        """
        return self.__task_list
    
    # -----------------------------------------------------------------------------
    # get_task_list_name
    # -----------------------------------------------------------------------------
    def get_task_list_name(self) -> str:
        """
        Get name of the tasklist

        Returns:
            str: Name of the tasklist
        """
        return self.__task_list_name
    
    # -----------------------------------------------------------------------------
    # get_task_list_owners
    # -----------------------------------------------------------------------------
    def get_task_list_owners(self) -> list:
        """
        Get list of owners of the tasklist

        Returns:
            list: List of owners of the tasklist
        """
        return self.__task_list_owners
    
    # -----------------------------------------------------------------------------
    # get_task_list_tags
    # -----------------------------------------------------------------------------
    def get_task_list_tags(self) -> list:
        """
        Get list of tags of the tasklist

        Returns:
            list: List of tags of the tasklist
        """
        return self.__task_list_tags
    

    

