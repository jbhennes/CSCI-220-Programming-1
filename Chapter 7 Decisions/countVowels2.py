# countVowels.py

def main():
    print ("This program will count the number of spaces, consonants ")
    print ("and vowels in a collection of words.")
    userIn = input("Enter your words (No punctuation): ")
    capIn = userIn.upper()
    vowelCount = 0
    spaceCount = 0
    conCount = 0
    for ch in capIn:
        isVowel = ch=='A' or ch=='E' or ch=='I' or ch =='O' or ch=='U'
        isSpace = ch == ' '
        if not(isVowel) and not(isSpace):
            conCount = conCount + 1
        elif isSpace:
            spaceCount = spaceCount + 1
        else:
            vowelCount = vowelCount + 1
    print ("\nIn your input:\n" + userIn)
    print ("\nThere are: \n{0:3} vowel(s)".format(vowelCount))
    print (str(spaceCount) + " spaces")
    print (str(conCount) + " consonants")

main()
    
