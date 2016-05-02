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
        if ch=='A' or ch=='E' or ch=='I' or ch =='O' or ch=='U':
            vowelCount = vowelCount + 1
        elif ch==' ':
            spaceCount = spaceCount + 1
        else:
            conCount = conCount + 1
    print ("\nIn your input:\n" + userIn)
    print ("\nThere are: \n{0:3} vowel(s)".format(vowelCount))
    print (str(spaceCount) + " spaces")
    print (str(conCount) + " consonants")

main()
    
