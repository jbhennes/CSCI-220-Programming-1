#Die class for 6 sided die

from random import randint

class Die:
    #constructor/initializer
    def __init__(self):
        self.faceValue = 1

    def getFaceValue(self):
        return self.faceValue

    def setFaceValue(self, value):
        if value >= 1 and value <= 6:
            self.faceValue = value

    def roll(self):
        randValue = randint(1, 6)
        self.faceValue = randValue

    def __str__(self):
        rtnStr = "Value: " + str(self.faceValue)
        return rtnStr
