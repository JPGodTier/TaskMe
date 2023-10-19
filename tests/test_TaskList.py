import pytest

from src.TaskList.TaskList import TaskList


# -----------------------------------------------------------------------------
# Tests for TaskList
# -----------------------------------------------------------------------------
def test_tasklist_init():
    task_list = TaskList("Test List", ["Jean", "PP"], ["Work", "Personal"])
    assert task_list.get_name() == "Test List"
    assert task_list.get_owners() == ["Jean", "PP"]
    assert task_list.get_tags() == ["Work", "Personal"]


def test_add_remove_owner():
    task_list = TaskList("Test List", ["Jean"], ["Work"])
    task_list.add_owner("PP")
    assert task_list.get_owners() == ["Jean", "PP"]
    with pytest.raises(ValueError):
        task_list.add_owner("PP")
    task_list.remove_owner("PP")
    assert task_list.get_owners() == ["Jean"]
    with pytest.raises(ValueError):
        task_list.remove_owner("PP")


def test_add_remove_tag():
    task_list = TaskList("Test List", ["Jean"], ["Work"])
    task_list.add_tag("Personal")
    assert task_list.get_tags() == ["Work", "Personal"]
    with pytest.raises(ValueError):
        task_list.add_tag("Personal")
    task_list.remove_tag("Personal")
    assert task_list.get_tags() == ["Work"]
    with pytest.raises(ValueError):
        task_list.remove_tag("Personal")


def test_add_task():
    task_list = TaskList("Test List", ["John"], ["Work"])
    task_list.add_task("Billy", "Test Task", "25/10/2023", "LOW", "This is a test task")
    tasks = task_list.get_tasks()
    assert len(tasks) == 1
    assert tasks[0].assignee == "Billy"
    assert tasks[0].name == "Test Task"
    assert tasks[0].due_date == "25/10/2023"
    assert tasks[0].priority == "LOW"
    assert tasks[0].description == "This is a test task"


def test_remove_task():
    task_list = TaskList("Test List", ["Jean"], ["Work"])
    task_list.add_task("Billy", "Test Task", "25/10/2023", "LOW", "This is a test task")
    task_list.remove_task(1)
    tasks = task_list.get_tasks()
    assert len(tasks) == 0
    with pytest.raises(ValueError):
        task_list.remove_task(1)


def test_update_task():
    task_list = TaskList("Test List", ["Jean"], ["Work"])
    task_list.add_task(
        "Billy",
        "Test Task",
        "25/10/2023",
        "LOW",
        "This is a test task")
    task_list.update_task(
        1,
        assignee="Jean",
        name="Updated Task",
        due_date="26/10/2023",
        priority="HIGH",
        description="This is not a task",
        progress_status="IN_PROGRESS")

    tasks = task_list.get_tasks()
    assert tasks[0].assignee == "Jean"
    assert tasks[0].name == "Updated Task"
    assert tasks[0].due_date == "26/10/2023"
    assert tasks[0].priority == "HIGH"
    assert tasks[0].description == "This is not a task"
    assert tasks[0].progress_status == "IN_PROGRESS"
