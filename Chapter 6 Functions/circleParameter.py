from graphics import *
import math

#input: circle
#output: color
#purpose: accepts a Circle object and returns the color the circle should be
#filled based on its diameter.  Small circles (diameter < 75) are yellow,
#big circles are green
def whichColor(c):
    diameter = c.getRadius() * 2
    if diameter < 75:
        rtnColor = "yellow"
    else:
        rtnColor = "green"
    return rtnColor

#input: diameter, Point
#output: Circle
#purpose: this function accepts a diameter and a Point and creates a Circle object
def makeCircle(diameter, p):
    radius = diameter/2.
    return Circle(p, radius)

def numRevolutions(c, dist):
    return dist / (c.getRadius()*2 * math.pi)

# main(): driver
# Creates a graphic window, allows user to enter the diameter, and x/y
# coordinates for multiple circles.  Uses makeCircle to create the circle
# and whichColor to determine the color of the circle.  Then draws the circle.
def main():
    
    win = GraphWin("Using objects with functions", 500, 500)
    win.setBackground("black")

    inputArea = Rectangle(Point(0,325), Point(500,500))
    inputArea.setFill("white")
    inputArea.draw(win)

    for i in range(1,3):
        #get diameter
        diaIns = Text(Point(175,350), "Enter the diameter for circle: " + str(i) + ": ")
        diaIns.draw(win)
        diameterBox = Entry(Point(350,350),5)
        diameterBox.setText("0")
        diameterBox.draw(win)
        
        #get x coordinate
        xIns = Text(Point(175,375), "Enter the x coordinate (between 0 and 500): ")
        xIns.draw(win)
        xBox = Entry(Point(350,375),5)
        xBox.setText("0")
        xBox.draw(win)

        #get y coordinate
        yIns = Text(Point(175,400),"Enter the y coordinate (between 0 and 300): ")
        yIns.draw(win)
        yBox = Entry(Point(350,400),5)
        yBox.setText("0")
        yBox.draw(win)

        #gather user input
        message = "Click to draw the circle"
        message = message + "\nYellow circles have diameter <75"
        message = message + "\nGreen circles have diameter >= 75"
        createIns = Text(Point (250, 450), message)
        createIns.draw(win)
        win.getMouse()
        diameter = eval(diameterBox.getText())
        x = eval(xBox.getText())
        y = eval(yBox.getText())
        # error checking should be done to insure diameter, x and y have
        #legitimate values.

        #undraw all instructions
        diaIns.undraw()
        diameterBox.undraw()
        xIns.undraw()
        xBox.undraw()
        yIns.undraw()
        yBox.undraw()
        createIns.undraw()

        #create circle using functions
        c = makeCircle(diameter, Point(x,y))
        color = whichColor(c)
        c.setFill(color)
        c.draw(win)
        print "The number of revolutions is " + str(numRevolutions(c, 15))

    Text(Point (250, 400), "Click to end").draw(win)
    win.getMouse()
    win.close()

main()
    
