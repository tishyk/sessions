# Create class Singleton and use __new__ method for this.
# http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html
import abc


class AbstractChair(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def seat(self):
        pass

    @abc.abstractmethod
    def get_color(self):
        pass


class ChairClass():
    metal_type = 'iron'


class WoodChairClass(AbstractChair):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    def get_color(self):
        pass

    def seat(self):
        super().seat()


class MetalChairClass(AbstractChair):
    __instance = None

    def get_color(self):
        pass

    def seat(self):
        super().seat()

    @property
    def core(self):
        if not self.__class__.__instance:
            self.__class__.__instance = ChairClass()
        return self.__class__.__instance


a = WoodChairClass()
b = WoodChairClass()

print(id(a) == id(b))

c = MetalChairClass()
c_core = c.core
d = MetalChairClass()
d_core = d.core

print(id(c) == id(d), c_core == d_core)

a.seat()
b.get_color()
