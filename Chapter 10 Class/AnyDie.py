# Die.py

# Class that defines a six-sided die object.

from random import randint

class Die:

    def __init__(self, numSides):
        if numSides > 0:
            self.numSides = numSides
        else:
            self.numSides = 6
        self.faceValue = randint(1, self.numSides)

    def roll(self):
        self.faceValue = randint(1, self.numSides)

    def getValue(self):
        return self.faceValue

    def setValue(self, value):
        if value >= 1 and value <= self.numSides:
            self.faceValue = int(value)
        else:
            self.faceValue = randrange(1, self.numSides)

    def __str__(self):
        return "The die's value is: " + str(self.faceValue)
