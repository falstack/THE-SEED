class Atom():
    def __init__(self, index, name):
        self.__index = index
        self.__name = name

    def get_name(self):
        return self.__name

    def test(self):
        return 'this is a atom'