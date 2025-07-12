"""!
JSON file writing and reading. This should be substituted with a database
interface in the future
"""

import json
#import logger
from pathlib import Path

def read_task_file(filepath:Path):
    try:
        with open(filepath, 'r') as file:
            task_list = json.load(file)
            #logger.Log(1,2000, f"Succesfully read task list")
            return task_list
    except FileNotFoundError as err:
        #logger.Log(0,1000, f"Task list file not found: {err}")
        raise
    except json.JSONDecodeError as err:
        #logger.Log(0,1001, f"Task list file not correctly formatted: {err}")
        raise

def write_task_file(filepath:Path, task_list:dict):
    try:
        with open(filepath, 'w') as file:
            json.dump(task_list, filepath)
            #logger.Log(1, 2001, f"Successfully saved task list")
    except IOError as err:
        #logger.Log(0, 1002, f"Error while writing task list: {err}")
        raise
    except TypeError as err:
        #logger.Log(0, 1003, f"Unable to serialize task list: {err}")
        raise
