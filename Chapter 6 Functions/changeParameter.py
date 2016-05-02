## changeParameter.py

## If a function modifies its parameter, does the change "take"
## in the calling program?

## The answer depends on what kind of parameter it is.
from graphics import *
from changeFunctions import *

def main():
    argument = 3
    print ("In main before call, argument = ", argument)
    change1(argument)
    print ("In main after call, argument = ", argument)

    argument = [1,2,3]
    print ("\nIn main before call, argument = ", argument)
    change2(argument)
    print ("In main after call, argument = ", argument)

    argument = [1,2,3]
    print ("\nIn main before call, argument = ", argument)
    change3(argument)
    print ("In main after call, argument = ", argument)

    argument = [1,2,3]
    print ("\nIn main before call, argument = ", argument)
    copyList(argument)
    print ("In main after call, argument = ", argument)

    #passing a circle object
    win = GraphWin()
    width = win.getWidth()
    height = win.getHeight()
    circle = Circle(Point(width/2, height/2), 20)
    circle.setFill("red")
    circle.draw(win)

    change4(circle)

    win.getMouse()
    win.close()




main()
