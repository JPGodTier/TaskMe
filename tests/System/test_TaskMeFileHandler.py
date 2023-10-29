import pytest
from unittest.mock import mock_open, patch, MagicMock
from src.System.TaskMeFileHandler.TaskMeFileHandler import TaskMeFileHandler


class TestTaskMeFileHandler:

    @pytest.fixture(autouse=True)
    def setup_method(self, mocker):
        self.file_data = {"taskLists": []}

        # Mock open and json.load/.dump
        mocker.patch('builtins.open', mock_open())
        mocker.patch('json.load', side_effect=self.json_load_side_effect)
        mocker.patch('json.dump', side_effect=self.json_dump_side_effect)

        self.handler = TaskMeFileHandler()
        self.sample_task_list = {
            "taskListName": "Task List Name n1",
            "owners": ["Bob"],
            "tags": ["work"],
            "tasks": []
        }

    def json_load_side_effect(self, fp):
        return self.file_data

    def json_dump_side_effect(self, data, fp, indent):
        self.file_data = data

    # -----------------------------------------------------------------------------
    # test_file_handler_init_file
    # -----------------------------------------------------------------------------
    def test_file_handler_init_file_exists(self):
        with patch("os.path.isfile", return_value=True):
            with patch("src.TaskListCLi.TaskListCli.logger", new_callable=MagicMock) as _:
                # File exists -> __initialize_data_file should not be called
                self.handler = TaskMeFileHandler()

                # File contents should remain unchanged
                assert self.file_data == {"taskLists": []}

    def test_file_handler_init_file_does_not_exist(self):
        with patch("os.path.isfile", return_value=False):
            with patch("src.TaskListCLi.TaskListCli.logger", new_callable=MagicMock) as _:
                # File doesn't exist -> __initialize_data_file should be called
                self.handler = TaskMeFileHandler()

                assert self.file_data == {"taskLists": []}

    # -----------------------------------------------------------------------------
    # test_write_and_read_all
    # -----------------------------------------------------------------------------
    def test_write_and_read_all(self):
        self.handler.write(self.sample_task_list)
        all_task_lists = self.handler.read_all()

        assert len(all_task_lists) == 1
        assert all_task_lists[0]["taskListName"] == "Task List Name n1"

    # -----------------------------------------------------------------------------
    # test_write_and_read_specific
    # -----------------------------------------------------------------------------
    def test_write_and_read_specific(self):
        self.handler.write(self.sample_task_list)
        retrieved_task_list = self.handler.read("Task List Name n1")

        assert retrieved_task_list["taskListName"] == "Task List Name n1"

    # -----------------------------------------------------------------------------
    # test_update_task_list
    # -----------------------------------------------------------------------------
    def test_update_task_list(self):
        self.handler.write(self.sample_task_list)
        updated_task_list = self.sample_task_list.copy()
        updated_task_list["tags"].append("personal")
        self.handler.write(updated_task_list)

        retrieved_task_list = self.handler.read("Task List Name n1")
        assert "personal" in retrieved_task_list["tags"]

    # -----------------------------------------------------------------------------
    # test_read_non_existent_task_list
    # -----------------------------------------------------------------------------
    def test_read_non_existent_task_list(self):
        retrieved_task_list = self.handler.read("Non-existent Tasks")
        assert not retrieved_task_list

    # -----------------------------------------------------------------------------
    # test_multiple_task_lists
    # -----------------------------------------------------------------------------
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
