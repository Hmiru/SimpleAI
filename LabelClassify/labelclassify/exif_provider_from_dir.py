from provider_from_dir import ProviderFromDir

class EXIFProviderFromDir(ProviderFromDir):
    def __init__(self, image_num: int):
        super().__init__(image_num, "EXIF")
        self.__file_content_arr = []
        self.__EXIF = {}
        self.__make_EXIF_dic()

    def __make_EXIF_dic(self):
        self.__read_file()
        self.__parse_to_dic()

    def __read_file(self):
        with open(self._file_location, "r") as f:
            self.__file_content_arr = f.readlines()

    def __parse_to_dic(self):
        for i in range(0, len(self.__file_content_arr), 2):
            key = self.__file_content_arr[i]
            value = self.__file_content_arr[i+1]
            key = key.strip("-").strip("\n")
            value = value.strip("\n")

            self.__EXIF[key] = value

    def get(self):
        return self.__EXIF


def main():
    test = EXIFProviderFromDir(2)
    print(test.get())

if __name__ == "__main__":
    main()