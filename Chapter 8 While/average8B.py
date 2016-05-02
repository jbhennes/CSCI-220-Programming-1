# average8.py
#    Based on average2.py from the text, this asks whether the user has more
#    input, but will average no more than five numbers.

#    Illustrates a compound condition: conditional loop plus counting loop.

def main():
    print "This program will average up to five numbers."
    print "It will stop asking for numbers after five.\n"
    
    sum = 0.0
    count = 0

    moredata = raw_input("Do you have a number (yes or no)? ")

    while moredata[0] == "y" and count < 5:
        x = input("Enter a number >> ")
        sum = sum + x
        count = count + 1
        
        # Better version of the question. If you have already entered
        # five numbers, it doesn't ask whether you want to enter more.
        if count == 5:
            print "The average will now be computed."
        else:
            moredata = raw_input("Do you have more numbers (yes or no)? ")

    # Most versions in the text crash if no numbers are entered.
    # This conditional fixes that problem.
    if count != 0:
        print "\nThe average of the numbers is", sum / count
    else:
        print "\nNo numbers were entered"

main()
