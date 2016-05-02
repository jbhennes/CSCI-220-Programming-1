# changeMaker.py
# Author: RoxAnn H. Stalvey

#    Given a value of money this program displays the smallest number
#    of dollars and coins equal to that amount.

import math

def main():
    print ("Given a value of money, this program displays the smallest")
    print ("number of dollars and coins equal to that amount.")

    amount = eval(input("Enter the amount of money: "))
    amount = int(amount * 100)
##    print (amount)
    
    dollars = amount // 100
    amount = amount % 100
    quarters = amount // 25
    amount = amount % 25
    dimes = amount // 10
    amount = amount % 10
    nickles = amount // 5
    amount = amount % 5

    print ("The smallest amount of change is:")
    print (dollars, "dollars")
    print (quarters, "quarters")
    print (dimes, "dimes")
    print (nickles, "nickles")
    print (amount, "pennies")


main()
