from die import Die

def main():
   die1 = Die(5)
   print(die1)
   stusDie = Die(37)   
   print(stusDie)

##   for i in range(10):
##      die1.roll()
##      stusDie.roll()
##
##      if stusDie.getFaceValue() <= die1.getFaceValue():
##         stusDie.setFaceValue(5.5)
##      print("Your " + str(die1), end = " ")
##      print("Stu's " + str(stusDie))
##  
      
##   print("You rolled", die1.getFaceValue())

   
##   die1.setFaceValue(5)
##   print(die1.getFaceValue())
##   die1.setFaceValue(38)
##   print(die1.getFaceValue())
##   
##   for i in range(10):
##      die1.roll()
##      rollValue = die1.getFaceValue()
##      print("You rolled " + str(rollValue))   
##      stusDie.roll()
##      stusValue = stusDie.getFaceValue()
##      print("He rolled " + str(stusValue))
##      if rollValue > stusValue:
##         print("You won")
##      else:
##         if rollValue == stusValue:
##            print("Tie")
##         else:
##            print("Stu won!")
##      print()
   print ("Done!")

main()
