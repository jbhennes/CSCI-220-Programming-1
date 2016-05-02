def main():
   text = "Sue, Bill, and Bob"
   print(text,"\n")
   print("1a.",text.find(","))
   print("b.",text.split(","))
   y = text.split(" ")
   print("c.",len(y[0]))
   print("d.",chr(ord(text[0]) + 3))
   print("e.", text[0:4])
   print("f.", text[5]+text[2]*2)

   print()
   print("2a. values[4] + values[1]")
   print("b. values[2] + values[0]")
   print("c. values[0] * eval(values[3])")
   print("d. values[1] * 5")
   print("e. values[:1] + values[2:4]")
   print("f. len(values)")

   print()

   "3. In class"

"4."
def insert(text, value, pos):
   newText = text[:pos] + value + text[pos:]
   return newText

"5. Two options: "
def reverse(text):
   revText = ""
   for ch in text:
      revText = ch + revText
   return revText

def reverse2(text):
   revText = ""
   for i in range(len(text) - 1, -1, -1):
      revText += text[i]
   return revText

"6."
def emailAddress(name):
   name = name.lower()
   nameList = name.split()

   first = nameList[0]
   mid = nameList[1]
   last = nameList[2]
   ext = "@g.cofc.edu"

   email = last[:8] + mid[0] + first[0] + ext
   return email

"7. In class."

"8."
infile = open("data.txt", "r")
total = 0
count = 0
for line in infile:
   data = line.split()
   total += eval(data[2])
   count += 1
avg = total/count
infile.close()

"9."
def alterColor(graphObj, color):
   graphObj.setFill(color)

"9.1."
def average():
   infileName = input(“what is the name is the file? <w/ .txt extension>) \nfile: ”)
   infile = open(infileName, “r”)
   outfileName = (“output.txt”, “w”)
   ages = []
   for line in lines:
      values = line.split()
      age = eval(values[2])
      ages.append(age)
   average = sum(ages)/ len(ages)
   print(average)
main()
