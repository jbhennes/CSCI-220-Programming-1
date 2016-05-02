# student.py

# for students we need what properties (attributes)?
#       First Name ------> String
#       Last Name ------> String
#       Grades ------> List []
#       Date enrolled in class ------> Date Obj

from date import Date

class Student:

    def __init__(self):
        self.firstName = firat
        self.lastName = last
        self.enrollDate = date
        self.grades = []

    def setFirst(self, first):
        self.firstName = first

    def setLast(self, last):
        self.lastName = last

    def getFirst(self):
        return self.firstName

    def getLast(self):
        return self.lastName

    def __str__(self):
        rtnStr = self.firstName + ' '
        rtnStr += self.lastName + '\n'
        rtnStr += 'Enrolled: ' + str(self.enrollDate) + '\n'
        if len(self.grades) == 0:
            rtnStr += 'No Grades Entered.'
        else:
            rtnStr += 'Grades: ' + str(self.grades)
        return rtnStr
        
        

