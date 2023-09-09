from labelclassify.label_classifier import LabelClassifier
from labelclassify.time_boundary import *
from datetime import datetime
from typing import Final

TIME_BOUNDARY_DIC : Final[TimeBoundaryDic] = {
    "Spring": {
        "Morning": TimeRange(time(5,34), time(12,33)),
        "Afternoon": TimeRange(time(12,33), time(19,35)),
        "Night": TimeRange(time(19,35), time(5,34))
    },
    "Summer": {
        "Morning": TimeRange(time(4, 58), time(12,34)),
        "Afternoon": TimeRange(time(12,34), time(20,9)),
        "Night": TimeRange(time(20,9), time(4, 58))
    },
    "Autumn": {
        "Morning": TimeRange(time(6,18), time(12,23)),
        "Afternoon": TimeRange(time(12,23), time(18,26)),
        "Night": TimeRange(time(18,26), time(6,18))
    },
    "Winter": {
        "Morning": TimeRange(time(7,5), time(12,37)),
        "Afternoon": TimeRange(time(12,37), time(18,10)),
        "Night": TimeRange(time(18,10), time(7,5))
    },
}

def is_between( t: time, start: time, end: time) -> bool:
    return t > start and t <= end

class LabelClassifierFromBoundary(LabelClassifier):
    def __init__(self, datetime: datetime, time_boundary_dic:TimeBoundaryDic):
        super().__init__(datetime)
        self.__label = ""
        self.__time_boundary_dic = time_boundary_dic
        self.__season = ""
        self.__classify_label()

    def __classify_label(self):
        self.__classify_season()
        self.__classify_time()

    def __classify_season(self):
        photoed_month = self.datetime().month
        if photoed_month in (3,4,5):
            self.__season = "Spring"
        elif photoed_month in (6,7,8):
            self.__season = "Summer"
        elif photoed_month in (9,10,11):
            self.__season = "Autumn"
        elif photoed_month in (1,2,12):
            self.__season = "Winter"
    
    def __classify_time(self):
        if self.__in_range_of_when("Morning"):
            self.__label = self.__season + "_" + "Morning"
        elif self.__in_range_of_when("Afternoon"):
            self.__label = self.__season + "_" + "Afternoon"
        elif self.__in_range_of_when("Night"):
            self.__label = self.__season + "_" + "Night"

    def __in_range_of_when(self, time_range: str):
        photoed_time = time(self.datetime().hour, self.datetime().minute, self.datetime().second)
        boundary = self.__time_boundary_dic[self.__season][time_range]
        return is_between(photoed_time, boundary.start(), boundary.end())

    @staticmethod
    def fromStringFormat(strf: str, time_boundary_dic: TimeBoundaryDic):
        try:
            time = datetime.strptime(strf, "%Y:%m:%d %H:%M:%S")
            return LabelClassifierFromBoundary(time, time_boundary_dic)
        except ValueError as e:
            print(e, file=sys.stderr)

    def label(self)->str:
        return self.__label

def main():
    dt = datetime.today()
    lc = LabelClassifierFromBoundary(dt, TIME_BOUNDARY_DIC)

    print(dt)
    print(lc.label())


if __name__ == "__main__":
    main()