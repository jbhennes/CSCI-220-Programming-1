# shootingStars.py
#
# Name: Jake Hennessy
#   I certify this program is my own work.
#
# Prof: Stalvey
# CSCI 220
# Date: 2.13.14

from graphics import *
import time

def shootingStars():
    # Create Window and set the color.
    win = GraphWin("Greeting Card", 500, 600)
    win.setBackground("blue4")
    # Create the rectangle that will appear in the window as grass
    rectPoint1 = Point(0, 400)
    rectPoint2 = Point(500, 600)
    grass = Rectangle(rectPoint1, rectPoint2)
    grass.draw(win)
    grass.setFill("green4")
    # Create the rectangle that will appear in the window as the house
    rectPoint3 = Point(150, 250)
    rectPoint4 = Point(350, 450)
    house = Rectangle(rectPoint3, rectPoint4)
    house.draw(win)
    house.setFill("white")
    # Create the triangle that will appear in the window as the roof
    roofPoint = Point(250, 200)
    roofPoint2 = Point(125, 260)
    roofPoint3 = Point(375, 260)
    roof = Polygon(roofPoint, roofPoint2, roofPoint3)
    roof.setFill("brown2")
    roof.draw(win)
    # Create the rectangle that will appear in the window as the door
    rectPoint5 = Point(225, 375)
    rectPoint6 = Point(275, 450)
    door = Rectangle(rectPoint5, rectPoint6)
    door.draw(win)
    door.setFill("red4")
    # Create the rectangle(s) that will appear in the window as the windows
    rectPoint7 = Point(175, 275)
    rectPoint8 = Point(225, 325)
    window1 = Rectangle(rectPoint7, rectPoint8)
    window1.draw(win)
    window1.setFill("gray")
    window2 = window1.clone()
    window2.move(100, 0)
    window2.draw(win)
    # create the text telling the user to click in the sky
    textPoint = Point(250, 550)
    textForClicks = Text(textPoint, "Click on the sky to create stars!")
    textForClicks.setFace("courier")
    textForClicks.setTextColor("yellow")
    textForClicks.setSize(22)
    textForClicks.draw(win)
    # Create the shooting stars.
    stars = []
    starCenters = []
    for i in range(8):
        userClick = win.getMouse()
        starCenters.append(userClick)
        star = Circle(userClick, 5)
        star.setFill("yellow")
        star.draw(win)
        stars.append(star)
    # Creating a "constellation" by using polygons
    constellation = Polygon(starCenters)
    constellation.setOutline("yellow2")
    constellation.draw(win)
    # Create the shooting star effect, first we change the directions
    textForClicks.undraw()
    textSurprise = Text(textPoint, "Click again to start the show!")
    textSurprise.setFace("courier")
    textSurprise.setTextColor("yellow")
    textSurprise.setSize(22)
    textSurprise.draw(win)
    win.getMouse()
    textSurprise.undraw()
    for star in stars:
        for i in range(50):
            star.move(5, 2)
            time.sleep(.01)
            star.setFill("black")
            star.move(5, 2)
            time.sleep(.01)
            star.setFill("white")
            star.move(5, 2)
            time.sleep(.01)
            star.setFill("yellow")
        star.undraw()
    # Create text for the card greeting!
    greetingText = Text(Point(((win.getWidth())/2), 100), "Happy Chinese New Year!")
    greetingText.setTextColor("red")
    greetingText.setFace("courier")
    greetingText.setStyle("bold italic")
    greetingText.setSize(30)
    greetingText.draw(win)
    time.sleep(4)
    greetingText.undraw()
    # Create text to instruct to close
    closeText = Text(Point(((win.getWidth())/2), 150), "Click Window to Close")
    closeText.setTextColor("red")
    closeText.setFace("courier")
    closeText.setStyle("bold italic")
    closeText.setSize(22)
    closeText.draw(win)
    # Close window
    win.getMouse()
    win.close()
    
shootingStars()
