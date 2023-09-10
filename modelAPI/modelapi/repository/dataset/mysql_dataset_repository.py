from dataset_repository import DatasetRepositry
from pymysql.connections import Connection
from pymysql.cursors import Cursor

class MySQLDatasetRepository(DatasetRepositry):
    __SCHEMA = "model_db"
    __TABLE = "dataset"
    __connection: Connection
    __cursor: Cursor

    def __init__(self, connection: Connection):
        self.__connection = connection
        self.__cursor = self.__connection.cursor()

    def insert(self, dto: DataDTO)->int:
        raise NotImplemented

    def insert_list(self, dtos :DatasetDTO)->list[int]:
        raise NotImplemented

    def get(id: int)->DataDTO:
        raise NotImplemented

    def get_list(id: list[int])->DatasetDTO:
        raise NotImplemented

    def get_all()->DatasetDTO:
        raise NotImplemented

    def get_all_with_label(label: str)->DatasetDTO:
        raise NotImplemented

    def delete(id: int)->DataDTO:
        raise NotImplemented

    def delete_list(id: list[int])->DatasetDTO:
        raise NotImplemented

    def update(id: int, dto: DataDTO)->DataDTO:
        raise NotImplemented

    def update_list(id: list[int], dto: DatasetDTO)->DatasetDTO:
        raise NotImplemented