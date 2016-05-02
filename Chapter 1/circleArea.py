#Stalvey and class
#Purpose: This code calculates the area of a circle
#  given the radius provided by the user

from math import *

def main():
   print("Calculates the area of a circle.")
   print()

   #ask for input of radius
   radius = input("Enter radius: ")
   radius = eval(radius)

   #calculate and output area
   area = pi * radius * radius
   print("Circle area =", area)
   print("Sqrt of area =",sqrt(area))
##   print("This is a new line.\n")
##   print("Anlther\t\tvalue astlja lalksg kasey", end =" ")
##   print("a;ljasld nfdsa ;ndsa jlkjlfdsag lask;nadia", end ="!!!!")
##   print("lkdsajf lkdsaflkdsajflk jjdsaf daniel", end="Goodbye!")
##   print("oahl nlvagas lkdsal")

main()
