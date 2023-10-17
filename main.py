from src.TaskList.TaskList import *

tl = TaskList("course", ["paul"], "")
tl.add_task("paul", "leclerc", "10/12/2023","LOW", "faire les courses chez leclerc")
print(tl.display())