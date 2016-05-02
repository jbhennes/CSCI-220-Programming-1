#Example of file i/o

def main():
   #Open a connection to input file
   infileName = "dataMultiple.txt" #input("Enter the filename: ")
   outfileName = "tyler.doc"
   infile = open(infileName, "r")
   outfile = open(outfileName, "w")
   
##   msg = ""
##   for i in range(1, 109014):
##      msg += str(i) + "\n"
##   
##   outfile = open(outfileName, "w")
##   outfile.write(msg)
##   outfile.close()
   
         
   total = 0
   lineNum = 0
   for line in infile:
      lineNum += 1
      lineInfo = line.split()
      lineTotal = 0
      for numStr in lineInfo:
         lineTotal += eval(numStr)
      print("Line " + str(lineNum) + " Total: {0:8.2f}".format(lineTotal), file=outfile)
      total += lineTotal   
   print("Total: " + str(total), file=outfile)

   outfile.close()
   infile.close()
   print("Data written to " + outfileName + ".")
main()
