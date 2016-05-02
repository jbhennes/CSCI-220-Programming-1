# average5.py
#    text p. 243
#    Computes the average of numbers listed in a file, using a for loop.

def main():
##    fileName = raw_input("What file are the numbers in? ")
##    infile = open(fileName,'r')
    infile = open("nums.dat",'r')
    sum = 0.0
    count = 0
    for line in infile:
        sum = sum + eval(line)
        count = count + 1
    print "\nThe average of the numbers is", sum / count

main()

