# Numerology
# Stalvey

def main():
   print ("Calculates a numerology score of your name. \n")
   
   name = input("Enter your name: ")
   newName = name.lower()
   total = 0
   for ch in newName:
      value = ord(ch) - ord("a") + 1
##      print (ch, value) #debug statement
      total = total + value
   
   print ("The numerological score for \'" + name + "\'", end="")
   print (" is " + str(total) + ".")

main()
