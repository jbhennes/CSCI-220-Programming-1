def main():
   outfile = open("john.txt", "w")
   output = "Hello\n"
   output = output + "Goodbye"
   print "Data written to " + "john.txt"
   outfile.write(output)
   outfile.close()   

main()

