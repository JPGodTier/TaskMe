import pytest
from unittest.mock import Mock, patch

from src.TaskListCLi.TaskListCli import *  # noqa: F405

# Initializing Cli Commands for help throughout the tests
COMMANDS = initialize_commands()


# -----------------------------------------------------------------------------
# test_handle_command
# -----------------------------------------------------------------------------
@pytest.mark.parametrize('command_key, command_func', COMMANDS.items())
def test_handle_command_for_all_commands(command_key, command_func):
    # Mock with specific command attribute
    mock_args = Mock()
    mock_args.subcommand = command_key
    mock_file_handler = Mock()

    # Command corresponding method
    with patch(f"src.TaskListCLi.TaskListCli.{command_func.__name__}", autospec=True) as mock_command:
        result = handle_command(mock_args, mock_file_handler)
        mock_command.assert_called_once()
        assert result is True


def test_handle_command_invalid_subcommand():
    mock_file_handler = Mock()
    args = Mock()
    args.subcommand = "invalid_subcommand"

    with patch("src.TaskListCLi.TaskListCli.logger", new_callable=Mock) as mock_logger:
        result = handle_command(args, mock_file_handler)
        mock_logger.warning.assert_called_with(f"Unknown command: {args.subcommand}")
        assert result is False


def test_handle_command_no_subcommand():
    mock_file_handler = Mock()
    args = Mock()
    args.subcommand = None

    with patch("src.TaskListCLi.TaskListCli.logger", new_callable=Mock) as mock_logger:
        result = handle_command(args, mock_file_handler)
        mock_logger.warning.assert_called_with("Unknown command: None")
        assert result is False


def test_handle_command_raises_exception():
    mock_file_handler = Mock()
    mock_args = Mock()

    # Set the subcommand to a known command that will raise an exception
    mock_args.subcommand = "known_command"

    # Mock the known command to raise an exception
    with patch("src.TaskListCLi.TaskListCli.initialize_commands",
               return_value={"known_command": Mock(side_effect=Exception("Simulated command error"))}):
        with patch("src.TaskListCLi.TaskListCli.logger", new_callable=Mock) as mock_logger:
            is_executed = handle_command(mock_args, mock_file_handler)

            # Check that the logger.error was called
            mock_logger.error.assert_called_with("Command known_command failed: Simulated command error")

            assert not is_executed


# -----------------------------------------------------------------------------
# test_task_list_sanity
# -----------------------------------------------------------------------------
def test_task_list_sanity_check_valid_data():
    mock_file_handler = Mock()
    mock_file_handler.read.return_value = {"taskListName": "TestTaskList", "owners": [], "tags": []}
    task_list_name = mock_file_handler.read.return_value["taskListName"]

    result = task_list_sanity_check(task_list_name, mock_file_handler)
    assert isinstance(result, TaskList)


def test_task_list_sanity_check_invalid_data():
    mock_file_handler = Mock()
    mock_file_handler.read.return_value = None
    task_list_name = "TestTaskList"

    with pytest.raises(Exception, match=f"Task list '{task_list_name}' not found"):
        task_list_sanity_check(task_list_name, mock_file_handler)


# -----------------------------------------------------------------------------
# test_create_task_list
# -----------------------------------------------------------------------------
def test_create_task_list():
    mock_file_handler = Mock()
    mock_file_handler.write.return_value = None
    args = Mock()

    args.task_list_name = "TestTaskList"
    args.owners = ["Owner1", "Owner2"]
    args.tags = ["tag1", "tag2"]

    with patch("src.TaskListCLi.TaskListCli.logger", new_callable=Mock) as mock_logger:
        create_task_list(args, mock_file_handler)

    mock_logger.info.assert_called_with(f"Task list '{args.task_list_name}' created and saved")
    mock_file_handler.write.assert_called_once()


