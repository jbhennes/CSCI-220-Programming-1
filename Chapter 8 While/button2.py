# button2.py

from graphics import *
from time import sleep
       
def main():
    buttonLeft = 120
    buttonRight = 180
    clickButtonTop = 85
    clickButtonBottom = 115
    quitButtonTop = 185
    quitButtonBottom = 215

    win = GraphWin("Buttons in a Loop", 300, 300)
    introText = Text(Point(150, 150), "Click anywhere to begin")
    introText.draw(win)
    pt = win.getMouse()
    x = pt.getX()
    y = pt.getY()
    introText.setText("")
    
    clickButtonUL = Point(buttonLeft, clickButtonTop)
    clickButtonLR = Point(buttonRight, clickButtonBottom)
    
    clickButton = Rectangle(clickButtonUL, clickButtonLR)
    clickButton.draw(win)
    clickButtonText = Text(Point(150, 100), "Click me")
    clickButtonText.draw(win)
    
    quitButtonUL = Point(buttonLeft, quitButtonTop)
    quitButtonLR = Point(buttonRight, quitButtonBottom)
    
    quitButton = Rectangle(quitButtonUL, quitButtonLR)
    quitButton.draw(win)
    quitButtonText = Text(Point(150, 200), "Quit")
    quitButtonText.draw(win)
    
    msg = ""
    output = Text(Point(150, 150), msg)
    output.draw(win)
    
    # Determine whether the user clicked a button
    running = True
    while running:
##        print x, y
        x = win.mouseX
        y = win.mouseY
        sleep(0.1)
        #print x, y
        if x >= buttonLeft and x <= buttonRight and y >= clickButtonTop and y <= clickButtonBottom:
            msg = "You clicked the button"
        elif x >= buttonLeft and x <= buttonRight and y >= quitButtonTop and y <= quitButtonBottom:
            msg = ""
            running = False
        else:
            msg = "You didn't click either button"
        output.setText(msg)
    
    win.close()

main()
