class DataDTO:
    def __init__(self, label: str, image_location: str):
        self.label = label
        self.image_location = image_location

    def values(self):
        return self.label, self.image_location

    def __str__(self):
        return "label : {}\nimage_location : {}".format(self.label, self.image_location)

DatasetDTO = list[DataDTO]