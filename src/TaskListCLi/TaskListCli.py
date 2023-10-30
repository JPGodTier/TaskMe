from src import logger

from src.TaskList.TaskList import TaskList


# -----------------------------------------------------------------------------
# initialize_commands
# -----------------------------------------------------------------------------
def initialize_commands():
    # CLI commands mapping
    return {
        "create": create_task_list,
        "addtask": add_task,
        "rmtask": remove_task,
        "update": update_task_list,
        "updatetask": update_task,
        "display": display_task_list,
        "taskdesc": display_task_description
    }


# -----------------------------------------------------------------------------
# handle_command
# -----------------------------------------------------------------------------
def handle_command(args, file_handler) -> bool:
    """ Handles the mapping between input args and CLI commands

    Args:
        args: command arguments
        file_handler: file handler object

    Returns:
        True if command was executed successfully, False otherwise
    """
    # Command status state
    is_executed = False

    # Get Available commands
    commands = initialize_commands()

    # Execute
    if args.subcommand in commands:
        try:
            logger.debug(f"Calling command: {args.subcommand}")
            commands[args.subcommand](args, file_handler)
            is_executed = True
        except Exception as e:
            logger.error(f"Command {args.subcommand} failed: {e}")
    else:
        logger.warning(f"Unknown command: {args.subcommand}")

    return is_executed


# -----------------------------------------------------------------------------
# task_list_sanity_check
# -----------------------------------------------------------------------------
def task_list_sanity_check(task_list_name, file_handler):
    """ Checks for the existence of the taskList using the task list name

    Args:
        task_list_name: command arguments
        file_handler: file handler object

    Returns:
        A Task List object if the task list exist in the data file,
        None otherwise

    Raises:
        Custom Exception if task list name was not found in the data file
    """
    task_list_data = file_handler.read(task_list_name)
    if not task_list_data:
        raise Exception(f"Task list '{task_list_name}' not found")

    return TaskList.from_dict(task_list_data)


# -----------------------------------------------------------------------------
# create_task_list
# -----------------------------------------------------------------------------
def create_task_list(args, file_handler) -> None:
    """ Creates a new task list and saves it into the data file

    Args:
        args: command arguments
        file_handler: file handler object
    """
    # TODO: check how args work when its optional
    task_list = TaskList(args.task_list_name, args.owners, args.tags)
    file_handler.write(task_list.to_dict())
    logger.info(f"Task list '{args.task_list_name}' created and saved")


# -----------------------------------------------------------------------------
# update_task_list
# -----------------------------------------------------------------------------
def update_task_list(args, file_handler) -> None:
    """ Updates an existing task list and saves it into the data file

    Args:
        args: command arguments
        file_handler: file handler object

    Raises:
        Exception if sanity check has failed
    """
    try:
        task_list = task_list_sanity_check(args.task_list_name, file_handler)
        task_list.update_tasklist(owners=args.owners, tags=args.tags)
        file_handler.write(task_list.to_dict())
        logger.info(f"Task list '{args.task_list_name}' updated and saved")
    except Exception as e:
        raise


# -----------------------------------------------------------------------------
# add_task
# -----------------------------------------------------------------------------
def add_task(args, file_handler) -> None:
    """ Adds a Task into an existing task list and saves it into the data file

    Args:
        args: command arguments
        file_handler: file handler object

    Raises:
        Exception if sanity check has failed
    """
    try:
        task_list = task_list_sanity_check(args.task_list_name, file_handler)
        task_list.add_task(assignee=args.assignee, name=args.name, due_date=args.due_date,
                           priority=args.priority, description=args.description)
        file_handler.write(task_list.to_dict())
        logger.info(f"Task '{args.name}' added and saved")
    except Exception as e:
        raise


# -----------------------------------------------------------------------------
# update_task
# -----------------------------------------------------------------------------
def update_task(args, file_handler) -> None:
    """ Updates an existing task and saves it into the data file

    Args:
        args: command arguments
        file_handler: file handler object

    Raises:
        Exception if sanity check has failed
    """
    try:
        task_list = task_list_sanity_check(args.task_list_name, file_handler)
        task_list.update_task(args.task_id, assignee=args.assignee, name=args.name, due_date=args.due_date,
                              priority=args.priority, description=args.description,
                              progress_status=args.progress_status)
        file_handler.write(task_list.to_dict())
        logger.info(f"Task '{args.name}' updated and saved")
    except Exception as e:
        raise


# -----------------------------------------------------------------------------
# remove_task
# -----------------------------------------------------------------------------
def remove_task(args, file_handler) -> None:
    """ Removes an existing task from the data file

    Args:
        args: command arguments
        file_handler: file handler object

    Raises:
        Exception if sanity check has failed
    """
    try:
        task_list = task_list_sanity_check(args.task_list_name, file_handler)
        task_list.remove_task(task_id=args.task_id)
        file_handler.write(task_list.to_dict())
        logger.info(f"Task  #{args.task_id} removed")
    except Exception as e:
        raise


# -----------------------------------------------------------------------------
# display_task_list
# -----------------------------------------------------------------------------
def display_task_list(args, file_handler) -> None:
    """ Displays the selected task list

    Args:
        args: command arguments
        file_handler: file handler object

    Raises:
        Exception if sanity check has failed
    """
    try:
        task_list = task_list_sanity_check(args.task_list_name, file_handler)
        task_list.display_tasklist()
    except Exception as e:
        raise


# -----------------------------------------------------------------------------
# display_task_description
# -----------------------------------------------------------------------------
def display_task_description(args, file_handler) -> None:
    """ Display the selected task description

    Args:
        args: command arguments
        file_handler: file handler object

    Raises:
        Exception if sanity check has failed
    """
    try:
        task_list = task_list_sanity_check(args.task_list_name, file_handler)
        task_list.display_task_description(args.task_id)
    except Exception as e:
        raise
