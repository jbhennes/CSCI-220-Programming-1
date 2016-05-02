## using a list, values, biSearch performs a binary search of the list for x
## low = lowest position in portion of list being considered
## high = highest position "     "   "   "   "       "
## mid = middle of

def biSearch(x, values):
    foundPos = -1
    low = 0 
    high = len(values) - 1
    while foundPos == -1 and low <= high:
        mid = (low + high) // 2 
        if x == values[mid]:
            foundPos = mid
        elif x > values[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return foundPos

#with comments
##def biSearch(x, nums):
##    foundPos = -1
##    low = 0 
##    high = len(nums) - 1
##    count = 0
##    while foundPos == -1 and low <= high:
##        mid = (low + high) // 2 
##        # print added for instructional purposes
##        print ("low =",low,"high =",high,"mid =", mid)
##        if x == nums[mid]:
##            foundPos = mid
##        elif x > nums[mid]:
##            low = mid + 1
##        else:
##            high = mid - 1
##        count = count + 1
##    print ("\nNumber iterations: " + str(count))
##    print ("After loop")
##    print ("low =",low,"high =",high,"mid =", mid)
##    return foundPos
