from _atom import Atom

class H(Atom):
    def __init__(self):
        self.__index = 1
        self.__name = 'H'


test = H()
print(test.get_name())