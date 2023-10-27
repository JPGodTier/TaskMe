# TaskMe The ultimate task manager (or not)!
TaskMe is a tool to create and managed tasks.  
GitHub: https://github.com/JPGodTier/TaskMe

         _____ ___   _____ _   _____  ___ _____ 
        |_   _/ _ \ /  ___| | / /|  \/  ||  ___|
          | |/ /_\ \\ `--.| |/ / | .  . || |__  
          | ||  _  | `--. \    \ | |\/| ||  __| 
          | || | | |/\__/ / |\  \| |  | || |___ 
          \_/\_| |_/\____/\_| \_/\_|  |_/\____/ 

The full documentation can be accessed here : 

## Description

* With TaskMe, you can create and different task lists with their own name, owners and tags describing the task list.  
* Within the different task lists you have created, you can add tasks with their name, assignee, due date, priority (LOW, MEDIUM, HIGH), description and progress status (PENDING, IN_PROGRESS, COMPLETED).  
* Each task can be also updated or removed.
You can display each task list to see its list of tasks and their current status.

## Getting Started

### Dependencies

See requirements.txt:
* iniconfig==2.0.0
* packaging==23.2
* pluggy==1.3.0
* pytest==7.4.3

### Installing

* To be completed once the setup is finalized
* How/where to download your program
* Any modifications needed to be made to files/folders

### Executing program

Launch the program:  
```
python3 TaskMe/bin/CliRunner.py
```
You can enter your command line (for multi-word arguments, please enclose them in quotes):
* ```create```: Creates a new task list
```
create <task_list_name> <owner1> [owner2 ...] [--tags tag1 tag2 ...]
```

*  ```addtask```: Adds a task
```
addtask <task_list_name> <assignee> <name> <due_date> <priority> <description>
```

*  ```rmtask```: Removes a task
```
rmtask <task_list_name> <task_id>
```

*  ```update```: Updates a task list
```
update <task_list_name> [--owners owner1 owner2 ...] [--tags tag1 tag2 ...]
```

*  ```updatetask```: Updates task attributes
```
updatetask <task_list_name> <task_id> [options...]
```

*  ```display```: Displays the content of a task list
```
display <task_list_name>
```

*  ```taskdesc```: Displays the description of a specific task
```
taskdesc <task_list_name> <task_id>
```

* Examples:
```
create MyTasks JohnDoe
```
```
addtask 'My tasks' JohnDoe BuyMilk 01-01-22 MEDIUM 'Buy milk from store'
```
```
rmtask MyTasks 5
```

## Help

To see a list of available commands:
```
--help
```
To quit:
```
exit
```

## Authors

Paul Aristidou (alias JP God Tier)  
Olivier Lapabe-Goastat

## Version History


## Acknowledgments

To our mothers, without whom this would not have been possible.