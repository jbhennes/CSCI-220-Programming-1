# Student.py
# Author: RoxAnn H. Stalvey

# Student class
# Student's data members: id number, firstName, lastName,
#                         list of grades, date of enrollment

from Date import Date

class Student:

    #fully parameterized constructor
    def __init__(self, stuNum, firstName, lastName, grades, date):
        self.studentNumber = stuNum
        self.setName(firstName, lastName)
        self.setGrades(grades)
        self.setEnrollDate(date)

    def setName(self, first, last):
        self.firstName = first
        self.lastName = last

    def setGrades(self, grades):
##        self.grades = grades #alias
        self.grades = []
        for grade in grades:
            self.grades.append(grade)

    def setEnrollDate(self, date):
##        self.enrollDate = date #alias
        self.enrollDate = Date()
        self.enrollDate.setDate(date.getMonth(),date.getDay(),date.getYear())

    def getStudentNumber(self):
        return self.studentNumber

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

    def addGrade(self, grade):
        self.grades.append(grade)

    #Input: nothing
    #Output: Numeric average.  Returns -1 if no grades entered.
    def calcAvg(self): 
        count = len(self.grades)        
        if count == 0:
            avg = -1
        else:
            total = 0.0
            for grade in self.grades:
                total = total + grade
            avg = total / count
        return avg

    def __str__(self):
        out = "Student number: " + str(self.getStudentNumber())
        out = out + "\nStudent name: " + self.getName()
        out = out + "\nEnroll Date: " + str(self.getEnrollDate())
        if len(self.grades) != 0:
            out = out + "\nGrades: " + str(self.getGrades())
            out = out + "\nAverage: " + str(self.calcAvg())
        else:
            out = out + "\nThis student has no grades."
        return out
    
