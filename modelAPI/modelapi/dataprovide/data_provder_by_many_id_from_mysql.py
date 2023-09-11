import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from dataprovide.data_provider_by_many_id import DataProviderByManyID
from pysql.connections import Connection
from repository.dataset.mysql_dataset_repository import MySQLDatasetRepository
from repository.dataset.data_dto import DataDTO, DatasetDTO
from copy import deepcopy

class DataProviderByManyIDFromMySQL(DataProviderByManyID):
    __repo: MySQLDatasetRepository
    __loaded_dataset: DatasetDTO
    
    def __init__(self, ids: list[int], db: Connection):
        super().__init__(ids)
        self.__repo = MySQLDatasetRepository(db)
        self.__loaded_dataset = self.__repo.get_list(ids)

    def loaded_dataset(self):
        return deepcopy(self.__loaded_dataset)

    @staticmethod
    def N_data_from_ID(int: id, n: id, db: Connection):
        return DataProviderByManyIDFromMySQL(list(range(id, id + n)), db)