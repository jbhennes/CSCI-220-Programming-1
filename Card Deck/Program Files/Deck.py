# Deck.py
#
# Name: Jake Hennessy
# Date: 4.20.14
# Prof: Stalvey
#
# Certification of Authenticity:
#   I certify that this program is my own work.
#
# Purpose: This is a program that will simulate a deck using python classes.
#           The deck will use the python card class created earlier.
#           the deck will initialize with 52 cards and a next property that
#           represents the next card available to deal.
#           In addition this class will contain a string, shuffle, deal,
#           and sort methods that will be used in a card game of war.

from Card import Card
from random import shuffle

class Deck:

    def __init__(self):
        self.next = 0
        self.cards = []
        i = 0
        j = 1
        for i in range(0, 4):
            for j in range(1, 14):
                if i == 0:
                    suit = 'Clubs'
                    card = Card(j, suit)
                elif i == 1:
                    suit = 'Diamonds'
                    card = Card(j, suit)
                elif i == 2:
                    suit = 'Hearts'
                    card = Card(j, suit)
                elif i == 3:
                    suit = 'Spades'
                    card = Card(j, suit)
                self.cards.append(card)
        

    def shuffle(self):
        shuffle(self.cards)
        self.next = 0

    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop(0)
        else:
            return -1

    def sort(self):
        self.next = 0
        n = len(self.cards)
        if 'Clubs' < 'Diamonds' < 'Hearts' < 'Spades':
            for bottom in range(n - 1):
                minP = bottom
                for i in range(bottom + 1, n):
                    iCard = self.cards[i].getSuit()
                    minCard = self.cards[minP].getSuit()
                    if iCard < minCard:
                        minP = i
                    elif iCard == minCard:
                        jCard = self.cards[i].getFaceValue()
                        minCard = self.cards[minP].getFaceValue()
                        if jCard < minCard:
                            minP = i
                temp = self.cards[minP]
                self.cards[minP] = self.cards[bottom]
                self.cards[bottom] = temp
                    
               
##        n = len(self.cards)
##        for bottom in range(n - 1):
##            minP = bottom
##            for j in range(bottom + 1, n):
##                jCard = self.cards[j].getFaceValue()
##                minCard = self.cards[minP].getFaceValue()
##                if jCard < minCard:
##                    minP = j
##            temp = self.cards[minP]
##            self.cards[minP] = self.cards[bottom]
##            self.cards[bottom] = temp
            
            
                

    def __str__(self):
        rtnStr = [str(card) for card in self.cards]
        return '\n'.join(rtnStr)

