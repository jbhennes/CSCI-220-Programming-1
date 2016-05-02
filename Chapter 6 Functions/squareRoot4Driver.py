# squareRoot4Driver.py
# Author: Pharr

from squareRoot4 import squareRoot

def main():
    print "This program approximates a square root using Newton's method."
    print "It also shows the math library's value for the square root,"
    print "and the difference between the two values."
    print
    print "This version can deal with negative input."
    print

    number = input("Enter the number whose root is to be extracted: ")
    print

    # square root computed by Newton's method:
    newtonsRoot = squareRoot(number)

    # Formatted output to show more decimal places:
    if newtonsRoot < 0:
        print "Cannot take the square root of a negative number:", number
    else:
        print "Approximate value of square root = %20.18f" % (newtonsRoot)

main()
