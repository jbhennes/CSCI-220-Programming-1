from Pizza import *

def main():
##   print("Testing constructor and str()...")
##   print("8\" pizza...")
   pizza8 = Pizza(8)
   print(pizza8)
##   
##   print()
##   print("10\" pizza...")
##   pizza10 = Pizza(10)
##   print(str(pizza10))
##
##   print()
##   print("12\" pizza...")
##   pizza12 = Pizza(12)
##   print(pizza12)
##
##   print()
##   print("-5\" pizza...")
##   pizzaIll = Pizza(-5)
##   print(pizzaIll)

##   print()
##   print("All following examples use 8\" pizza")
##   print("---\nTesting getPrice() and setPrice()...")
##   print("Using getPrice() price is: " + str(pizza8.getPrice()))
   pizza8.setPrice(11.75)
##   print("Price set to 11.75...")
##   print("Using getPrice() price is: " + str(pizza8.getPrice()))
##   pizza8.setPrice(-12)
##   print("Price set to -12")
##   print("Using getPrice() price is: " + str(pizza8.getPrice()))
##
##   print("\n---\nTesting getNumSlices() and cut()...")
##   print("Using getNumSlices() num slices is: " + str(pizza8.getNumSlices()))
   pizza8.cut()
##   print("After cut() num slices is: " + str(pizza8.getNumSlices()))

##   print("\n---\nTesting buildPizza()...")
   top = ["pep", "sausage"]
   pizza8.buildPizza(top)
   print(pizza8)
##
##   print("\n---\nTesting class.  Does adding a topping to", end = " ")
##   print("list in main() cause the topping list to change", end = " ")
##   print("in the pizza object?...")
##   top.append("anchovies")
##   print(pizza8)
##
   print("\n---\nTesting serve()...")
   pizza8.serve(2)
   print("After serving 2 num slices is: " + str(pizza8.getNumSlices()))
   pizza8.serve(5)
   print("After serving 5 num slices is: " + str(pizza8.getNumSlices()))
   pizza8.serve(2)
   print("After serving 2 num slices is: " + str(pizza8.getNumSlices()))
   pizza8.serve(2)
   print("After serving 2 num slices is: " + str(pizza8.getNumSlices()))
   
   
   
   
main()
