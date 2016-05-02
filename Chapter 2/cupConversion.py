#RH Stalvey
#Purpose: To convert cups to oz and ml

def main():
   print("This program converts cups to ounces and ml.\n")

   cups = eval(input("Enter cups: "))

   ounces = cups * 8
   print("Ounces =", ounces)

   ml = ounces * 29.57
   print("Milliliters =", ml)
   
main()
