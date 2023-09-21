from pymysql.connections import Connection
from pymysql import connect
from propertise.propertise_loader import PropertiseLoader

class DatabaseManager:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            return super().__new__(cls, *args, **kwargs)
        else:
            return cls.__instance
    
    def __init__(self):
        self.__db: Connection
        self.__connect()

    def __del__(self):
        self.__close()

    def __connect(self):
        propertise = PropertiseLoader().get().get("repository")
        self.__db = connect(host = propertise["host"],
                            user = propertise["user"], 
                            password = propertise["password"],
                            database = propertise["database"])
    def __close(self):
        self.__db.close()

    def get(self):
        return self.__db
