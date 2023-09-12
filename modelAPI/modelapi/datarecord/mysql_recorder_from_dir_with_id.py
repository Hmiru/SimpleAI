from datarecord.data_recorder_from_dir_with_id import DataRecorderFromDirWithID
from repository.dataset.mysql_dataset_repository import MySQLDatasetRepository, DataDTO
from pymysql.connections import Connection

class MySQLRecorderFromDirWithID(DataRecorderFromDirWithID):
    __repository: MySQLDatasetRepository
    __db: Connection
    __dto: DataDTO
    
    def __init__(self, id: int, db: Connection):
        super().__init__(id)
        self.__db = db
        self.__repository = MySQLDatasetRepository(db)
        self.__dto = DataDTO(self.label(), self.image_location())

    def record(self):
        self.__repository.insert(self.__dto)