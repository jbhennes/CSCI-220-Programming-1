#Creates a basic definition of a student
#Attributes: firstName (string), lastName (string), grades (list)
#Methods:
## constructor accepts first and last
## getName() returns first + last
## getGrades() returns list of grades
## setLast(newName) sets lastName equal to newName
## addGrade(grade) appends grade into list of grades
## calcAvg() returns the average of the grades
## str() returns a string representation of a Student


class Student:
    #constructor
    def __init__(self, first, last):
        self.firstName = str(first)
        self.lastName = str(last)
        self.grades = []

    def getName(self):
        return self.firstName + " " + self.lastName

    def getGrades(self):
        return self.grades

    def setLast(self, lastName):
        self.lastName = str(lastName)

    def addGrade(self, grade):
        if grade >= 0 and grade <=115:
            self.grades.append(grade)

    def hasGrades(self):
        return len(self.grades) > 0

    def calcAvg(self):
        total = 0
        for grade in self.grades:
            total += grade
        avg = total / len(self.grades)
        return avg

    def __str__(self):
        rtnStr = self.getName() + "\n"
##        rtnStr = self.firstName + " " + self.lastName + "\n"
        if len(self.grades) == 0:
            rtnStr += " No grades entered for this student."
        else:
            rtnStr += " Grades are: "
            for grade in self.grades:
                rtnStr += str(grade) + " "
        return rtnStr
        
