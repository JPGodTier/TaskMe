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
* colorama==0.4.6
* coverage==7.3.2
* iniconfig==2.0.0
* packaging==23.2
* pluggy==1.3.0
* pytest==7.4.3
* pytest-cov==4.1.0
* pytest-mock==3.12.0

### Installing

#### For Users:

* To install TaskMe: 

```
git clone https://github.com/JPGodTier/TaskMe.git
cd TaskMe
pip install .
```

#### For Developers/Contributors:

If you're planning to contribute or test the latest changes, you should first set up a virtual environment and then install the package in "editable" mode. This allows any changes you make to the source files to immediately affect the installed package without requiring a reinstall.

* Clone the repository:

```
git clone https://github.com/JPGodTier/TaskMe.git
cd TaskMe
```

* Set up a virtual environment:

```
python3 -m venv taskme_env
source taskme_env/bin/activate  # On Windows, use: taskme_env\Scripts\activate
```

* Install the required dependencies:

```
pip install -r requirements.txt
```

* Install TaskMe in editable mode:

```
pip install -e . 
```

### Executing program

Launch the program:  
```
python3 bin/CliRunner.py
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
create 'My tasks' 'John Doe'
```
```
addtask 'My tasks' 'John Doe' 'Buy milk' 01/01/2023 MEDIUM 'Buy fat milk from Walmart'
```
```
rmtask 'My Tasks' 5
```


## Help

To see a list of available commands:
```
--help           # General help
<command> --help # Specific command help
```
To quit:
```
exit
```

## Authors

Paul Aristidou (alias JP God Tier)  
Olivier Lapabe-Goastat (alias GoatStat)

## Version History


## Acknowledgments

To our mothers, without whom this would not have been possible.