# binary search implementations
# Assumes data is sorted

from binarySearchFunctionOnly import biSearch

def main():
    numbers = [-18, -1, 2, 5, 8, 8, 8, 9, 17, 20, 28, 32, 50, 50, 50]
    searchValues = [20, 5, 19, 50]#, -20, -18, -7, 2, 12, 25, 28, 35, 50, 60]


    
##    numbers = ["apple", "april", "bcd", "bobby sue", "fred", "home"]
##    searchValues = ["bcd", "zoo", "ant"]

##    numbers = list(range(1000000))
##    searchValues = [99999999]

    searchVal = 8
    foundAt = biSearch(searchVal, numbers)
    print("Found", searchVal, "at", foundAt)
    
    #for i in range(-20, 60, 5):
    #for i in numbers:
##    #for i in [3]:
##    for val in searchValues:
##        print("Searching for " + str(val))
##        pos = biSearch(val, numbers)
##        if pos == -1:
##            print (str(val) + " not found.") # in " + str(numbers))
##        else:
##            print (str(val) + " found at position " + str(pos))# + " in " + str(numbers))
##        print ()

main()
