
from modelAPI.modelapi.dataprovide.datetime_provider_by_image_location import *
from labelclassify.label_classifier_from_boundary import *
class LabelClassifierFromFilename():
    def __init__(self,filename: str):
        base_folder = ImageInfoExtractor.get_base_image_folder()
        relative_folder_path = "Phototimestamp_ds\\test"
        self.filename=filename
    def classify_and_return(self, filename):
        extractor = ImageInfoExtractor(filename)
        datetime_str=extractor.get()
        datetime_obj = datetime.strptime(datetime_str, "%Y:%m:%d %H:%M:%S")
        lc = LabelClassifierFromBoundary(datetime_obj, TIME_BOUNDARY_DIC)
        season_time=lc.label()
        return season_time

def main():
    folder = os.path.join(ImageInfoExtractor.get_base_image_folder(), "Phototimestamp_ds\\test")
    for file in os.listdir(folder):
        if file.endswith('.jpg'):
            label_classifier = LabelClassifierFromFilename(file)
            season_time=label_classifier.classify_and_return(file)
            print(f" season_time : {season_time}")

if __name__== "__main__":
    main()
