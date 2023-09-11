import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from repository.dataset.data_dto import DataDTO, DatasetDTO
import abc

class DatasetRepositry:
    def __init__(self):
        pass

    @abc.abstractmethod
    def insert(self, dto: DataDTO)->int:
        raise NotImplemented

    @abc.abstractmethod
    def insert_list(self, dtos :DatasetDTO)->list[int]:
        raise NotImplemented

    @abc.abstractmethod
    def get(self, id: int)->DataDTO:
        raise NotImplemented

    @abc.abstractmethod
    def get_list(self, id: list[int])->DatasetDTO:
        raise NotImplemented

    @abc.abstractmethod
    def get_all(self, )->DatasetDTO:
        raise NotImplemented

    @abc.abstractmethod
    def get_all_with_label(self, label: str)->DatasetDTO:
        raise NotImplemented

    @abc.abstractmethod
    def delete(self, id: int)->DataDTO:
        raise NotImplemented

    @abc.abstractmethod
    def delete_list(self, id: list[int])->DatasetDTO:
        raise NotImplemented

    @abc.abstractmethod
    def update(self, id: int, dto: DataDTO)->DataDTO:
        raise NotImplemented

    @abc.abstractmethod
    def commit(self):
        raise NotImplemented

    