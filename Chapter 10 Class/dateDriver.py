#RHS

from Date import Date

def main():
    scotts = Date()
    print scotts
    scotts.setDate(3,30,1995)
    print "Scott: " + str(scotts)
    print
    
    averys = Date()
    print "Avery: " + str(averys)
    averys.setDate(4, 31, 2000)    
    print "Avery: " + str(averys)
    averys.setDate(2, 29, 2008)    
    print "Avery: " + str(averys)    
    averys.setDate(2, 29, 2009)    
    print "Avery: " + str(averys)    
    averys.setDate(14, 29, 2008)    
    print "Avery: " + str(averys)
    averys.setDate(11,13,2009)    
    print "Avery: " + str(averys)
    

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
##    d3.setDate(4, 31, 1900)
##    print "d3 = " + str(d3)
##    print
##    d3.setDate(4, 30, 1900)
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
##    if d1 == d2:
##        print str(d1) + " equals " + str(d2)
##    elif d1 < d2:
##        print str(d1) + " occured before " + str(d2)
##    else:
##        print str(d1) + " occured after " + str(d2)
##
##
##    if d1 == d3:
##        print str(d1) + " equals " + str(d3)
##    elif d1 < d3:
##        print str(d1) + " occured before " + str(d3)
##    else:
##        print str(d1) + " occured after " + str(d3)
##
##    
##    if d1 == d4:
##        print str(d1) + " equals " + str(d4)
##    elif d1 < d4:
##        print str(d1) + " occured before " + str(d4)
##    else:
##        print str(d1) + " occured after " + str(d4)
