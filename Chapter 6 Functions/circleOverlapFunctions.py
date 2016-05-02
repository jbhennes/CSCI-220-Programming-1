from graphics import *
from math import *

def makeCircle(win, label=""):
   centerPt = win.getMouse()
   edgePt = win.getMouse()
   #Create a label for the center of the circle
   text = Text(centerPt, str(label))
   text.draw(win)
   #calculateDistance
   radius = calculateDistance(centerPt, edgePt)
   circle = Circle(centerPt, radius)
   return circle

def calculateDistance(pt1, pt2):
   x1 = pt1.getX()
   y1 = pt1.getY()
   x2 = pt2.getX()
   y2 = pt2.getY()
   return sqrt((x1-x2)**2 + (y1-y2)**2)

def overlap(circle1, circle2):
   center1 = circle1.getCenter()
   center2 = circle2.getCenter()
   distance = calculateDistance(center1, center2)
   radius1 = circle1.getRadius()
   radius2 = circle2.getRadius()
   totalRadius = radius1 + radius2
   if distance > totalRadius:
      rtnValue = False
   else:
      rtnValue = True
   return rtnValue



   
   
