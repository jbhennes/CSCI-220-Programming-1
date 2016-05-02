def main():
    outFilename = "output.txt"
    infile = open("dataMultiple.txt","r")
    outfile = open(outFilename, "w")

    print("Cortney", file=outfile)
    print("Mood", file=outfile)
    print("is taking CSCI220", file=outfile)

    output = ""
    for i in range(10):
        output += str(i)

    outfile.write(output)
    outfile.write("420 got out early.")

    print("Data written to " + outFilename)
    infile.close()
    outfile.close()

main()
