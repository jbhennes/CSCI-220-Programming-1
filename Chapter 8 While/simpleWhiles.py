def main():
##   print("Grade summer..\n")
##   
####   print("<negative to quit>:\n")
##
##
##   value = eval(input("Enter a number: "))           # <negative to quit>: "))
##   total = 0
##   while value >= 0:
##      total += value
##      print(total)
##      value = eval(input("Enter a number <negative to quit>: "))
##            
##   print("Last entered:", value)
##   print("Final total:", total)
   
##   print("Final total is:", total)


##      print("Guess my magic number!")
##      
##      magicNum = 5
##      num = eval(input("Guess my number: "))
##      numGuesses = 1
##      while (num != magicNum):
##            print("Wrong. Guess again: ", end = "")
##            num = eval(input())
##            numGuesses += 1
##
##            
##      print("You guessed it!!")
##      print("It took " + str(numGuesses) + " guesses.")
      
##   print ("Enter 5 to terminate")
##   num = eval(input("Enter a number: "))
##   while num != 5:
##      print(num)
####      num = eval(input("Enter a number: "))

      total = 0
      count = 0
##      while not (total > 100):
      while total <= 100: 
         count += 1
         total += count
         print(count, total)
         
      print("Final total: ", total)
      print("Final count: ", count)

##   num = 0
##   count = 0
##   while num >= 0:
##      print "Enter a negative to quit"
##      num = input("Enter a number: ")
##      if isinstance(num, str):
##         print "\nYou must enter a number."
##      else:
##         count = count + 1
##   print "You entered " + str(count-1) + " non-negative(s)."

##   num = input("enter a number: ")
##   while (isinstance(num, str)):
##      num = input("enter a number: ")
##   print "You followed directions."

##   total = 0
##   count = 0
##   while total < 100 and count < 5:
##      num = input("Enter a number: ")
##      total = total + num
##      count = count + 1
##      print "Total: " + str(total)
##   if total >= 100:
##      print "total has exceeded or met 100"
##   if count >= 5:
##      print "You entered 5 values"

##
##   num = 1
##   while num > epsilon:
##      num = num - 1
##      print num

##   f1 = .1 + .1 + .1 + .1 + .1 + .1 + .1 + .1 + .1 + .1
##   f2 = .1 * 10
##
##   print f1, f2
##   epsilon = .0001
##   
##   while abs(f1-f2) > epsilon:
##      print f1, f2
##      print "f1: %0.20f" % f1
##      print "f2: %0.20f" % f2

##   num = input("Enter 12 or 57: ")
##   while not(num == 12 or num == 57):
##      num = input("Enter 12 or 57: ")
##   while not (isinstance(num,str)):
##      num = input("Enter a value: ")
main()
