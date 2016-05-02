##Draws a shape based on the user clicks.

from graphics import *

def main():
   win = GraphWin("User Creates",400, 400)
   win.setBackground("white")

   
   width = win.getWidth()
   height = win.getHeight()
   
   textPt = Point(width/2, height -10)
   t = Text(textPt, "Click five points on the screen")
   t.draw(win)

   clickPt1 = win.getMouse()
   x = clickPt1.getX()
   y = clickPt1.getY()
   print ("User clicked at: (" +str(x) + ", " + str(y) + ").")

   clickPt2 = win.getMouse()
   x = clickPt2.getX()
   y = clickPt2.getY()
   print ("User clicked at: (" +str(x) + ", " + str(y) + ").")

   clickPt3 = win.getMouse()
   clickPt4 = win.getMouse()
   clickPt5 = win.getMouse()
   
##   rect = Rectangle(clickPt1, clickPt2)
##   rect.setFill("purple")
##   rect.draw(win)
##
##   ptList = [clickPt1, clickPt2,clickPt3, clickPt4, clickPt5]
##   poly = Polygon(ptList)
   poly = Polygon(clickPt1, clickPt2, clickPt3, clickPt4, clickPt5)
   poly.setFill("blue")
   poly.draw(win)
   
   #waits on user to click the window before closing
   t.setText("Click to close")
   win.getMouse()
   win.close()

main()
