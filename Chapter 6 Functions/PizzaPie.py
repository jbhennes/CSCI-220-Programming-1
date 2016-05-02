#PizzaPie.py
#Function practice
#In-class Exercise #3

import math

def calculateCostPerSquareInch(dia, price):
   radius = dia/2
   area = math.pi * radius ** 2
   return price / area

def updateCost(initialPrice, numToppings):
   newPrice = initialPrice + numToppings * 1.5
   return newPrice

def main():
   print ("Calculates cost / sq in of pizza and new price")

   diameters = [5, 10, 12, 14]
   prices = [5, 9.99, 11.5, 7.95]

   for i in range(len(diameters)):
      cost = calculateCostPerSquareInch(diameters[i], prices[i])
      print ("\n{1:2}\" Price : ${0:0.02f}".format(prices[i], diameters[i]))
      print ("Cost per square inch ${0:0.02f}".format(cost))

   prices[0] = updateCost(prices[0], 4)
   print ("\n{1:2}\" Price : ${0:0.02f}".format(prices[0], diameters[0]))
      
