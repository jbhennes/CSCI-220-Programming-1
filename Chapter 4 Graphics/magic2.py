## magic2.py

from graphics import *

def main():
   winHeight = 400
   winWidth = 400

   ## ----------------------------------------------
   ## ------ NO MAGIC NUMBERS BELOW THIS LINE ------
   ## ----------------------------------------------

   win = GraphWin("No Magic Numbers", winWidth, winHeight)
   radius = winWidth / 10
   c = Circle(Point(winWidth/2, winHeight/2), radius)
   c.setFill("Red")
   c.draw(win)
   commentHeight = winHeight * 0.9
   t = Text(Point(winWidth/2, commentHeight), "The cirlce is centered in the window.")
   t.draw(win)

   # Wait for another click to exit
   msgHeight = winHeight * 0.95
   Text(Point(winWidth/2, msgHeight), "Click anywhere to quit").draw(win)
   win.getMouse()
   win.close()
main()
