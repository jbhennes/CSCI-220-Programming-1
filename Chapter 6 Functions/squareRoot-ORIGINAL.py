# squareRoot-ORIGINAL.py
# Author: Pharr

import math

def main():
    print "This program approximates a square root using Newton's method."
    print "It also shows the math library's value for the square root,"
    print " and the difference between the two values."
    print

    number = input("Enter the number whose root is to be extracted: ")
    times = input("Enter the number of times to improve the guess: ")
    print

    # Initial guess of the number
    # guess is in floaing point even if number was an int
    guess = number / 2.0

    # Newton's method for approximating the square root:
    for rep in range(times):
        guess = (guess + (number / guess)) / 2.0

    # square root computed by math library function:
    squareRoot = math.sqrt(number)

    # Formatted output to show more decimal places:
    print
    print "Approximate value of square root = %20.18f" % (guess)
    print "Square root using math library   = %20.18f" % (squareRoot)
    print
    print "Difference = %20.18f" % (guess - squareRoot)
    
main()
