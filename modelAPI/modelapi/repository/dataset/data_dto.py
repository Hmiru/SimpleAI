class DataDTO:
    label: str
    image_location: str

    def __init__(self, label: str, image_location: str):
        self.label = label
        self.image_location = image_location

DatasetDTO = list[DataDTO]