from atom.export import Atom

class H(Atom):
    def __init__(self):
        Atom.__init__(self, 233, 'H')

test = H()
print(test.index)