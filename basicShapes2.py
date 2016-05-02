# basicShapes.py

from graphics import *
import time

def main():
    # Drawing a graphics window of a specified size.
    win = GraphWin("Win", 500, 500)

    p1 = Point(150, 250)

    c = Circle(p1, 100)
    p1.draw(win)
    c.draw(win)
    c.setFill("red")
    c.setOutline("blue")
    clickPt = win.getMouse()
    dX = clickPt.getX()
    dY = clickPt.getY()
    # REMEMBER: move is changed by the mouse coordinates, the circle will
    #   not move to where you click.
    c.move(dX, dY)

    # New circle
    for i in range(5):
        c2 = Circle(clickPt, 20)
        c2.setFill("blue")
        c2.draw(win)
        clickPt = win.getMouse()

    win.getMouse()
    c.undraw()

    # Drawing a square/rectangle.
    p3 = Point(50, 50)
    p4 = Point(250, 250)
    square = Rectangle(p3, p4)
    square.draw(win)
    square.setFill("chartreuse")
    p5 = Point(325, 77)
    p6 = Point(250, 167)
    rect = Rectangle(p5, p6)
    rect.draw(win)
    colors = ["red", "green", "blue", "yellow", "black"]
    for color in colors:
        rect.setFill(color)

    # Drawing an oval.

    # Drawing a polygon.
    pp1 = Point(277, 325)
    pp2 = Point(34, 56)
    pp3 = Point(345, 7)
    pp4 = Point(407, 90)
    pp5 = Point(400, 400)
    polyPoints = [pp1, pp2, pp3, pp4, pp5]
    polygon = Polygon(polyPoints)

    # Defining our own polygon.
    """win2 = GraphWIn("User Defined Points", 400, 400)
    points = []
    for i in range(10):
        pt = win.getMouse()
        pt.draw(win)
        points.append(pt)

    polygon2 = Polygon(points)
    poly.draw(win)"""

    
    
main()
