from random import randint

class Die:

##   def __init__(self):
##      self.faceValue = 1

   def __init__(self, value):
      self.faceValue = 1
      self.setFaceValue(value)

   def setFaceValue(self, newValue):
      if newValue >= 1 and newValue <= 6:
         self.faceValue = int(newValue)
         
   def getFaceValue(self):
      return self.faceValue
   
   def roll(self):
      self.faceValue = randint(1, 6)

   def __str__(self):
      output = "Die value: " + str(self.faceValue)
      return output

   
