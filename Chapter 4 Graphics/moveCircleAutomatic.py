# moveCircle.py

# Illustrates getting the position of the mouse and using
# that position to move a graphics object.

from graphics import *
from random import randint
from time import sleep

def main():
    winHeight = 400
    winWidth = 400
    
    win = GraphWin("Test Window", winWidth, winHeight)
    pt = Point(winWidth/2, winHeight/2)
    pt.draw(win)

    message = Text(Point(winWidth/2, winHeight-10), "")
    message.draw(win)
    
    circ = Circle(pt, 20)
    circ.draw(win)
    circ.setFill("yellow")
    circ.setOutline("red")
    
    message.setText("Click to begin movement")
    win.getMouse()
    
    newX = randint(-10,10)
    newY = randint(-10,10)

    for count in range(25):        
        circ.move(newX, newY)
        sleep(1)


    message.setText("Click to quit")
    win.getMouse()
    win.close()

main()
