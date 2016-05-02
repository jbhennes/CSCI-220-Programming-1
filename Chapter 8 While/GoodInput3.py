## GoodInput3.py

# This program asks the user to enter exactly 12 or 57.

def main():
    
    number = input("Enter the number 12 or 57: ")
    
    # This version applies de Morgan's law to the second version,
    # thus moving the negation in correctly:
    
    while number != 12 and number != 57:
        print "That number was not the requested value.\n"
        number = input("Enter the number 12 or 57: ")

    print "Thank you for entering", number

main()
