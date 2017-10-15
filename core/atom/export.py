from electron import Electron
from nucleus import Nucleus

class Atom(Nucleus, Electron):
    def __init__(self, index, name):
        self.__index = index
        self.__name = name

    @property
    def index(self):
        return self.__index

    @property
    def name(self):
        return self.__name
