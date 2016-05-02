from simpleMath2 import *

def main():
   print ("In main before function call.")
   total = 9876
   print ("In main total is " + str(total))
   total, value= add( 3,5)
   print ("In main total is " + str(total))
   print ("Va;ie: " + str(value))
   print ("In main after function call.")
   value = 3 #eval(input("Enter value: "))
   total, value = add(value,52)
   calculation = total * 3 / 10
   print(calculation)
##   total = add(6,-3)
##   for i in range(total):
##      print (i)
##
   total = div(7,3)
   print ("Division: " + str(total))
   win.getMouse()
   win.close()

main()


   
