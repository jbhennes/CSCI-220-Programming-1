def countVowelsBeforeZ(string):
   vowelCount = 0
   if len(string) > 0:
      
      vowels = "aeiou"
      string = string.lower()

      numIter = 0
      foundZ = False
      for ch in string:
         if ch == "z":
            foundZ = True
         else:
            if foundZ == False and ch in vowels:
               vowelCount += 1
         numIter += 1
      print("For vowelCount", vowelCount)   
      print("For took", numIter, "iterations")
      
      numIter = 0
      vowelCount = 0
      pos = 0
      character = string[pos]
      while pos < len(string) and character != "z":
         if character in vowels:
            vowelCount += 1
         pos += 1
         if pos < len(string):
            character = string[pos]
         numIter += 1

      print("While took", numIter, "iterations")

   return vowelCount


def main():
   numVowels = countVowelsBeforeZ("The quick brown fox jumps over the lazy dog.")
   print("Vowels b4 z", numVowels, "\n")

   numVowels = countVowelsBeforeZ("")
   print("Vowels b4 z", numVowels, "\n")

   numVowels = countVowelsBeforeZ("zachary")
   print("Vowels b4 z", numVowels, "\n")

   numVowels = countVowelsBeforeZ("aeizaei")
   print("Vowels b4 z", numVowels, "\n")

main()
