#test Button class

from graphics import *
from buttonClassDefinition import Button
    
def main():
    winWidth = 300
    winHeight = 230
    win = GraphWin("Colorful square", winWidth, winHeight)
    win.setBackground("white")

    buttons = []
    buttons.append(Button(20, 130, 80, 170, "red"))
    buttons.append(Button(120, 130, 180, 170, "yellow"))
    buttons.append(Button(220, 130, 280, 170, "blue"))

    for button in buttons:
       button.draw(win)
       
    square = Rectangle(Point(130,50), Point(170,90))
    square.setFill("black")
    square.draw(win)

    # Prepare to output error msg if necessary
    msg = ""
    output = Text(Point(winWidth/2, winHeight - 40), msg)
    output.draw(win)

    numTimes = 5
    for i in range(numTimes):
        # Determine if the user clicked within the button
        pt = win.getMouse()
        i = 0
        clicked = False
        while i < len(buttons) and not clicked:
           if buttons[i].isClicked(pt):
              clicked = True
           else:
              i = i + 1
        if clicked:
           color = buttons[i].getColor()
           print (color,"in if")
        else:
           color = "black"
            
        # If not on a button, output error message

        output.undraw()
        if color == "black":
            msg = "You must select a color"
            output.setText(msg)
            output.setSize(10)
            output.draw(win)
        print (color)
        square.setFill(color)
        square.undraw()
        square.draw(win)

    for button in buttons:
       button.undraw()
    square.setFill("purple")
       
    # Click anywhere to quit
    quitInstructions = Text(Point(winWidth/2, winHeight - 20),"Click anywhere to close")
    quitInstructions.setSize(10)
    quitInstructions.draw(win)
    win.getMouse()
    
    win.close()

main()
