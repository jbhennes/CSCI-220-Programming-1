## disfiguredFace.py
## Exercise 3, p. 160

from graphics import *

def main():
    win = GraphWin()

    head = Circle(Point(100, 90), 90)
    head.setOutline("pink")
    head.setFill("pink")
    head.draw(win)

    leftEye = Circle(Point(70, 70), 10)
    leftEye.setOutline("blue")
    leftEye.setFill("blue")
    leftEye.draw(win)

    rightEye = leftEye
    leftEye.setFill("black")
    rightEye.move(60, 0)

    print ("rightEye = ", rightEye)
    print ("leftEye = ", leftEye)
    print ("head = ", head)
    

    nose = Polygon(Point(100, 90), Point(95, 120), Point(105, 120))
    nose.setOutline("red")
    nose.setFill("red")
    nose.draw(win)

    mouth = Rectangle(Point(70, 140), Point(130, 150))
    mouth.setOutline("red")
    mouth.setFill("white")
    mouth.draw(win)

    Text(Point(100, 190), "Click to quit").draw(win)
    w = win.getMouse()
    win.close()

main()
