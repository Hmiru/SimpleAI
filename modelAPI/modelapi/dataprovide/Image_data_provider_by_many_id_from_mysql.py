from dataprovide.data_provder_by_many_id_from_mysql import DataProviderByManyIDFromMySQL
from dataprovide.image_data_dto import ImageDataDTO, ImageDatasetDTO
from repository.dataset.data_dto import DataDTO
from dataprovide.image_provider_by_location import ImageProviderByLocation
from PIL import Image
from pymysql.connections import Connection

class ImageDataProviderByManyIdFromMySQL(DataProviderByManyIDFromMySQL):
    def __init__(self, ids: list[int], db: Connection):
        super().__init__(ids, db)
        self.__image_dataset: ImageDatasetDTO = []
        self.__make_image_dataset()

    def __make_image_dataset(self):
        dataset = self.loaded_dataset()
        for data in dataset:
            image_dto: ImageDataDTO = self.__make_image_dto(data)
            self.__image_dataset.append(image_dto)

    @staticmethod
    def __make_image_dto(data_dto: DataDTO) -> ImageDataDTO:
        image_provider = ImageProviderByLocation(data_dto.image_location)
        img: Image = image_provider.get()

        return ImageDataDTO(img, data_dto.label)

    def get(self) -> ImageDatasetDTO:
        return self.__image_dataset
        