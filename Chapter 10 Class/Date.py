# Date.py
# Author: RoxAnn H. Stalvey

class Date:
    def __init__(self): #default constructor sets date to 1-1-2000
        self.month = 1
        self.day = 1
        self.year = 2000

    def getMonth(self):
        return self.month

    def getDay(self):
        return self.day

    def getYear(self):
        return self.year

    def setDate(self, mthParm, dayParm, yrParm):  	
  	#call to validYear, validMonth, validDay methods to
        #make certain values passed to setDate represent valid dates.
        isValid = self.validYear(yrParm) and self.validMonth(mthParm)
        isValid = isValid and self.validDay(mthParm, dayParm, yrParm)
        if isValid:
            self.year = yrParm
            self.month = mthParm
            self.day = dayParm

    def validMonth(self,mth):
        return mth>=1 and mth<=12

##    #equivalent
##    def validMonth(self, mth):
##        if mth>=1 and mth<=12:
##            rtnVal = True
##        else:
##            rtnVal = False
##        return rtnval

    def validYear(self, yr):
        return yr >= 1582

    #method for determining if date input is valid
    def validDay (self, mth, day, yr):
        valid = day >= 1
        if valid:
            mthWith30 = [4, 6, 9, 11]
            if mth in mthWith30:
                valid = day <= 30
            elif mth == 2:
                #must consider year for Feb.
                if (yr % 400 == 0 or (yr % 100 != 0 and yr % 4 == 0)): 
                    valid = day <= 29
                else: #not a leap year
                    valid = day <=28
            else:
                valid = day <= 31
        return valid

    def compareTo(self, date):
        if self.year < date.getYear():
            rtnVal = -1
        elif self.year > date.getYear():
            rtnVal = 1
        else:
            if self.month < date.getMonth():
                rtnVal = -1
            elif self.month > date.getMonth():
                rtnVal = 1
            else:
                if self.day < date.getDay():
                    rtnVal = -1
                elif self.day > date.getDay():
                    rtnVal = 1
                else:
                    rtnVal = 0
        return rtnVal
    
    def __str__(self):
        dateStr = str(self.month) + "/" + str(self.day)
        dateStr = dateStr + "/" + str(self.year)
        return dateStr

  
  

  
   


