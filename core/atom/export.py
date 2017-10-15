from electron import Electron
from nucleus import Nucleus

class Atom(Nucleus, Electron):
    def __init__(self, index, name):
        self.__index = index
        self.__name = name

    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, value):
        if not isinstance(value, int):
            raise ValueError('atom index must be an integer!')
        if value < 1 or value > 118:
            raise ValueError('atom index must between 1 ~ 118!')
        self.__index = value

    def name(self):
        return self.__name
