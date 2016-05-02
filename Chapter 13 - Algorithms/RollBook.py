# RollBook.py
# Author: Pharr

from Student import Student

class RollBook:
    def __init__(self, number, name, term):
        self.number = number     # really a string
        self.name = name
        self.term = term
        self.students = []

    ## addStudent appends a clone of the student
    def addStudent(self, stu):
        newStu = Student(stu.getStudentNumber(), stu.getFirst(),
                         stu.getLast(), stu.getGrades(), stu.getEnrollDate())
        self.students.append(newStu) 

    def addGrade(self, stuNum, grade):
        loc = self.findStudent(stuNum)
        if loc > -1:
            self.students[loc].addGrade(grade)

    def displayCourseInfo(self):
        s = "Course: " + self.number + " - " + self.name + " - "
        s = s + self.term + "\n"
        return s

    def findStudent(self, stuNum):
        location = -1
        found = False
        length = len(self.students)
        i = 0
        while not found and i < length:
            if self.students[i].getStudentNumber() == stuNum:
                location = i
                found = True
            else:
                i = i + 1
        return location
    
    def displayStudent(self, stuNum):
        loc = self.findStudent(stuNum)
        if loc > -1:
            s = "Number: " + str(self.students[loc].getStudentNumber())
            s = s + "  Name: " + self.students[loc].getName()
            s = s + "\nGrades: " + str(self.students[loc].getGrades())
            avg = self.students[loc].calcAvg()
            if avg == -1:
                s = s + "\nThis student has no average"
            else:
                s = s + "\nAverage: " + str(avg)
        else:
            s = "There is no student with the number " + str(stuNum)
        return s

    def classAverage(self):
        avg = 0
        total = 0
        count = 0
        for i in range(len(self.students)):
            stuAvg = self.students[i].calcAvg()
            if stuAvg >= 0:
                total = total + stuAvg
                count = count + 1
        if count != 0:
            avg = total / count
        else:
            avg = "No average"
        return avg

    def sortStudentsByID(self):
        # sort students into ascending order by ID number
        n = len(self.students)        
        for bottom in range(n-1):
            mp = bottom
            for i in range(bottom+1, n):
                if self.students[i].getStudentNumber() < self.students[mp].getStudentNumber():
                    mp = i
            temp = self.students[mp]
            self.students[mp] = self.students[bottom]
            self.students[bottom] = temp

    def sortStudentsByEnrollDate(self):
        # sort students into ascending order by date of enrollment
        n = len(self.students)        
        for bottom in range(n-1):
            mp = bottom
            for i in range(bottom+1, n):
                # local variables used because expression would be so long
                iDate = self.students[i].getEnrollDate()
                mpDate = self.students[mp].getEnrollDate()
                if iDate.compareTo(mpDate) < 0:
                    mp = i
            temp = self.students[mp]
            self.students[mp] = self.students[bottom]
            self.students[bottom] = temp

    def __str__(self):
        s = "Course: " + self.number + " - " + self.name + " - "
        s = s + self.term + "\n"
        length = len(self.students)
        if length == 0:
            s = s + "No students enrolled\n"
        else:
            for i in range(length):
                s = s + str(self.students[i]) + "\n\n"
        return s




