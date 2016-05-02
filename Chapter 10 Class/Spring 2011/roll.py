#Rollbook:
##list of Student objects
##courseNumber - actually a string

from student import Student

class Rollbook:
    def __init__(self, courseNum):
        self.courseNum = str(courseNum)
        self.students = []

    def getCourseNum(self):
        return self.courseNum

    def getStudents(self):
        return self.students

    def addStudentByName(self, first, last, grades):
        student = Student(first, last)
        for grade in grades:
            student.addGrade(grade)
        self.students.append(student)

    def classAvg(self):
        total = 0
        count = 0
        for student in self.students:
            if student.hasGrades():
                total += student.calcAvg()
                count += 1
        if count > 0:
            avg = total / count
        else:
            avg = -1
        return avg

    def __str__(self):
        rtnStr = "Course number: " + self.courseNum + "\n"
        if len(self.students) > 0:
            rtnStr += "Students: " + "\n"
            for student in self.students:
                rtnStr += str(student) + "\n"
        else:
            rtnStr += "No students in this course.\n"
        return rtnStr
