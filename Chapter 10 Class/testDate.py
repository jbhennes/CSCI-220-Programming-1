#RHS

from Date import Date

def main():
    kati = Date()
    strKB = str(kati.getMonth()) + "/" + str(kati.getDay())
    strKB = strKB   + "/" + str(kati.getYear())
    print strKB

    kati.setDate(20, 45, -15)
    print
    print kati

    kati.setDate(13, 29, 1990)
    print
    print kati
##    d1 = Date()
##    d1.setDate(12,30,1969)
##    print "d1 = " + str(d1)
##    print
##    d2 = Date()
##    d2.setDate(12,28,2005)
##    print "d2 = " + str(d2)
##    print
##    d3 = Date()
##    print "d3 = " + str(d3)
##    print
##    d3.setDate(13, 115, -3)
##    print "d3 = " + str(d3)
##    print
##    d3.setDate(13, 32, 1900)
##    print "d3 = " + str(d3)
##    print
##    d3.setDate(4, 32, 1900)
##    print "d3 = " + str(d3)
##    print
##    d3.setDate(4, 29, 1900)
##    print "d3 = " + str(d3)
##    print
##    d4 = Date()
##    d4.setDate(12,30,1969)
##    print "d4 = " + str(d4)
##    print
##    d5 = Date()
##    d5.setDate(12,30,0)
##    print "d5 = " + str(d5)
##    print 
##    print str(d1)+ " as a Julian = " + str(d1.convertToJulian())
##    print
##    print str(d3)+ " as a Julian = " + str(d3.convertToJulian())
##    print
##    print str(d5)+ " as a Julian = " + str(d5.convertToJulian())
##    print
##    compare = d1.compareTo(d2)
##    if compare == 0:
##        print str(d1) + " equals " + str(d2)
##    elif compare > 0:
##        print str(d1) + " occured before " + str(d2)
##    else:
##        print str(d1) + " occured after " + str(d2)
##
##    compare = d1.compareTo(d3)
##    if compare == 0:
##        print str(d1) + " equals " + str(d3)
##    elif compare > 0:
##        print str(d1) + " occured before " + str(d3)
##    else:
##        print str(d1) + " occured after " + str(d3)
##
##    compare = d1.compareTo(d4)
##    if compare == 0:
##        print str(d1) + " equals " + str(d4)
##    elif compare > 0:
##        print str(d1) + " occured before " + str(d4)
##    else:
##        print str(d1) + " occured after " + str(d4)
