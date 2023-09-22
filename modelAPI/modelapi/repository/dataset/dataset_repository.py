from repository.dataset.data_dto import DataDTO, DatasetDTO
import abc

class DatasetRepositry:
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
    def count(self) -> int:
        raise NotImplemented

    @abc.abstractmethod
    def count_label(self, label: str) -> int:
        raise NotImplemented

    @abc.abstractmethod
    def commit(self):
        raise NotImplemented

    