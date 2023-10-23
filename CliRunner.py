import argparse
import pickle
from typing import Optional, Type

from src.TaskList.TaskList import TaskList


# Validation variables
VALID_PRIORITIES = ['LOW', 'MEDIUM', 'HIGH']
VALID_PROGRESS_STATUSES = ['PENDING', 'IN_PROGRESS', 'COMPLETED']

def main():
    parser = argparse.ArgumentParser(description="Task List Manager")
    
    subparsers = parser.add_subparsers(title="subcommands", dest="subcommand")

    # Parser for task list creation
    create_parser = subparsers.add_parser("create", help="Create a new task list")
    create_parser.add_argument("task_list_name", type=str, help="Name of the new task list")
    create_parser.add_argument("owners", nargs='+', type=str, help="Owners of the new task list")
    create_parser.add_argument("--tags", nargs='+', default=[], type=str, help="Tags for the new task list")

    # Parser for task addition
    addtask_parser = subparsers.add_parser("addtask", help="Add new task to a task list")
    addtask_parser.add_argument("task_list_name", type=str, help="Name of the task list where to add a new task")
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
    updatetask_parser.add_argument("task_list_name", type=str, help="Name of the task list where to update a task")
    updatetask_parser.add_argument("task_id", type=int, help="ID of task to be updated")
    updatetask_parser.add_argument("--assignee", type=str, help="Task assignee")
    updatetask_parser.add_argument("--name", type=str, help="Task name")
    updatetask_parser.add_argument("--due_date", type=str, help="Task due date")
    updatetask_parser.add_argument("--priority", type=str, choices=VALID_PRIORITIES, help="Task priority")
    updatetask_parser.add_argument("--description", type=str, help="Task description")
    updatetask_parser.add_argument("--progress_status", type=str, choices=VALID_PROGRESS_STATUSES, help="Task progress status")

    # Parser for task list display
    display_parser = subparsers.add_parser("display", help="Display a saved task list")
    display_parser.add_argument("task_list_name", type=str, help="Input file containing the saved task list")

    # Parser for task description display
    taskdesc_parser = subparsers.add_parser("taskdesc", help="Display the description of a task")
    taskdesc_parser.add_argument("task_list_name", type=str, help="Name of the task list where task belongs")
    taskdesc_parser.add_argument("task_id", type=int, help="ID of task to be displayed")
    
    # Complilation of parser arguments
    args = parser.parse_args()

    # Create new task list
    if args.subcommand == "create":
        task_list = TaskList(args.task_list_name, args.owners, args.tags)
        with open(f"{args.task_list_name}.pkl", 'wb') as file:
            pickle.dump(task_list, file)
        print(f"Task list '{args.task_list_name}' created and saved")

    # Open existing task list
    with open(f"{args.task_list_name}.pkl", 'rb') as file:
        task_list = pickle.load(file)

    # Add new task
    if args.subcommand == "addtask":
        task_list.add_task(assignee = args.assignee, 
                           name = args.name, 
                           due_date = args.due_date, 
                           priority = args.priority,
                           description = args.description
                           )

    # Remove task
    if args.subcommand == "rmtask":
        task_list.remove_task(task_id = args.task_id)

    # Update task list
    if args.subcommand == "update":
        task_list.update_tasklist(owners = args.owners, 
                                  tags = args.tags
                                  )

    # Update task
    if args.subcommand == "updatetask":
        task_list.update_task(args.task_id,
                              assignee = args.assignee, 
                              name = args.name, 
                              due_date = args.due_date, 
                              priority = args.priority, 
                              description = args.description,
                              progress_status = args.progress_status
                              )
    
    # Display task list
    if args.subcommand == "display":
        task_list.display_tasklist()

    # Display task description
    if args.subcommand == "taskdesc":
        task_list.display_task_description(args.task_id)

    with open(f"{args.task_list_name}.pkl", 'wb') as file:
        pickle.dump(task_list, file) 

if __name__ == "__main__":
    main()