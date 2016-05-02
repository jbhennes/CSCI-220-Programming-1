def squareEach(nums):
   for i in range(len(nums)):
      nums[i] = nums[i] ** 2

def main():
   numbers = [5, 7, 10, 2]
   print (numbers)
   squareEach(numbers)
   print (numbers)
