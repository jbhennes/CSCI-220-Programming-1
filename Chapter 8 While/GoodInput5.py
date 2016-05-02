## GoodInput5.py

# This program asks the user to enter exactly 12 or 57.

# This version is WRONG!!!!!!

def main():
    
    number = input("Enter the number 12 or 57: ")
    
    # This version tries to move the negation in, but incorrectly,
    # thus creating an infinite loop:
    
    while number != 12 or number != 57:
        print "That number was not the requested value.\n"
        number = input("Enter the number 12 or 57: ")

    print "Thank you for entering", number

main()
