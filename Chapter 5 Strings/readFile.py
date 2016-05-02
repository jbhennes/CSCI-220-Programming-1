# readFile.py
# Various ways to read a text file

def main():

    infile = open("myfile.txt", "r")
    print (infile)
    # 1 - Using a for loop to go through the file:
    for line in infile:
        print (line)
    infile.close()

    infile = open("myfile.txt", "r")
    # 2 - to avoid double-spacing:
    for line in infile:
        print (line,end="")

    # 3 - another way to avoid double-spacing:
    for line in infile:
        print (line[:-1])

    # 4 - read entire file into a string:
    allContents = infile.read()
    print (allContents)
    lineList = allContents.split("\n")
    print (lineList)
    print ("lineList[0] = " + lineList[0])

    allContents = infile.read()
    print ("allContents" + allContents)
    
    # 5 - reads only the first line into a string:
    line = infile.readline()
    print (line)

    #Skip lines of the file
    for i in range(2):
        line = infile.readline()
    allContents = infile.read()
    print (allContents)

    # 6 - reads entire file, a line at a time:
    #     (You must know how many lines there are.)
    for count in range(3):
        line = infile.readline()
        print (line, end="")

    # 7 - reads entire file into a list of strings:
    list = infile.readlines()
    print (list)
    line = list[0]
    print ("line initially" + line)
    line = line[0:-1]
    print ("line without return" + line)

    # 8 - reads entire file, a line at a time:
    for line in infile.readlines():
        print (line,end="")

    # 9 - new line character at the end of each line
    for line in infile:
        lineSplit = string.split(line)
        print (lineSplit)
        
    # 10 - read line of file, then process through each word
    for line in infile:
        lineSplit = string.split(line)
        for word in lineSplit:
            print (word + ", ", end="")
        print ()

    infile.close()


main()
 
