import os
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS
def day_night_clssify(dt):
    if 6 <= dt.month <= 8 and 5 <= dt.hour <= 11:
        print('summer morning')
    elif 3 <= dt.month <= 5 and 5 <= dt.hour <= 11:
        print('spring morning')
def print_files_in_dir(root_dir):
    dates=[]
    folder = os.listdir(root_dir)
    for file in folder:
        image_path = os.path.join(root_dir, file)
        try:
            img = Image.open(image_path)
            img_info = img._getexif()
            img.close()
            for tag_id, value in img_info.items():
                tag = TAGS.get(tag_id, tag_id)
                if tag == 'DateTime':
                    dt = datetime.strptime(value, '%Y:%m:%d %H:%M:%S')
                    day_night_clssify(dt)
        except:
            # 이미지 파일이 아니거나 EXIF 정보를 읽을 수 없는 경우를 대비
            print(f"{file}는 처리할 수 없습니다.")
    return dates



dates = print_files_in_dir("C:\\Users\\mirun\\PycharmProjects\\PhotoTimestamp-AI\\for_vision\\test_my_photo")
for date in dates:
    print(day_night_clssify(date))

# def month_hour_extract(value):
#     try:
#         date_part, time_part = value.split(' ')
#         month = int(date_part.split(':')[1])
#         hour = int(time_part.split(':')[0])
#         minute = int(time_part.split(':')[1])
#         return month, hour, minute
#     except Exception as e:
#         print(f"Error: {e}")
#         return None

from datetime import datetime




