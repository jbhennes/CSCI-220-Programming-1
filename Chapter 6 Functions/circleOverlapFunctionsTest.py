from circleOverlapFunctions import *
from graphics import *

def main():
   width = 400
   height = 400
   numCircles = 5
   win = GraphWin("Overlapping Circles", width, height)

   instructionsPt = Point(width/2, 20)

   instructions = Text(instructionsPt, "Click two points")
   instructions.draw(win)

   circles = []
   for i in range(numCircles):
      instructions.setText("Click two points for circle #" + str(i+1))
      circles.append(makeCircle(win, i+1))
      instructions.setText("")
      circles[i].draw(win)
      

##   print ("i\tj")
##   for i in range(numCircles - 1):
##      for j in range(i+1, numCircles):
##         print ("circle " + str(i+1) + " overlaps circle ", end = " ")
##         print (str(j+1) + ": ", end = " ")
##         print (overlap(circles[i], circles[j]))

   
   textPt = Point(width/2, height - 20)
   text = Text(textPt, "Click to close")
   text.draw(win)
   win.getMouse()
   win.close()

main()
   
