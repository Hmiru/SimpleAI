from datetime import time

class TimeRange:
    def __init__(self, start: time, end: time):
        self.__start = start
        self.__end = end

    def start(self):
        return self.__start

    def end(self):
        return self.__end

TimeBoundary = {
    "Morning": TimeRange,
    "Afternoon": TimeRange,
    "Night": TimeRange
}

TimeBoundaryDic= {
    "Spring": TimeBoundary,
    "Summer": TimeBoundary,
    "Autumn": TimeBoundary,
    "Winter": TimeBoundary
}