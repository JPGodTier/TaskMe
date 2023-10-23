import os
import json


class TaskMeFileHandler:
    # Pre-defined data file and location for the TaskMe project.
    FILE_PATH = os.path.expanduser(".taskme_data.json")

    def __init__(self):
        """Initialize a file handler for TaskMe JSON storage."""
        if not os.path.exists(self.FILE_PATH):
            self.__initialize_data_file()

    # -----------------------------------------------------------------------------
    # __initialize_data_file
    # -----------------------------------------------------------------------------
    def __initialize_data_file(self) -> None:
        """Initialize the data file with default values.

        Returns:
            None
        """
        default_data = {"taskLists": []}
        with open(self.FILE_PATH, 'w') as file:
            json.dump(default_data, file, indent=4)

    # -----------------------------------------------------------------------------
    # __write_all
    # -----------------------------------------------------------------------------
    def __write_all(self, task_lists: list) -> None:
        """Writes all TasklList to the data file (internal).

        Args:
            task_lists (list): A list of TaskList dictionaries.

        Returns:
            None
        """
        data = {"taskLists": task_lists}

        with open(self.FILE_PATH, 'w') as file:
            json.dump(data, file, indent=4)

    # -----------------------------------------------------------------------------
    # Interface
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    # read_all
    # -----------------------------------------------------------------------------
    def read_all(self) -> list:
        """Reads all TaskLists from the data file.

        Returns:
            list: A list of TaskList dictionaries.
        """
        with open(self.FILE_PATH, 'r') as file:
            data = json.load(file)
            return data["taskLists"]

    # -----------------------------------------------------------------------------
    # read
    # -----------------------------------------------------------------------------
    def read(self, task_list_name: str) -> dict:
        """Reads a specific TaskList.

        Args:
            task_list_name (str): The name of the TaskList.

        Returns:
            dict: The desired dictionary if successful, None otherwise.
        """
        read_tl = []
        all_task_lists = self.read_all()
        for task_list in all_task_lists:
            if task_list["taskListName"] == task_list_name:
                read_tl = task_list

        return read_tl

    # -----------------------------------------------------------------------------
    # write
    # -----------------------------------------------------------------------------
    def write(self, task_list_dict: dict) -> None:
        """Adds or updates a TaskList in the data file.

        Args:
            task_list_dict: The TaskList dictionary to write.

        Returns:
            None
        """
        # TODO: might be expensive as the file grows, to investigate
        all_task_lists = self.read_all()
        updated = False
        for idx, task_list in enumerate(all_task_lists):
            if task_list["taskListName"] == task_list_dict["taskListName"]:
                all_task_lists[idx] = task_list_dict
                updated = True
                break

        if not updated:  # If the TaskList wasn't found and updated, add it.
            # TODO: add logging
            all_task_lists.append(task_list_dict)

        self.__write_all(all_task_lists)
