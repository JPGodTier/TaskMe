from datetime import datetime


class Progress:
    PENDING = 0
    IN_PROGRESS = 1
    COMPLETED = 2


class Task:
    def __init__(self, assignee, task_name, due_date, priority, description, progress_status):
        self.__assignee = assignee
        self.__task_name = task_name
        self.__due_date = due_date
        self.__priority = priority
        self.__description = description
        self.__progress_status = progress_status
        self.__creation_date = datetime.now()

    def set_assignee(self, new_assignee: str) -> None:
        self.__assignee = new_assignee

    def set_task_name(self, new_name: str) -> None:
        self.__task_name = new_name

    def set_due_date(self, new_due_date: str) -> None:
        self.__due_date = new_due_date

    def set_priority(self, new_priority) -> None:
        self.__priority = new_priority

    def set_description(self, new_description: str) -> None:
        self.__description = new_description

    def set_progress_status(self, new_progress) -> None:
        self.__progress_status = new_progress

    def get_name(self) -> str:
        return self.__task_name

    def get_status(self) -> str:
        return self.__progress_status
    
    def get_assignee(self) -> str:
        return self.__assignee
    
    def get_due_date(self) -> str:
        return self.__due_date
    
    def get_priority(self) -> str:
        return self.__priority
