import math


def main():
   num = eval(input("Enter num: "))

   try:
      answer = math.sqrt(num)
      print ("answer = " + str(answer))
   except:
      print("Can't take sqrt of negative value.")

main()
