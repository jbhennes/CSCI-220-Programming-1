# average2B.py
#    text pp. 238-9
#    A program to average a set of numbers.
#    Illustrates an indefinite, interactive loop with two accumulators.

#    Modified so that the user doesn't have to enter any data,
#    and it doesn't crash in that case.

def main():
    sum = 0.0
    count = 0
    moredata = raw_input("Do you have a number (yes or no)? ")
    while moredata[0] == "y":
        x = input("Enter a number >> ")
        sum = sum + x
        count = count + 1
        moredata = raw_input("Do you have more numbers (yes or no)? ")
    if count != 0:
        print "\nThe average of the numbers is", sum / count
    else:
        print "\nNo numbers were entered"

main()
