## Input: Search value, x, and a list of comparable values, nums
## Output: position where x is found in list or -1 if x not found
def biSearch(x, nums):
    foundPos = -1
    low = 0 
    high = len(nums) - 1
    count = 0
    while foundPos == -1 and low <= high:
        mid = (low + high) // 2 
        # print added for instructional purposes
##        print ("low =",low,"high =",high,"mid =", mid)
        if x == nums[mid]:
            foundPos = mid
        elif x > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
        count = count + 1
    print ("\nNumber iterations: " + str(count))
    print ("After loop")
    print ("low =",low,"high =",high,"mid =", mid)
    return foundPos

#Input: list of numbers, srchVal
#Output: Position of the last occurence of the srchVal
#        Returns -1 if the srchVal is not in the list
def searchFor(srchVal, nums):
    foundPos = -1
    count = 0
    for i in range(len(nums)):
        if srchVal == nums[i]:
            foundPos = i
        count += 1
    print("For comparisons = " + str(count))
    return foundPos

#Input: list of numbers, srchVal
#Output: Position of the first occurence of the srchVal
#        Returns -1 if the srchVal is not in the list
def search(srchVal, nums):
    foundPos = -1
    i = 0
    count = 0
    while not(foundPos >= 0 or i == len(nums)):
        if srchVal == nums[i]:
            foundPos = i
        else:
            i += 1
        count += 1
    print("While comparisons = " + str(count))
    return foundPos

#Input: list of numbers
#Output: None, but at completion list of numbers is sorted
def selSort(nums):
    # sort nums into ascending order
    
    n = len(nums)
    
    # for each position in the list (except the very last)
    for front in range(n-1):
        # find the smallest item in nums[bottom]..nums[n-1]
        # ("mp" seems to mean "position of the minimum")
        mp = front                     # bottom is smallest initially
        for i in range(front+1,n):     # look at each position
            if nums[mp] > nums[i]:      # this one is smaller
                mp = i                  #   remember its index

        # swap smallest item to the bottom
        temp = nums[mp]
        nums[mp] = nums[front]
        nums[front] = temp
