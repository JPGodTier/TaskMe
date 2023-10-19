import pytest

from src.TaskList.Task import Task


# -----------------------------------------------------------------------------
# Task Initialization Testing
# -----------------------------------------------------------------------------
def test_task_init():
    task = Task("Billy", "Test Task", "25/10/2023", "LOW", "This is a test task", "PENDING")
    assert task.assignee == "Billy"
    assert task.name == "Test Task"
    assert task.due_date == "25/10/2023"
    assert task.priority == "LOW"
    assert task.description == "This is a test task"
    assert task.progress_status == "PENDING"


def test_invalid_priority():
    with pytest.raises(ValueError):
        Task("Billy", "Test Task", "25/10/2023", "INVALID", "This is a test task", "PENDING")


def test_invalid_progress_status():
    with pytest.raises(ValueError):
        Task("Billy", "Test Task", "25/10/2023", "LOW", "This is a test task", "INVALID_STATUS")


def test_invalid_due_date():
    with pytest.raises(ValueError):
        Task("Billy", "Test Task", "25/102023", "LOW", "This is a test task", "INVALID_STATUS")


# -----------------------------------------------------------------------------
# Task Getter & Setter Testing
# -----------------------------------------------------------------------------
def test_getters_using_setters():
    task = Task("Billy", "Test Task", "25/10/2023", "LOW", "This is a test task", "PENDING")

    task.assignee = "Jack"
    assert task.assignee == "Jack"

    task.name = "Buy a keyboard"
    assert task.name == "Buy a keyboard"

    task.due_date = "26/10/2023"
    assert task.due_date == "26/10/2023"

    task.priority = "HIGH"
    assert task.priority == "HIGH"

    task.description = "Buy a RGB keyboard to type faster"
    assert task.description == "Buy a RGB keyboard to type faster"

    task.progress_status = "IN_PROGRESS"
    assert task.progress_status == "IN_PROGRESS"


def test_priority_setter_invalid_value():
    task = Task("Billy", "Test Task", "25/10/2023", "LOW", "This is a test task", "PENDING")
    with pytest.raises(ValueError):
        task.priority = "VERY HIGH"


def test_progress_status_setter_invalid_value():
    task = Task("Billy", "Test Task", "25/10/2023", "LOW", "This is a test task", "PENDING")
    with pytest.raises(ValueError):
        task.progress_status = "IN BETWEEN"


def test_due_date_setter_invalid_value():
    task = Task("Billy", "Test Task", "25/10/2023", "LOW", "This is a test task", "PENDING")
    with pytest.raises(ValueError):
        task.due_date = "aaaa/23/42"

