# colorButtons.py
# Creates a white square and several buttons to change the color of the square

from graphics22 import *

def main():
    win = GraphWin("Colorful square", 300, 230)

    redButton = Text(Point(50, 150), "Red")
    redButton.draw(win)
    Rectangle(Point(20, 130), Point(80, 170)).draw(win)

    yellowButton = Text(Point(150, 150), "Yellow")
    yellowButton.draw(win)
    Rectangle(Point(120, 130), Point(180, 170)).draw(win)

    blueButton = Text(Point(250, 150), "Blue")
    blueButton.draw(win)
    Rectangle(Point(220, 130), Point(280, 170)).draw(win)

    square = Rectangle(Point(130,50), Point(170,90))
    square.setFill("black")
    square.draw(win)
    
    # Prepare to output error msg if necessary
    msg = ""
    output = Text(Point(150, 190), msg)
    output.draw(win)

    numTimes = 5
    for i in range(numTimes):
        # Determine if the user clicked within the button
        pt = win.getMouse()
        if pt.getY() >= 130 and pt.getY()<= 170:
            if pt.getX() >= 20 and pt.getX() <= 80: 
                color = "red"
            elif pt.getX() >= 120 and pt.getX() <= 180:
                color = "yellow"
            elif pt.getX() >= 220 and pt.getX() <= 280:
                color = "blue"
            else:
                color = "black"
        else:
            color = "black"
            
        # If not on a button, output error message

        output.undraw()
        if color == "black":
            msg = "You must select a color"
            output.setText(msg)
            output.setSize(10)
            output.draw(win)
            
        square.setFill(color)
        square.undraw()
        square.draw(win)
    
    # Click anywhere to quit
    quitInstructions = Text(Point(150, 210),"Click anywhere to close")
    quitInstructions.setSize(10)
    quitInstructions.draw(win)
    win.getMouse()
    
    win.close()

main()
