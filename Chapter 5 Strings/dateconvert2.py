# dateconvert2.py
# Author: Zelle
# text pp. 101-2
# Modified by Pharr

#    Converts day month and year numbers into two date formats

import string

def main():
    print "Asks for a date as numbers and displays it in other formats\n"
    
    # get the day month and year
    day = input("Please enter the day as a number: ")
    month = input("Please enter the month as a number: ")
    year = input("Please enter the year as a number: ")

    date1 = str(month)+"/"+str(day)+"/"+str(year)

    months = ["January", "February", "March", "April",
              "May", "June", "July", "August",
              "September", "October", "November", "December"]
    monthStr = months[month-1]
    date2 = monthStr+" " + str(day) + ", " + str(year)

    print "\nThe date is", date1, "or", date2

main()

