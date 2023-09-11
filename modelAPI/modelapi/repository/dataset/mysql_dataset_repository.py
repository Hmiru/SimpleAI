import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from repository.dataset.dataset_repository import DatasetRepositry
from repository.dataset.data_dto import DataDTO, DatasetDTO
from pymysql.connections import Connection
from pymysql.cursors import Cursor

class MySQLDatasetRepository(DatasetRepositry):
    __SCHEMA = "model_db"
    __TABLE = "dataset"
    __connection: Connection
    __cursor: Cursor

    __INSERT_QUERY = "INSERT INTO " + __TABLE + " (label, image_location) VALUES (%s, %s)"
    __SELECT_QUERY_BASE = "SELECT label, image_location FROM " +__TABLE
    __DELETE_QUERY_BASE = "DELETE FROM " + __TABLE
    __UPDATE_QUERY = "UPDATE " + __TABLE + " SET label = %s, image_location = %s WHERE id = %s"
    def __init__(self, connection: Connection):
        self.__connection = connection
        self.__cursor = self.__connection.cursor()

    def insert(self, dto: DataDTO)->int:
        self.__cursor.execute(self.__INSERT_QUERY, dto.values())

    def insert_list(self, dtos :DatasetDTO)->list[int]:
        values = self.__packing_values(dtos)
        self.__cursor.executemany(self.__INSERT_QUERY, values)

    @staticmethod
    def __packing_values(dtos: DatasetDTO)->list[tuple[str, str]]:
        values = []
        for dto in dtos:
            values.append(dto.values())
        return values


    def get(self, id: int)->DataDTO:
        query = self.__SELECT_QUERY_BASE + " WHERE id=%s"
        self.__cursor.execute(query, id)
        result = self.__cursor.fetchone()
        dto = self.__packing_dto(result)

        return dto

    @staticmethod
    def __packing_dto(result :tuple)->DataDTO:
        if len(result) >= 1:
            return DataDTO(result[0], result[1])

    def get_list(self, ids: list[int])->DatasetDTO:
        query = self.__SELECT_QUERY_BASE + " WHERE id IN %s"
        id_tuple: str = self.__list_to_tuple(ids)

        self.__cursor.execute(query % id_tuple)
        result = self.__cursor.fetchall()

        dtos = self.__packing_dtos(result)
        
        return dtos

    @staticmethod
    def __list_to_tuple(ids: list[int]) -> str:
        return tuple(ids).__str__()

    @staticmethod
    def __packing_dtos(results :tuple[tuple])->DatasetDTO:
        dtos: DatasetDTO = []
        for result in results:
            dtos.append(MySQLDatasetRepository.__packing_dto(result))
        
        return dtos

    def get_all(self)->DatasetDTO:
        self.__cursor.execute(self.__SELECT_QUERY_BASE)
        result = self.__cursor.fetchall()
        dtos = self.__packing_dtos(result)

        return dtos

    def get_all_with_label(self, label: str)->DatasetDTO:
        query = self.__SELECT_QUERY_BASE + ' WHERE label = "%s"'
        self.__cursor.execute(query % label)
        result = self.__cursor.fetchall()
        dto = self.__packing_dtos(result)

        return dto

    def delete(self, id: int)->DataDTO:
        dto = self.get(id)

        query = self.__DELETE_QUERY_BASE  + " WHERE id = %s"
        self.__cursor.execute(query, id)

        return dto

    def delete_list(self, ids: list[int])->DatasetDTO:
        dtos = self.get_list(ids)

        id_tuple = self.__list_to_tuple(ids)
        query = self.__DELETE_QUERY_BASE + " WHERE id IN %s"

        self.__cursor.execute(query % id_tuple)

        return dtos

    def update(self, id: int, dto: DataDTO)->DataDTO:
        dto_before = self.get(id)

        self.__cursor.execute(self.__UPDATE_QUERY, (dto.label, dto.image_location, id))

        return dto_before
    
    def commit(self):
        self.__connection.commit()