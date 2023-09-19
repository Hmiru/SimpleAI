from abc import ABC, abstractmethod

class BaseModel(ABC):
    def __init__(self, image_info):
        self.input_width = image_info.image_width
        self.input_height = image_info.image_height

    @abstractmethod
    def build(self):
        pass