def main():

   x1 = input("Enter a number: ")
   x2 = input("Enter a number: ")
   x3 = input("Enter a number: ")

   if x1 > x2:
      maximum = x1
   else:
      maximum = x2
      
   if x3 > maximum:
      maximum = x3

   print str(maximum) + " is biggest."
   
main()
