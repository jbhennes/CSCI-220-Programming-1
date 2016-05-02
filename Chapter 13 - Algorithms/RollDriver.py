from RollBook import RollBook
from Student import Student
from Date import Date

def main():
    cs220 = RollBook("CSCI220", "Prog I", "Sp 2012")

    print(cs220)
    print("\n" + "*" * 10 + "\n")
    
    d1 = Date ()
    d1.setDate(8,15,2006)
    chad = Student(5, "Tenessee", "Williams", [90, 93], d1)
    cs220.addStudent(chad)

    brad = Student(2, "Bob", "Marley", [95, 90, 92],d1)
    cs220.addStudent(Student(4, "Diana", "Ross", [],d1))
    cs220.addStudent(Student(3, "Peter", "Townsend", [87, 92, 98, 94, 92],d1))
    cs220.addStudent(brad)
    
    print(cs220)

##    average = cs220.classAverage()
##
##    print("Average:", average)
##
##    print("\n" + "*" * 10 + "\n")
##
##    print(cs220.displayStudent(3))
##    
##    print("\n" + "*" * 10 + "\n")
##
##    print(cs220.displayStudent(99))

    print("\n" + "*" * 10 + "\n")

    cs220.sortStudentsByID()
    print(cs220)
    print("\n" + "*" * 10 + "\n")

    cs220.sortStudentsByEnrollDate()
    print(cs220)
    print("\n" + "*" * 10 + "\n")
    

main()