# -----------------------------------------------------------------------------
# test_update_task_list
# -----------------------------------------------------------------------------
def test_update_task_list():
    mock_file_handler = Mock()
    mock_file_handler.write.return_value = None

    with patch("src.TaskListCLi.TaskListCli.task_list_sanity_check") as mock_sanity:
        # Returns a Mock TaskList
        mock_sanity.return_value = Mock()

        args = Mock()
        args.task_list_name = "TestTaskList"
        args.owners = ["Owner1", "Owner2"]
        args.tags = ["tag1", "tag2"]

        with patch("src.TaskListCLi.TaskListCli.logger", new_callable=Mock) as mock_logger:
            update_task_list(args, mock_file_handler)

        mock_logger.info.assert_called_with(f"Task list '{args.task_list_name}' updated and saved")
        mock_file_handler.write.assert_called_once()


def test_update_task_list_failure():
    mock_file_handler = Mock()

    # Mock the task_list_sanity_check to raise an exception
    with patch("src.TaskListCLi.TaskListCli.task_list_sanity_check",
               side_effect=Exception("Task list 'NonExistentTaskList' not found")):
        args = Mock()
        args.task_list_name = "NonExistentTaskList"

        # Assert that calling update_task_list raises the expected exception
        with pytest.raises(Exception, match="Task list 'NonExistentTaskList' not found"):
            update_task_list(args, mock_file_handler)


# -----------------------------------------------------------------------------
# test_add_task
# -----------------------------------------------------------------------------
def test_add_task():
    mock_file_handler = Mock()
    mock_file_handler.write.return_value = None

    with patch("src.TaskListCLi.TaskListCli.task_list_sanity_check") as mock_sanity:
        mock_task_list = Mock()
        mock_sanity.return_value = mock_task_list

        args = Mock()
        args.task_list_name = "TestTaskList"
        args.assignee = "Assignee1"
        args.name = "TestTask"
        args.due_date = "31-12-2023"
        args.priority = "HIGH"
        args.description = "Test Description"

        with patch("src.TaskListCLi.TaskListCli.logger", new_callable=Mock) as mock_logger:
            add_task(args, mock_file_handler)

        mock_task_list.add_task.assert_called_once_with(assignee=args.assignee,
                                                        name=args.name,
                                                        due_date=args.due_date,
                                                        priority=args.priority,
                                                        description=args.description)
        mock_logger.info.assert_called_with(f"Task '{args.name}' added and saved")


def test_add_task_failure():
    mock_file_handler = Mock()

    # Mock the task_list_sanity_check to raise an exception
    with patch("src.TaskListCLi.TaskListCli.task_list_sanity_check",
               side_effect=Exception("Task list 'NonExistentTaskList' not found")):
        args = Mock()
        args.task_list_name = "NonExistentTaskList"

        # Assert that calling add_task raises the expected exception
        with pytest.raises(Exception, match="Task list 'NonExistentTaskList' not found"):
            add_task(args, mock_file_handler)


# -----------------------------------------------------------------------------
# test_update_task
# -----------------------------------------------------------------------------
def test_update_task_success():
    mock_file_handler = Mock()
    mock_task_list = Mock()

    mock_args = Mock()
    mock_args.task_list_name = "TestTaskList"
    mock_args.task_id = 1
    mock_args.assignee = "Assignee1"
    mock_args.name = "TestTask"
    mock_args.due_date = "31-12-2023"
    mock_args.priority = "HIGH"
    mock_args.description = "Test Description"
    mock_args.progress_status = "IN_PROGRESS"

    with patch("src.TaskListCLi.TaskListCli.task_list_sanity_check", return_value=mock_task_list):
        with patch("src.TaskListCLi.TaskListCli.logger", new_callable=Mock) as mock_logger:
            update_task(mock_args, mock_file_handler)

            # Asserts
            mock_task_list.update_task.assert_called_once_with(
                mock_args.task_id,
                assignee=mock_args.assignee,
                name=mock_args.name,
                due_date=mock_args.due_date,
                priority=mock_args.priority,
                description=mock_args.description,
                progress_status=mock_args.progress_status
            )
            mock_file_handler.write.assert_called_once_with(mock_task_list.to_dict())
            mock_logger.info.assert_called_with(f"Task '{mock_args.name}' updated and saved")


