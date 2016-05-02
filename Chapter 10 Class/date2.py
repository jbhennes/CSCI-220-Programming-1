#Date class

class Date:

    def __init__(self):
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
        self.month = mthParm
        self.day = dayParm
        if self.validYear(yrParm):
            self.year = yrParm

    def validYear(self, yr):
        return yr > 0

    def __str__(self):
        output = str(self.month) + "/"
        output = output + str(self.day) + "/"
        output = output + str(self.year)
        return output
