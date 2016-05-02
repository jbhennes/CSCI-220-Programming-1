## weightedAverage.py
##
## Name: Jake Hennessy
##   I certify that this program is my own work.
##
## Class: CSCI 220
## Prof: Stalvey
## Date: 2.18.14
##
## Purpose: This program is intended to utilize Python's ability to read text
##    files and take the numeric data contained and use that within functions
##    defined inside of this program.

def main():

    # Ask the user to input the name of a text file that contains grades
    #   with weights.
    print('Welcome! \n This program is designed to read numeric input from a .txt file\n and use it inside of a Python program.')
    print()
    fileName = input('What is the name of the file that you would like to use? \n (Please Include .txt Extension!) \n\t Name of file: ')
    
    # Create an empty list to hold the values for all of the weighted averages,
    #   so they are easy to average later.
    weightedAveragesList = []
    
    # Open the text file, and designate that it will be used for reading.
    infile = open(fileName, 'r')
    
    # Print an opening introduction so the user knows that the .txt file is being
    #   read and data is being extracted.
    print ("\n###-- " + fileName + " --###\n")
    
    # Loop that will separate values, and empty lists to hold what will become numeric values.
    for line in infile:
        allValues = line.split()
        # Empty list(s) to hold the weight and grade values
        grades = []
        weights = []
        # This is used to reset this variable for each student to 0
        weightedAverage = 0
        # This will take the values pertinent for the weights list, and will
        #   append them to the aforementioned list
        for i in range(2, len(allValues), 2):
            numWeight = eval(allValues[i])
            weights.append(numWeight)
        # This will take the values pertinent for the grades list, and will
        #   append them to the aforementioned list
        for i in range(3, len(allValues), 2):
            numGrade = eval(allValues[i])
            grades.append(numGrade)
        # Using a final loop to index though the grades and weights list
        #   to be able to calculate the weighted average!
        for i in range(len(grades)):
            weightedAverage = ((weights[i]) * (grades[i])) + weightedAverage
        finalWeightAverage = weightedAverage / 100
        weightedAveragesList.append(finalWeightAverage)
        # Output print line for each student
        print(allValues[0] + " " + allValues[1] + "'s average: {0:.1f}".format(finalWeightAverage))
    # Calculate the average for the whole class, and output it in a print line
    totalAverageWeighted = ( sum(weightedAveragesList) / len(weightedAveragesList) )
    print("\nClass Average: ", (totalAverageWeighted))
    # Close the file
    infile.close()

main()
