import pytest
from unittest.mock import Mock, patch

from src.TaskListCLi.TaskListCli import *

# Initializing Cli Commands for help throughout the tests
COMMANDS = initialize_commands()


@pytest.mark.parametrize('command_key, command_func', COMMANDS.items())
def test_handle_command_for_all_commands(command_key, command_func):
    # Mock with specific command attribute
    mock_args = Mock()
    mock_args.subcommand = command_key
    mock_file_handler = Mock()

    # Command corresponding method
    with patch(f"src.TaskListCLi.TaskListCli.{command_func.__name__}", autospec=True) as mock_command:
        handle_command(mock_args, mock_file_handler)
        mock_command.assert_called_once()


def test_handle_command_invalid_subcommand():
    mock_file_handler = Mock()
    args = Mock()
    args.subcommand = "invalid_subcommand"

    with patch("src.TaskListCLi.TaskListCli.logger", new_callable=Mock) as mock_logger:
        handle_command(args, mock_file_handler)
        mock_logger.warning.assert_called_with(f"Unknown command: {args.subcommand}")


def test_handle_command_no_subcommand():
    mock_file_handler = Mock()
    args = Mock()
    args.subcommand = None

    with patch("src.TaskListCLi.TaskListCli.logger", new_callable=Mock) as mock_logger:
        handle_command(args, mock_file_handler)
        mock_logger.warning.assert_called_with("Unknown command: None")


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


def test_display_task_list():
    mock_file_handler = Mock()

    with patch("src.TaskListCLi.TaskListCli.task_list_sanity_check") as mock_sanity:
        mock_task_list = Mock()
        mock_sanity.return_value = mock_task_list

        args = Mock()
        args.task_list_name = "TestTaskList"

        display_task_list(args, mock_file_handler)
        mock_task_list.display_tasklist.assert_called_once()


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
