#This program calculates the area of a circle.
def circleArea():
    #Introduction
    print("This program is designed to calculate the area of a circle.")

    #Define variables.
    units = input("The units that will be used are: ")
    pi = 3.14159
    diameter = eval(input("Please enter the diameter of the circle: "))
    radius = diameter / 2

    #Calculate the area of the circle.
    area = 2 * pi * radius

    #Output the result.
    print("The area of the circle is", area, units, "squared.")
