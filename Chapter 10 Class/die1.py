#Create a die

from random import randint
MIN = 1
MAX = 6

class Die:
   
   
   #Set the initial value for all attributes
   def __init__(self): #default constructor
      self.faceValue = 1

##   def __init__(self, value):
##      self.faceValue = 1
##      self.setFaceValue(value)
####      if value >= 1 and value <= 6:
####         self.faceValue = value
      
   def getFaceValue(self):
      return self.faceValue

   def setFaceValue(self, value):
      if value >= MIN and value <= MAX:
         self.faceValue = value

   def roll(self):
      self.faceValue = randint(MIN, MAX)

   def __str__(self):
      return "Die: " + str(self.faceValue)
      