def test_update_task_failure():
    mock_file_handler = Mock()
    mock_args = Mock()
    mock_args.task_list_name = "TestTaskList"

    # Simulate an exception when sanity check is called
    with patch("src.TaskListCLi.TaskListCli.task_list_sanity_check", side_effect=Exception("Sanity check error")):
        with pytest.raises(Exception, match="Sanity check error"):
            update_task(mock_args, mock_file_handler)


# -----------------------------------------------------------------------------
# test_remove_task
# -----------------------------------------------------------------------------
def test_remove_task():
    mock_file_handler = Mock()
    mock_file_handler.write.return_value = None

    with patch("src.TaskListCLi.TaskListCli.task_list_sanity_check") as mock_sanity:
        mock_task_list = Mock()
        mock_sanity.return_value = mock_task_list

        args = Mock()
        args.task_list_name = "TestTaskList"
        args.task_id = 1

        with patch("src.TaskListCLi.TaskListCli.logger", new_callable=Mock) as mock_logger:
            remove_task(args, mock_file_handler)

        mock_task_list.remove_task.assert_called_once_with(task_id=args.task_id)
        mock_logger.info.assert_called_with(f"Task  #{args.task_id} removed")


def test_remove_task_failure():
    mock_file_handler = Mock()

    # Mock the task_list_sanity_check to raise an exception
    with patch("src.TaskListCLi.TaskListCli.task_list_sanity_check",
               side_effect=Exception("Task list 'NonExistentTaskList' not found")):
        args = Mock()
        args.task_list_name = "NonExistentTaskList"

        # Assert that calling remove_task raises the expected exception
        with pytest.raises(Exception, match="Task list 'NonExistentTaskList' not found"):
            remove_task(args, mock_file_handler)


# -----------------------------------------------------------------------------
# test_display_task_list
# -----------------------------------------------------------------------------
def test_display_task_list():
    mock_file_handler = Mock()

    with patch("src.TaskListCLi.TaskListCli.task_list_sanity_check") as mock_sanity:
        mock_task_list = Mock()
        mock_sanity.return_value = mock_task_list

        args = Mock()
        args.task_list_name = "TestTaskList"

        display_task_list(args, mock_file_handler)
        mock_task_list.display_tasklist.assert_called_once()


def test_display_task_list_failure():
    mock_file_handler = Mock()

    # Mock the task_list_sanity_check to raise an exception
    with patch("src.TaskListCLi.TaskListCli.task_list_sanity_check",
               side_effect=Exception("Task list 'NonExistentTaskList' not found")):
        args = Mock()
        args.task_list_name = "NonExistentTaskList"

        # Assert that calling display_task_list raises the expected exception
        with pytest.raises(Exception, match="Task list 'NonExistentTaskList' not found"):
            display_task_list(args, mock_file_handler)


# -----------------------------------------------------------------------------
# test_display_task_description
# -----------------------------------------------------------------------------
def test_display_task_description():
    mock_file_handler = Mock()

    with patch("src.TaskListCLi.TaskListCli.task_list_sanity_check") as mock_sanity:
        mock_task_list = Mock()
        mock_sanity.return_value = mock_task_list

        args = Mock()
        args.task_list_name = "TestTaskList"
        args.task_id = 1

        display_task_description(args, mock_file_handler)
        mock_task_list.display_task_description.assert_called_once_with(args.task_id)


def test_display_task_description_failure():
    mock_file_handler = Mock()

    # Mock the task_list_sanity_check to raise an exception
    with patch("src.TaskListCLi.TaskListCli.task_list_sanity_check",
               side_effect=Exception("Task list 'NonExistentTaskList' not found")):
        args = Mock()
        args.task_list_name = "NonExistentTaskList"

        # Assert that calling display_task_description raises the expected exception
        with pytest.raises(Exception, match="Task list 'NonExistentTaskList' not found"):
            display_task_description(args, mock_file_handler)
