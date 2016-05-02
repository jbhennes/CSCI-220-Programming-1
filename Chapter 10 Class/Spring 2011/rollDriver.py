
from roll import Rollbook

def main():

    csci220 = Rollbook("CSCI220")
    print(csci220)
    print(csci220.getCourseNum())
    print(csci220.getStudents())
    print("Average: " + str(csci220.classAvg()))
    grades = [95, 80, 75, 100, 100]
    csci220.addStudentByName("Lee", "Blackwell", grades)
    csci220.addStudentByName("Daniel", "Allen", [90, 100])
    print(csci220)
    csci220.addStudentByName("Kevin", "Patton", [])
    print(csci220)
    print("Average: " + str(csci220.classAvg()))
    
##    krista = Student("Krista", "Grooms")
##    krista.addGrade(95)
##    krista.addGrade(80)
##    krista.addGrade(92)
##    krista.addGrade(100)
##    krista.addGrade(0)
##    krista.addGrade(115)
##    krista.addGrade(-5)
##    krista.addGrade(120)
##    print(krista.getGrades())
##    print(krista)
##    print(krista.calcAvg())
##    print(krista.getName())
##    krista.setLast("Williams")
##    print(krista)
##    print(krista.getName())
##
##    dirk = Student("Dirk", "Hanenkratt")
##    dirk.addGrade(100)
##    dirk.addGrade(90)
##    dirk.addGrade(75)
##
##    ainsley = Student("Ainsley", "Binnicker")
##    ainsley.addGrade(90)
##    ainsley.addGrade(85)
##    ainsley.addGrade(92)
##
##    danny = Student("Danny", "Lewis")
##    print(krista)
##    print(dirk)
##    print(ainsley)
##    print(danny)
##
##
##    students = []
##    students.append(krista)
##    students.append(dirk)
##    students.append(ainsley)
##    students.append(danny)
##
##    print(students)
##
##    for student in students:
##        print(student)
##        
    

main()
