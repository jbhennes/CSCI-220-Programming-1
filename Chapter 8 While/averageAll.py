# average1.py
# Examples of various loops from text: Zelle.
# All average a set of numbers.

def main():
    #Illustrates a counted loop (for loop) with an accumulator.
##    n = eval(input("How many numbers do you have? "))
##    total = 0.0
##    for i in range(n):
##        x = eval(input("Enter a number >> "))
##        total = total + x
##    if n > 0:
##        print ("\nThe average of the numbers is", total / n)
##    else:
##        print ("\nNo numbers to average.")

    #Using a while loop. 
    #Yes/No question of user. --> Interactive loop
##    total = 0
##    count = 0
##    moredata = "yes" #Forces initial test to be true
##    while moredata[0] == "y":
##        x = eval(input("Enter a number >> "))
##        total = total + x
##        count = count + 1
##        moredata = input("Do you have more numbers (yes or no)? ")
##    #count will be atleast 1
##    print ("\nThe average of the numbers is", total / count)
    

    #Using a while loop. 
    #Yes/No question of user. --> Interactive loop
    #Priming read - ask user for answer to determine whether
    #loop should be executed
##    total = 0
##    count = 0
##    moredata = input("Do you have numbers (y = yes or n = no)? ")
##    while moredata[0] == "y":
##        x = eval(input("Enter a number >> "))
##        total = total + x
##        count = count + 1
##        moredata = input("Do you have more numbers (yes or no)? ").lower()
##    if count > 0:
##        print ("\nThe average of the numbers is", total / count)
##    else:
##        print ("\nNo numbers to average.")

    #While loop with sentinel value.  (Sentinel is a stopping
    #value.) Better choice than interactive loop, in this case,
    #because less data entry from the user.  However, sentinel
    # value can not be part of average, thus this code can only
    # average non-negative numbers.
##    
##    total = 0
##    count = 0
##    x = eval(input("Enter a number (negative to quit) >> ")) #priming read
##    while x >= 0:        
##        total = total + x
##        count = count + 1
##        x = eval(input("Enter a number (negative to quit)>> "))
##    if count > 0:
##        print ("\nThe average of the numbers is", total / count)
##    else:
##        print ("\nNo numbers to average.")

##    total = 0
##    count = 0
##    x = input("Enter a number (Type \"quit\" to quit) >> ") #priming read
##    while x != "quit":
##        x = eval(x)
##        total = total + x
##        count = count + 1
##        x = input("Enter a number (Type \'quit\' to quit) >> ")
##    if count > 0:
##        print ("\nThe average of the numbers is", total / count)
##    else:
##        print ("\nNo numbers to average.")

    #reading from a file - for loop
    ##    fileName = input("What file are the numbers in? ")
    ##    infile = open(fileName,'r')
##    infile = open("nums.dat",'r')
##    total = 0.0
##    count = 0
##    for line in infile:
##        total = total + eval(line)
##        count = count + 1
##    if count > 0:
##        print ("\nThe average of the numbers is", total / count)
##    else:
##        print ("\nNo numbers to average.")

    # reading from a file - while loop
    ##    fileName = input("What file are the numbers in? ")
    ##    infile = open(fileName,'r')
    infile = open("nums.dat",'r')
    total = 0.0
    count = 0
    line = infile.readline()
    while line != "" and eval(line) !=0:
        total = total + eval(line)
        count = count + 1
        line = infile.readline()
    if count > 0:
        print ("\nThe average of the numbers is", total / count)
    else:
        print ("\nNo numbers to average.")

    #Average of numbers with multiple data per line -->
    # Nested loop
    ##    fileName = input("What file are the numbers in? ")
    ##    infile = open(fileName,'r')
##    infile = open("nums2.dat",'r')
##    total = 0.0
##    count = 0
##    line = infile.readline()
##    while line != "":
##        # update sum and count for values in line
##        for xStr in line.split(","):
##            total = total + eval(xStr)
##            count = count + 1
##        line = infile.readline()
##    if count > 0:
##        print ("\nThe average of the numbers is", total / count)
##    else:
##        print ("\nNo numbers to average.")
main()
