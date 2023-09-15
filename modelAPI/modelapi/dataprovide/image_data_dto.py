from PIL import Image

class ImageDataDTO:
    def __init__(self, image: Image, label: str):
        self.image: Image = image
        self.label: str = label

ImageDatasetDTO = list[ImageDataDTO]