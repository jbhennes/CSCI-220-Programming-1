from graphics import *
from time import sleep

def main():
   win = GraphWin("Move",500,500)
   c2 = Circle(Point(50, 75), 20)
   c2.setFill("blue")
   c2.draw(win)

   dx = .5
   dy = .9
   for i in range(100):
      c2.move(dx, dy)
      sleep(.1)

   win.getMouse()
   win.close()

main()

   
