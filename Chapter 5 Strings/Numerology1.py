## Numerology1.py
##
## Enter a name, return its numerological score.

import string

def main():
    name = raw_input("Enter a name: ")

    #print name
    name = string.lower(name)
    #print name

    sum = 0

    for letter in name:
        #print letter,
        number = ord(letter) - ord("a") + 1
        #print number
        sum = sum + number

    print "The name's numerological score is", sum

