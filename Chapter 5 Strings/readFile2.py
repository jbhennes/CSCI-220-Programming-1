def main():
    infile = open("names.txt", "r")


##    for line in infile:
##        dataList = line.split()
##        for dataStr in dataList:
##            data = eval(dataStr)
##            print(str(data * 5) + " ", end ="")
##        print()
            
    output = ""    
    for line in infile:
        dataList = line.split()
        for data in dataList:
            output = output + data + "-"
        output = output + "\n"    
            
    output = output + "\nAll done."
    print(output)

##    for line in infile:
##        lineNoReturn = line[:-1]
##        num = eval(lineNoReturn)
##        print(num*5)
main()
