## Acronym.py
##
## User enters a phrase, an acronym is formed from its words.


def main():
    phrase = input("Enter a phrase: ")
    newPhrase = phrase.upper()
    words = newPhrase.split()
    print("\n",words)

##    print ("The acronym for \'" + phrase + "\' is:")
##    for word in words:
##        print (word[0], end = "")
##    print()

##    for i in range(len(words)):
##        word = words[i]
##        print (word[0], end = "")
##
    print("\nUsing an accumulating string:")
    acronym = ""
    for word in words:
        acronym = acronym + word[0]
    print (acronym)


main()
    
