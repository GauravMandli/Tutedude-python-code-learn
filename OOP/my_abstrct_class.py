from abc import ABC,abstractclassmethod

class shape(ABC):
    @abstractclassmethod
    def area(self):
        pass