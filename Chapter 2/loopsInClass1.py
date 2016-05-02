def main():
   # even numbers
   print("Prints even numbers 0..limit")
   upperLimit = eval(input("Enter limit: "))
   numLoops = upperLimit // 2

   print("Even\tOdd")
   for i in range(numLoops):
      even = i * 2
      odd = i * 2 + 1
##      print (str(even) + "\t" + str(odd))
      print(even,"\t",odd)
   even = (i+1) * 2
   print (even)
      
   print("Done")

main()
