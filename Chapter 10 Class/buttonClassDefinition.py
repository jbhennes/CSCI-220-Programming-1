#Button Class
#Stalvey

from graphics import *

class Button:
   def __init__(self, x1, y1, x2, y2, colorStr):
      midX = (x1+x2)/2
      midY = (y1+y2)/2
      self.color = colorStr.lower()
      self.text = Text(Point(midX, midY), colorStr.capitalize())
      self.border = Rectangle(Point(x1, y1), Point(x2, y2))
      self.isDrawn = False

   def getColor(self):
      return self.color

   def setColor()

   def draw(self, win):
      if not self.isDrawn:
         self.text.draw(win)
         self.border.draw(win)
         self.isDrawn = True

   def undraw(self):
      if self.isDrawn:
         self.text.undraw()
         self.border.undraw()
         self.isDrawn = False

   def isClicked(self, pt):
      ptX = pt.getX()
      ptY = pt.getY()

      buttonP1 = self.border.getP1()
      buttonP2 = self.border.getP2()
      bX1 = buttonP1.getX()
      bY1 = buttonP1.getY()
      bX2 = buttonP2.getX()
      bY2 = buttonP2.getY()

      clicked = False
      
      if ptX >= bX1 and ptX <= bX2:
         if ptY >= bY1 and ptY <= bY2:
            clicked = True

      return clicked
   
      
