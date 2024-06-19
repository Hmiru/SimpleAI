import os
from datetime import datetime
import shutil
from PIL import Image
from PIL.ExifTags import TAGS


class datasetIntoSmallDir:

    def __init__(self,root_dir):
        self.root_dir = root_dir

    @staticmethod
    def day_time_classify(dt):
        season_times = {
            "Spring": [(5, 34), (12, 33), (12, 34), (19, 35)],
            "Summer": [(4, 58), (12, 34), (12, 34), (20, 9)],
            "Autumn": [(6, 18), (12, 23), (12, 23), (18, 26)],
            "Winter": [(7, 5), (12, 37), (12, 37), (18, 10)]
        }
        if dt.month in [3, 4, 5]:
            season = "Spring"
        elif dt.month in [6, 7, 8]:
            season = "Summer"
        elif dt.month in [9, 10, 11]:
            season = "Autumn"
        else:
            season = "Winter"
        morning_start, morning_end, afternoon_start, afternoon_end = season_times[season]

        if (dt.hour == morning_start[0] and dt.minute >= morning_start[1]) or \
                (morning_start[0] < dt.hour < morning_end[0]) or \
                (dt.hour == morning_end[0] and dt.minute <= morning_end[1]):
            return f"{season}_Morning"
        elif (dt.hour == afternoon_start[0] and dt.minute >= afternoon_start[1]) or \
                (afternoon_start[0] < dt.hour < afternoon_end[0]) or \
                (dt.hour == afternoon_end[0] and dt.minute <= afternoon_end[1]):
            return f"{season}_Afternoon"
        else:
            return f"{season}_Night"

    def divide_into_groups_by_daytime(self):
        folder = os.listdir(self.root_dir)
        for file in folder:
            image_path = os.path.join(self.root_dir, file)
            try:
                img = Image.open(image_path)
                img_info = img.getexif()
                if img_info and TAGS.get(306,306) in img_info:
                    dt_str = img_info[TAGS.get(306, 306)]
                    dt = datetime.strptime(dt_str, '%Y:%m:%d %H:%M:%S')
                    destination_folder = os.path.join(self.root_dir,self.day_time_classify(dt))
                    if not os.path.exists(destination_folder):
                        os.mkdir(destination_folder)
                    shutil.move(image_path, destination_folder)
                img.close()
            except:
                print(f"{file}는 처리할 수 없습니다.")



if __name__=="__main__":
    divide = datasetIntoSmallDir("C:\\Users\\mirun\\PycharmProjects\\PhotoTimestamp-AI\\image_Dataset")
    divide.divide_into_groups_by_daytime()





