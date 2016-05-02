# Student class
# Student's data members: firstName, lastName, list of grades, date of enrollment

from Date import Date

class Student:

    def __init__(self,firstName,lastName,grades,date):
        self.setName(firstName, lastName)
        self.setGrades(grades)
        self.setEnrollDate(date)

##        self.firstName = firstName
##        self.lastName = lastName
##        self.grades = []
##        for grade in grades:
##            self.grades.append(grade)
##        #clone date for enrollDate instead of setting enrollDate = date
##        self.enrollDate = Date()
##        self.enrollDate.setDate(date.getMonth(),date.getDay(),date.getYear())

    def getName(self):
        return self.firstName + " " + self.lastName

    def getFirst(self):
        return self.firstName

    def getLast(self):
        return self.lastName

    def getGrades(self):
        return self.grades

    def getEnrollDate(self):
        return self.enrollDate

    def setName(self, first, last):
        self.firstName = first
        self.lastName = last

    def setGrades(self, grades):
        self.grades = []
        for grade in grades:
            self.grades.append(grade)

    def setEnrollDate(self, date):
        self.enrollDate = Date()
        self.enrollDate.setDate(date.getDay(),date.getMonth(),date.getYear())

    def addGrade(self, grade):
        self.grades.append(grade)

    def calcAvg(self):
        total = 0
        for grade in self.grades:
            total = total + grade
        count = len(self.grades)
        if count == 0:
            avg = -1
        else:
            avg = total / count
        return avg

    def __str__(self):
        out = "Student: " + self.getName()
        out = out + "\nEnroll Date: " + str(self.getEnrollDate())
        out = out + "\nGrades: " + str(self.getGrades())
        out = out + "\nAverage: " + str(self.calcAvg())
        return out
    
