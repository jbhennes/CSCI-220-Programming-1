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

    def findStudent(self, stuNum):
        location = -1
        found = False
        length = len(self.students)
        i = 0
        while not found and i < length:
            if self.student[i].getStudentNumber() == stuNum:
                location = i
                found = True
            else:
                i += 1
        return location

    def addGrade(self, stuNum, grade):
        location = self.findStudent(stuNum)
        if location > -1:
            self.students[location].addGrade(grade)

    def displayCourseInfo(self):
        s = "Course: " + self.number + " - " + self.name + " - "
        s = s + self.term + "\n"
        return s

    def displayStudent(self, stuNum):
        location = self.findStudent(stuNum)
        if location > -1:
            s = str(self.students[location])
            avg = self.students[location].calcAvg()
            if avg == -1:
                s += "\nThis student has no average"
            else:
                s += "\nAverage: " + str(avg)
        else:
            s = "There is no student with the number " + str(stuNum)

    def classAverage(self):
        avg = 0
        sum = 0.0
        count = 0
        for i in range(len(self.students)):
            stu = self.students[i]
            stuAvg = stu.calcAvg()
            if stuAvg >= 0:
                sum = sum + stuAvg
                count = count + 1
        if count != 0:
            avg = sum / count
        else:
            avg = "No average"
        return avg

    def sortStudentByID(self):
        # sort students into ascending order by id number
        n = len(self.students)
        for bottom in range(n-1):
            mp = bottom
            for i in range(bottom + 1, n):
                iNumber = self.students[i].getStudentNumber()
                mpNumber = self.students[i].getStudentNumber()
                if iNumber < mpNumber:
                    mp = i
            temp = self.students[mp]
            self.students[mp] = self.students[bottom]
            self.students[bottom] = temp

    def sortStudentByEnrollDate(self):
        n = len(self.students)
        for bottom in range(n - 1):
            mp = bottom
            for i in range(bottom + 1, n):
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
            for stu in self.students:
                s = s + str(stu) + "\n\n"
        return s




