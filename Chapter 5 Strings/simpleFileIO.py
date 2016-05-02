import string

def main():
   infile = open("values.txt", "r")
   
   for line in infile:
      #line = string.replace(line,"\n","")
      num = eval(line)
      num = num * 2
      print line[:len(line) - 1] + ": " + str(num)
   

   infile.close()
   print "Done"
   
main()
