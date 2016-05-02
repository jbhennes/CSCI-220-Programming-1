# mousePolygon.py
# Author: Zelle (p. 147)
# Modified by Pharr to draw a pentagon also

from graphics22 import *

def main():
    winWidth = 400
    winHeight = 400
    
    win = GraphWin("Draw a Polygon", winWidth, winHeight)
##    win.setCoords(0.0, 0.0, 10.0, 10.0)
    win.setBackground("blue")
    message = Text(Point(winWidth/2, winHeight-10), "Click on some points")
    message.draw(win)

    # Get and draw the vertices of a polygon
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)
##    p4 = win.getMouse()
##    p4.draw(win)
##    p5 = win.getMouse()
##    p5.draw(win)

    # Use a Polygon object to draw the polygon
    polygon = Polygon(p1, p2, p3)
##    polygon = Polygon(p1, p2, p3, p4, p5)
    polygon.setFill("white")
    polygon.setOutline("white")
    polygon.draw(win)

    # Wait for another click to exit
    message.setText("Click anywhere to quit")
    win.getMouse()
    win.close()

main()
