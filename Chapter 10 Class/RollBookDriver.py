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
    print ("\n*****\n")
    
    d1 = Date ()
    d1.setDate(8,15,2006)
    stu1 = Student(123, "Tenessee", "Williams", [90, 93], d1)
    roll.addStudent(stu1)
    
    d2 = Date()
    d2.setDate(5, 12, 2000)
    stu2 = Student(234, "Bob", "Marley", [95, 90, 92], d2)
    roll.addStudent(stu2)
    
    d3 = Date()
    d3.setDate(12, 1, 2004)
    stu3 = Student(345, "Diana", "Ross", [], d3)
    roll.addStudent(stu3)

    d4 = Date()
    d4.setDate(3, 9, 2007)
    stu4 = Student(456, "Peter", "Townshend", [87, 92, 98, 94, 92], d4)
    roll.addStudent(stu4)

    print (roll)

    print ("Class Average:", roll.classAverage())
    

main()
