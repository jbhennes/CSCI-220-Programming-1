# forVsWhile

from random import *


def main():
    nums = []
    for i in range(10):
        nums.append(randint(10, 50))

    print(nums)

    found = False
    srchVal = 15

    for i in range(len(nums)):
        if nums[i] == srchVal:
            found == True
            print(found)
        print(nums[i], "is in List at position", [i])

    while i < len(nums) and nums[i] != srchVal:
        if nums[i] == srchVal:
            print(nums[i], "was found at", i, "and", srchVal, "found", found)
        i += 1

main()
