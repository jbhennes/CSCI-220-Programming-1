from random import randint

def totalValues(values):
    numsUsed = []
    total = 0
    count = 0
    while (total <= 100) and count < len(values):
        total += values[count]
        count += 1
        numsUsed.append(values[count])
    return count, numsUsed

randomValues = []
for i in range(20):
    value = randint(1, 20)
    randomValues.append(value)

n, valueList = totalValues(randomValues)
print('The number of terms used: ', n, '\n')
print('The list of all the values is: ', valueList)


## Professor Stalvey's:
def totalValuesA(values):
    total = 0
    i = 0
    while total <= 100 and i < len(values):
        total += values[i]
        i += 1
    return total

## Part B
def totalValuesB(values):
    total = 0
    i = 0
    while total <= 100 and i < len(values):
        total += values[i]
        i += 1
    return total, i

## Part C
def totalValuesC(values):
    numsUsed = []
    total = 0
    i = 0
    while total <= 100 and i < len(values):
        total += values[i]
        i += 1
        numUsed.append(values[i])
    return total, i, numsUsed

## Part D
def totalValuesC(values):
    numsUsed = []
    total = 0
    i = 0
    while total <= 100 and i < len(values) and i <= 5:
        total += values[i]
        i += 1
        numUsed.append(values[i])
    return total, i, numsUsed

## Part D.1
def getGoodInput():
    message = 'Input a number greater than 100 or divisble by 3 and non-positive.'
    number = eval(input('Number: '))

    while number <= 100 and (number > 0) or ((number % 3) != 0):
        print(message)
        number = eval(input('Number: '))
    print('The number is a valid number')
    return number
        
getGoodInput()

## Number 2

words = ['apple', 'boy', 'cat', 'dog', 'each', 'every', 'frog', 'girl', 'hello']

