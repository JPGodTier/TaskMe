import json
import os
from pathlib import Path

from src import logger


class TaskMeFileHandler:
    def __init__(self):
        """Initialize a file handler for TaskMe JSON storage."""
        self.__file_path = self.__get_data_file_path()
        logger.debug(f"Data file path: {self.__file_path}")
        if not os.path.isfile(self.__file_path):
            self.__initialize_data_file()

    # -----------------------------------------------------------------------------
    # __get_data_file_path
    # -----------------------------------------------------------------------------
    @staticmethod
    def __get_data_file_path():
        # Retrieve the root TaskMe directory
        parent_dir = Path(__file__).resolve().parents[3]

        data_dir = parent_dir / "data"

        # If the directory doesn't exist, create it
        data_dir.mkdir(exist_ok=True)

        # Define the file path inside the data directory
        return data_dir / ".taskme_data.json"

    # -----------------------------------------------------------------------------
    # __initialize_data_file
    # -----------------------------------------------------------------------------
    def __initialize_data_file(self) -> None:
        """Initialize the data file with default values.
        """
        default_data = {"taskLists": []}
        with open(self.__file_path, 'w') as file:
            json.dump(default_data, file, indent=4)

    # -----------------------------------------------------------------------------
    # __write_all
    # -----------------------------------------------------------------------------
    def __write_all(self, task_lists: list) -> None:
        """Writes all TasklList to the data file (internal).

        Args:
            task_lists (list): A list of TaskList dictionaries.
        """
        data = {"taskLists": task_lists}

        with open(self.__file_path, 'w') as file:
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
        with open(self.__file_path, 'r') as file:
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
        """
        # TODO: might be expensive as the file grows, replace by database in the futur
        all_task_lists = self.read_all()
        updated = False
        for idx, task_list in enumerate(all_task_lists):
            if task_list["taskListName"] == task_list_dict["taskListName"]:
                all_task_lists[idx] = task_list_dict
                updated = True
                break

        # If the TaskList wasn't found, add it.
        if not updated:
            logger.info(f"TaskList {task_list_dict['taskListName']} wasn't found - hence got created")
            all_task_lists.append(task_list_dict)

        self.__write_all(all_task_lists)
