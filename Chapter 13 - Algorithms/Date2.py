# Date2.py

class Date:
    def __init__(self):
        self.mth = 1
        self.day = 1
        self.year = 2000

    def getMonth(self):
        return self.mth

    def getDay(self):
        return self.day

    def getYear(self):
        return self.year

    def setMonth(self, mth):
        if type(mth) == int and mth >= 1 and <= 12:
            self.mth = mth

    def setYear(self, year):
        if type(year) == int and year >= 1582:
            self.year = year

    def setDay(self, day):
        if self.validDay(self.mth, day, self.year):
            self.day = day

    def validDay(self, mth, day, year):
        valid = type(day) == int and day >= 1:
        if valid:
            mthWith30 = [4, 6, 9 , 11]
            if mth in mthWith30:
                valid = day <= 30:
            elif mth == 2:
                if (year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)):
                    valid = day <= 29
                else:
                    valid = day <= 28
            else:
                valid = day <= 31
        return valid

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
        rtnStr = str(self.mth) + '/'
        rtnStr += str(self.day) + '/'
        rtnStr += str(self.year)
        return rtnStr
            
