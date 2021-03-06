# button.py
# Creates a button and determines where the user clicked in relation to
# the button.  The last portion creates a quit button.  This requires a
# while loop to exit only when the user clicks the button.

from graphics import *

def main():
    win = GraphWin("Working button", 300, 200)    
    button = Text(Point(150, 100), "Click me")
    button.draw(win)
    Rectangle(Point(115, 80), Point(185, 120)).draw(win)
    
    # Determine if the user clicked within the button
    pt = win.getMouse()
    if pt.getX() >= 115 and pt.getX() <= 185:
        if pt.getY() >= 80 and pt.getY()<=120:
           msg = "I've been clicked"
        else:
            msg = "You clicked too high or too low"
    else:
        msg = "You clicked to the right or to the left"
        

    output = Text(Point(150, 150), msg)
    output.draw(win)
    
    # Click anywhere to quit
    quitInstructions = Text(Point(150, 170),"Click anywhere to close")
    quitInstructions.draw(win)
    win.getMouse()
    
    win.close()

main()
