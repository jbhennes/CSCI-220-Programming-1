#This function calculates the area of a rectangle.
def rectArea():
    #Purpose of the program.
    print("This program calculates the area of a rectangle.")
    units = input("First, tell me the units that will be used: ")
    #Define variables
    length = eval(input("Please input the length of the rectangle: "))
    width = eval(input("Please input the width of the rectangle: "))
    #Perform the calculation.
    area = length * width
    print("The area of the rectangle is", area, units, "squared.")
    #Restart command.
    restart = int(input("Would you like to restart? (1 = Yes / 0 = No): "))
    if restart == (1):
        rectArea()
    elif restart == (0):
        print("Gsme Over")
    elif restart < (0) or > (1):
        print("Funny. Try again.")
        restart = int(input("( Yes = 1 / No = 0): "))
        if restart == (1):
            rectArea()
        elif restart == (0):
            print("Game Over")
        elif restart < (0) or > (1):
            print("Fine, have it your way.")
            rectArea()

