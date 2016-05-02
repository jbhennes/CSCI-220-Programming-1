# average6.py
#    Computes the average of numbers listed in a file, using a while loop.
#    Illustrates a sentinel loop using an empty line as the sentinel.

def main():
##    fileName = raw_input("What file are the numbers in? ")
##    infile = open(fileName,'r')
    infile = open("nums.dat",'r')
    sum = 0.0
    count = 0
    line = infile.readline()
    while line != "":
        sum = sum + eval(line)
        count = count + 1
        line = infile.readline()
    print "\nThe average of the numbers is", sum / count

main()

