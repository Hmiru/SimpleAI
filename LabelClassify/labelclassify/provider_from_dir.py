# 파일명: EXIFProviderFromDir.py
# 목적: EXIF를 파일로부터 불러오는 EXIFProvider의 구현체 
# 메모 사항:
#   - 서버 내에서 이미지와 EXIF 디렉토리 구조
#   - 총 100만 장의 파일이 있음
#   - 10,000장씩 100개의 디렉토리로 나누어짐 (0~99)
#   - 각 파일 명은 번호임

from provider import Provider
import yaml
import abc

class ProviderFromDir(Provider):
    def __init__(self, image_num: int, type: str):
        super().__init__(image_num)
        self.type = type
        self._dir_location = ""
        self._file_location = ""
        self.__load__File_name()

    def file_location(self) -> str:
        return self._file_location
        
    def __load__File_name(self):
        self.__load_dir_location()
        self.__make_file_location()
        pass

    def __load_dir_location(self):
        with open('propertise.yaml', "r") as f:
            propertise = yaml.full_load(f)
            self._dir_location = propertise['location'][self.type]

    def __make_file_location(self):
        sub_dir = str(self._image_num // 10000)
        self._file_location = self._dir_location + "/" +\
                                     sub_dir + "/" +\
                                     str(self._image_num) + ".txt" 

def main():
    test_exif = ProviderFromDir(22222, "EXIF")
    print(test_exif.file_location())
    test_image = ProviderFromDir(11112, "Image")
    print(test_image.file_location())
    
if __name__ == '__main__':
    main()