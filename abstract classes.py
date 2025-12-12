from abc import ABC, abstractmethod
class absclass(ABC):
    def print(self, x):
        print("passed value: ", x)
    @abstractmethod
    def tuskact(self):
        print("print we are inside an absclass task and in a abstract art style manga")
class test_class(absclass):
    def tuskact(self):
        print("print we are inside an test_class task and in a abstract art style manga")
test_obj = test_class()
test_obj.tuskact()
test_obj.print(4)