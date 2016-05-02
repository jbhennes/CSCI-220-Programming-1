### newList(numList, multiplier) accepts a list of numbers and multiplies
### each element by the multiplier returning this as a new list
### input: list of numbers, number
### output: new list of numbers as described above
##
##def newList(numList, multiplier):
##    newList = []
##    for i in range(len(numList)):
##        newList.append(numList[i] * multiplier)
##    return newList

# alterList(numList, multiplier) accepts a list of numbers and multiplies
# each element by the multiplier
# input: list of numbers, number
# output: new list of numbers as described above

def alterList(numList, multiplier):
    for i in range(len(numList)):
        numList[i] = numList[i] * multiplier

def main():
    numbers = [-5,-2,-1,0,1,2,10]
    print "Before calling alterList(), the list holds:", numbers
    alterList(numbers, 3)
    print "After calling alterList(), the list holds:", numbers
    # print multiplier

main()
