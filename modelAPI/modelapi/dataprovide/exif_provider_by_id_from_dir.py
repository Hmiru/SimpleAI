from dataprovide.data_provider_by_id_from_dir import DataProviderByIDFromDir
import sys
import chardet

class EXIFProviderByIDFromDir(DataProviderByIDFromDir):
    def __init__(self, image_num: int):
        super().__init__(image_num, "EXIF")
        self.__file_content_arr = []
        self.__EXIF = {}
        self.__make_EXIF_dic()

    def __make_EXIF_dic(self):
        self.__read_file()
        self.__parse_to_dic()

    def __read_file(self):
        try:
            with open(self.file_location(), "r", encoding="iso-8859-1") as f:
                self.__file_content_arr = f.readlines()
        except FileNotFoundError as e:
            print(e, file=sys.stderr)

    def __parse_to_dic(self):
        for i in range(0, len(self.__file_content_arr), 2):
            key = self.__file_content_arr[i]
            value = self.__file_content_arr[i+1]
            key = key.strip("-").strip("\n")
            value = value.strip("\n")

            self.__EXIF[key] = value

    def get_exif(self):
        return self.__EXIF


def main():
    test = EXIFProviderFromDir(2)
    print(test.get())

if __name__ == "__main__":
    main()