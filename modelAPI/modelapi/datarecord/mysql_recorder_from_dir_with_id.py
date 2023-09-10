import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from datarecord.data_recorder_from_dir_with_id import DataRecorderFromDirWithID

class MySQLRecorderFromDirWithID(DataRecorderFromDirWithID):
    def __init__(self, id: int):
        super().__init__(id)