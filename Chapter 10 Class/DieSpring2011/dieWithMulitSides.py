#Die class for user-defined number of sides

from random import randint

class Die:
    #constructor/initializer
    #user specifies number of sides
    #if value is not reasonable (<=0) numSides set to 6
    def __init__(self, numSides):
        self.numSides = 6
        self.setNumSides(numSides)
        self.faceValue = 1

    #assessor methods
    def getFaceValue(self):
        return self.faceValue

    def getNumSides(self):
        return self.numSides

    #mutator methods
    def setFaceValue(bananas, value):
        if value >= 1 and value <= bananas.numSides:
            bananas.faceValue = value

    def setNumSides(self, numSides):
        if numSides >= 1:
            self.numSides = int(numSides)

    #method to simulate a roll
    #roll value inclusively between 1 and numSides of the die
    def roll(apples):
        randValue = randint(1, apples.numSides)
        apples.faceValue = randValue

    #converts die into a string in the form Value: faceValue
    def __str__(self):
        rtnStr = "Value: " + str(self.faceValue)
        return rtnStr
