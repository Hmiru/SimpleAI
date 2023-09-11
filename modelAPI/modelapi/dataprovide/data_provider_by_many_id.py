import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from dataprovide.data_provider import DataProvider

class DataProviderByManyID(DataProvider):
    __id_list : list[int]
    
    def __init__(self, ids: list[int]):
        self.__id_list = ids

    def id(self) -> tuple[int]:
        return tuple(self.__id_list)