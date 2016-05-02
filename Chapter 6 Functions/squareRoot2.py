# squareRoot2.py
# Author: Pharr

import math

# Computes a square root using Newton's method
# This version iterates until the difference between two
# approximations is very small.
# value of epsilon
def squareRoot(number):
    epsilon = 0.000000001
    
    # Initial guess of the number
    # guess is in floaing point even if number was an int
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

    number = input("Enter the number whose root is to be extracted: ")
    print

    # square root computed by Newton's method:
    newtonsRoot = squareRoot(number)

    # square root computed by math library function:
    libRoot = math.sqrt(number)

    # Formatted output to show more decimal places:
    print
    print "Approximate value of square root = %20.18f" % (newtonsRoot)
    print "Square root using math library   = %20.18f" % (libRoot)
    print
    print "Difference = %20.18f" % (newtonsRoot - libRoot)
    
main()
