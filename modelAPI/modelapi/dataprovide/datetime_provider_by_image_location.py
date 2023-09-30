import re
from dataprovide.image_provider_by_location import ImageProviderByLocation
import os
class DateTimeProviderByLocationFromDir(ImageProviderByLocation):
    def __init__(self, relative_location: str):
        super().__init__(relative_location)

    def get(self):
        filename = os.path.basename(self.get_path())
        match = re.search(r'^(\d{4})(\d{2})(\d{2})_(\d{2})(\d{2})(\d{2})\.jpg$', filename)
        if match:
            datetime_str = (match.group(1)+":"+match.group(2)+":"+match.group(3)+" "+
                            match.group(4) + ":" + match.group(5)+":" + match.group(6))
            return datetime_str
        else:
            return None

def main():
    extractor = DateTimeProviderByLocationFromDir("Phototimestamp_ds\\test\\20230928_123456.jpg")
    datetime_str = extractor.get()
    print(datetime_str)

if __name__=="__main__":
    main()
