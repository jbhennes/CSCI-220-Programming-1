# testCard.py
#
# Name: Jake Hennessy
# Date: 4.20.14
# Prof: Stalvey
#
# Certification of Authenticity:
#   I certify that this program is my own work.
#
# Purpose: This program is to test the card class program written as step
#           one of the homework assignment. This program will create an
#           instance of the class and will test the various methods to ensure
#           that they work.

from Card import Card

def main():

    ## Create instance(s) of cards to ensure constructor and string method are
    ##  functional, as well as the validSuit() method
    card = Card(1, "Diamonds")
    print(card)
    card1 = Card(14, "Hearts")
    print(card1)
    card2 = Card(13, "Clubs")
    print(card2)
    card3 = Card(11, "Spades")
    print(card3)
    card4 = Card(12, "Kitty Paws")
    print(card4)
    card5 = Card(12.5, "Kitty Paws")
    print(card5)
    card6 = Card(13, "Diamonds")
    print(card6)

    ## Next, we will test the getter functions to ensure that they work as well
    card = Card(4, "Clubs")
    print(card)
    card.getSuit()
    card.getFaceValue()

    ## Finally once again we test the string method.
    card = Card(1, "Diamonds")
    print(card)
    print(card1)
    card1 = Card(8, "Spades")
    print(card1)

main()
    

