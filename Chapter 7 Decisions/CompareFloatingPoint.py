## CompareFloatingPoint.py

def main():
    f1 = .1 + .1 + .1 + .1 + .1 + .1 + .1 + .1 + .1 + .1
    f2 = .1 * 10
    
    print (f1)
    print (f2)

      
    print ("{0:.20f}".format(f1))
    print ("{0:.20f}".format(f2))

    if f1 == f2:
        print ("f1 and f2 are equal")
    else:
        print ("f1 and f2 are NOT equal")

    print ("\nf2 = " + str(f2))
    print ("f1 = " + str(f1))
    
    if abs(f2 - f1) < 0.0001:
        print ("f1 and f2 are considered equal")
    else:
        print ("f1 and f2 are NOT equal")

    print ("difference = {0:0.20f}".format(abs(f1 - f2)))

main()
