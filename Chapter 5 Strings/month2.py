# month.py
#  A program to print the month name, given it's number.


def main():
    
    # months is used as a lookup table
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    
    n = input("Enter a month number (1-12): ")

    print "The month is", months[n-1] + "."

main()
