from datarecord.data_recorder import DataRecorder
from dataprovide.data_provider_by_id_from_dir import DataProviderByIDFromDir
from dataprovide.exif_provider_by_id_from_dir import EXIFProviderByIDFromDir
from labelclassify.label_classifier_from_boundary import *

class DataRecorderFromDirWithID(DataRecorder):
    def __init__(self, id: int):
        self.__id = id
        self.__image_location = DataProviderByIDFromDir(self.__id, "Image").file_location()
        self.__label = None
        self.__get_label()

    def __get_label(self):
        exif = EXIFProviderByIDFromDir(self.__id).get()
        photoed_time = exif.get("Date and Time (Original)")
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
    dr = DataRecorderFromDirWithID(id)
    print("ID : {}".format(id))
    print("Image Location: {}".format(dr.image_location()))
    print("Label : {}".format(dr.label()))

if __name__ == "__main__":
    main()