## pig.py
##
## Name : Jake Hennessy
## Date : 3.19.14
## Class : CSCI 220
## Prof : Stalvey
##
## Certification of Authenticity :
##    I certify that this program is my own work.
##
## Purpose : This program is intended to replicate a game of "pig", a dice game
##    that involves rolling a pair of dice and accumulating points. The first
##    player to reach 100 wins. If "snakeyes" is rolled, all of the points for
##    the rolling player are lost and the turn goes to the other player.
##        If one shows up on either die, then the turn is passed, but points
##    will remain. Player has the ability to forfeit their turn after any roll,
##    but they risk having the other player win.
##        There will be a computer player that the user will play against, and
##    the computer player will forfeit their turn rolling the dice after 20
##    points are accumulated, or if a one is rolled.
##        Also, this program will practice modulation of code through creation
##    of several independent functions, and will also practice implementation of
##    conditionals via the if/then statements, and the while statements.
##


# Importing random library in order to simulate random dice rolls

from random import *


# This function will simulate a six sided dice roll.

def roll():
    # Picks a random integer (1-6) and stores it
    diceRoll = randint(1, 6)
    # Returns the value to be used in other functions
    return diceRoll


# This function will roll the dice in the previous function, and accumulate
#   the total points earned by the player, giving them the option to continue
#   rolling the dice until a 1 (or snakeyes) is rolled.

def playerPlays(totalPlayerPoints):
    # Variable that will represent whether the turn will continue: 1,
    #   or the turn will end: 0.
    continueRoll = 1
    print('\n##############################################################\n')
    print('User\'s turn: \n')
    # Quick prompt to allow the game's progression to be controlled by the user
    readyPrompt = input('<-- Hit Enter To Begin -->\n')
    # Conditionals:
    #   This creates the indefintie loop that allows the turn to continue
    while (continueRoll == 1) and (totalPlayerPoints < 100):
        print()
        # Using the roll() function defined above
        roll_1 = roll()
        print('\nThe User\'s first roll was: \n', roll_1)
        roll_2 = roll()
        print('\nThe User\'s second roll was: \n', roll_2)
        # If statements that cause the while loop to stop.
        if (roll_1 == 1) and (roll_2 == 1):
            # rolled snakeyes, turn is over and points = 0
            totalPlayerPoints = 0
            continueRoll = 0
            print('\n\t***** Oh No!! Snakeyes!! *****\n\t***** All points are lost! *****\n')
            print('\nUser\'s Score:', totalPlayerPoints, '\n')
        elif (roll_1 == 1) or (roll_2 == 1):
            # rolled a 1, so turn is over
            totalPlayerPoints = (0 + totalPlayerPoints)
            continueRoll = 0
            print('\n\t***** You rolled a one! *****\n\t***** No points accumulated! *****\n')
            print('\nUser\'s Score:', totalPlayerPoints, '\n')
        elif (roll_1 != 1) and (roll_2 != 1):
            # 1 was not rolled, and points accumulate
            totalPlayerPoints = (roll_1 + roll_2 + totalPlayerPoints)
            print('\nUser\'s Score:', totalPlayerPoints, '\n')
            # If statements determining whether game is won, or if turn will continue
            if totalPlayerPoints < 100:
                continuePrompt = input('\nWould you like to roll again?:\ny = Yes / n = No: ')
                # If statement asking if the user wants to continue
                if continuePrompt == 'y' or continuePrompt == 'Y' or continuePrompt == 'yes' or continuePrompt == 'Yes':
                    continueRoll = 1
                    print('\n\t***** User has elected to roll again! *****\n')
                elif continuePrompt == 'n' or continuePrompt == 'N' or continuePrompt == 'no' or continuePrompt == 'No':
                    continueRoll = 0
                    print('\n\t***** User has elected to end turn! *****\n')
                    print('\nUser\'s Score:', totalPlayerPoints, '\n')
            # Player has 100 or more points, so turn ends.
            elif totalPlayerPoints >= 100:
                print()
    # Announcing end of turn, and returning the score value.
    print('\n***** END OF USER\'S TURN! *****\n')
    return totalPlayerPoints
    
# This function controls the computer's rolls, the same rules will apply,
#   but after the computer accumulates 20 points or rolls at least one (1)
#   the turn will end and user will play.

