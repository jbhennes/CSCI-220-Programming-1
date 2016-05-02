from dieWithMulitSides import Die

def main():
##    print("Create dice")
##    die1 = Die(5)
##    die2 = Die(3)
##
##    die1Value = die1.getFaceValue()
##    print("Die 1's value is: " + str(die1Value))
##    print("Die 2's value is: " + str(die2.getFaceValue()))
##
##    die1.roll()
##    die1Value = die1.getFaceValue()
##    print("Die 1's value is: " + str(die1Value))

    print("\nPlay dice...")

    kevins = Die(20)
    nadias = Die(12)

    for i in range(10):
        kevins.roll()
        kValue = kevins.getFaceValue()
        nadias.roll()
        nValue = nadias.getFaceValue()
        print("Kevin's " + str(kevins))
        print("Nadia's " + str(nadias))
##        print ("Kevin rolled: " + str(kValue), end = " ")
##        print ("Nadia rolled: " + str(nValue))
        if kValue > nValue:
            print("Kevin won")
        elif kValue < nValue:
            print("Nadia won")
        else:
            print("Tie")

    print("Done")

main()
    
