##jumpingJack.py
##
##Name : Jake Hennessy
##Date : 3.30.14
##Class : CSCI 220 - Programming I
##Prof : Stalvey
##
##Certification of Authenticity :
##    I certify this program is my own work.
##
##Description :
##    Using the author's graphics package, this program will create a
##    representation of a stick figure and three additional buttons that will
##        be labeled "START", "STOP", and "QUIT".
##    Clicking 'Start' will make the stick figure begin doing jumping jacks.
##    Clicking 'Stop' will make the stick figure stop doing jumping jacks.
##    Clicking 'Quit' will make the stick figure stop doing jumping jacks,
##        and it will also close the graphics window.
##    If User clicks outside of the buttons, nothing will occur.
##    Directions for the program will be included on the window.

## Importing different packages to use within the program.
from graphics import *
import time
from random import *

## Creating a function to produce buttons.

def createButton(anchorPoint, textString):
    # Using parameters above, we will create a standard button.
    button = Rectangle((anchorPoint), (Point((anchorPoint.getX() + 80), (anchorPoint.getY() + 50))))
    # Cloning button to create a shadow effect
    buttonShadow = button.clone()
    # Setting button styles
    button.setOutline('white')
    button.setWidth(2)
    button.setFill(color_rgb(100, 149, 237))
    # Setting shadow styles
    buttonShadow.setFill('black')
    buttonShadow.move(3, 3)
    # Setting button text style
    buttonText = Text((button.getCenter()), (textString))
    buttonText.setTextColor('white')
    buttonText.setFace('helvetica')
    # return the various objects
    return button, buttonText, buttonShadow

## Create an animate button function.

def animateButton(button, buttonText):
    # moving the upper button to appear 'clicked'
    button.move(3, 3)
    buttonText.move(3, 3)
    # Changing the styles of the button when 'clicked'
    buttonText.setStyle('bold')
    button.setWidth(4)
    button.setFill(color_rgb(255, 99, 71))
    # Pause
    time.sleep(.5)
    # Undo the above changes, to make button appear to 'pop back out'
    button.move(-3, -3)
    buttonText.move(-3, -3)
    buttonText.setStyle('normal')
    button.setWidth(2)
    button.setFill(color_rgb(100, 149, 237))
    return

## Define a function to style the text on the window in a similar manner.

def setTextStyle(textObject, size, textColor, style):
    textObject.setFace('')
    textObject.setStyle(style)
    textObject.setSize(size)
    textShadow = textObject.clone()
    textShadow.move(2, 2)
    textObject.setTextColor(textColor)
    textShadow.setTextColor('black')
    return textObject, textShadow

## Defining the function that will define the logic for the buttons.
## This function accepts a Point object where the user clicked and
## a Rectangle object that is the bounding box for a button.
## This function should return True if the click occurred within the
## bounds of the rectangle and False otherwise.
def wasClicked(pt, rect):
    rectP1 = rect.getP1()
    rectP2 = rect.getP2()
    rectP1X = rectP1.getX()
    rectP1Y = rectP1.getY()
    rectP2X = rectP2.getX()
    rectP2Y = rectP2.getY()
    if (pt.getX() > rectP1X and pt.getX() < rectP2X) and (pt.getY() > rectP1Y and pt.getY() < rectP2Y):
        return True
    else:
        return False

## Defining a function to make jack jump.

#def startJack():
    
    ## Creating a point for the stick figure
    ## Create the head
    headCenter = Point(325, 130)
    head = Circle(headCenter, 40)
    head.setFill('Dark Turquoise')
    head.setOutline('tomato')
    ## Create the body
    bodyLine = Line(Point(325, 170), Point(325, 250))
    bodyLine.setOutline('tomato')
    ## Create the legs.
    legLine1 = Line(Point(325, 250), Point(285, 340))
    legLine2 = Line(Point(325, 250), Point(365, 340))
    legLine1.setOutline('tomato')
    legLine2.setOutline('tomato')
    ## Create the arms.
    armLine1 = Line(Point(325, 190), Point(230, 155))
    armLine2 = Line(Point(325, 190), Point(395, 155))
    armLine1.setOutline('tomato')
    armLine2.setOutline('tomato')
    return


## Defining a function to make jack stop.

#def stopJack():

    ## Creating a point for the stick figure
    ## Create the head
    headCenter = Point(325, 130)
    head = Circle(headCenter, 40)
    head.setFill('Dark Turquoise')
    head.setOutline('tomato')
    ## Create the body
    bodyLine = Line(Point(325, 170), Point(325, 250))
    bodyLine.setOutline('tomato')
    ## Create the legs.
    legLine1 = Line(Point(325, 250), Point(315, 340))
    legLine2 = Line(Point(325, 250), Point(335, 340))
    legLine1.setOutline('tomato')
    legLine2.setOutline('tomato')
    ## Create the arms.
    armLine1 = Line(Point(325, 190), Point(300, 260))
    armLine2 = Line(Point(325, 190), Point(350, 260))
    armLine1.setOutline('tomato')
    armLine2.setOutline('tomato')
    


## Creating the main function for the program.
def main():

