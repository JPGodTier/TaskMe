import argparse
from src.TaskListCLi.TaskListCli import handle_command
from src.System.TaskMeFileHandler.TaskMeFileHandler import TaskMeFileHandler

# Validation variables
VALID_PRIORITIES = ['LOW', 'MEDIUM', 'HIGH']
VALID_PROGRESS_STATUSES = ['PENDING', 'IN_PROGRESS', 'COMPLETED']


def main():
    parser = setup_parser()
    file_handler = TaskMeFileHandler()

    while True:
        user_input = input("Enter your command (or 'exit' to quit): ")

        if user_input.lower() in ['exit', 'quit']:
            break

        try:
            args = parser.parse_args(user_input.split())
            handle_command(args, file_handler)
        except SystemExit:
            continue
        except Exception as e:
            print(f"Command error: {e}")


def setup_parser():
    """ Setting up necessary parsers

    Returns:
        the initialized parser object
    """
    # TODO: consider using a specific library like 'click'p
    # TODO: Known limitation: task description and name can only be one word without space
    parser = argparse.ArgumentParser(description="Task List Manager")
    subparsers = parser.add_subparsers(title="subcommands", dest="subcommand")

    # Parser for task list creation
    create_parser = subparsers.add_parser("create", help="Create a new task list")
    create_parser.add_argument("task_list_name", type=str, help="Name of the new task list")
    create_parser.add_argument("owners", nargs='+', type=str, help="Owners of the new task list")
    create_parser.add_argument("--tags", nargs='+', default=[], type=str, help="Tags for the new task list")

    # Parser for task addition
    addtask_parser = subparsers.add_parser("addtask", help="Add new task to a task list")
    addtask_parser.add_argument("task_list_name", type=str,
                                help="Name of the task list where to add a new task")
    addtask_parser.add_argument("assignee", type=str, help="Task assignee")
    addtask_parser.add_argument("name", type=str, help="Task name")
    addtask_parser.add_argument("due_date", type=str, help="Task due date")
    addtask_parser.add_argument("priority", type=str, choices=VALID_PRIORITIES, help="Task priority")
    addtask_parser.add_argument("description", type=str, help="Task description")

    # Parser for task removal
    rmtask_parser = subparsers.add_parser("rmtask", help="Add new task to a task list")
    rmtask_parser.add_argument("task_list_name", type=str, help="Name of the task list where to remove a task")
    rmtask_parser.add_argument("task_id", type=int, help="ID of task to be removed")

    # Parser for task list update
    update_parser = subparsers.add_parser("update", help="Update a new task list")
    update_parser.add_argument("task_list_name", type=str, help="Name of the task list to be updated")
    update_parser.add_argument("--owners", nargs='+', type=str, help="New owner(s) of the task list")
    update_parser.add_argument("--tags", nargs='+', type=str, help="New tag(s) for the task list")

    # Parser for task update
    updatetask_parser = subparsers.add_parser("updatetask", help="Update a task in the list")
    updatetask_parser.add_argument("task_list_name", type=str,
                                   help="Name of the task list where to update a task")
    updatetask_parser.add_argument("task_id", type=int, help="ID of task to be updated")
    updatetask_parser.add_argument("--assignee", type=str, help="Task assignee")
    updatetask_parser.add_argument("--name", type=str, help="Task name")
    updatetask_parser.add_argument("--due_date", type=str, help="Task due date")
    updatetask_parser.add_argument("--priority", type=str, choices=VALID_PRIORITIES, help="Task priority")
    updatetask_parser.add_argument("--description", type=str, help="Task description")
    updatetask_parser.add_argument("--progress_status", type=str, choices=VALID_PROGRESS_STATUSES,
                                   help="Task progress status")

    # Parser for task list display
    display_parser = subparsers.add_parser("display", help="Display a saved task list")
    display_parser.add_argument("task_list_name", type=str, help="Input file containing the saved task list")

    # Parser for task description display
    taskdesc_parser = subparsers.add_parser("taskdesc", help="Display the description of a task")
    taskdesc_parser.add_argument("task_list_name", type=str, help="Name of the task list where task belongs")
    taskdesc_parser.add_argument("task_id", type=int, help="ID of task to be displayed")

    return parser


def startup_msg():
    """ Startup message of the TaskMe CLI

    Returns:

    """
    logo = """
         _____ ___   _____ _   _____  ___ _____ 
        |_   _/ _ \ /  ___| | / /|  \/  ||  ___|
          | |/ /_\ \\\ `--.| |/ / | .  . || |__  
          | ||  _  | `--. \    \ | |\/| ||  __| 
          | || | | |/\__/ / |\  \| |  | || |___ 
          \_/\_| |_/\____/\_| \_/\_|  |_/\____/ 
                                        """

    # Welcome message
    welcome_msg = """
    Welcome to TASK ME - The ultimate task manager (or not)!
    Type '--help' to see a list of available commands or 'exit' to quit.
    """

    # Print the logo and welcome message
    print(logo)
    print(welcome_msg)


if __name__ == "__main__":
    startup_msg()
    main()
