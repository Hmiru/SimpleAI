import abc

class DataProvider:
    @abc.abstractmethod
    def get(self):
        raise NotImplemented