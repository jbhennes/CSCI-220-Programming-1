# convert_gui.py
# Converts celsius to fahrenheit using a simple gui
# Author: Zelle (pp. 148-9)
# Modified by Pharr so as not to use coordinates

from graphics import *

def main():
    win = GraphWin("Celsius to Fahrenheit", 300, 200)

    # Draw the interface
    Text(Point(100, 50), "   Celsius temperature: ").draw(win)
    Text(Point(100, 150), "Fahrenheit temperature: ").draw(win)
    inp = Entry(Point(200, 50), 5)
    inp.setText("0.0")
    inp.draw(win)
    output = Text(Point(200, 150), "")
    output.draw(win)
    inp.setText("")
    button = Text(Point(150, 100), "Convert It")
    button.draw(win)
    Rectangle(Point(115, 80), Point(185, 120)).draw(win)

    # Wait for a mouse click
    win.getMouse()

    # Convert input
    celsius = eval(inp.getText())
    fahrenheit = 9.0/5.0 * celsius + 32

    # Display output and change button
    output.setText("%0.1f" % fahrenheit)
    button.setText("Quit")
    
    # Wait for another click to exit
    win.getMouse()
    win.close()

main()
