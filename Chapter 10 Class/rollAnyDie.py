# roll any sided die

from AnyDie import *

def main():

    die1 = Die(6)
    die2 = Die(9)
    die3 = Die(20)

    for i in range (5):
        print "Roll " + str(i+1) + ":"
        print "die1 = " + str(die1.getValue())
        print "die2 = " + str(die2.getValue())
        print "die3 = " + str(die3.getValue())
        print
        
        die1.roll()
        die2.roll()
        die3.roll()
        

main()
