# date3.py

class Date:

    def __init__(self):         ## This is a default constructor.
        self.month = 1
        self.day = 1
        self.year = 2000
        

    def __str__(self):
        rtnStr = str(self.month) + '/'
        rtnStr += str(self.day) + '/'
        rtnStr += str(self.year)
        return rtnStr


    def getMDY(self):
        return self.month, self.day, self.year

    def setMonth(self, month):
        if type(month) == int and month >= 1 and month <= 12:
            self.month = month

    def setYear(self, year):
        if type(year) == int and year >= 1582 and year <= 2014:
           self.year = year

    def setDay(self, day, month, year):
        if self.validDate(self.month, day, self.year):
            self.day = day

    def validDate(self, month, day, year):
        valid = True
        return valid

def main():
    print('Welcome! This program will tell you the current date and conatins various methods to use on the date')
    today = Date()
    print(today)

    today.setMonth(12)
    print(today)

    today.setDay(5, 4, 2014)
    print(today)

main()
