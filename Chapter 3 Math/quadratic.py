# quadratic.py
#    A program that computes the real roots of a quadratic equation.
#    Illustrates use of the math library.
#    Note: This program crashes if the equation has no real roots.


import math  # Makes the math library available.

def main():
    print ("This program finds the real solutions to a quadratic")
    print ()

    a = eval(input("Please enter the coefficient a: "))    
    b = eval(input("Please enter the coefficient b: "))
    c = eval(input("Please enter the coefficient c: "))
    
    
    discRoot = math.sqrt(b * b - 4 * a * c)
    root1 = (-b + discRoot) / (2 * a)
    root2 = (-b - discRoot) / (2 * a)

    print ()
    print ("The solutions are:", root1, root2)
    print ("The value of pi is: " + str(math.pi))

main()
