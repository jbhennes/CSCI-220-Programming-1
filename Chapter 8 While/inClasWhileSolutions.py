from graphics import *
from random import randint

def main():
    circles = []
    for i in range(10):
        rad = randint(10, 40)
        circles.append(Circle(Point(0,0), rad))
        print(str(rad) + ", ", end = "")

    print()
    i = 0
    while not (i >= len(circles) or circles[i].getRadius() > 30):
        i += 1
    if i == len(circles):
        print("All circles are too small")
    else:
        print("Circles[" + str(i) + "] has radius of ", end = "")
        print(str(circles[i].getRadius()))
##    names = ["jake", "israel", "kevin", "kim"]
##    answer = input("Enter name: ")
##    answer = answer.lower()
####    found = False
##    stillSearching = True
##    
##    while stillSearching: #equivalent to: while not found
##        i = 0
##        while (i < len(names) and answer != names[i]):
##            i += 1
##        if i < len(names):
##            print ("You guessed correctly")
##            print ("Found student at " + str(i) + ".")
##            stillSearching = False
##        else:
##            print ("Guess again.")
##            answer = input("Enter name: ")
        
##    while not (answer in names):
##        answer = input("Enter name: ")
##        answer = answer.lower()
##    print("You entered "  + answer)

##    value = eval(input("Enter num: "))
##    while not (value == 10 or value >= 20 and value < 30):
##        print("Enter 10 or a value in the twenties to terminate.")
##        value = eval(input("Enter num: "))
##    print("You entered " + str(value) + ".")



##    passwd = input ("Enter your password: ")
##    attempts = 1
##    while not (passwd == "abc123" or attempts == 3):
##        print("Incorrect password!")
##        passwd = input ("Enter your password: ")
##        attempts += 1
##    if passwd == "abc123":
##        print("You entered the correct password.")
##        print("It took " + str(attempts) + " try/tries.")
##    else:
##        print("You only had three tries to enter the correct password.")
##        print("You failed.")
    
##    message = "Enter number (Type nothing to quit): "
##    infile = open("data.txt", "r")
##    total = 0
##    count = 0
##    line = infile.readline()
##    while line != "":
##        values = line.split()
##        for valueStr in values:
##            count = count + 1
##            total = total + eval(valueStr)
##        line = infile.readline()
##    if count > 0:
##        print("Sum: " + str(total))
##        print("Average: {0:.2f}".format(total/count))
##    else:
##        print("No values to average")
##    print("Done!")

main()
