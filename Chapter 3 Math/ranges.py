# ranges.py
# Author: Pharr

#    Program to llustrate versions of range

def main():
    n = input("Please enter a whole number: ")
    print "A range with a single parameter, n, generates"
    print "the ints from 0 to n-1."
    for number in range(n): 
       print number

    print 
    n = input("Please enter a whole number: ")
    print "A range with a two parameters, 1 and n+1, generates"
    print "the ints from 1 to n."
    for number in range(1, n+1): 
       print number

    print 
    low = input("Please enter a lower whole number: ")
    high = input("Please enter a higher whole number: ")
    print "A range with a two parameters, low and high, generates"
    print "the ints from low to high-1."
    for number in range(low, high): 
       print number

    print 
    low = input("Please enter a lower whole number: ")
    high = input("Please enter a higher whole number: ")
    step = input("Please enter a step by which to go up: ")
    print "A range with a three parameters, low, high and step,"
    print "generates the ints from low to high-1, going up by"
    print "the value in step."
    for number in range(low, high, step): 
       print number

    print 
    high = input("Please enter a higher whole number: ")
    low = input("Please enter a lower whole number: ")
    print "A range with a three parameters, high, low and -1,"
    print "generates the ints from high to low+1, going DOWN by 1."
    for number in range(high, low, -1): 
       print number

    print 
    high = input("Please enter a higher whole number: ")
    low = input("Please enter a lower whole number: ")
    step = input("Please enter a step by which to go down (negative): ")
    print "A range with a three parameters, high, low and step,"
    print "generates the ints from high to low+1, going DOWN by"
    print "the value in step."
    for number in range(high, low, step): 
       print number

main()
