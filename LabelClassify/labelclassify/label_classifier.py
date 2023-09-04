import abc
import sys
from datetime import datetime

class LabelClassifier:
    def __init__(self, datetime: datetime):
        pass
    
    @staticmethod
    @abc.abstractstaticmethod
    def fromStringFormat(strf: str):
        raise NotImplemented
    
    @abc.abstractmethod
    def label(self) -> str:
        raise NotImplemented