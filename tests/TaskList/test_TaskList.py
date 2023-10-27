import pytest
from unittest.mock import patch

from src.TaskList.TaskList import TaskList
from src.TaskList.Task import Task


# -----------------------------------------------------------------------------
# Tests for TaskList
# -----------------------------------------------------------------------------
def test_tasklist_init():
    task_list = TaskList("Test List", ["Jean", "PP"], ["Work", "Personal"])
    assert task_list.name == "Test List"
    assert task_list.owners == ["Jean", "PP"]
    assert task_list.tags == ["Work", "Personal"]


# -----------------------------------------------------------------------------
# test_add_task
# -----------------------------------------------------------------------------
def test_add_task():
    task_list = TaskList("Test List", ["John"], ["Work"])
    kwargs = {"assignee": "Billy",
              "name": "Test Task",
              "due_date": "25/10/2023",
              "priority": "LOW",
              "description": "This is a test task"
              }
    task_list.add_task(**kwargs)
    tasks = task_list.tasks

    assert len(tasks) == 1
    assert tasks[0].assignee == "Billy"
    assert tasks[0].name == "Test Task"
    assert tasks[0].due_date == "25/10/2023"
    assert tasks[0].priority == "LOW"
    assert tasks[0].description == "This is a test task"


# -----------------------------------------------------------------------------
# test_remove_task
# -----------------------------------------------------------------------------
def test_remove_task():
    task_list = TaskList("Test List", ["Jean"], ["Work"])
    kwargs = {
        "assignee": "Billy",
        "name": "Test Task",
        "due_date": "25/10/2023",
        "priority": "LOW",
        "description": "This is a test task"
    }
    task_list.add_task(**kwargs)
    task_list.remove_task(1)
    tasks = task_list.tasks

    assert len(tasks) == 0
    with pytest.raises(ValueError):
        task_list.remove_task(1)


# -----------------------------------------------------------------------------
# test_update_tasklist
# -----------------------------------------------------------------------------
def test_update_tasklist():
    task_list = TaskList("Test List", ["Jean"], ["Work"])
    kwargs = {
        "owners": ["Jean", "Paul", "Olivier"],
        "tags": ["Fun"]
    }
    task_list.update_tasklist(**kwargs)
    assert task_list.__owners == ["Jean", "Paul", "Olivier"]
    assert task_list.__tags == ["Fun"]


# -----------------------------------------------------------------------------
# test_update_task
# -----------------------------------------------------------------------------
def test_update_task():
    task_list = TaskList("Test List", ["Jean"], ["Work"])
    kwargs = {
        "assignee": "Billy",
        "name": "Test Task",
        "due_date": "25/10/2023",
        "priority": "LOW",
        "description": "This is a test task"
    }
    task_list.add_task(**kwargs)
    tasks = task_list.tasks

    assert tasks[0].assignee == "Billy"
    assert tasks[0].name == "Test Task"
    assert tasks[0].due_date == "25/10/2023"
    assert tasks[0].priority == "LOW"
    assert tasks[0].description == "This is a test task"
    assert tasks[0].progress_status == "PENDING"

    kwargs_new = {
        "assignee": "Jean",
        "name": "Updated Task",
        "due_date": "26/10/2023",
        "priority": "HIGH",
        "description": "This is not a task",
        "progress_status": "IN_PROGRESS"
    }
    task_list.update_task(1, **kwargs_new)

    tasks = task_list.tasks
    assert tasks[0].assignee == "Jean"
    assert tasks[0].name == "Updated Task"
    assert tasks[0].due_date == "26/10/2023"
    assert tasks[0].priority == "HIGH"
    assert tasks[0].description == "This is not a task"
    assert tasks[0].progress_status == "IN_PROGRESS"


def test_update_task_invalid_id():
    task_list = TaskList("Test List", ["Jean"], ["Work"])
    kwargs = {
        "assignee": "Billy",
        "name": "Test Task",
        "due_date": "25/10/2023",
        "priority": "LOW",
        "description": "This is a test task"
    }
    task_list.add_task(**kwargs)

    with pytest.raises(ValueError, match=r"Task ID #100 is out of range.") as exc_info:
        task_list.update_task(100, **kwargs)


