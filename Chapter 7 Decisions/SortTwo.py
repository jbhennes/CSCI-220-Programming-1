## SortTwo.py

def main():
    
##    print "This program will sort (put into order) two numbers."

    # get the numbers to sort
    value1 = eval(input("Enter a number: "))
    value2 = eval(input("Enter another number: "))
                            
    ## rearrange the numbers if necessary	

    if value2 < value1:       # values are not in sorted order
        temporary = value1    # swapping puts them in order
        value1 = value2
        value2 = temporary
        print ("The values were swapped")
                            
    # display values	
    print ("The numbers in sorted order are")
    print (value1, "and then", value2)

main()
