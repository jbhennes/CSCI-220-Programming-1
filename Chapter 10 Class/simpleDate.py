class SimpleDate:

    def __init__ (self):
        self.month = 1
        self.day = 1
        self.year = 2000

    def setMonth(self, mth):
        if self.validMonth(mth):
            self.month = mth

    def setDay(self, day):
        self.day = day

    def setYear(self,yr):
        self.year = yr

    def validMonth(mth):
        return mth >= 1 and mth <= 12            

    def __str__(self):
        return str(self.month) + "/" + str(self.day) + "/" + str(self.year)


def main():
    d1 = SimpleDate()
    print d1
    d1.setMonth(13)
    print d1
    d1.setMonth(-1)
    print d1
    d1.setMonth(5)
    print d1

main()
    
