import os
from datetime import datetime
import shutil
from PIL import Image
from PIL.ExifTags import TAGS
from exif_provider_from_dir import EXIFProviderFromDir
from Get_ready_photo import datasetIntoSmallDir

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
        try:
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
        except:
            return f"unknown data"


    def create_destination_folder(self,dt):
        destination_folder = os.path.join(self.root_dir, self.day_time_classify(dt))
        if not os.path.exists(destination_folder):
            os.mkdir(destination_folder)
        return destination_folder

    def extract_datetime_using_EXIFmethod(self, image_number):
        extract = EXIFProviderFromDir(image_number).get()
        dt_str = extract.get('Date and Time (Original)')

        if dt_str is None:
            dt_str = extract.get('Date and Time (Digitized)')
            if dt_str is None:  # 두 경우 모두 없는 경우
                return None

        return datetime.strptime(dt_str, '%Y:%m:%d %H:%M:%S')

    def move_file(self,image_path,destination_folder):
        shutil.move(image_path, destination_folder)
    def datetime_checker(self,dt):
        if dt=='0000:00:00 00:00:00' or ':  :     :  :':
            return None
        return dt


    def divide_into_groups_by_daytime(self):
        folder = os.listdir(self.root_dir)
        for file in folder:
            file_extension = os.path.splitext(file)[1].lower()
            image_path = os.path.join(self.root_dir, file)

            if file_extension in ['.jpg', '.jpeg']:
                try:
                    image_number = int(file[2:-4])
                    dt = self.extract_datetime_using_EXIFmethod(image_number)

                    if self.datetime_checker(dt) is None:  # 날짜 정보가 없는 경우
                        dest_folder = os.path.join(self.root_dir, 'unknown')
                    else:
                        dest_folder = self.create_destination_folder(dt)
                    if not os.path.exists(dest_folder):
                        os.mkdir(dest_folder)
                    self.move_file(image_path, dest_folder)
                except Exception as e:
                    print(f"Error processing '{file}': {e}")

if __name__=="__main__":
    divide = datasetIntoSmallDir("C:\\Users\\mirun\\PycharmProjects\\PhotoTimestamp-AI\\test_git\\LabelClassify\\DS\\mirflickr25k\\\images")
    divide.divide_into_groups_by_daytime()