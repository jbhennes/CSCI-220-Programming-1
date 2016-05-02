import math

def add(op1, op2):
   print op1 + op2


def sayHello():
   print "Hello"

def cube(op1):
   return op1 ** 3

def circleArea(rad):
   if rad >= 0:
      area = math.pi * rad ** 2
   else:
      area = "Can not calculate area for negative radius."
   return area

def squareEach(numList):
   for i in range(len(numList)):
      numList[i] = numList[i] ** 2

def squareEachNewList(numList):
   newList = []
   for num in numList:
      newList.append(num**2)
   return newList

def main():   
##      nums = [3, 0, -2]
##      print nums
##      squareEach(nums)
##      print nums

      nums = [3, 0, -2]
      print nums
      numsSquared = squareEachNewList(nums)
      print "nums = " + str(nums)
      print "numsSquared = " + str(numsSquared)

      ##   add(3,2)
##   sayHello()
##   add(7,8)
##   for i in range(3):
##      num = input("Enter num: ")
##      value = cube(num)
##      print value
##
##   print math.sqrt(-1)

##   for i in range(3):
##      radius = input("Enter radius: ")
##      calculatedArea = circleArea(radius)
##      print "The area was calculated as: "
##      print calculatedArea

main()
