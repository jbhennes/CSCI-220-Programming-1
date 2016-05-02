## BadNestedIf.py

# THIS PROGRAM IS DECEPTIVE!!!
# This is a "bad" example of a nested conditional.

# Enter 1 2
# Then 1 -2
# Why is the message wrong?

# Then enter -1 2
# Then enter -1 -2
# What happened to the message?

def main():
    
    n1, n2 = input("Enter two integers separated by commas: ")
        
    if n1 > 0:
        if n2 > 0:
            print "Both integers are positive."
        else:
            print "First integer is <= zero."
        
main()
