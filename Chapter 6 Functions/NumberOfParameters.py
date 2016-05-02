## NumberSame.py

# Does the number of parameters have to be the same the number of arguments?
# Does the order have to be the same?

def difference(minuend, subtrahend=167):
    return minuend - subtrahend

def main():
    minuend = 7
    subtrahend = 5

    print "The difference of", minuend, "and", subtrahend, "is",
##    print difference(subtrahend, minuend)
##    print difference(subtrahend=27)
##    print difference()
    print difference(minuend)
##    print difference(minuend, subtrahend, minuend)

##    print "The difference of", minuend, "and", subtrahend, "is",
##    print difference(100,subtrahend=8)


main()
    
