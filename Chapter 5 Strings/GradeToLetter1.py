## GradeToLetter1.py
##
## User enters a grade in the range 0-5. Letter grade is displayed.

def main():
   
   letterGrades = "FFDCBA"

   grade = input("Enter numerical grade: ")
   print "Letter grade:", letterGrades[grade]

   # The following loop tests all grades in the  range.

   ##for grade in range(6):
   ##    print "Number grade:", grade,
   ##    print "Letter grade:", letterGrades[grade]
   ##    print
