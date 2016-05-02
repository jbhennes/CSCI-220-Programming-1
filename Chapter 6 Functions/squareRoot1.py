# squareRoot1.py
# Author: Pharr

import math

def squareRoot(number, times):
    # Computes a square root using Newton's method
    
    # Initial guess of the number
    # guess is in floaing point even if number was an int
    guess = number / 2.0

    # Newton's method for approximating the square root:
    for rep in range(times):
        guess = (guess + (number / guess)) / 2.0

    return guess

def main():
    print ("This program approximates a square root using Newton's method.")
    print ("It also shows the math library's value for the square root,")
    print ("and the difference between the two values.")
    print()

    number = input("Enter the number whose root is to be extracted: ")
    times = input("Enter the number of times to improve the guess: ")
    print ()

    # square root computed by Newton's method: 
    newtonsRoot = squareRoot(number, times)

    # square root computed by math library function:
    libRoot = math.sqrt(number)

    # Formatted output to show more decimal places:
    print ()
    mess = "Approximate value of square root = "
    mess = mess + "{0:20.18f}".format(newtonsRoot)
    mess = mess + "\n"
    mess = mess + "Square root using math library   = "
    mess = mess + "{0:20.18f}".format(libRoot) + "\n" + "\n"
    mess = mess + "Difference = {0:20.18f}".format(newtonsRoot - libRoot)
    print (mess)



    
main()
