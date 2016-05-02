# factorialAscending.py
# Author: Pharr

#    Program to compute the factorial of a number
#    Illustrates for loop, starting with  value other than zero,
#    with an accumulator

def main():
    n = input("Please enter a whole number: ")
    fact = 1
    for factor in range(1, n+1): 
       fact = fact * factor
    print "The factorial of", n, "is", fact

main()
