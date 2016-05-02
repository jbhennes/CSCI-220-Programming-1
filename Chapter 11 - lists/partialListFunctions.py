# listFunctions.py
# Author: Pharr

#    Program to implement the list operations count and reverse.

from math import sqrt

def getElements():
    list = []     # start with an empty list

    # sentinel loop to get elements
    item = raw_input("Enter an element (<Enter> to quit) >> ")
    while item != "":
        list.append(item)   # add this value to the list
        item = raw_input("Enter an element (<Enter> to quit) >> ")
    return list

# count(list, x) counts the number of times that x occurs in list
def count(list, x):
    num = 0
    for item in list:
        if item == x:
            num = num + 1
    return num
    
# isinBad(list, x) returns whether x occurs in list
# This is bad because it is inefficient.
def isinBad(list, x):
    occurs = False
    for item in list:
        if item == x:
            occurs = True
    return occurs
    
# isin(list, x) returns whether x occurs in list
# This is better because it is more efficient.
def isin(list, x):
    return False
    
# reverse(list) reverses the list
# This function destructively modifies the list.
# It would be easier to write if it just returned the reversed list!
def reverse(list):
    print "Your code will reverse the list in place"

def main():
    print 'This program reads a list, counts the number of elements,'
    print 'and reverses the list.'

    data = getElements()
    item = raw_input("Enter element you want to count in the list: ")
    theCount = count(data, item)
    print "\nTnere are", theCount, "occurrences of", item, "in", data

    item = raw_input("\nEnter element that should occur in the list: ")
    occurs = isinBad(data, item)
    if occurs:
        print item, "occurs in", data
    else:
        print item, "does not occur in", data
    occurs = isin(data, item)
    if occurs:
        print item, "occurs in", data
    else:
        print item, "does not occur in", data

    reverse(data)
    print "\nTne reversed list is", data

main()
