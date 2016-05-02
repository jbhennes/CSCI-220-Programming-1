# Usind Die.py to create a graphical die
# Rolls the die

from die2 import Die
from graphics import *

class GraphicDie:

   #Constructs a die with instance variables:
   #self.win: a GraphWin object
   #self.numSides: the numbers of sides of the die
   #self.graphDie: A Rectangle object, bounding box for the die
   #self.dot: A list of black circles representing the dots on the die
   def __init__(self,win): 
    self.win = win
    width = self.win.getWidth()
    self.numSides = 6

    #die's outer boundaries
    rUXY = width/2 - 50
    lLXY = width/2 + 50    
    self.graphDie = Rectangle(Point(rUXY,rUXY), Point(lLXY,lLXY))
    self.graphDie.setFill("white")
    self.graphDie.draw(self.win)

    #1st dot's initial location
    dX = width/2 - 25
    dY = width/2 - 35
    rad = 10
    aDot = Circle(Point(dX, dY),rad)
    aDot.setFill("black")

    #creates dots on left
    self.dot = []
    for i in range(self.numSides//2):
        self.dot.append(aDot.clone())
        self.dot[i].move(0,30*i)
        self.dot[i].draw(self.win)

    #creates dots on right
    aDot.move(50,0)
    for i in range(self.numSides//2, self.numSides):
        self.dot.append(aDot.clone())
        self.dot[i].move(0,30*(i-self.numSides//2))
        self.dot[i].draw(self.win)
   
   def roll(self):
      theDie = Die()
      for i in range(self.numSides):
        self.dot[i].undraw()
      theDie.roll()
      value = theDie.getFaceValue() 
      for i in range(value):
        self.dot[i].draw(self.win)


def main():
    win = GraphWin("Die", 400, 400)
    gDie = GraphicDie(win)
    win.getMouse()
    for i in range(10):
       gDie.roll()
       win.getMouse()
    win.getMouse()
    win.close()
       


