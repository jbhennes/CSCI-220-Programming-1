# Die.py

# Class that defines a six-sided die object.

from random import randrange

class Die:

    def __init__(self):
        value = randrange(1, 7)

    def roll(self):
        self.value = randrange(1, 7)

    def getValue(self):
        return self.value

    def setValue(self, value):
        if value >= 1 and value <= 6:
            self.value = int(value)
        else:
            self.value = randrange(1, 7)

    def __eq__(self,other):
        return self.getValue() == other.getValue()

    def __cmp__(self,other):
        return self.value - other.getValue()
