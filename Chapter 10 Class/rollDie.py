# rollDie.py

# Creates a single die object, then rolls it for each <enter>
# until user says "no".

from Die import Die

def main():
    theDie = Die()

    go = raw_input("Roll the die? <enter> for yes, no for stopping: ")

    theDie.roll()
    
    while go == "":
        theDie.roll()
        print theDie.getValue()
        print "die = " + str(theDie)
        go = raw_input("Roll the die? <enter> for yes, no for stopping: ")

##    die2 = Die()
##    die1 = Die()
##    for i in range(10):
##        die1.roll()
##        die2.roll()
##        print "equals",die1.getValue(), die2.getValue(), die1 == die2
##        print "greater than",die1.getValue(), die2.getValue(), die1 > die2
##        print "less than",die1.getValue(), die2.getValue(), die1 < die2

main()
