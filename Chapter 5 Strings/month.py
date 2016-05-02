# month.py
#  A program to print the abbreviation of a month, given its number


def main():
    
    # months is used as a lookup table
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"

    for start in range(0, len(months), 3):
        end = start + 3
        print(months[start:end])
        

##    n = eval(input("Enter a month number (1-12): "))
##
##    pos = (n - 1) * 3
##    pos2 = n * 3 - 3
##
##    print("Month starts with: " + months[pos] + " or " + months[pos2] + ".")
##    print("Month abbreviation: " + months[pos] + months[pos+1],end = "")
##    print(months[pos+2] + ".")
##    # compute starting position of month n in months
####    pos = (n-1) * 3
####    
##    # Grab the appropriate slice from months
##    monthAbbrev = months[pos:pos+3]
##
##    # print the result    
##    print ("The month abbreviation is", monthAbbrev + ".")

main()
