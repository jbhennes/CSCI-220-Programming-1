## face1.py
## Exercise 3, p. 160

from graphics import *

def main():
    win = GraphWin("Face", 200, 700)
    winWidth = win.getWidth()
    winHeight = win.getHeight()

    head = Circle(Point(100, 90), 90)
    head.setOutline("pink")
    head.setFill("pink")
    head.draw(win)

##    p = Point(70,70)
    leftEye = Circle(Point(70, 70), 15)
    leftEye.setOutline("brown")
    leftEye.setFill("brown")
    leftEye.draw(win)

##    rightEye = leftEye #alias
    rightEye = leftEye.clone() #clone
    rightEye.move(60, 0)
    rightEye.draw(win)
    rightEye.setFill("blue")

##    rightEye = Circle(Point(130, 70), 10)
##    rightEye.setOutline("blue")
##    rightEye.setFill("blue")
##    rightEye.draw(win)

    nose = Polygon(Point(100, 90), Point(95, 120), Point(105, 120))
    nose.setOutline("red")
    nose.setFill("red")
    nose.draw(win)

    mouth = Rectangle(Point(70, 140), Point(130, 150))
    mouth.setOutline("red")
    mouth.setFill("white")
    mouth.draw(win)

    closePt = Point(winWidth/2, winHeight - 10)
    closeText = Text(closePt, "Click to quit")
    closeText.draw(win)
    w = win.getMouse()
    win.close()

main()
