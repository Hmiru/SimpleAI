from dataprovide.data_provider import DataProvider
import abc

class DataProviderByID(DataProvider):
    def __init__(self, image_num: int):
        self.__image_num = image_num

    def image_num(self) -> int:
        return self.__image_num