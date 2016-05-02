from random import randint

class Die:
##   def __init__(self):
##      self.faceValue = 1

   def __init__(self):
      self.faceValue = 1

   def getFaceValue(self):
      return self.faceValue

   def setFaceValue(self, num):
      if (num >= 1 and num <= 6):
         self.faceValue = int(num)
      
   def roll(self):
      self.faceValue = randint(1, 6)

   def __str__(self):
      output = "Die value: " + str(self.faceValue)
      return output
