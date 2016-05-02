from die import Die

def main():
   trisha = Die(-5)
##   trisha.roll()
   print("Trisha", trisha.getFaceValue())
   print(trisha)
##   sheldon = Die()
##   for i in range(10):
##      trisha.roll()
##      sheldon.roll()
##      tValue = trisha.getFaceValue()
##      sValue = sheldon.getFaceValue()
##      if sValue <= tValue:
##         sheldon.setFaceValue(5.5)
##         sValue = sheldon.getFaceValue()
##      print("Trisha: " + str(tValue), end = " ")
##      print("Sheldon: " + str(sValue))
##      if tValue > sValue:
##         print ("Trisha won!")
##      elif tValue == sValue:
##         print("Tie")
##      else:
##         print("Sheldon won!")
   print ("Done!")

main()
