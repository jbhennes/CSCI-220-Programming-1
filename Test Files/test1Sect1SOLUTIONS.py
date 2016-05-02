def gpa():

   total = 0
   for i in range(25):
      gpa = eval(input("GPA: "))
      total = total + gpa
   avg = total/25
   print(avg)

import math
def ques8():
   n = eval(input("Limit: "))

   ans1 = 3 * n / 4 + 2
   ans2 = 3 / (7 + n)
   ans3 = math.pi * math.sqrt(n)

   print(ans1, ans2, ans3)

def ques9():
   n = eval(input("Limit: "))
   prod = 1

   for i in range(n):
      num = 2 ** i
      denom = (i+1) * 2 + 1
      prod = prod * num/denom

   print(prod)

from graphics import *
def ques10():
   win = GraphWin("Test", 300, 400)
   center = Point(0, 0)
   cir = Circle(center, 40)
   cir.draw(win)


def ques12():
   op1 = eval(input("Num: "))
   op2 = eval(input("Num: "))

   total = op2
   for i in range(op1-1):
      total = total + op2

   print(total)
