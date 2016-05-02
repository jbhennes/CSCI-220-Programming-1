## NameSame.py

# Does the name of the argument have to be the same as that of the parameter?
# Does it have to be different? Can it be a constant?

# Does it have to be a compatible type?

def cube(n):
    return n * n * n

def main():
    print "The parameter is named n."

    n = 3
    print "\nThe argument, n, has the same name as the parameter:"
    print "The cube of", n, "is", cube(n)

    x = 3
    print "\nThe argument, x, has a different name from the parameter:"
    print "The cube of", x, "is", cube(x)

    print "\nThe argument, 3, is a constant:"
    print "The cube of 3 is", cube(3)

    s = "three"
    print "\nThe argument, 'three', is a string:"
    print "The cube of", s, "is", cube(s)

main()
    
