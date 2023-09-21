import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from datarecord.directory_recorder_from_dir_with_id import DirectoryRecorderFromDirWithID

for i in range(1,25001):
    DirectoryRecorderFromDirWithID(i).record()