from dataprovide.data_provider import DataProvider

class DataProviderByManyID(DataProvider):   
    def __init__(self, ids: list[int]):
        self.__id_list: list[int] = ids

    def id(self) -> tuple[int]:
        return tuple(self.__id_list)