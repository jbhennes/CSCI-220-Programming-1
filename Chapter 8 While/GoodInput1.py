## GoodInput1.py

# This program asks the user to enter exactly 12 or 57.

def main():
    
    number = eval(input("Enter the number 12 or 57: "))
    
    # This version does exactly the opposite of what we want:
    
##    while not(number == 12 or number == 57):
    while number != 12 and number != 57:
        print ("That number was not the requested value.\n")
        number = eval(input("Enter the number 12 or 57: "))
    
    print ("Thank you for entering", number)

main()
