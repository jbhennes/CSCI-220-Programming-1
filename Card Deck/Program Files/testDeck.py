# testDeck.py
#
# Name: Jake Hennessy
# Date: 4.20.14
# Prof: Stalvey
#
# Certification of Authenticity:
#   I certify that this program is my own work.
#
# Purpose: This program is designed to test all of the methods created
#           in the Deck class, including constructors, methods shuffle(),
#           sort(), and deal(), and the __str__ method.
#           in addition, this program will also use the card and deck
#           classes to play a simulated game of war.

## Importing the deck (and card) classes.

from Card import Card
from Deck import Deck

## Testing the Deck() constructor.

print('#<====== Creating Deck ======>#\n')
d = Deck()
print('The __str__ method shows the deck like so:\n')
print(d)
print('The length of this deck is', len(d.cards))
print('\nAnd the other property is d.next =', str(d.next))
print()

## Testing the Shuffle method.

print('\n#<====== Shuffling Deck ======>#\n')
d.shuffle()
print('The shuffle method will return the deck as:\n')
print(d, '\n')

## Testing the sort method.

print('\n#<====== Sorting Deck ======>#\n')
d.sort()
print('The sort method will return the deck as:\n')
print(d, '\n')

## Testing the Deal method.

print('\n#<====== Dealing Deck ======>#\n')
print('Card #1 is', d.deal())
print('Card #2 is', d.deal())
print('\nThe number of cards left in the deck:', len(d.cards))
print()

def battle():
    print('\n#<====== Playing a Game of War ======>#\n')
    ## Creating p1Score, p2Score, ties variables.
    p1Score = 0
    p2Score = 0
    ties = 0
    ## Creating two hands to hold cards (that are dealt for each player)
    h1 = []
    h2 = []
    ## Creating a new deck for the cards
    d = Deck()
    ## Shuffling the new deck
    d.shuffle()
    ## Using a loop to deal cards to the two players.
    for i in range(len(d.cards)):
        if i % 2 == 0:
            h1.append(d.deal())
        elif i % 2 == 1:
            h2.append(d.deal())
        i += 1
    ## printing each player's hands
    print('\n#<====== Player 1\'s Hand: ======>#\n')
    for card in h1:
        print(card)
    print('\n#<====== Player 2\'s Hand: ======>#\n')
    for card in h2:
        print(card)
    print('\n#<====== Now its time for WAR!!! ======>#\n')
    
    

battle()
