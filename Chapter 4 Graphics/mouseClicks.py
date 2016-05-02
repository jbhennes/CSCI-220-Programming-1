# mouseClicks.py
# Author: Zelle (pp. 146-7)

from graphics import *

def main():
    winHeight = 400
    winWidth = 400
    
    win = GraphWin("Click Me!", winWidth, winHeight)
    for i in range(5):
        p = win.getMouse()
        print ("You clicked (",p.getX(), ",",p.getY(),")")

    # Wait for another click to exit
    Text(Point(winWidth/2, winHeight-10), "Click anywhere to quit").draw(win)
    win.getMouse()
    win.close()

main()
