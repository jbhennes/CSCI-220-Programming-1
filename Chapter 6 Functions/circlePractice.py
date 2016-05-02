#function practice using Circle objects

from math import pi
from graphics import *

def validRadius(radius):
    return radius > 0 and radius <= 100

def circleSize(circle):
    radius = circle.getRadius()
    if radius > 50:
        size = "Large"
    elif radius > 25:
        size = "Medium"
    elif radius > 0:
        size = "Small"
    else:
        size = "Error"
    return size

def circleArea(circle):
    radius = circle.getRadius()
    return pi * radius ** 2

def equalAreas(area1, area2):
    return abs(area1 - area2) <= .001

def main():
    win = GraphWin("Circle", 300, 300)

    rad = input("Enter radius: >0 and <= 100 ")

##    while not validRadius(rad):
    while validRadius(rad) == False:
        rad = input("Enter radius: >0 and <=100 ")

    cir = Circle(Point(150,150), rad)
    cir.setFill("purple")
    cir.draw(win)

    print "Your circle is " + circleSize(cir)
    area = circleArea(cir)
    print "Area: " + str(area) + " square units"

    area2 = 1256.637
    equal = equalAreas(area, area2)
    if equal == True:
        print "The area is equal to " + str(area2)
    else:
        print "Not equal to " + str(area2)

    area2 = 7853.9816
    equal = equalAreas(area, area2)
    if equal:
        print "The area is equal to " + str(area2)
    else:
        print "Not equal to " + str(area2)

    win.getMouse()
    win.close()

main()





    
