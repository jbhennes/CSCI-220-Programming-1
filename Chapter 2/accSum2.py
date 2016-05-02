#Accumulating values

def main():
##   print("Counts total number of siblings.")
##
##   numStudents = eval(input("Enter number of students: "))
##   numSiblings = 0
##
##   for i in range(numStudents):
##      siblings = eval(input("Enter number of siblings: "))
##      numSiblings = numSiblings + siblings
##      print ("Siblings = " + str(siblings))
##      print ("Total = " + str(numSiblings))
##
##   print ("\nTotal number of siblings: " + str(numSiblings))

##   print ("Calculate sigma.")
##
##   upperLimit = eval(input("Enter upper limit: "))
##   total = 0
##
##   for i in range(upperLimit + 1):
##      total = total + i
##      print ("i: " + str(i))
##      print ("Total: " + str(total))
##
##   print ("\nSigma: " + str(total))
##
   print ("Calculate factorial.")

   upperLimit = eval(input("Enter upper limit: "))
   total = 1

   for i in range(upperLimit):
      total = total * (i + 1)
      print ("i+1: " + str(i+1))
      print ("Total: " + str(total))

   print ("\nFactorial: " + str(total))
   
main()
