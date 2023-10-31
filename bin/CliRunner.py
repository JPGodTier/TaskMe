# flake8: noqa: F405

import argparse
from src import logger, __version__
import shlex

from src.TaskListCLi.TaskListCli import handle_command
from src.System.TaskMeFileHandler.TaskMeFileHandler import TaskMeFileHandler
from src.Common.utils import VALID_PRIORITIES, VALID_PROGRESS_STATUSES


def main():
    """ Main Cli loop
    """
    parser = setup_parser()
    file_handler = TaskMeFileHandler()
    while True:
        user_input = input("Enter your TaskMe command (or 'exit' to quit): ")

        if user_input.lower() in ['exit', 'quit']:
            break

        try:
            args = parser.parse_args(shlex.split(user_input))
            if not handle_command(args, file_handler):
                print(f"Failed to execute command {args.subcommand}. Check logs for more details.")
        except SystemExit:
            print("Invalid command or arguments. Try again or check the documentation.")
            continue
        except Exception as e:
            logger.error(f"Error when running command: {e}")
            print("An unexpected error occurred. Check logs for more details.")


def setup_parser():
    """ Setting up necessary parsers

    Returns:
        the initialized parser object
    """
    # TODO: consider using a specific library like 'click'p
    parser = argparse.ArgumentParser(
        description="""Task List Manager

        Subcommands:
        create       - Create a new task list.
        addtask      - Add a new task to an existing task list.
        rmtask       - Remove a task from a task list.
        update       - Update the details of an existing task list.
        updatetask   - Update details of a task in a task list.
        display      - Display the tasks in a task list.
        taskdesc     - Display the detailed description of a specific task.
        
        Examples:
           create 'My tasks' 'John Doe'
           addtask 'My tasks' 'John Doe' 'Buy milk' 01/01/2023 MEDIUM 'Buy fat milk from Walmart'
           rmtask 'My Tasks' 5
           
        NOTE: For multi-word arguments, please enclose them in quotes.
        """,
        epilog="For detailed information about each command, type 'CliRunner.py <command> -h'.",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    subparsers = parser.add_subparsers(title="subcommands", dest="subcommand")

    # Parser for task list creation
    create_parser = subparsers.add_parser("create",
                                          help="Creates a new task list: create <task_list_name> <owner1> "
                                               "[owner2 ...] [--tags tag1 tag2 ...]")
    create_parser.add_argument("task_list_name", type=str,
                               help="Name of the future Task Lst (if multiple words per tag, enclose in quotes)")
    create_parser.add_argument("owners", nargs='+', type=str,
                               help="<owner1> [owner2 ...]: Owners of the new task list")
    create_parser.add_argument("--tags", nargs='+', default=[], type=str,
                               help="[--tags tag1 tag2 ...]: Tags for the new task list")

    # Parser for task addition
    addtask_parser = subparsers.add_parser("addtask",
                                           help="Adds a task: addtask <task_list_name> <assignee> <name> <due_date>"
                                                " <priority> <description>")
    addtask_parser.add_argument("task_list_name", type=str,
                                help="Task list to add to")
    addtask_parser.add_argument("assignee", type=str,
                                help="Task assignee")
    addtask_parser.add_argument("name", type=str,
                                help="Task name")
    addtask_parser.add_argument("due_date", type=str,
                                help="Due date (format: DD-MM-YYYY)")
    addtask_parser.add_argument("priority", type=str, choices=VALID_PRIORITIES,
                                help=f"Priority choices)")
    addtask_parser.add_argument("description", type=str,
                                help="Task description (if multiple words, enclose in quotes)")

    # Parser for task removal
    rmtask_parser = subparsers.add_parser("rmtask",
                                          help="Removes a task: rmtask <task_list_name> <task_id>")
    rmtask_parser.add_argument("task_list_name", type=str,
                               help="Task List from which to remove (if multiple words, enclose in quotes)")
    rmtask_parser.add_argument("task_id", type=int,
                               help="ID of the task to remove")

    # Parser for task list update
    update_parser = subparsers.add_parser("update",
                                          help="Updates a task list: update <task_list_name>"
                                               " [--owners owner1 owner2 ...] [--tags tag1 tag2 ...]")
    update_parser.add_argument("task_list_name", type=str,
                               help="Task List name to update (if multiple words, enclose in quotes)")
    update_parser.add_argument("--owners", nargs='+', type=str,
                               help="Specify new owner(s) for the task list")
    update_parser.add_argument("--tags", nargs='+', type=str,
                               help="Add/Modify tags for the task list")

    # Parser for task update
    updatetask_parser = subparsers.add_parser("updatetask",
                                              help="Updates task attributes: updatetask <task_list_name>"
                                                   " <task_id> [options...]")
    updatetask_parser.add_argument("task_list_name", type=str,
                                   help="Task List name containing targeted task"
                                        " (if multiple words, enclose in quotes)")
    updatetask_parser.add_argument("task_id", type=int,
                                   help="ID of the task to update")
    updatetask_parser.add_argument("--assignee", type=str,
                                   help="Update the assignee of the task")
    updatetask_parser.add_argument("--name", type=str,
                                   help="Update the name/title of the task")
    updatetask_parser.add_argument("--due_date", type=str,
                                   help="Change the task due date")
    updatetask_parser.add_argument("--priority", type=str, choices=VALID_PRIORITIES,
                                   help="Set a new task priority")
    updatetask_parser.add_argument("--description", type=str,
                                   help="Modify the task's description")
    updatetask_parser.add_argument("--progress_status", type=str, choices=VALID_PROGRESS_STATUSES,
                                   help="Update the task's progress status")

    # Parser for task list display
    display_parser = subparsers.add_parser("display",
                                           help="Displays the content of a task list: display <task_list_name>")
    display_parser.add_argument("task_list_name", type=str,
                                help="Task List name you want to display (if multiple words, enclose in quotes)")

    # Parser for task description display
    taskdesc_parser = subparsers.add_parser("taskdesc",
                                            help="Displays the description of a specific task:"
                                                 " taskdesc <task_list_name> <task_id>")
    taskdesc_parser.add_argument("task_list_name", type=str,
                                 help="Task List name of the targeted task (if multiple words, enclose in quotes)")
    taskdesc_parser.add_argument("task_id", type=int,
                                 help="ID of the task whose description you want to display ")

    return parser


def startup_msg():
    """ Startup message of the TaskMe CLI
    """
    # noinspection PyPep8
    logo = f"""
         _____ ___   _____ _   _____  ___ _____ 
        |_   _/ _ \ /  ___| | / /|  \/  ||  ___|
          | |/ /_\ \\\ `--.| |/ / | .  . || |__  
          | ||  _  | `--. \    \ | |\/| ||  __| 
          | || | | |/\__/ / |\  \| |  | || |___ 
          \_/\_| |_/\____/\_| \_/\_|  |_/\____/ 
                                         v{__version__}"""

    welcome_msg = """
    Welcome to TASK ME - The ultimate task manager (or not)!
    Type '--help' to see a list of available commands or 'exit' to quit.
    """

    print(logo)
    print(welcome_msg)


if __name__ == "__main__":
    startup_msg()
    main()
