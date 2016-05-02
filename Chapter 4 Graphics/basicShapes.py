# basicShapes.py

# Illustrates elementary drawing of graphics objects.

from graphics import *
import time

def main():
    # drawing a graphics window (default size)
##    win = GraphWin("First Try")

    # drawing a graphics window (specified size)
    win = GraphWin("Basic Shapes", 600, 500)
    win.setBackground("magenta")
##
####    print win.getHeight()
####    print win.getWidth()
##
##    # drawing a Point
    p1 = Point(200, 400)
##    
##
##    # drawing a Circle - requires one point
##    # the point doesn't have to be drawn if you don't want to see it!
    c = Circle(p1, 50)
    c.draw(win)
##    p1.draw(win)
    c.setFill("green")
    c.setOutline("blue")
##    
##
##    # coloring the Circle
##    c.setOutline("red")
##    c.setFill("red")
##    c.setFill("magenta")
##    #c.setFill("blue")
##    #c.setFill("green")
##
    c2 = Circle(Point(50, 75), 20)
    c2.setFill("blue")
    c2.draw(win)

##    win.getMouse()
##    # undrawing the Circle
##    c.undraw()

    # drawing a Line - requires two points
    p2 = Point(300, 100)
    p2.draw(win)
    line = Line(p1, p2)
    line.draw(win)
##
##    # for any figure the points can be put in without being named
##    line2 = Line(Point(50, 50), Point(350, 350))
##    line2.draw(win)
##
##    # drawing a Rectangle - requires opposite corners
    p3 = Point(50, 50)
    p4 = Point(250, 250)
    square = Rectangle(p3, p4)
    square.draw(win)
    square.setFill("yellow")
    p5 = Point(325, 77)
    p6 = Point(255, 375)
    rec = Rectangle(p5, p6)
    rec.draw(win)
    rec.setFill("red")

    # drawing an Oval - requires upper left and lower right corners
    # of the "bounding box" that you imagine around it
    p7 = Point(550, 50)
    p8 = Point(350, 475)
    ov = Oval(p7, p8)
    ov.draw(win)
    ov.setFill("green")
##
##    # drawing Polygons - in this case a triangle and a pentagon
    pt1 = Point(20, 20)
    pt2 = Point(170, 100)
    pt3 = Point(130, 190)
    tri = Polygon(pt1, pt2, pt3)
    tri.draw(win)
##    tri.setFill("blue")
    pp1 = Point(300, 150)
    pp2 = Point(250, 200)
    pp3 = Point(275, 275)
    pp4 = Point(325, 275)
    pp5 = Point(350, 200)
    pent = Polygon(pp1, pp2, pp3, pp4, pp5)
    pent.draw(win)
##
##    # Writing Text - REMEBER!!: Point is the center of the message
    t1 = Text(Point(100, 100), "Message 1")
    t1.setFace("courier")
    t1.setSize(10)
    t1.setStyle("bold")
    t1.setTextColor("white")
    t1.draw(win)

    for i in range(10):
        t1.setText( i + 1 )
        time.sleep(.5)
        
    
    t2 = Text(Point(200, 200), "Message 2")
    t2.setFace("times roman")
    t2.setSize(20)
    t2.setStyle("italic")
    t2.draw(win)
    
    t3 = Text(Point(300, 300), "Message 3")
    t3.setFace("helvetica")
    t3.setSize(30)
    t3.setStyle("bold italic")
    t3.draw(win)
    width = win.getWidth()
    height = win.getHeight()
    textPt = Point(width/2, height -10)
    t = Text(textPt, "Click to quit")
    t.draw(win)

    textX = textPt.getX()
    textY = textPt.getY()
    print ("point's x: " + str(textX))
    print ("point's y: " + str(textY))
####    
    win.getMouse()
    win.close()

main()
    
