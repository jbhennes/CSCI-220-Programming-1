# linear search implementations

#no early termination therefore least efficient
#returns last occurence of x in nums
def search1(x, nums):
    foundPos = -1
    for i in range(len(nums)):
##        print ("in for")
        if x == nums[i]:
            foundPos = i
    return foundPos

#terminates once element is found
#returns first occcurence of x in nums
def search2(x, nums):
    foundPos = -1
    count = 0
    while foundPos == -1 and count < len(nums):
##        print ("in while")
        if x == nums[count]:
            foundPos = count
        else:
            count = count + 1
    return foundPos

#Zelle's implementation -
#Which of above does it most closely match in terms of efficiency?
def search3(x, nums):
    for i in range(len(nums)):
        if nums[i] == x:
            return i
    return -1

def main():

    numbers = list(range(0,10000000)) #[17, -18, 20, 5, 2, 9, -1, 2, 8]
    val = 999999999
##    print(numbers)
##    print("Value to find: " + str(val))
##    print()

    print ("search1")
    pos = search1(val, numbers)
    if pos == -1:
        print (str(val) + " not found" )# in " + str(numbers))
    else:
        print (str(val) + " found at position " + str(pos))# + " in " + str(numbers))

    print ("\nsearch2")
    pos = search2(val, numbers)
    if pos == -1:
        print (str(val) + " not found" )# in " + str(numbers))
    else:
        print (str(val) + " found at position " + str(pos))# + " in " + str(numbers))

##    print ("\nsearch3")
##    pos = search3(val, numbers)
##    if pos == -1:
##        print (str(val) + " not found in " + str(numbers))
##    else:
##        print (str(val) + " found at position " + str(pos) + " in " + str(numbers))

main()
