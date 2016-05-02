from simpleMath import *

def main():
   print ("In main before call.")
   total = 9134135
   print ("Total is (in main)" + str(total))
   total = add(3,5)
   print ("Total is (in main)" + str(total))
   print ("In main after call.")
   total = add(-3, 5)
   for i in range(total):
      print (i, end=",")
   print()
   for i in range(5):
      print (total)

   division = div(27,3.8)
   print (division)
main()