def test_update_task_no_arguments():
    task_list = TaskList("Test List", ["Jean"], ["Work"])
    kwargs = {
        "assignee": "Billy",
        "name": "Test Task",
        "due_date": "25/10/2023",
        "priority": "LOW",
        "description": "This is a test task"
    }
    task_list.add_task(**kwargs)

    original_task = task_list.tasks[0]

    task_list.update_task(1)
    updated_task = task_list.tasks[0]

    # Check that Task Remains unchanged
    assert original_task.assignee == updated_task.assignee


def test_update_task_nonexistent_attribute():
    task_list = TaskList("Test List", ["Jean"], ["Work"])
    kwargs = {
        "assignee": "Billy",
        "name": "Test Task",
        "due_date": "25/10/2023",
        "priority": "LOW",
        "description": "This is a test task"
    }
    task_list.add_task(**kwargs)

    kwargs_new = {
        "nonexistent_attribute": "value"
    }
    with pytest.raises(ValueError, match=r"Task does not have a setter for 'nonexistent_attribute'.") as exc_info:
        task_list.update_task(1, **kwargs_new)


# -----------------------------------------------------------------------------
# test_to_dict
# -----------------------------------------------------------------------------
def test_to_dict():
    task_list = TaskList("Test List", ["Jean"], ["Work"])
    kwargs = {
        "assignee": "Billy",
        "name": "Test Task",
        "due_date": "25/10/2023",
        "priority": "LOW",
        "description": "This is a test task"
    }
    task_list.add_task(**kwargs)

    task_list_dict = TaskList.to_dict(task_list)
    assert task_list_dict["taskListName"] == "Test List"
    assert task_list_dict["owners"] == ["Jean"]
    assert task_list_dict["tags"] == ["Work"]
    assert task_list_dict["tasks"][0]["assignee"] == "Billy"
    assert task_list_dict["tasks"][0]["name"] == "Test Task"
    assert task_list_dict["tasks"][0]["due_date"] == "25/10/2023"
    assert task_list_dict["tasks"][0]["priority"] == "LOW"
    assert task_list_dict["tasks"][0]["description"] == "This is a test task"
    assert task_list_dict["tasks"][0]["progress_status"] == "PENDING"


# -----------------------------------------------------------------------------
# test_from_dict
# -----------------------------------------------------------------------------
def test_from_dict():
    task = Task("Billy", "Test Task", "25/10/2023", "LOW", "This is a test task", "PENDING")
    task_list_dict = {
        "taskListName": "Test List",
        "owners": ["Jean"],
        "tags": ["Work"],
        "tasks": [Task.to_dict(task)]
    }
    task_list = TaskList.from_dict(task_list_dict)
    assert task_list.name == "Test List"
    assert task_list.owners == ["Jean"]
    assert task_list.tags == ["Work"]
    assert task_list.tasks[0].assignee == "Billy"
    assert task_list.tasks[0].name == "Test Task"
    assert task_list.tasks[0].due_date == "25/10/2023"
    assert task_list.tasks[0].priority == "LOW"
    assert task_list.tasks[0].description == "This is a test task"
    assert task_list.tasks[0].progress_status == "PENDING"


def test_from_dict_with_invalid_task_object():
    # Create a valid TaskList object
    task_list_dict = {
        "taskListName": "Test List",
        "owners": ["BillyBoy"],
        "tags": ["Work"],
        "tasks": [{"dummy": "This is not a valid Task object"}]
    }

    # Mock the Task.from_dict method to return an invalid object
    with patch('src.TaskList.TaskList.Task.from_dict', return_value="Invalid object"):
        with pytest.raises(ValueError, match=r"Expected a Task object.") as exc_info:
            task_list = TaskList.from_dict(task_list_dict)
