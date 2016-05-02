
#Accumulating problems

def main():
##   print ("Calculates number of siblings")
##
##   numLoops = eval(input("Number of people to question: "))
##   numSiblings = 0
##   
##   for i in range(numLoops):
##      siblings = eval(input("Enter number of siblings: "))
##      numSiblings = numSiblings + siblings
##   print ("Total number of siblings is " + str(numSiblings) + ".")

##   print ("Calculates sigma")
##
##   upperLimit = eval(input("Enter upper limit: "))
##   total = 0
##
##   for i in range(upperLimit + 1):
##      total = total + i
##      print ("i: " + str(i))
##      print ("total: " + str(total))
##
##   print ("Total: " + str(total))

   print ("Calculates factorial")

   upperLimit = eval(input("Enter upper limit: "))
   total = 1

   for i in range(upperLimit):
      total = total * (i+1)
      print ("i+1: " + str(i+1))
      print ("total: " + str(total))

   print ("Total: " + str(total))
   
main()
