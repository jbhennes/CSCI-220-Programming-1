# RollBookDriver.py
# Author: Pharr

# RollBookDriver - creates a RollBook object and inserts Students

from RollBook import RollBook
from Student import Student
from Date import Date

def main():
    roll = RollBook("CSCI220", "Programming I", "Spring 2008")
    print ("When roll book is empty...")
    print (roll)
    print ("Class Average:", roll.classAverage())
    print ("\n*************************\n")
    
    d1 = Date ()
    d1.setDate(8,15,2006)
    stu1 = Student(923, "Tenessee", "Williams", [90, 93], d1)
    roll.addStudent(stu1)
    
    d2 = Date()
    d2.setDate(5, 12, 2000)
    stu2 = Student(834, "Bob", "Marley", [95, 90, 92], d2)
    roll.addStudent(stu2)
    
    d3 = Date()
    d3.setDate(12, 1, 2004)
    stu3 = Student(745, "Diana", "Ross", [], d3)
    roll.addStudent(stu3)

    d4 = Date()
    d4.setDate(3, 9, 2007)
    stu4 = Student(656, "Peter", "Townshend", [87, 92, 98, 94, 92], d4)
    roll.addStudent(stu4)

    print (roll)
##    print "*************************\n"
##
##    print roll.displayCourseInfo()
##    print roll.displayStudent(923)
##    print
##    print roll.displayStudent(834)
##    print
##    print roll.displayStudent(999)
##    print
##    print roll.displayStudent(745)
##    print
##    print roll.displayStudent(656)
##    print
##
##    roll.addGrade(923, 93)
##    roll.addGrade(923, 89)
##    roll.addGrade(923, 97)
##    print "After adding grades 93, 89, 97 to student 123:"
##
##    print roll.displayStudent(923)
##    print

    print ("Class Average:", roll.classAverage())

    print ("\n*************************\n")
    
    print ("Sorted by student ID")
    roll.sortStudentsByID()
    print (roll)

    print ("\n*************************\n")
    
    print ("Sorted by date of enrollment")
    roll.sortStudentsByEnrollDate()
    print (roll)

main()
