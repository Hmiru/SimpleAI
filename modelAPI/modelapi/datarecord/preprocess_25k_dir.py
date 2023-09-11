import os
import shutil

DIR = "/home/junhee0110/Phototimestamp_data/mirflickr/"

def main():
    os.mkdir(DIR+"images")
    files = os.listdir(DIR)
    for file in files:
        if file.endswith(".jpg"):
            new_name = file.split("im")[1]

            id = int(new_name.split(".jpg")[0])
            subdir = id // 10000
            if not(os.path.exists(DIR+"images/"+ str(subdir))):
                os.mkdir(DIR+"images/"+ str(subdir))
            print(DIR+"images/"+ str(subdir) + "/" +new_name)
            shutil.move(DIR+file, DIR+"images/"+ str(subdir) + "/" +new_name)

    shutil.move(DIR+"meta/exif", DIR+"exif")

    exifs = os.listdir(DIR+"exif")
    for file in exifs:
        if file.endswith(".txt"):
            new_name = file.split("exif")[1]

            id = int(new_name.split(".txt")[0])
            subdir = id // 10000
            if not(os.path.exists(DIR+"exif/"+ str(subdir))):
                os.mkdir(DIR+"exif/"+ str(subdir))
            print(DIR+"exif/"+ str(subdir) + "/" +new_name)
            shutil.move(DIR+"exif/"+file, DIR+"exif/"+ str(subdir) + "/" +new_name)

if __name__ == "__main__":
    main()