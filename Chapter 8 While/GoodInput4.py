## GoodInput4.py

# This program asks the user to enter exactly 12 or 57.

def main():

    keepGoing = True  # this is a boolean variable
    
    number = input("Enter the number 12 or 57: ")
    
    # This version uses a boolean variable:
    
    while keepGoing:
        print "That number was not the requested value.\n"
        number = input("Enter the number 12 or 57: ")
        if number == 12 or number == 57:
            keepGoing = False

    print "Thank you for entering", number

main()
