# studentDriver - creates Student objects and tests Student methods

from StudentWithDate import Student
from Date import Date

def main():
    d1 = Date ()
    d1.setDate(8,15,2006)
    d2 = Date()
    d2.setDate(5, 12, 2000)
    d3 = Date()
    d3.setDate(12, 1, 2004)
    d4 = Date()
    d4.setDate(3, 9, 2007)
    
    chad = Student("Tenessee", "Williams", [90, 93], d1)
    chad.addGrade(93)
    chad.addGrade(89)
    chad.addGrade(97)
    print (chad.getName() + "'s grades are: " + str(chad.getGrades()))
    print ("Average: " + str(chad.calcAvg()))
    
    brad = Student("Bob", "Marley", [95, 90, 92],d2)
    print ()
    print (str(brad)) #What is this printing?
    
    csci220 = []
    csci220.append(chad)
    csci220.append(brad)
    csci220.append(Student("Diana", "Ross", [],d3))
    csci220.append(Student("Peter", "Townsend", [87, 92, 98, 94, 92],d4))

    for student in csci220:
        print ()
        print (student)

    print ()
    for i in range (len(csci220)):
        compare = csci220[1].getEnrollDate().compareTo(csci220[i].getEnrollDate())
        if  compare == 0:
            print (csci220[1].getName() + " enrolled the same day as " + csci220[i].getName())
        elif compare > 0:
            print (csci220[1].getName() + " enrolled after " + csci220[i].getName())
        else:
            print (csci220[1].getName() + " enrolled before " + csci220[i].getName())
main()
