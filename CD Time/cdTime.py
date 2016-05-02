## cdTime.py
##
## Name: Jacob Hennessy
##  I certify that this program is my own work.
## Purpose: This is a program that is used to calculate the total playtime
##  of any possible number of CDs, according to the input of number of
##  tracks and track times by the user.
## Prof: Stalvey
## Date: 1/26/14
##

def totalPlayTime():
    ## Introductions and purpose
    print("Welcome! \n\n This program is designed to calculate the total playtime of multiple CDs.\n")
    ## Create empty list to hold CD time totals outside of the loop(s).
    CDTotals = []
    ## Obtain the number of CDs that will be processed.
    numCDs = round(abs(eval(input("1.) How many CDs will be processed? \n\n Number of CDs: <Hit Enter When Finished> "))))
    ## Declare the first (outer) loop that will iterate for each CD
    for (CD) in range(numCDs):
        ## Creation of empty list(s) to hold data
        CDList = []
        trackTimes = []
        ## Adding each iteration to a list for CD numbers
        CDList.append(CD + 1)
        ## (re)Setting variables, to obtain the correct values for each loop
        totalTrackSeconds = 0
        totalMinutes = 0
        totalSeconds = 0
        ## For use in the second (inner) loop, obtain the number of tracks
        numTracks = round(abs(eval(input("\n2.) How many tracks are on CD " + str(CD + 1) + " ? \n\n Number of Tracks: <Hit Enter Whem Finished> "))))
        print("\nNext, we will gather the play times of the tracks. \n\n ( NOTE: If track time is 3:06, input should be: 3,6 )\n")
        ## Declaring the second (inner) loop that stores data for each track.
        for track in range(numTracks):
            minutes, seconds = eval(input("Please enter the time of track " + str(track + 1) + " (Minutes, Seconds): "))
            '''The lines of code underneath are an alternative declaration of the variables 'minutes' and 'seconds'.'''
            ## minutes = eval(input("Please enter the minutes of track " + str(track + 1) + ":"))
            ## seconds = eval(input("Please enter the seconds of track " + str(track + 1) + ":"))
            ## Conditional statements to correct possible faulty input.
            if minutes < 0:
                minutes, seconds = eval(input("Please enter the time of track " + str(track + 1) + "(Minutes, Seconds): "))
            elif seconds < 0:
                minutes, seconds = eval(input("Please enter the time of track " + str(track + 1) + "(Minutes, Seconds): "))
            ## Perform calculations
            ## Multiplying (minutes * 60) to yield answer in seconds,
            ##  and adding the remaining seconds for a total(sec).
            minInSeconds = minutes * 60
            secondsTrackTime = minInSeconds + seconds
            ## Finally, append each total to trackTimes list
            trackTimes.append(secondsTrackTime)
            ## End of second (inner) loop.
        ## Now that track times are stored in the list, we can perform the neccessary calculations.
        totalTrackSeconds = sum(trackTimes)
        CDTotals.append(totalTrackSeconds)
        totalMinutes = totalTrackSeconds // 60
        totalSeconds = totalTrackSeconds % 60
        ## Output the results.
        print("\nThe total time of CD", (CD + 1), "is", totalMinutes, "minutes and", totalSeconds, "seconds.\n")
    ## Calculate the total time of all CDs.
    allCDSecTotal = sum(CDTotals)
    ## Taking the 'allCDSecTotals' value (in seconds!) and converting it to minutes and hours, if needed.
    finalSecondsTotal = allCDSecTotal % 60
    finalMinutesTotal = allCDSecTotal // 60
    ## Variables for hours if needed.
    finalHoursTotal = finalMinutesTotal // 60
    minutesRemainder = finalMinutesTotal % 60
    ## Conditional that will alter output based on if finalMinutesTotal is greater than/equal to 60.
    if finalMinutesTotal < 60:
        print("Total time of all CDs: " + str(finalMinutesTotal) + " minutes and " + str(finalSecondsTotal) + " seconds.\n")
    elif finalMinutesTotal >= 60:
        print("Total time of all CDs: " + str(finalHoursTotal) + " hours " + str(minutesRemainder) + " minutes and " + str(finalSecondsTotal) + " seconds.\n")

totalPlayTime()
