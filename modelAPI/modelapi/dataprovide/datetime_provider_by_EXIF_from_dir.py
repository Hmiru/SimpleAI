from dataprovide.exif_provider_by_id_from_dir import *

from modelAPI.modelapi.dataprovide.exif_provider_by_id_from_dir import EXIFProviderByIDFromDir
from exif_provider_by_image_location import DateTimeProviderByLocationFromDir


class DateTimeProviderByEXIFfromDir(EXIFProviderByIDFromDir):
    def __init__(self, image_num: int):
        super().__init__(image_num)

    def get(self):
        #1번방법
        exif = super.get_exif()
        photoed_time = exif.get("Date and Time (Original)")
        return photoed_time
