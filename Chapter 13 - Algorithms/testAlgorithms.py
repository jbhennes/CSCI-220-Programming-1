#import algorithms
from algorithms import *
from random import randint

def main():
##    numbers = [-18, -1, 2, 5, 8, 9, 17, 20, 28, 32, 50, 50, 50]
####    print(numbers)
##    searchValues = [20, 5, 19, 50, -20, -18, -7, 2, 12, 25, 28, 35, 50, 60]
####    pos = biSearch(-20, numbers)
####    print("8 found at: " + str(pos))
##    
####    numbers = ["apple", "april", "bcd", "bobby sue", "fred", "home"]
####    searchValues = ["bcd", "zoo", "ant"]
####
####    numbers = list(range(1000000))
####    searchValues = [99999999]
##    
##    #for i in range(-20, 60, 5):
##    #for i in numbers:
##    #for i in [3]:
####    for val in searchValues:
####        print("Searching for " + str(val))
####        pos = biSearch(val, numbers)
####        if pos == -1:
####            print (str(val) + " not found.") # in " + str(numbers))
####        else:
####            print (str(val) + " found at position " + str(pos))# + " in " + str(numbers))
######        print ()
####
##    numbers = []
##    for i in range(100000):
##        numbers.append(randint(1, 5000000))
##
##    numbers.sort()
##    val = numbers[0]
##    print("Searching for: " + str(val) + ".\n")
##    pos = biSearch(val, numbers)
##    if pos == -1:
##        print (str(val) + " not found.") # in " + str(numbers))
##    else:
##        print (str(val) + " found at position " + str(pos))# + " in " + str(numbers))
##    print ()
##
##    pos = searchFor(val, numbers)
##    if pos == -1:
##        print (str(val) + " not found.") # in " + str(numbers))
##    else:
##        print (str(val) + " found at position " + str(pos))# + " in " + str(numbers))
##    print ()
##
##    pos = search(val, numbers)
##    if pos == -1:
##        print (str(val) + " not found.") # in " + str(numbers))
##    else:
##        print (str(val) + " found at position " + str(pos))# + " in " + str(numbers))
##    print ()

    list1 = [18,12,1,24,6,30,8,3,15,22]
    print ("Unsorted list:")
    print (list1)

    selSort(list1)

    print ("\nSorted list:")
    print (list1)

    l2 = ["ban", "home", "apple", "cow", "doe", "zoo"]
    print ("Unsorted list:")
    print (l2)

    selSort(l2)

    print ("\nSorted list:")
    print (l2)
##    
##
main()