def computerPlays(totalComputerPoints):
    # Variable that will represent whether the turn will continue: 1,
    #   or the turn will end: 0.
    continueRoll = 1
    # Initializing point values for each computer turn, so that turn will end if
    #   computer scores more than 20 points
    totalPointsThisTurn = 0
    print('\n##############################################################\n')
    print('Computer\'s turn: \n')
    # Conditionals.
    #   This creates the indefintie loop that allows the turn to continue
    while continueRoll == 1 and totalComputerPoints < 100:
        # Initializing this variable
        cpuPointsThisTurn = 0
        # Quick prompt to allow the game's progression to be controlled by the user
        readyPrompt = input('<-- Hit Enter To Begin -->\n')
        print()
        # Rolling dice
        diceRoll1 = roll()
        print('\nThe Computer\'s first roll was: \n', diceRoll1)
        diceRoll2 = roll()
        print('\nThe Computer\'s second roll was: \n', diceRoll2)
        # storing points earned this roll, and adding them to the points earned
        #   this turn
        cpuPointsThisTurn += diceRoll1 + diceRoll2
        totalPointsThisTurn += cpuPointsThisTurn
        # If statements to make turn end
        if (diceRoll1 == 1) and (diceRoll2 == 1):
            # Snakeyes, points = 0 and turn is over
            totalComputerPoints = 0
            continueRoll = 0
            print('\n\t***** The Computer rolled Snakeyes!! *****\n\t***** All of the Computer\'s points are lost! *****\n')
            print('\nComputer\'s Score:', totalComputerPoints, '\n')
        elif (diceRoll1 == 1) or (diceRoll2 == 1):
            # Rolled a 1, turn is over and no points are added from the last roll
            totalComputerPoints += 0
            continueRoll = 0
            print('\n\t***** The Computer rolled a one! *****\n\t***** No points accumulated! *****\n')
            print('\nComputer\'s Score:', totalComputerPoints, '\n')
        elif (diceRoll1 != 1) and (diceRoll2 != 1):
            # Rolled no 1's, so we check to see if points earned this turn are less
            #   than 20, and checking if computer's score is sufficient for a win
            if (totalPointsThisTurn) >= 20 and totalComputerPoints < 100:
                # Computer earned 20+ points, but has not won
                totalComputerPoints += cpuPointsThisTurn
                continueRoll = 0
                print('\n\t***** Computer has earned at least 20 points! *****\n\t***** The Computer has elected to forfeit this turn! *****\n')
                print('\nComputer\'s Score:', totalComputerPoints, '\n')
            elif (totalPointsThisTurn) < 20 and totalComputerPoints < 100:
                # Computer earned less than 20 points and has not won,
                #   turn continues
                totalComputerPoints += cpuPointsThisTurn
                continueRoll = 1
                print('\nComputer\'s Score:', totalComputerPoints, '\n')
            elif (totalPointsThisTurn) < 20 and totalComputerPoints >= 100:
                # Computer earned less than 20 points, but has enough points to win
                totalComputerPoints += cpuPointsThisTurn
                continueRoll = 0
                print('\n\t***** Computer has earned at least 20 points! *****\n\t***** The Computer has elected to forfeit this turn! *****\n')
                print('\nComputer\'s Score:', totalComputerPoints, '\n')
            elif (totalPointsThisTurn) >= 20 and totalComputerPoints >= 100:
                # Computer earned 20+ points and has enough to win
                totalComputerPoints += cpuPointsThisTurn
                continueRoll = 0
                print('\nComputer\'s Score:', totalComputerPoints, '\n')
    # End of turn, and returning computer's score value
    print('\n***** END OF COMPUTER\'S TURN! *****\n')
    return totalComputerPoints

# This function will control the game itself, seeing if player or
#   computer has scored 100 or more points

