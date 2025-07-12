"""!

"""
#import logger
import tableformatter as tf
import json_reader as ir
#TODO Add urgency to tasks


def user_interface_message():
    print("\n<-----Made in Python----->")
    print("------By Jorge------")
    print("\nOptions")
    print("1-Add task")
    print("2-Remove task")
    print("3-Mark a task as done")
    print("4-Mark a task as not done")
    print("5-Show to do list")
    print("0-Exit\n")

def add_task(name:str, task_list:dict):
    """
    brief: Adds a task to de to-do list
    name: Name of the task
    task_list: Dictionary with tasks
    """
    if name in task_list:
        print(f"{name} already exists. Select another option\n")
    else:
        task_list[name] = False
        #logger.Log(1,2100, f"The task {name} has been added to the task list")

def remove_task(name:str, task_list:dict):
    """
    brief: Removes a task from the to-do list
    name: Name of the task
    task_list: Dictionary with tasks
    """
    if name in task_list:
        task_status = task_list.pop(name)
        if task_status:
            task_status = 'incomplete'
        else:
            task_status = 'completed'
        print(f"The task {name} was removed. Its status was {task_status}")
        #logger.Log(1, 2101, f"The task {name} has been deleted. Its status was {task_status}")
    else:
        print(f"{name} does not exist. Select another option\n")

def set_status_done(name:str,task_list:dict):
    """
    brief: Change task status to done
    name: Name of the task
    task_list: Dictionary with tasks
    """
    if name in task_list:
        task_list[name] = True
        print(f"The task {name} was removed. Its status was {task_status}")
        #logger.Log(1, 2102, f"The status of the task {name} was set to done.")
    else:
        print(f"{name} does not exist. Select another option\n")

def set_status_not_done(name:str, task_list:dict):
    """
    brief: Change task status to not done
    name: Name of the task
    task_list: Dictionary with tasks
    """
    if name in task_list:
        task_list[name] = False
        print(f"The task {name} was removed. Its status was {task_status}")
        #logger.Log(1, 2103, f"The status of the task {name} was set to done.")
    else:
        print(f"{name} does not exist. Select another option\n")

def show_list(task_list):
    """
    brief: Shows to do list
    task_list: Dictionary with tasks
    """
    task_table = []
    for task in task_list:
        if task_list[task]:
            status = u"\u2705"
        else:
            status = u"\u274C"
        task_table.append((task, status))
    print(tf.generate_table(task_table))

data = {"comprar": False, "limpiar": True, "ver perdidos": True}
    
        
    
    
    
