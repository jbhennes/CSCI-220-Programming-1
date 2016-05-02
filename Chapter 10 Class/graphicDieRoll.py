# Usind Die.py to create a graphical die
# Rolls the die

from die2 import Die
from graphics import *

def playGame(): 
        win = GraphWin("Rolling a die", 400, 400)
        rTX = 120 #roll button's top x and y
        rTY = 330
        rBX = 180 #roll button's bottom x and y
        rBY = 370
        qTX = 220 #quit button's top x and y
        qTY = 330
        qBX = 280 #quit button's bottom x and y
        qBY = 370
        
        rollButton = Rectangle(Point(rTX, rTY), Point(rBX, rBY))
        rollButton.setFill("blue")
        rollText = Text(Point(rTX + 30, rTY + 20), "Roll")
        rollText.setFill("white")
        rollText.setSize(20)
        rollButton.draw(win)
        rollText.draw(win)    
  
        quitButton = Rectangle(Point(qTX, qTY), Point(qBX, qBY))
        quitButton.setFill("blue")
        quitText = Text(Point(qTX + 30, qTY + 20), "Quit")
        quitText.setFill("white")
        quitText.setSize(20)
        quitButton.draw(win)    
        quitText.draw(win)
        
        graphDie = Rectangle(Point(150,150), Point(250,250))
        graphDie.setFill("white")
        graphDie.draw(win)
        aDot = Circle(Point(175,165),10)
        aDot.setFill("black")
        dot = []

        #creates dots on left
        for i in range(3):
            dot.append(aDot.clone())
            dot[i].move(0,30*i)
            dot[i].draw(win)

        #creates dots on right
        aDot.move(50,0)
        for i in range(3,6):
            dot.append(aDot.clone())
            dot[i].move(0,30*(i-3))
            dot[i].draw(win)
    
        pt = win.getMouse()
        quitClicked = pt.getX() >= qTX and pt.getX() <= qBX
        quitClicked = quitClicked and pt.getY() >= qTY and pt.getY() <= qBY
        rollClicked = pt.getY() >= rTY and pt.getY()<= rBY
        rollClicked = rollClicked and pt.getX() >= rTX and pt.getX() <= rBX
        value = 6
        theDie = Die()
        
        while not quitClicked:
            for i in range(value):
                dot[i].undraw()
            if rollClicked:
                theDie.roll()
                value = theDie.getFaceValue() 
                for i in range(value):
                    dot[i].draw(win)
            pt = win.getMouse()
            quitClicked = pt.getX() >= qTX and pt.getX() <= qBX
            quitClicked = quitClicked and pt.getY() >= qTY and pt.getY() <= qBY
            rollClicked = pt.getY() >= rTY and pt.getY()<= rBY
            rollClicked = rollClicked and pt.getX() >= rTX and pt.getX() <= rBX
        win.close()

def main():
    playGame()
##        cir = Circle()
main()

