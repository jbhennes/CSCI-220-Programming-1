# Factorial.py
# Computes the factorial up to an upper limit set by the user

def main():
    print "This program calculates the factorial up to",
    print "the upper limit set by the user."
    print

    limit = input("Enter the upper limit: ")

    factorial = 1
    for i in range(limit):
        #import code; code.interact(local = locals())
        factorial = factorial * (i+1)

    print limit, "! =", factorial

main()
