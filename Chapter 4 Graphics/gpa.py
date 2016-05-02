from graphics import *

def main():
   width = 400
   height = 400
   win = GraphWin("GPA", width, height)

   box = Entry(Point(width/2, height/2), 15)
   box.setText("Type gpa here")
   box.draw(win)
   
   text = Text(Point(width/2, height-10), "click to print")
   text.draw(win)
   win.getMouse()
   
   gpa = eval(box.getText())
   gpa = gpa + 1
   box.undraw()

   text.setText("Gpa is " + str(gpa) + ". Click to close")
   win.getMouse()
   win.close()

main()

   
