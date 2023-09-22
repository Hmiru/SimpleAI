from dataprovide.image_provider_by_location import ImageProviderByLocation
from propertise.propertise_loader import PropertiseLoader
from PIL import ImageShow  # 이미지를 화면에 표시하기 위한 모듈
import os
import re

class ImageInfoExtractor(ImageProviderByLocation):

    def __init__(self, filename: str):
        relative_location = os.path.join("Phototimestamp_ds\\test", filename)
        super().__init__(relative_location)
        self.filename = filename
        self.datetime = self.extract_date_time(self.filename)

    def get(self):
        image=super().get()
        return self.datetime

    @staticmethod
    def get_base_image_folder():
        propertise = PropertiseLoader().get()
        return propertise['location']['Image']

    def extract_date_time(self, filename):
        match = re.search(r'^(\d{4})(\d{2})(\d{2})_(\d{2})(\d{2})(\d{2})\.jpg$', filename)
        datetime = (match.group(1)+":"+match.group(2)+":"+match.group(3)+" "+
                    match.group(4) + ":" + match.group(5)+":" + match.group(6))

        return datetime



def main():
    folder=os.path.join(ImageInfoExtractor.get_base_image_folder(), "Phototimestamp_ds\\test")
    for file in os.listdir(folder):
        print(file)
        if file.endswith('.jpg'):
            extractor = ImageInfoExtractor(file)
            datetime = extractor.get()



if __name__=="__main__":
    main()


