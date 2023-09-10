from repository.dataset.dataset_dto import DataDTO, DatasetDTO
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
    def get(id: int)->DataDTO:
        raise NotImplemented

    @abc.abstractmethod
    def get_list(id: list[int])->DatasetDTO:
        raise NotImplemented

    @abc.abstractmethod
    def get_all()->DatasetDTO:
        raise NotImplemented

    @abc.abstractmethod
    def get_all_with_label(label: str)->DatasetDTO:
        raise NotImplemented

    @abc.abstractmethod
    def delete(id: int)->DataDTO:
        raise NotImplemented

    @abc.abstractmethod
    def delete_list(id: list[int])->DatasetDTO:
        raise NotImplemented

    @abc.abstractmethod
    def update(id: int, dto: DataDTO)->DataDTO:
        raise NotImplemented

    @abc.abstractmethod
    def update_list(id: list[int], dto: DatasetDTO)->DatasetDTO:
        raise NotImplemented

    