# Student.py
# Author: RoxAnn H. Stalvey

# Student class
# Student's data members: id number, firstName, lastName,
#                         list of grades, date of enrollment

from Date import Date

class Student:

    def __init__(self, stuNum, firstName, lastName, grades, date):
        self.studentNumber = stuNum
        self.firstName = firstName
        self.lastName = lastName
        self.grades = []
        for grade in grades:
            self.grades.append(grade)
        #clone date for enrollDate instead of setting enrollDate = date
        self.enrollDate = Date()
        self.enrollDate.setDate(date.getMonth(),date.getDay(),date.getYear())

    def addGrade(self, grade):
        self.grades.append(grade)

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

    def calcAvg(self):
        total = 0.0
        count = 0
        for grade in self.grades:
            count = count + 1
            total = total + grade
        if count == 0:
            avg = -1
        else:
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
    