## The first steps are for ceating the GUI
    ## Create a graphics window.
    win = GraphWin('Jumping Jack', 600, 400)
    win.setBackground('light blue')
    ## Creating the ground for jack to jump on
    anchorGrassPt1 = Point(0, 335)
    anchorGrassPt2 = Point(600, 400)
    grass = Rectangle(anchorGrassPt1, anchorGrassPt2)
    grass.setFill('SeaGreen')
    grass.draw(win)
## Drawing the buttons for the different functions.
    ## Start Button.
    startBttnAnch = Point(30, 45)
    startBttn, startMsg, startBttnShadow = createButton(startBttnAnch, 'Start')
    startBttnShadow.draw(win)
    startBttn.draw(win)
    startMsg.draw(win)
    ## Stop Button.
    stopBttnAnch = Point(30, 130)
    stopBttn, stopMsg, stopBttnShadow = createButton(stopBttnAnch, 'Stop')
    stopBttnShadow.draw(win)
    stopBttn.draw(win)
    stopMsg.draw(win)
    ## Quit Button.
    quitBttnAnch = Point(30, 215)
    quitBttn, quitMsg, quitBttnShadow = createButton(quitBttnAnch, 'Quit')
    quitBttnShadow.draw(win)
    quitBttn.draw(win)
    quitMsg.draw(win)
## Creating the graphics objects that will form 'jack'.
    ## Create the head
    headCenter = Point(325, 130)
    head = Circle(headCenter, 40)
    head.setFill('Dark Turquoise')
    head.setOutline('tomato')
    ## Create the body
    bodyLine = Line(Point(325, 170), Point(325, 250))
    bodyLine.setOutline('tomato')
    bodyLine.setWidth(10)
    ## Create the legs.
    legLine1 = Line(Point(325, 250), Point(315, 340))
    legLine2 = Line(Point(325, 250), Point(335, 340))
    legLine1.setOutline('tomato')
    legLine2.setOutline('tomato')
    legLine1.setWidth(10)
    legLine2.setWidth(10)
    ## Create the arms.
    armLine1 = Line(Point(325, 190), Point(300, 260))
    armLine2 = Line(Point(325, 190), Point(350, 260))
    armLine1.setOutline('tomato')
    armLine2.setOutline('tomato')
    armLine1.setWidth(10)
    armLine2.setWidth(10)
    ## Create the legs (when jumping)
    legLine3 = Line(Point(325, 250), Point(285, 340))
    legLine4 = Line(Point(325, 250), Point(365, 340))
    legLine3.setOutline('tomato')
    legLine4.setOutline('tomato')
    legLine3.setWidth(10)
    legLine4.setWidth(10)
    ## Create the arms (when jumping)
    armLine3 = Line(Point(325, 190), Point(255, 155))
    armLine4 = Line(Point(325, 190), Point(395, 155))
    armLine3.setOutline('tomato')
    armLine4.setOutline('tomato')
    armLine3.setWidth(10)
    armLine4.setWidth(10)
    ## Drawing all graphics objects ('jack') in the window.
    head.draw(win)
    bodyLine.draw(win)
    legLine1.draw(win)
    legLine2.draw(win)
    armLine1.draw(win)
    armLine2.draw(win)

## Beginning the while loop that will wait on a mouse
    ##  click to execute commands
    ##
    goVar = 0
    jumpingJackCount = 0
    point = None
    while point == None:
        point = win.checkMouse()
        if point != None:
            userX = point.getX()
            userY = point.getY()
            userClick = Point(userX, userY)
            startClick = wasClicked(userClick, startBttn)
            stopClick = wasClicked(userClick, stopBttn)
            quitClick = wasClicked(userClick, quitBttn)
            if startClick == True:
                animateButton(startBttn, startMsg)
                goVar = 1
                while goVar == 1:
                    legLine1.undraw()
                    legLine2.undraw()
                    armLine1.undraw()
                    armLine2.undraw() 
                    legLine3.draw(win)
                    legLine4.draw(win)
                    armLine3.draw(win)
                    armLine4.draw(win)
                    jumpingJackCount += 1
                    print(jumpingJackCount)
                    time.sleep(.25)
                    legLine3.undraw()
                    legLine4.undraw()
                    armLine3.undraw()
                    armLine4.undraw() 
                    legLine1.draw(win)
                    legLine2.draw(win)
                    armLine1.draw(win)
                    armLine2.draw(win)
                    time.sleep(.25)
                    point = win.checkMouse()
                    if point != None:
                        userX = point.getX()
                        userY = point.getY()
                        userClick = Point(userX, userY)
                        stopClick = wasClicked(userClick, stopBttn)
                        quitClick = wasClicked(userClick, quitBttn)
                        if stopClick == True:
                            goVar = 0
                            animateButton(stopBttn, stopMsg)
                        elif quitClick == True:
                            animateButton(quitBttn, quitMsg)
                            win.close()
                        else:
                            print('Nothing was clicked')
            elif stopClick == True:
                goVar = 0
                animateButton(stopBttn, stopMsg)
                point = win.checkMouse()
                if point != None:
                    userX = point.getX()
                    userY = point.getY()
                    userClick = Point(userX, userY)
                    startClick = wasClicked(userClick, startBttn)
                    stopClick = wasClicked(userClick, stopBttn)
                    quitClick = wasClicked(userClick, quitBttn)
            elif quitClick == True:
                goVar = 0
                animateButton(quitBttn, quitMsg)
                win.close()
            else:
                print('Nothing was clicked')
            point = None
            

main()
