from PIL import Image

class ImageDataDTO:
    image: Image
    label: str

ImageDatasetDTO = list[ImageDataDTO]