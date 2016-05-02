# Card.py
#
# Name: Jake Hennessy
# Date: 4.20.14
# Prof: Stalvey
#
# Certification of Authenticity:
#   I certify that this program is my own work.
#
# Purpose: To create a class program that will simulate a card.
#           Defined in this class will be variables as to face value
#           and suit, and some additional methods that will allow the
#           cards to be used within a deck (defined elsewhere).


class Card:

    # Constructor.
    def __init__(self, value, suit):
        if self.validSuit(suit) == True and type(value) == int and value > 0 and value < 14:
            self.face = value
            self.suit = suit
        else:
            self.face = 1
            self.suit = "Spades"

    # "Getter" methods for value and suit
    def getSuit(self):
        return self.suit

    def getFaceValue(self):
        return self.face

    # Valid suit method.
    def validSuit(self, suit):
        suit = str(suit.lower())
        validList = ['clubs', 'diamonds', 'hearts', 'spades']
        if suit in validList:
            return True
        else:
            return False

    # String method.
    def __str__(self):
        if self.face == 1:
            rtnStr = ('Ace of '+ str(self.suit))
        elif self.face == 11:
            rtnStr = ('Jack of ' + str(self.suit))
        elif self.face == 12:
            rtnStr = ('Queen of ' + str(self.suit))
        elif self.face == 13:
            rtnStr = ('King of ' + str(self.suit))
        else:
            rtnStr = str(self.face) + ' of ' + str(self.suit)
        return rtnStr
        
        
        
