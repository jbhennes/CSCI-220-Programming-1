# closedShapes.py
# A program designed to calculate the volume and suface area of a rectangular
#   prism and a closed cylinder.
# Class: CSCI 220 - Programming I
# By: Jake Hennessy
#   I certify this lab is my own work.
# Prof: Stalvey
# Date: 1/12/14

import math

# Define the prism function that calculates volume and surface area.
def prism():
    # Introductions to the prism program.
    print("Welcome!")
    print("This program will calculate the volume and surface area of a rectangular prism with a sqaure base.")
    print("All that will be needed is the length of any side of the base and the height of the prism.")
    # Gathering data from the user and defining variables.
    prismUnits = input("First, what are the units being used?: ")
    sideLength = eval(input("Please provide the value for the length of one side of the base: "))
    prismHeight = eval(input("Please provide the value for the height: "))
    # Perform the calculations.
    prismVolume = (sideLength ** 2) * prismHeight
    prismSurfaceArea = (4 * sideLength * prismHeight) + (2 * sideLength ** 2)
    # Provide the output for the calculations.
    print("The volume of the rectangular prism is", (prismVolume), (prismUnits), "cubed.")
    print("The surface area of the rectangular prism is", (prismSurfaceArea), (prismUnits), "squared.")

# Define the cylinder function for volume and surface area.
def cylinder():
    # Introductions to the cylinder program.
    print("Welcome!")
    print("This program will calculate the volume and surface area of a closed cylinder.")
    print("All that will be needed is the radius and height of the cylinder.")
    # Gathering data from the user and defining variables.
    pi = 3.14159
    cylinderUnits = input("First, what are the units being used?: ")
    cylinderRadius = eval(input("Please provide the value for the radius of the cylinder: "))
    cylinderHeight = eval(input("Please provide the value for the height of the cylinder: "))
    # Perform the calculations.
    cylinderVolume = (pi * (cylinderRadius * cylinderRadius) * cylinderHeight)
    cylinderSurfaceArea = (2 * pi * cylinderRadius ** 2) + (2 * pi * cylinderRadius * cylinderHeight)
    # Provide the output for the calculations.
    print("The volume of the cylinder is", (cylinderVolume), (cylinderUnits), "cubed.")
    print("The surface area of the cylinder is", (cylinderSurfaceArea), (cylinderUnits), "squared.")

# Define the main function of the program.
def main():
    prism()
    cylinder()
    restart()

# Define the restart function.
def restart():
    print("Would you like to perform another calculation?")
    restartAnswer = abs(int(input("1 = Yes/ 0 = No: ")))
    if restartAnswer == (1):
        main()
    elif restartAnswer == (0):
        print("Thanks for playing, and have a great day!")
    elif restartAnswer < (0):
        print("My, aren't we creative?")
        restart()
    elif restartAnswer > (1):
        print("My, aren't we creative?")
        restart()

main()
