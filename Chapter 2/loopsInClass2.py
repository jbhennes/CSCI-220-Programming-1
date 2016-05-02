def main():
   print ("Prints even values up to limit")
   upperLimit = eval(input("Enter limit: "))
   numLoops = upperLimit // 2 + 1
   for i in range(numLoops):
      even = i * 2
##      print (even, end = " ")
   print("Done. Even = " + str(even))

main()
