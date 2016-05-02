## MaxOfTwo.py
## Displays the larger of two user-specified values

def main():
    
    print "This program displays the larger of two user-specified values." 	

    # Enter the two numbers

    value1 = input("Enter a number: ")
    value2 = input("Enter another number: ")

    # Determine the maximum

    if value1 == value2:
        print "The values are equal"
    else:
        if value1 < value2:        # is value2 larger?
            maximum = value2       # yes: value2 is larger
        else:
            maximum = value1       # no: value2 is not larger

        # Display maximum
        print "The maximum of", value1, "and", value2, "is", maximum

main()
