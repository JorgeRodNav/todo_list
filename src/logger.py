"""!
"""
from pathlib import Path
import os


level_dict = {
            0: "Error",
            1: "Success",
            2: "Warning"
        }

id_dict = {}

log_file_path = Path() #TODO Add path for log file

class Log:
    """!
    Class for logging.
    log_level can be: 0-Error, 1-Success, 2-Warning
    log_id can be: TBD
    log_msg: String with log message
    """
    def __init__(self, log_level:int, log_id:int, log_msg:str):
        self.level = log_level
        self.id = log_id
        self.msg = log_msg
        self.log_file_path = log_file_path
        self.__record__()

    def __record__(self):
        try:
            message = f"\n{level_dict[self.level]: <{id_dict[log_id]}>{self.msg}}"
            with open(self.log_file_path, 'a') as file:
                file.write(message)

