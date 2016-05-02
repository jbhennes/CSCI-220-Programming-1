JAN = 1
DEC = 12

class Date:
   def __init__(self):
      self.month = 1
      self.day = 1
      self.year = 1900

   def setDate(self, mth, day, year):
      if mth >= JAN and mth <= DEC:
         self.month = mth
      self.day = day
      self.year = year

   def getMonth(self):
      return self.month

   def __str__(self):
      return str(self.month) + "/" + str(self.day) + "/" + str(self.year)
   
      
