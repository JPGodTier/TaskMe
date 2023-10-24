from src.TaskList.TaskList import TaskList


def handle_command(args, file_handler):
    """ Handles the mapping between input args and CLI commands

    Args:
        args: command arguments
        file_handler: file handler object

    Returns:
        None
    """
    # Commands mapping
    commands = {
        "create": create_task_list,
        "addtask": add_task,
        "rmtask": remove_task,
        "update": update_task_list,
        "updatetask": update_task,
        "display": display_task_list,
        "taskdesc": display_task_description
    }

    # Execute
    if args.subcommand in commands:
        commands[args.subcommand](args, file_handler)
    else:
        print(f"Unknown command: {args.subcommand}")


# -----------------------------------------------------------------------------
# task_list_sanity_check
# -----------------------------------------------------------------------------
def task_list_sanity_check(task_list_name, file_handler,):
    """ Checks for the existence of the taskList using the task list name

    Args:
        args: command arguments
        file_handler: file handler object

    Returns:
        A Task List object if the task list exist in the data file,
        None otherwise
    """
    task_list_data = file_handler.read(task_list_name)
    if not task_list_data:
        print(f"Task list '{task_list_name}' not found, aborting command")
        return None

    return TaskList.from_dict(task_list_data)


# -----------------------------------------------------------------------------
# create_task_list
# -----------------------------------------------------------------------------
def create_task_list(args, file_handler):
    """ Creates a new task list and saves it into the dta file

    Args:
        args: command arguments
        file_handler: file handler object

    Returns:
        None
    """
    task_list = TaskList(args.task_list_name, args.owners, args.tags)
    file_handler.write(task_list.to_dict())
    print(f"Task list '{args.task_list_name}' created and saved")


# -----------------------------------------------------------------------------
# create_task_list
# -----------------------------------------------------------------------------
def update_task_list(args, file_handler):
    """ Updates an existing task list and saves it into the data file

    Args:
        args: command arguments
        file_handler: file handler object


    Returns:
        None
    """
    if not (task_list := task_list_sanity_check(args.task_list_name, file_handler)):
        return
    task_list.update_tasklist(owners=args.owners, tags=args.tags)
    file_handler.write(task_list.to_dict())


# -----------------------------------------------------------------------------
# add_task
# -----------------------------------------------------------------------------
def add_task(args, file_handler):
    """ Adds a Task into an existing task list and saves it into the data file

    Args:
        args: command arguments
        file_handler: file handler object

    Returns:
        None
    """
    if not (task_list := task_list_sanity_check(args.task_list_name, file_handler)):
        return
    task_list.add_task(assignee=args.assignee, name=args.name, due_date=args.due_date,
                       priority=args.priority, description=args.description)
    file_handler.write(task_list.to_dict())


# -----------------------------------------------------------------------------
# update_task
# -----------------------------------------------------------------------------
def update_task(args, file_handler):
    """ Updates an existing task and saves it into the data file

    Args:
        args: command arguments
        file_handler: file handler object=

    Returns:
        None
    """
    if not (task_list := task_list_sanity_check(args.task_list_name, file_handler)):
        return
    task_list.update_task(args.task_id, assignee=args.assignee, name=args.name, due_date=args.due_date,
                          priority=args.priority, description=args.description,
                          progress_status=args.progress_status)
    file_handler.write(task_list.to_dict())


# -----------------------------------------------------------------------------
# remove_task
# -----------------------------------------------------------------------------
def remove_task(args, file_handler):
    """ Removes an existing task from the data file

    Args:
        args: command arguments
        file_handler: file handler object

    Returns:
        None
    """
    if not (task_list := task_list_sanity_check(args.task_list_name, file_handler)):
        return
    task_list.remove_task(task_id=args.task_id)
    file_handler.write(task_list.to_dict())


# -----------------------------------------------------------------------------
# display_task_list
# -----------------------------------------------------------------------------
def display_task_list(args, file_handler):
    """ Displays the selected task list

    Args:
        args: command arguments
        file_handler: file handler object


    Returns:
        None
    """
    if not (task_list := task_list_sanity_check(args.task_list_name, file_handler)):
        return
    task_list.display_tasklist()


# -----------------------------------------------------------------------------
# display_task_description
# -----------------------------------------------------------------------------
def display_task_description(args, file_handler):
    """ Display the selected task description

    Args:
        args: command arguments
        file_handler: file handler object


    Returns:
        None
    """
    if not (task_list := task_list_sanity_check(args.task_list_name, file_handler)):
        return
    task_list.display_task_description(args.task_id)
