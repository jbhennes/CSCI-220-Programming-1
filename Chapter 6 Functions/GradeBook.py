#Gradebook.py
#Practice functions
#In-class exercise #3

def getGrades():
   numGrades = eval(input("How many grades?: "))
   grades = []
   for i in range(numGrades):
      grade = eval(input("Enter grade " + str(i+1) + ": "))
      grades.append(grade)
   return grades

def averageGrades(grades):
   total = 0
   for grade in grades:
      total = total + grade
   average = total/len(grades)
   return average

def increaseScores(grades, adjustAmount):
   for i in range(len(grades)):
      grades[i] = grades[i] + adjustAmount

def main():
   print ("This program gathers grades, finds their ", end = "")
   print ("average, and allows them to be curved.")
   print()

   gradeList = getGrades()
   avg = averageGrades(gradeList)

   print("\nThe grades entered are: ")
   for grade in gradeList:
      print (grade, end = " ")
   print("\nThe average is {0:.3f}\n".format(avg))

   message = "Enter amount to add to/subtract from each grade: "
   change = eval(input(message))

   increaseScores(gradeList, change)

   print()
   print("The adjusted grades are: ")
   for grade in gradeList:
      print (grade, end = " ")

main()
   
   
   
