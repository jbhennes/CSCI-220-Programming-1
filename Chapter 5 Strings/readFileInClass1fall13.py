#Example of reading from a file

def main():
   outfileName = "output.txt"
   infile = open("dataMultiple.txt", "r")
   outfile = open(outfileName, "w")

   total = 0
   for line in infile:
      lineInfo = line.split()
      lineTotal = 0
      for item in lineInfo:
         lineTotal += eval(item)
         print(item, end=" ")
      print("Line total: ", lineTotal)
      total += lineTotal

   print("\nTotal: " + str(total))

##   print("Contents written to " + outfileName)
   infile.close()
   outfile.close()

main()
