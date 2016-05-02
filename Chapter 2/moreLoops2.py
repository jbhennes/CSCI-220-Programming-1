#more loops

def main():
   print ("Outputs odd numbers between 1 and 20")
   for i in range(10):
      odd = i * 2 + 1
      print (odd)
      
   print ("Outputs even numbers between 1 and 20")
   for i in range(10):
      even = (i+1) * 2
      print (even, end=" ")

   print ("\nOutputs even numbers between 1 and 20")
   for i in range(10):
      even = i * 2 + 2
      print (even, end=" ")

   print()
   howMany = eval(input("Enter how many iterations: "))
   total = 0
   for i in range(howMany):
      value = eval(input("Enter the value: "))
      total = total + value
   print ("Total: ", total)

   #summation formula
   howMany = eval(input("Enter how many iterations: "))
   total = 0
   for i in range(howMany+1):
      total = total + i
      print ("Total: ", total)

   #factorial formula
   print ("Calculates factorial.")
   howMany = eval(input("Upper limit: "))
   fact = 1
   for i in range(howMany):
      fact = fact * (i + 1)
##      print ("Factorial: ", fact)
      print (i+1, "! = ", fact)

   print ("Averaging values")
   num1 = eval(input("Enter a value: "))
   num2 = eval(input("Enter a value: "))
   num3 = eval(input("Enter a value: "))
   total = num1 + num2 + num3
   avg = total / 3.0
   print ("Average: ", avg)
main()
