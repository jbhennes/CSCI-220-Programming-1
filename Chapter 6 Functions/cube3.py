## cube3.py

# The function cube() returns the cube of its parameter.

def main():
    n = input("Enter a number to be cubed: ")

    theCube = cube(n)

    print "The cube of", n, "is", theCube

main()

def cube(n):
    return n * n * n
