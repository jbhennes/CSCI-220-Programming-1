## Die.py

from random import *

class Die:
    # Constructor
    def __init__(self, sides):
        self.numSides = 6
        if sides >= 2:
            self.numSides = sides
        else:
            self.numSides = 6
        self.faceValue = 1

    # Accessor for face value
    def getFaceValue(self):
        return self.faceValue

    # Accessor for # of sides
    def getNumSides(self):
        return self.numSides

    # mutator for face value.
    def setFaceValue(self, value):
        if value >= 1 and value <= self.numSides:
            self.faceValue = value

    # Mutator for num sides.
    def setNumSides(self, num):
        if num >= 2:
            self.numSides(num)

    # Method to roll die
    def roll(self):
        value = randint(1, self.numSides)

    
