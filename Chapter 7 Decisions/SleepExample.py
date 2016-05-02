# simple program to place a circle on the screen waith some time remove it
# and place a rectangle on the screen.
# RHS   

from graphics import *
from time import sleep

def main():
    wHeight = 400
    wWidth = 400
    win = GraphWin("Shapes Appear", wWidth, wHeight)
    circle = Circle(Point(wWidth/2, wHeight/2), 50)
    circle.setFill("blue")
    circle.draw(win)
    sleep(0.2)
    circle.undraw()
    rect = Rectangle(Point(wWidth/4,wHeight/4),Point(wWidth*2,wheight*2))
    rect.setFill("yellow")
    rect.draw(win)
    sleep(0.1)
    text = Text(Point(wWidth/2, wHeight/2),"Click to close")
    win.getMouse()
    win.close()

main()

    
    
