from abc import ABC, abstractmethod
class Destination(ABC):
    @abstractmethod
    def append(self, msg):
        pass