def playPig():
    # Initializing total score values
    playerScore = 0
    computerScore = 0
    # Initializing variable to switch between players per each turn
    turnCounter = 1
    # Initializing strings for the winner of the game
    winnerMsg = ''
    winnerName = ''
    # Prompt to decide who will go first!
    #   Random number is generated (1-100), whoever is closer will go first
    randomNumber = randint(1, 100)
    print('To determine who goes first, guess a number from 1 to 100: ')
    userGuess = eval(input('\tUser guess: '))
    computerGuess = randint(1, 100)
    print('\nThe Computer has guessed:', computerGuess)
    print('\nThe Secret Number was:', randomNumber,'\n')
    # Conditionals to determine flow of game
    #   User won the number pick, user goes first
    if (abs(randomNumber - userGuess)) < (abs(randomNumber - computerGuess)):
        # turnCounter is reset to reflect this flow of game
        turnCounter = 2
        # Conditionals to determine if game will continue
        while (playerScore < 100) and (computerScore < 100):
            # this is where turnCounter will switch between players,
            #   by incrementing by 1, and mod 2 the result
            if (turnCounter % 2) == 0:
                # Player's turn
                playerScore = playerPlays(playerScore)
                print('\n\t<---- SCOREBOARD ---->\n')
                print('\tUser\'s Score:', playerScore)
                print('\tComputer\'s Score:', computerScore)
                turnCounter += 1
            elif (turnCounter % 2) == 1:
                # Computer's turn
                computerScore = computerPlays(computerScore)
                print('\n\t<---- SCOREBOARD ---->\n')
                print('\tUser\'s Score:', playerScore)
                print('\tComputer\'s Score:', computerScore)
                turnCounter += 1
        # Checking to see if game is over!
        if (playerScore >= 100):
            winnerName = 'user'
            print('\n##############################################################\n')
            print('\n\t***** User has accumulated', playerScore, 'points! *****\n')
            winnerMsg = '\t***** USER WINS!! *****\n'
        elif (computerScore >= 100):
            winnerName = 'computer' 
            print('\n##############################################################\n')
            print('\n\t***** Computer has accumulated', computerScore, 'points! *****\n')
            winnerMsg = '\t***** COMPUTER WINS!! *****\n'
    elif (abs(randomNumber - userGuess)) > (abs(randomNumber - computerGuess)):
        # Computer won the number pick, computer goes first
        #   turnCounter is reset to reflect this flow of game
        turnCounter = 1
        # Conditionals to determine if game will continue
        while (playerScore < 100) and (computerScore < 100):
            if (turnCounter % 2) == 0:
                playerScore = playerPlays(playerScore)
                print('\n\t<---- SCOREBOARD ---->\n')
                print('\tUser\'s Score:', playerScore)
                print('\tComputer\'s Score:', computerScore)
                turnCounter += 1
            elif (turnCounter % 2) == 1:
                computerScore = computerPlays(computerScore)
                print('\n\t<---- SCOREBOARD ---->\n')
                print('\tUser\'s Score:', playerScore)
                print('\tComputer\'s Score:', computerScore)
                turnCounter += 1
        # Checking to see if game is over!
        if (playerScore >= 100):
            winnerName = 'user'
            print('\n##############################################################\n')
            print('\n\t***** User has accumulated', playerScore, 'points! *****\n')
            winnerMsg = '\t***** USER WINS!! *****\n'
        elif (computerScore >= 100):
            winnerName = 'computer' 
            print('\n##############################################################\n')
            print('\n\t***** Computer has accumulated', computerScore, 'points! *****\n')
            winnerMsg = '\t***** COMPUTER WINS!! *****\n'
    # if computer number guess and user guess are equidistant from the randomNumber:
    else:
        print('Woah There buddy, let\'s do that again...')
        playPig()
    # Returning the winner
    return winnerMsg, winnerName


# This is the main function that will call the game functions, store number of
#   wins, and also allow players to play again.

def main():
    # Initializing variables for number of wins per player
    computerWins = 0
    userWins = 0
    # Initializing variable to keep game running in while loop
    gameRunning = 1
    # Conditionals.
    #   These will control the start and stop of game
    while gameRunning == 1:
        print('\t***** Welcome! *****\n***** Let\'s play a game of PIG!! *****\n')
        winnerMsg, winnerName = playPig()
        if winnerName == 'user':
            userWins += 1
        elif winnerName == 'computer':
            computerWins += 1
        print(winnerMsg)
        print('\n##############################################################\n')
        print('\n\t***** PLAYER RECORDS *****\n')
        print('\tUser\'s Wins:', userWins)
        print('\tComputer\'s Wins:', computerWins, '\n')
        # Game has ended, do we want to play another?
        print('\nWould you like to play another game of pig?\n')
        userYorN = input('y = Yes / n = No: ')
    # If statements to determine is game will be played again
    if (userYorN == 'y') or (userYorN == 'Y') or (userYorN == 'yes') or (userYorN == 'Yes'):
        # gameRunning will be set so that the while loop runs again
        gameRunning == 1
        print('\nAll right, here we go again!\n')
        playPig()
    elif (userYorN == 'n') or (userYorN == 'N') or (userYorN == 'no') or (userYorN == 'No'):
        # gameRunning will be set so that the while loop does not run again
        gameRunning == 0
        print('\nThanks for playing!!')
    else:
        # If all else fails, play again.
        main()
            
# Call main() function to start the game.
main()
