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
  	#call to validDay method to make certain values passed to setDate
  	#represent valid dates.
        if self.validYear(yrParm):
            self.year = yrParm
            if self.validMonth(mthParm):
                self.month = mthParm
                if self.validDay(mthParm, dayParm, yrParm):
                    self.day = dayParm
                else:
                    msg = "The number of days given, " + str(dayParm)
                    msg = msg + ", is not valid for the month " + str(mthParm)
                    print (msg)
            else:
                print ("Month must be between 1 and 12")
        else:
            print ("Year must be greater than -1")

    def validMonth(self,mth):
        return mth>=1 and mth<=12

    def validYear(self, yr):
        return yr >= 0

    #method for determining if date input is valid
    def validDay (self, mth, day, yr):
        valid = day >= 1
        if valid:
            if mth in [1, 3, 5, 7, 8, 10, 12]:
                valid = day <= 31
            elif mth in [4, 6, 9, 11]:
                valid = day <= 30
            else:
                #must consider year for Feb.
                if (yr % 400 == 0 or (yr % 100 !=0 and yr % 4==0)): #leap year
                    valid = day <= 29
                else: #not a leap year
                    valid = day <=28      
        return valid
  
    ##
    ## returns negative value if self is less than (occurred before) d2
    ## returns 0 if self and d2 are equal
    ## returns positive value if self is greater than (occurred after) d2
    ##
    def compareTo(self, d2):
        comp = 0
        if self.year != d2.getYear():
            comp = self.year - d2.getYear()
        elif self.month != d2.getMonth():
            comp = self.month - d2.getMonth()
        else:
            comp = self.day - d2.getDay()
        return comp 
  
    def __str__(self):
        return str(self.month) + "/" + str(self.day) + "/" + str(self.year)
  
  
##def main():
##    d1 = Date()
##    d1.setDate(10, 30, 1969)
##    print "d1 = " + str(d1)
##    print
##    d2 = Date()
##    d2.setDate(10, 30, 1968)
##    print "d2 = " + str(d2)
##    print
##    d3 = Date()
##    d3.setDate(10, 30, 1970)
##    print "d3 = " + str(d3)
##    print
    
    #testing bad data in call to constructor
##    d3 = Date()
##    print "d3 = " + str(d3)
##    print
##    d3.setDate(13, 115, -3)
##    print "d3 = " + str(d3)
##    print
##    d3.setDate(13, 32, 1900)
##    print "d3 = " + str(d3)
##    print
##    d3.setDate(4, 32, 1900)
##    print "d3 = " + str(d3)
##    print
##    d3.setDate(4, 30, 1900)
##    print "d3 = " + str(d3)
##    print
##    d4 = Date()
##    d4.setDate(12, 5, 1969)
##    print "d4 = " + str(d4)
##    print
##    d5 = Date()
##    d5.setDate(3, 31, 1969)
##    print "d5 = " + str(d5)
##    print 
##    d6 = Date()
##    d6.setDate(10, 30, 1969)
##    print "d6 = " + str(d6)
##    print 
##    d7 = Date()
##    d7.setDate(10, 5, 1969)
##    print "d7 = " + str(d7)
##    print 
##    d8 = Date()
##    d8.setDate(4, 30, 1969)
##    print "d8 = " + str(d8)
##    print 
##
##    #Create and fill a list of dates
##    dates = []
##    dates.append(d1)
##    dates.append(d2)
##    dates.append(d3)
##    dates.append(d4)
##    dates.append(d5)
##    dates.append(d6)
##    dates.append(d7)
##    dates.append(d8)
##
##    print "Dates in original order:"
##    for date in dates:
##        print date
##
##    dates.sort()
##
##    print
##    print "Dates in sorted order: "
##    for date in dates:
##        print date
##    
##
##main()

 
