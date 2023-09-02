import abc

class Provider:
    def __init__(self, image_num: int):
        self._image_num = image_num

    @abc.abstractmethod
    def get(self):
        raise NotImplemented