## magic1.py

from graphics import *


def main():
   #win = GraphWin("Magic Numbers")
   win = GraphWin("Magic Numbers", 500, 200)
   winMidWidth = 200
   winMidHeight = 200
   c = Circle(Point(winMidWidth, winMidHeight), 20)
   c.setFill("Red")
   c.draw(win)
   Text(Point(winMidWidth, winMidHeight+30), "The circle is centered in the window.").draw(win)

   # Wait for another click to exit
   Text(Point(winMidWidth, winMidHeight +50), "Click anywhere to quit").draw(win)
   win.getMouse()
   win.close()

main()
