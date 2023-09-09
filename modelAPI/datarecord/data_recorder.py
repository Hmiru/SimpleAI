import abc

class DataRecorder:
    @abc.abstractmethod
    def record(self):
        raise NotImplemented