def main():

##   num = eval(input("Enter number (>=5 to quit): "))
##
##   while num < 5:
##      print ("num = " + str(num))
##      num = eval(input("Enter number (>=5 to quit): "))
##
##   print("Done!")
##
##   totalFor = 0
##   for i in range(1001):
##      totalFor = totalFor + i
##
##   i = 0
##   total = 0
##   while i <= 1000 and total < 200:
##      total = total + i
##      i = i + 1
##      
##
##   print ("For total = " + str(totalFor))
##   print ("While total = " + str(total))
##   print ("Num executions = " + str(i))

   num = eval(input("Enter 12 or 57 to quit: "))

   while num != 12 and num != 57: #not(num == 12 or num == 57):
      print("You entered " + str(num))
      num = eval(input("Enter 12 or 57 to quit: "))

   print("Good job!")
   

main()
