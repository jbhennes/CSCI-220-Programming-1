from die1 import Die

def main():
   #test init()
   d1 = Die(8)
   d2 = Die(-1)

   #test getters
   print "The value of die1 is : " + str(d1.getFaceValue())
   print "The value of die2 is : " + str(d2.getFaceValue())

   #test setters
   d1.setFaceValue(5)
   print "The value of die1 is : " + str(d1.getFaceValue())
   d1.setFaceValue(3)
   print "The value of die1 is : " + str(d1.getFaceValue())
   d1.setFaceValue(7)
   print "The value of die1 is : " + str(d1.getFaceValue())

   print "\nTesting roll..."
   #test roll()
   d1.roll()
   print "The value of die1 is : " + str(d1.getFaceValue())

   for i in range(5):
      d1.roll()
      print "The value of die1 is : " + str(d1.getFaceValue())

   print "\nPrinting the die.."
   print d1
      
   print "Done"
   
main()
