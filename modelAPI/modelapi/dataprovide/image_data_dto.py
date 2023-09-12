from PIL import Image

class ImageDataDTO:
    image: Image
    label: str

    def __init__(self, image: Image, label: str):
        self.image = image
        self.label = label

ImageDatasetDTO = list[ImageDataDTO]