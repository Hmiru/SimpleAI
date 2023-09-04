import abc
import sys
from datetime import datetime

class LabelClassifier:
    def __init__(self, datetime: datetime):
        self.__datetime = datetime

    def datetime(self):
        return self.__datetime
    
    @staticmethod
    @abc.abstractstaticmethod
    def fromStringFormat(strf: str):
        raise NotImplemented
    
    @abc.abstractmethod
    def label(self) -> str:
        raise NotImplemented