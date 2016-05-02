def main():
   #1. convert the following
##   total = 1
##   for i in range(5):
##      total = total * i
##      print (i, total)
##
##   #2. sum the values input by the user until  the user
##   #   enters a value greater than 30
##
##   #3. print the values entered by the user until the
##   #   user enters a negative value or 100
##   
##   total = 1
##   i = 0
##   while (i < 5):
##      total = total * i
##      print (i, total)
##      i = i + 1
##
##   
##   print("\n2.")
##   total = 0
##   value = eval(input("Enter value: "))
##
##   while (value <= 30):
##      total = total + value
##      print (total)
##      value = eval(input("Enter value: "))
##
   print("\n3.")
   value = eval(input("Enter value: ")) #priming read
   while not (value < 0 or value == 100):
      print (value)
      value = eval(input("Enter value: "))

   #3. print the values entered by the user until the
   #   user enters a negative value or 100
   print("\n3. another way")
   value = 0
##   while not (value < 0 or value == 100):
   while (value >= 0 and value != 100):
      value = eval(input("Enter value: "))
      if (value >= 0 and value != 100):
         print (value)
      
main()
