import os
from src.System.TaskMeFileHandler.TaskMeFileHandler import TaskMeFileHandler


class TestTaskMeFileHandler:

    def setup_method(self):
        # This runs before each test
        self.handler = TaskMeFileHandler()
        self.sample_task_list = {
            "taskListName": "Task List Name n1",
            "owners": ["Bob"],
            "tags": ["work"],
            "tasks": []
        }

    def teardown_method(self):
        # Clean up by removing the test file after each test
        if os.path.exists(self.handler.FILE_PATH):
            os.remove(self.handler.FILE_PATH)

    def test_write_and_read_all(self):
        self.handler.write(self.sample_task_list)
        all_task_lists = self.handler.read_all()
        assert len(all_task_lists) == 1
        assert all_task_lists[0]["taskListName"] == "Task List Name n1"

    def test_write_and_read_specific(self):
        self.handler.write(self.sample_task_list)
        retrieved_task_list = self.handler.read("Task List Name n1")
        assert retrieved_task_list["taskListName"] == "Task List Name n1"

    def test_update_task_list(self):
        self.handler.write(self.sample_task_list)
        updated_task_list = self.sample_task_list.copy()
        updated_task_list["tags"].append("personal")
        self.handler.write(updated_task_list)

        retrieved_task_list = self.handler.read("Task List Name n1")
        assert "personal" in retrieved_task_list["tags"]

    def test_read_non_existent_task_list(self):
        retrieved_task_list = self.handler.read("Non-existent Tasks")
        assert not retrieved_task_list

    def test_multiple_task_lists(self):
        second_task_list = {
            "taskListName": "Task n1",
            "owners": ["Bobby"],
            "tags": ["vacation"],
            "tasks": []
        }

        self.handler.write(self.sample_task_list)
        self.handler.write(second_task_list)

        all_task_lists = self.handler.read_all()
        assert len(all_task_lists) == 2

        retrieved_task_list = self.handler.read("Task n1")
        assert retrieved_task_list["taskListName"] == "Task n1"
