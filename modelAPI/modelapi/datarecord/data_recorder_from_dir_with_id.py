from datarecord.data_recorder import DataRecorder
from dataprovide.data_provider_by_id_from_dir import DataProviderByIDFromDir
from dataprovide.exif_provider_by_id_from_dir import EXIFProviderByIDFromDir
from labelclassify.label_classifier_from_boundary import *
from dataprovide.image_info_extractor import ImageInfoExtractor
from dateprovide.data_provider import data_provider

from dataprovide.datetime_provider_by_EXIF_from_dir import DateTimeProviderByEXIFfromDir


class DataRecorderFromDirWithID(DataRecorder):
    def __init__(self, id: int, datetime_provider):
        self.__id = id
        self.__image_location = DataProviderByIDFromDir(self.__id, "Image").sub_location()
        self.__label = None
        self.__get_label()
        self.__datetime_provider = datetime_provider
        self.__datetime_provider = None

    def __get_label(self):

        photoed_time=self.__datetime_provider.get()

        if photoed_time == None: # 촬영 시간 없음
            self.__label = "Unknown"
            return

        try:
            label_classifier = LabelClassifierFromBoundary.fromStringFormat(photoed_time, TIME_BOUNDARY_DIC)
            self.__label = label_classifier.label()
        except ValueError: # String format to Datetime 변환 실패
            self.__label = "Unknown"

    def id(self):
        return self.__id

    def image_location(self):
        return self.__image_location
    
    def label(self):
        return self.__label


def main():
    id = int(input("Image num: "))
    datetime_provider = DateTimeProviderByEXIFfromDir(id)
    #datetime_provider = DateTimeProviderByLocationFromDir("Phototimestamp_ds\\test\\20230928_123456.jpg")
    dr = DataRecorderFromDirWithID(id, datetime_provider)
    

    print("ID : {}".format(id))
    print("Image Location: {}".format(dr.image_location()))
    print("Label : {}".format(dr.label()))

if __name__ == "__main__":
    main()