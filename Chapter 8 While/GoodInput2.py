## GoodInput2.py

# This program asks the user to enter exactly 12 or 57.

def main():
    
    number = input("Enter the number 12 or 57: ")
        
    # This version is the negation of the first,
    # so it does what we want:
    
    while not (number == 12 or number == 57):
        print "That number was not the requested value.\n"
        number = input("Enter the number 12 or 57: ")

    print "Thank you for entering", number

main()
