import logging
import pickle
from src.TaskList.TaskList import TaskList

logging.basicConfig(filename='CliRunner.log', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

def main():

    logging.info("CliRunner.py has been started.") 

    while True:

        print("\nWelcome to TaskMe")
        print("1. Create new Task List")
        print("2. Open existing Task List")
        print("3. Quit")

        choice_0 = input("Enter your choice (1/2/3): ")

        if choice_0 == "1":
            task_list_name = input("Enter the name of the task list: ")
            task_list_owners = input("Enter the owner(s) of the task list (separated by ,): ")
            task_list_tags = input("Enter the tag(s) of the task list (separated by ,): ")
            task_list_description = input("Enter the description of the task list: ")

            task_list = TaskList(task_list_name, task_list_owners.split(", "), task_list_tags.split(", "), task_list_description)
            logging.info(f"New task list \"{task_list_name}\" has been created.") 
            pass

        elif choice_0 == "2":
            list_name = input("Enter the name of the task list: ")
            try:
                with open(f"{list_name}.pkl", "rb") as pkl_file:
                    task_list = pickle.load(pkl_file)
                logging.info(f"Task list \"{list_name}\" has been opened.") 
                print("Task list successfully open")
                pass
            except Exception as e:
                logging.error("Erreur rencontrée : {e}") 
                print(f"Erreur rencontrée : {e}")
                break
        
        elif choice_0 == "3":
            print("Goodbye!")
            logging.info("CliRunner.py has been stopped.") 
            break

        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")
            continue


        while True:
            task_list.display()

            print("\nCommand Line Todo List")
            print("1. Add or Remove Task")
            print("2. Get Task description")
            print("3. Update Existing Task")
            print("4. Update Task List infos")
            print("5. Go back")

            choice = input("Enter your choice (1/2/3/4/5): ")

            if choice == "1":

                while True:
                    print("\n1. Add Task")
                    print("2. Remove Task")
                    print("3. Go back")

                    choice_1 = input("Enter your choice (1/2/3): ")

                    if choice_1 == "1":
                        task_owner = input("Enter the task owner: ")
                        task_name = input("Enter the task name: ")
                        task_date = input("Enter the due date (dd/mm/yyyy): ")
                        task_prio = input("Enter the priority level (LOW, MEDIUM, HIGH): ")
                        task_desc = input("Enter the task description: ")

                        task_list.add_task(task_owner, task_name, task_date, task_prio, task_desc)
                        logging.info(f"New task \"{task_name}\" has been added to \"{task_list.get_task_list_name}\" task list.") 
                        break

                    elif choice_1 == "2":
                        task_no = int(input("Enter the task number you want to remove: "))
                        if type(task_no)==int and 1 <= task_no <= len(task_list.get_tasks()):
                            task_list.remove_task(task_no)
                            logging.info(f"Task \"{task_name}\" has been removed \"{task_list.get_task_list_name}\" task list.")
                        else:
                            print("Invalid task number.")

                        break

                    elif choice_1 == "3":
                        break

                    else:
                        print("Invalid choice. Please enter 1, 2, or 3.")
            
            elif choice == "2":
                task_id = int(input("Enter the task number you want to display: "))
                if type(task_id)==int and 1 <= task_id <= len(task_list.get_tasks()):
                    task_list.display_task_description(task_id-1)
                else:
                    print("Invalid task number.")

                pass

            elif choice == "3":
                while True:
                    print("\n1. Update Task Assignee")
                    print("2. Update Task Name")
                    print("3. Update Task Due Date")
                    print("4. Update Task Priority")
                    print("5. Update Task Description")
                    print("6. Update Task Status")
                    print("7. Go back")

                    choice_3 = input("Enter your choice (1/2/3/4/5/6/7): ")

                    if choice_3 == "1":
                        task_no = int(input("Enter the task number you want to update: "))
                        new_task_assignee = input("Enter the new task assignee: ")
                        
                        if type(task_no)==int and 1 <= task_no <= len(task_list.get_tasks()):
                            task_list.update_task_assignee(task_no, new_task_assignee)
                            logging.info(f"Task \"{task_no}\" has been new assignee \"{new_task_assignee}\".")
                        else:
                            print("Invalid task number.")
                        
                        break

                    elif choice_3 == "2":
                        task_no = int(input("Enter the task number you want to update: "))
                        new_task_name = input("Enter the new task name: ")
                        
                        if type(task_no)==int and 1 <= task_no <= len(task_list.get_tasks()):
                            task_list.update_task_name(task_no, new_task_name)
                            logging.info(f"Task \"{task_no}\" has a new name \"{new_task_name}\".")
                        else:
                            print("Invalid task number.")
                        
                        break

                    elif choice_3 == "3":
                        task_no = int(input("Enter the task number you want to update: "))
                        new_task_due_date = input("Enter the new task due date (dd/mm/yyyy): ")
                        
                        if type(task_no)==int and 1 <= task_no <= len(task_list.get_tasks()):
                            task_list.update_task_due_date(task_no, new_task_due_date)
                            logging.info(f"Task \"{task_no}\" has a new due date \"{new_task_due_date}\".")
                        else:
                            print("Invalid task number.")
                        
                        break

                    elif choice_3 == "4":
                        task_no = int(input("Enter the task number you want to update: "))
                        new_task_priority = input("Enter the new task priority level (LOW, MEDIUM, HIGH): ")
                        logging.info(f"Task \"{task_no}\" has a new priority \"{new_task_priority}\".")
                        
                        if type(task_no)==int and 1 <= task_no <= len(task_list.get_tasks()):
                            task_list.update_task_priority(task_no, new_task_priority)

                        else:
                            print("Invalid task number.")
                        
                        break

                    elif choice_3 == "5":
                        task_no = int(input("Enter the task number you want to update: "))
                        new_task_description = input("Enter the new task description: ")
                        
                        if type(task_no)==int and 1 <= task_no <= len(task_list.get_tasks()):
                            task_list.update_task_description(task_no, new_task_description)
                            logging.info(f"Task \"{task_no}\" has a new description \"{new_task_description}\".")
                        else:
                            print("Invalid task number.")
                        
                        break

                    elif choice_3 == "6":
                        task_no = int(input("Enter the task number you want to update: "))
                        new_task_status = input("Enter the new task status (PENDING, IN_PROGRESS, COMPLETED): ")
                        
                        if type(task_no)==int and 1 <= task_no <= len(task_list.get_tasks()):
                            task_list.update_task_status(task_no, new_task_status)
                            logging.info(f"Task \"{task_no}\" has a new status \"{new_task_status}\".")
                        else:
                            print("Invalid task number.")
                        
                        break

                    elif choice_3 == "7":
                        break

                    else:
                        print("Invalid choice. Please enter 1, 2, 3, 4, 5, 6 or 7.")

            elif choice == "4":
                while True:
                    print("\n1. Update Task List Name")
                    print("2. Update Task List Owner(s)")
                    print("3. Update Task List Tag(s)")
                    print("4. Update Task List Description")
                    print("5. Go back")

                    choice_4 = input("Enter your choice (1/2/3/4/5): ")

                    if choice_4 == "1":
                        new_task_list_name = input("Enter the new task list name: ")
                        task_list.update_task_list_name(new_task_list_name)
                        logging.info(f"Task list {task_list.get_task_list_name} has a new name \"{new_task_list.get_task_list_name}\".")

                        break

                    elif choice_4 == "2":

                        while True:
                            print("\n1. Add Task List Owner")
                            print("2. Remove Task List Owner")
                            print("3. Go back")

                            choice_4_1 = input("Enter your choice (1/2/3): ")

                            if choice_4_1 == "1":
                                add_owner_name = input("Enter the task list owner to be added: ")
                                task_list.manage_owners(add_owner_name, "Add")
                                logging.info(f"Task list {task_list.get_task_list_name} has a new owner \"{add_owner_name}\".")
                                break

                            elif choice_4_1 == "2":
                                remove_owner_name = input("Enter the task list owner to be removed: ")
                                task_list.manage_owners(remove_owner_name, "Remove")
                                logging.info(f"Owner \"{remove_owner_name}\" is removed from Task list {task_list.get_task_list_name}.")
                                break

                            elif choice_4_1 == "3":
                                break

                            else:
                                print("Invalid choice. Please enter 1, 2, or 3.")

                        break

                    elif choice_4 == "3":

                        while True:
                            print("\n1. Add Task List Tag")
                            print("2. Remove Task List Tag")
                            print("3. Go back")

                            choice_3_2 = input("Enter your choice (1/2/3): ")

                            if choice_3_2 == "1":
                                add_tag = input("Enter the task list tag to be added: ")
                                task_list.manage_tags(add_tag, "Add")
                                logging.info(f"Task list {task_list.get_task_list_name} has a new tag \"{add_tag}\".")
                                break

                            elif choice_3_2 == "2":
                                remove_tag = input("Enter the task list tag to be removed: ")
                                task_list.manage_tags(remove_tag, "Remove")
                                logging.info(f"Tag \"{add_tag}\" is removed from Task list {task_list.get_task_list_name}.")
                                break

                            elif choice_3_2 == "3":
                                break

                            else:
                                print("Invalid choice. Please enter 1, 2, or 3.")

                        break

                    elif choice_4 == "4":
                        new_task_list_description = input("Enter the new task list description: ")
                        task_list.update_task_list_description(new_task_list_description)
                        logging.info(f"Task list {task_list.get_task_list_name} has a new description \"{new_task_list_description}\".")

                        break
                    
                    elif choice_4 == "5":
                        break

                    else:
                        print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")
                
            elif choice == "5":

                while True:
                    choice_5 = input("Do you want to save the list (Y/N)? ")

                    if choice_5 == "Y":
                        with open(f"{task_list.get_task_list_name()}.pkl", "wb") as pkl_file:
                            pickle.dump(task_list, pkl_file)
                        print("Modifications saved")
                        logging.info(f"Task list {task_list.get_task_list_name} has a been saved.")
                        break

                    elif choice_5 == "N":
                        print("Modifications not saved")
                        logging.info(f"Task list {task_list.get_task_list_name} has not been saved.")
                        break

                    else:
                        print("Invalid choice. Please enter Y or N.")

                break

            else:
                print("\nInvalid choice. Please enter 1, 2, 3, 4, or 5.")


if __name__ == "__main__":
    main()