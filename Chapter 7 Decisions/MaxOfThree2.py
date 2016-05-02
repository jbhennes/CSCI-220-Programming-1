## MaxOfThree2.py
## Finds largest of three user-specified numbers 	

def main():
    
    x1 = input("Enter a number: ")
    x2 = input("Enter a number: ")
    x3 = input("Enter a number: ")
    
    # Determine which number is the largest

    if x1 >= x2:	
        if x1 >= x3:	
            max = x1     # x1 is largest
        else:	
            max = x3     # x3 is largest
    else:
        if x2 >= x3:     
            max = x2     # x2 is largest
        else:
            max = x3     # x3 is largest

    # display result	
    print "\nLargest number is", max

main()
