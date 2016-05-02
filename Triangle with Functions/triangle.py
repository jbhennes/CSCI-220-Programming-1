### triangle.py
###
### Author: Zelle (pp. 103-04)
### Modified by Pharr to eliminate coordinates
### Latest revision by Jake Hennesssy
###   I certify that this update of the program is my work.
### Date: 2.19.14
###
### Purpose: This is a program intended to use functions defined
###   outside the main function and return information to the main function.
###   Specifically this will create a graphic program that will allow user input
###   to create a triangle (using a function), and also to output perimeter and
###   area based on information returned from other functions as well.

from graphics import *
from math import *
import time

def distance(p1, p2):
    euclidDist = sqrt(((p1.getX()-p2.getX())**2) + (p1.getY()-p2.getY())**2)
    return euclidDist
    
def makeTriangle(p1, p2, p3):
    # Use Polygon object to draw the triangle
    triangle = Polygon(p1, p2, p3)
    return triangle

def perimeter(tri):
    listPoints = tri.getPoints()
    dist1 = distance(listPoints[0], listPoints[1])
    dist2 = distance(listPoints[1], listPoints[2])
    dist3 = distance(listPoints[2], listPoints[1])
    perimeter = dist1 + dist2 + dist3
    return perimeter

def area(tri):
    listPoints = tri.getPoints()
    dist1 = distance(listPoints[0], listPoints[1])
    dist2 = distance(listPoints[1], listPoints[2])
    dist3 = distance(listPoints[2], listPoints[1])
    s = (dist1 + dist2 + dist3) / 2
    area = sqrt(s * (s - dist1) * (s - dist2) * (s - dist3))
    return area


def main():
    winWidth = 400
    winHeight = 400

    # Create a graphic window for the visual part of this assignment
    win = GraphWin("Draw a Triangle", winWidth, winHeight)
    message = Text(Point(winWidth/2, winHeight-10), "Click on three points")
    message.draw(win)

    # Create empty list for the points to come
    vertexList = []

    # Creating a list of colors for a nice color changing effect later on
    colors = ["cyan","chartreuse", "peachpuff", "yellow", "blue", "purple"]

    # Get and draw three vertices of a triangle
    point1 = win.getMouse()
    vertexList.append(point1)
    point1.draw(win)
    point2 = win.getMouse()
    vertexList.append(point2)
    point2.draw(win)
    point3 = win.getMouse()
    vertexList.append(point3)
    point3.draw(win)

    # Call the makeTriangle() function to use the above points
    userTriangle = makeTriangle(vertexList[0], vertexList[1], vertexList[2])
    userTriangle.setFill("cyan")
    userTriangle.setOutline("peachpuff")
    userTriangle.draw(win)

    # Set a color loop in motion when the triangle is drawn
    for i in range(len(colors)):
        win.setBackground(colors[i])
        time.sleep(.125)
        
    """# Call the distance function and store it in variables, for all
    #   the side distances
    distanceA = distance(vertexList[0], vertexList[1])
    distanceB = distance(vertexList[1], vertexList[2])
    distanceC = distance(vertexList[2], vertexList[0])"""

    # Calling the perimeter function
    userPerimeter = perimeter(userTriangle)

    # Calling the area funtction
    userArea = area(userTriangle)
    
    # Displaying text to the screen that displays the calculated values
    perimText = Text(Point(winWidth / 2, winHeight - 50), "The perimeter is: " + str(round(userPerimeter, 2)) + " units.")
    areaText = Text(Point(winWidth / 2, winHeight - 30), "The area is: " + str(round(userArea, 2)) + " units squared.")
    areaText.setStyle("bold")
    perimText.setStyle("bold")
    message.setTextColor("white")
    areaText.setTextColor("white")
    perimText.setTextColor("white")
    areaText.setSize(20)
    perimText.setSize(20)
    areaText.draw(win)
    perimText.draw(win)
    
    # Wait for another click to exit
    message.setText("Click anywhere to quit")
    win.getMouse()
    win.close()

main()
    
