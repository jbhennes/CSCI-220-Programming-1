# moveCircle.py

# Illustrates getting the position of the mouse and using
# that position to move a graphics object.

from graphics import *

def main():
    winHeight = 400
    winWidth = 400
    
    win = GraphWin("Click to move circle", winWidth, winHeight)

    pt = Point(winWidth/2, winHeight/2)
    pt.draw(win)

    circ = Circle(pt, 60)
    circ.draw(win)
    circ.setFill("yellow")
    circ.setOutline("red")

    message = Text(Point(winWidth/2, winHeight-10), "")
    message.draw(win)
    message.setText("Click on window to move circle to that point")

    for count in range(5):
        mousePt = win.getMouse()
        centerPt = circ.getCenter()
        newX = mousePt.getX() - centerPt.getX()
        newY = mousePt.getY() - centerPt.getY()
        circ.move(newX, newY)


    message.setText("Click to close")
    win.getMouse()
    win.close()

main()
