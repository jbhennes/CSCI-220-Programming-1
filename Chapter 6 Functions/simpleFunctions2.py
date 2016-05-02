##from simpleMath import *
from simpleMath import *

#Input: Two numbers
#Output: returns the absolute difference of the numbers

def subtract(op1, op2):
   total = abs(op1 - op2)

   return total

def add(str1, str2):
   return str1 + " " + str2

def abs(number):
   return (number/2)
   

def main():
   print("First iteration...")
   num = eval(input("Num: "))
   total = subtract(num,7)
   print("Difference:", total)

   print("\nalgjl;asgjklbn,bnladfhg\n")

   print("Second iteration....")
   num = subtract(0, -3)

   for i in range(int(num)):
      print("Hello")

##   print("Add: ", add(4,5))
##   print(subtract(4, 5))
##   print(div(6,8))
##   print(add("Hello", "How are you?"))
   

   
main()
