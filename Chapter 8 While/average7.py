# average7.py
#    text p. 245
#    Computes the average of numbers in a file.
#    Uses nested loops so that there may be more than one number on a line.

import string

def main():
##    fileName = raw_input("What file are the numbers in? ")
##    infile = open(fileName,'r')
    infile = open("nums2.dat",'r')
    sum = 0.0
    count = 0
    line = infile.readline()
    while line != "":
        # update sum and count for values in line
        for xStr in string.split(line, ","):
            sum = sum + eval(xStr)
            count = count + 1
        line = infile.readline()
    print "\nThe average of the numbers is", sum / count

main()

