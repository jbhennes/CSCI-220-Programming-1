# readNumericData.py
# illustrates how to retrieve numeric data from a file

def main(): 

    #reading data from a file for calculations - fine for integer values
##    infileName = "data.txt"
##    infileName = "dataWithFloat.txt"
##    infile = open(infileName,"r")
##    print ("\n*** Integer values ***")
##    for line in infile:
##        print ("Value read: " + line[:-1])
##        value = int(eval(line)) + 1
##        print ("Value plus 1: " + str(value))
##        print ()
##    infile.close()

    # Reading multiple pieces of numeric data per line
##    infileName = "dataMultiple.txt"
##    infile = open(infileName,"r")
##    print ("\n*** Multiple data per line ***")
##    for line in infile:
##        values = line.split()
##        for valueStr in values:
##            print ("Value read: " + valueStr)
##            value = eval(valueStr) + 1
##            print ("Value plus 1: " + str(value))
##            print ()
##    infile.close()


##    # Reading multiple pieces of data per line - fixed length of data
    # This code segment reads in from files with the format
    # studentFirstName studentLastName grade1 grade2 grade3
    # and computes and outputs the student's gpa
##    print ("Outputs student data to a file")
##    infileName = "dataStudentInfo3Grades.txt"
##    outfileName = "studentInfoOutput.txt"
##    numGrades = 3
##    startPos = 2
##    infile = open(infileName,"r")
##    outfile = open(outfileName, "w")
##    print ("\n*** Student Info with 3 grades ***", file=outfile)
##    for line in infile:
##        values = line.split()
##        total = 0
##        for i in range(startPos, startPos + numGrades):
##            total = total + float(values[i])
##        average = total / numGrades
##        message = values[0] + " " + values[1]
##        message = message + "'s GPA: {0:.3f}".format(average)
##        print (message, file=outfile)
##    infile.close()
##    print()
##    print("Your data has been written to " + outfileName)


    # Reading multiple pieces of data per line - unknown length of data
    # This code segment reads in from files with the format
    # studentFirstName studentLastName grade1 grade2 grade3 ... gradeN
    # and computes and outputs the student's gpa
    infileName = "dataStudentInfoMultipleGrades.txt"
    infile = open(infileName,"r")
    print ("\n*** Student Info with Multiple grades ***")
    for line in infile:
        values = line.split()
        total = 0
        count = 0
        for i in range(2,len(values)):
            total = total + float(values[i])
            count = count + 1
        average = total / count
        print (values[0] + " " + values[1] + "'s GPA: {0:.3f}".format(average))
    infile.close()    


main()

        
    
