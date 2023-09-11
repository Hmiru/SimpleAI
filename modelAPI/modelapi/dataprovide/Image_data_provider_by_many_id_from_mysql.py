import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from dataprovide.data_provder_by_many_id_from_mysql import DataProviderByManyIDFromMySQL
from dataprovide.image_data_dto import ImageDataDTO, ImageDatasetDTO

class ImageDataProviderByManyIdFromMySQL(DataProviderByManyIDFromMySQL):
    __image_dataset: ImageDatasetDTO
    
    def __init__(self, ids: list[int], db: Connection):
        super().__init__(ids, db)
        self.__make_image_dataset()

    def __make_image_dataset(self):
        dataset = self.loaded_dataset()
        for data in dataset:
            pass # data -> Imagedata 변환 로직

    def get(self) -> ImageDatasetDTO:
        return self.__image_dataset
        