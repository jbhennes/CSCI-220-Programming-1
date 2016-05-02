## GradeToLetter.py
##
## User enters a grade in the range 0-100. Letter grade is displayed.

def main():
   letterGrades = "FFFFFFDCBAA"
   ##
   grade = input("Enter numerical grade: ")
   grade = grade / 10
   print "Letter grade:", letterGrades[grade]

   # Following to test ranges:

   ##for g in range(0, 101, 5):
   ##    grade = g / 10
   ##    print g, letterGrades[grade]
   ##
   ##print
   ##for g in range(1, 101, 5):
   ##    grade = g / 10
   ##    print g, letterGrades[grade]
   ##
   ##print
   ##for g in range(4, 101, 5):
   ##    grade = g / 10
   ##    print g, letterGrades[grade]
