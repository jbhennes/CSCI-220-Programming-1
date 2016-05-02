## Test GraphicDie
#Stalvey

from graphicDie import GraphicDie
from graphics import *

def drawRollButton(win):
##   rTX = 120 #roll button's top x and y
##   rTY = 330
##   rBX = 180 #roll button's bottom x and y
##   rBY = 370
   
   #roll button coordinates top x, top y, bottom x, bottom y
   rBCoord = [120, 330, 180, 370]
   p1 = Point(rBCoord[0], rBCoord[1])
   p2 = Point(rBCoord[2], rBCoord[3])   
   rollButton = Rectangle(p1, p2)
   rollButton.setFill("blue")
   rollText = Text(Point(rBCoord[0] + 30, rBCoord[1] + 20), "Roll")
   rollText.setFill("white")
   rollText.setSize(20)
   rollButton.draw(win)
   rollText.draw(win)
   return rBCoord
   

def drawQuitButton(win):
##   qTX = 220 #quit button's top x and y
##   qTY = 330
##   qBX = 280 #quit button's bottom x and y
##   qBY = 370
   #quit button coordinates top x, top y, bottom x, bottom y
   qBCoord = [220, 330, 280, 370]
   p1 = Point(qBCoord[0], qBCoord[1])
   p2 = Point(qBCoord[2], qBCoord[3])   
   quitButton = Rectangle(p1, p2)
   quitButton.setFill("blue")
   quitText = Text(Point(qBCoord[0]+ 30, qBCoord[1]+ 20), "Quit")
   quitText.setFill("white")
   quitText.setSize(20)
   quitButton.draw(win)    
   quitText.draw(win)
   return qBCoord


def playDie(win, qBC, rBC):
   pt = win.getMouse()
   quitClicked = pt.getX() >= qBC[0] and pt.getX() <= qBC[2]
   quitClicked = quitClicked and pt.getY() >= qBC[1] and pt.getY() <= qBC[3]
   rollClicked = pt.getY() >= rBC[1] and pt.getY()<= rBC[3]
   rollClicked = rollClicked and pt.getX() >= rBC[0] and pt.getX() <= rBC[2]
   
   theDie = GraphicDie(win)
   while not quitClicked:
      if rollClicked:
          theDie.roll()
      pt = win.getMouse()
      quitClicked = pt.getX() >= qBC[0] and pt.getX() <= qBC[2]
      quitClicked = quitClicked and pt.getY() >= qBC[1] and pt.getY() <= qBC[3]
      rollClicked = pt.getY() >= rBC[1] and pt.getY()<= rBC[3]
      rollClicked = rollClicked and pt.getX() >= rBC[0] and pt.getX() <= rBC[2]
   win.close()


def main():
    win = GraphWin("Die", 400, 400)
    rollButtonCoord = drawRollButton(win)
    quitButtonCoord = drawQuitButton(win)
    playDie(win,quitButtonCoord, rollButtonCoord)
   
main()
