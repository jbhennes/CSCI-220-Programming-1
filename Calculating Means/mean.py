## mean.py
## This is a program that is designed to calculate the mean, rms average,
##  and the harmonic mean of a set of numbers that is provided by the user.
## Class: CSCI 220 - Programming I
## Author: Jake Hennessy
##  I certify this lab is my own work.
## Prof: Stalvey
## Date: 1/26/14
##
## Software development process:
## 1.) This program will take a series of numbers provided by the users, and
##  use them to calculate a series of means including the RMS average and the
##  harmonic mean.
## 2.) The inputs will be series or list of numbers provided by the user, and
##  the outputs will be the values that will be calculated as mentioned in
##  question 1.
## 3.)  a.) Obtain the values to be calculated, and store them in variables.
##      b.) Use them to calculate the mean, RMS average, and harmonic mean,
##          in the various equations.
##      c.) Output the various averages.
## 4.) Implement the code:

    ## Import the math library.
from math import *
    ## Define the main function.
def mean():
    ## Introductions to the program.
    print("Welcome! \n This program is designed to calculate the mean \n RMS average and harmonic mean.")
    ## Obtain the list of values from the user.
    numbers = input("Please input a series of numbers separated by spaces \n <Hit Enter to Finish>: ")
    ## Create an empty list to hold the values provided by the user.
    numList = []
    ## Create a loop in which the numbers entered by spaces are placed into list created above.
    for number in numbers.split():  ## .split takes each set of numbers divided by spaces
        num = eval(number)          ## "num" is the evaluated result of each "number" in "numbers".
        numList.append(num)         ## adding each number evaluated to numList

    ## Perform the calculations to obtain the result.
    mean = (sum(numList))/(len(numList))                                ## Both RMS and Harmonic mean use a for loop
    rmsAverage = sqrt((sum(num*num for num in numList))/(len(numList))) ## with no body-- but list beforehand the
    harmonicMean = len(numList)/sum((1/num) for num in numList)         ## operations for the loop to iterate through

    ## Print the results.
    print("The Mean is: \t", mean)
    print("The RMS Average is: \t", rmsAverage)
    print("The Harmonic Mean is: \t", harmonicMean)
    restart()

    ## Allow the user to restart the function.
def restart():
    print("Would you like to restart?")
    restart = round(eval(input("1 - Yes / 0 - No: ")))
    if restart == (1):
        main()
    elif restart == (0):
        print("Thanks for playing and have a great day!")
    elif restart < (1) and restart > (0):
        restart = 0
        print("OK-- Thanks for playing, i guess . . .")
    elif restart > 1:
        restart = 1
        print("All right, I guess you meant to say '1' so . . .")
        main()
    elif restart < 0:
        restart = 0
        print("That's nice, see you later.")

    ## Define the main function.
def main():
    mean()
    restart()

## Start the program.
main()
