from dataprovide.data_provider import DataProvider
from propertise.propertise_loader import PropertiseLoader
from PIL import Image, UnidentifiedImageError

class ImageProviderByLocation(DataProvider):
    
    def __init__(self, relative_location: str):
        self.__relative_location: str = relative_location
        self.__image : Image
        self.__absolute_location: str
        
        self.__make_abs_location()
        self.__load_image()

    def __make_abs_location(self):
        propertise = PropertiseLoader().get()
        base_location = propertise['location']['Image']
        self.__absolute_location = base_location + "/" +\
                                    self.__relative_location

    def __load_image(self):
        self.__image = Image.open(self.__absolute_location)

    def get(self)->Image:
        return self.__image
