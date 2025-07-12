"""!
"""
import logic
import json_reader as jr
from pathlib import Path

todo_list_file_path = Path("")

operations_dict = {
        1: logic.add_task,
        2: logic.remove_task,
        3: logic.set_status_done,
        4: logic.set_status_not_done,
        5: logic.show_list
    }
def main():
    while True:
        logic.user_interface_message()
        operation = input("Enter an option: ")
        task_list = jr.read_task_file(todo_list_file_path)
        if operation in [1,2,3,4]:
            name = input("Enter task name: ")
            operations_dict[operation](name, task_list)
        elif operation == 5:
            operations_dict[operation](task_list)
        else:
            jr.write_task_file(todo_list_file_path)
            break
