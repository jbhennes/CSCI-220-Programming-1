# studentDriver - creates Student objects and tests Student methods

from Student import Student
from Date import Date


def main():
    date = Date()
    date.setDate(12, 28, 2000)
    scores = [90, 93]
    
    chad = Student(1, "Chad", "Williams", scores, date)
    chad.addGrade(93)
    chad.addGrade(89)
    chad.addGrade(97)
    print (chad.getName() + "'s grades are: " + str(chad.getGrades()))
    print ("Average: " + str(chad.calcAvg()))
    

    date.setDate(3,20,2000)
    scores.append(42)
    brad = Student(2, "Brad", "Smith", scores, date)
    print ()
    print (str(brad))

    print ("\n" + str(chad))

    print ("\nIn main scores = " + str(scores))
main()
