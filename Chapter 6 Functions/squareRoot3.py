# squareRoot3.py
# Author: Pharr
# Modified: Stalvey

import math

# Computes a square root using Newton's method
# This version iterates until the difference between two
# approximations is very small
# This version can deal with negative input:
def squareRoot(number):
    if number < 0:
        return -1
    else:
       # value of epsilon
        epsilon = 0.000000001
        
        # Initial guess of the number
        # guess is in floating point even if number was an int
        previous = number
        guess = number / 2.0

        # Newton's method for approximating the square root:
        while abs(previous - guess) > epsilon:
            previous = guess
            guess = (guess + (number / guess)) / 2.0

        return guess

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
