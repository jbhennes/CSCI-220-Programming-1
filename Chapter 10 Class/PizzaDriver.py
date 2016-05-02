# Stalvey
# Test Pizza class

from Pizza import Pizza

def main():

    print "Testing constructor and str()..."
    pie8 = Pizza(8)
    pie10 = Pizza(10)
    pie12 = Pizza(12)
    pie6 = Pizza(6)

    print pie8
    print
    print pie10
    print
    print pie12
    print
    print pie6

    print "\nTesting setPrice and getPrice..."
    pie8.setPrice(15.85)
    print "Pie's price is: " + str(pie8.getPrice())
    print
    pie8.setPrice(-6)
    print "Pie's price is: " + str(pie8.getPrice())

    print "\nTesting buildPizza()..."
    toppingsInMain = ["Chicken", "Basil", "Tomatoes", "Feta"]
    pie8.buildPizza(toppingsInMain)
    print pie8
    print "\nEnsuring clone..."
    toppingsInMain.append("Anchovies")
    print pie8

    print "\nTesting cut()..."
    pie8.cut()
    print pie8

    print "\nTesting serve and getNumSlices..."
    print "Serve 1 person:"
    pie8.serve(1)
    print "Num slices remaining: " + str(pie8.getNumSlices())

    for i in range(10):
        print "Serve another person:"
        pie8.serve(1)
        print "Num slices remaining: " + str(pie8.getNumSlices())

    print"\nEnd of testing:"
    print pie8
main()
    
