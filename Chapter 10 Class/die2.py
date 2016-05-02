# Die.py

# Class that defines a six-sided die object.

from random import randint

class Die:
    def __init__(self):
        self.faceValue = 1

    def getFaceValue(self):
        return self.faceValue

    def setFaceValue(self, value):
        value = int(value)
        if value >= 1 and value <= 6:
            self.faceValue = value

    def roll(self):
        self.faceValue = randint(1,6)

    def __str__(self):
        return "Die Value: " + str(self.faceValue)
    















    

##    def __init__(self):
##        self.faceValue = 1
##
##    def getFaceValue(self):
##        return self.faceValue
##
##    def setFaceValue(self, value):
##        if value > 0 and value < 7:
##            self.faceValue = value
##        else:
##            print "Don't try to cheat!"
##
##    def roll(self):
##        value = randint(1,6)
##        self.faceValue = value
##
##    def __str__(self):
##        return "Die Value: " + str(self.faceValue)
##    
##    



        
##
##    def roll(self):
##        self.faceValue = randrange(1, 7)
##
##    def getValue(self):
##        return self.faceValue
##
##    def setValue(self, value):
##        if value >= 1 and value <= 6:
##            self.faceValue = int(value)
##        else:
##            self.faceValue = randrange(1, 7)
##
##    def __str__(self):
##        return "The die's value is: " + str(self.faceValue)
