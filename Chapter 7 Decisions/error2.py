import math

def main():
##   try:
##      num = eval(input("Enter number: "))
##      num = num + 1
##      print ("num = " + str(num))
##   except:
##      print ("Input must be a number or a defined variable")
##
##   try:
##      num = eval(input("Enter number: "))
##      num = num + 1
##   except:
##      print("Input must be a number")
##      print("Value defaulted to zero")
##      num = 0
##   print ("num = " + str(num))
   print("sqrt(9) = " + str(calculateSqRt(9)))
   print("\nsqrt(-9) = " + str (calculateSqRt(-9)))
   print("\nsqrt(\"bob\") = " + str(calculateSqRt("bob")))

   print("\'\"\'")
         
def calculateSqRt(num):
   try:
      answer = math.sqrt(num)
   except ValueError:
      print("Can't calculate squareroot of negative")
      print("Returning 0")
      answer = 0
   except TypeError:
      print("Need a float")
      answer = 0
   return answer
      
main()
