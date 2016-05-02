## writeFile.py

import string

def main():
    print "Executing writeFile.py"

    # for testing:
    inFileName = "domainNames.txt"
    outFileName = "companyNames.txt"

    #inFileName = raw_input("Enter the file of domain names: ")
    #outFileName = raw_input("Enter the file of company names: ")

    infile = open(inFileName, "r")
    outfile = open(outFileName, "w")

    for line in infile:
        splitLine = string.split(line, ".")
        #print splitLine
        outfile.write(splitLine[1] + "\n")

    infile.close()
    #outfile.close()

main()
