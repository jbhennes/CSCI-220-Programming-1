 # Defining our own polygon.

from graphics import *
 
def main():
    win2 = GraphWin("User Defined Points", 400, 400)
    points = []
    for i in range(10):
        pt = win2.getMouse()
        pt.draw(win2)
        points.append(pt)
        print("(", pt.getX(), ",", pt.getY(), ")")

    polygon2 = Polygon(points)
    polygon2.draw(win2)

    win2.getMouse()
    win2.close()

main()
