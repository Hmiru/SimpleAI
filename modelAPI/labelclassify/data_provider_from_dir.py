from labelclassify.data_provider import DataProvider
import yaml
import abc
import os.path

class DataProviderFromDir(DataProvider):
    def __init__(self, image_num: int, type: str):
        super().__init__(image_num)
        self.__type = type
        self.__dir_location = ""
        self.__file_location = ""
        self.__file_format = ""
        self.__set_file_format()
        self.__load__File_name()

    def file_location(self) -> str:
        return self._file_location

    def __set_file_format(self):
        if self.__type == "EXIF":
            self.__file_format = ".txt"
        elif self.__type == "Image":
            self.__file_format = ".jpg"
        else:
            self.__file_format = ""
        
    def __load__File_name(self):
        self.__load_dir_location()
        self.__make_file_location()
        pass

    def __load_dir_location(self):
        with open(os.path.dirname(__file__) + '/../propertise.yaml') as f:
            propertise = yaml.full_load(f)
            self._dir_location = propertise['location'][self.__type]

    def __make_file_location(self):
        sub_dir = str(self._image_num // 10000)
        self._file_location = self._dir_location + "/" +\
                                     sub_dir + "/" +\
                                     str(self._image_num) + self.__file_format 

def main():
    test_exif = ProviderFromDir(22222, "EXIF")
    print(test_exif.file_location())
    test_image = ProviderFromDir(11112, "Image")
    print(test_image.file_location())
    
if __name__ == '__main__':
    main()