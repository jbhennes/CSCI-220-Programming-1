def main():
##    infile = open("myfile.txt", "r")
##
##    for line in infile:
##        print(line)
##
##    infile.close()

##    infile = open("myfile.txt", "r")
##
##    line = infile.readline()
##    print(line)
##
##    print("Using for loop:")
##    for line in infile:
##        print(line)
##
##    line = infile.readline()
##    print(line)
##    
##    infile.close()

##    infile = open("myfile.txt", "r")
##    allContents = infile.read()
##    print(allContents)
##
##    words = allContents.split()
##    print("Words:\n" + str(words))
##
##    lines = allContents.split("\n")
##    print("Lines:\n" + str(lines))
##
##    infile.close()
    
    infile = open("myfile.txt", "r")
    lines = infile.readlines()
    print(lines)
    infile.close()
    
main()


    
        
